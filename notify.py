import argparse
import sheetsapi
import plivoapi
import config
import phonenumbers

def make_parser():
    parser = argparse.ArgumentParser(description="Send notifications to a list @ HackNC")
    parser.add_argument("--group", "-g", required=False, help="The list from config to send notification to")
    parser.add_argument("--subject", "-s", required=False, default=config.DEFAULT_SUBJECT, help="a subject to prepend to the message body")
    args = parser.parse_args()
    return args

def waitfor_message():
    """
    Get a message from raw input.
    """
    message = input("Type a message: ")
    return message

def do_send(numlist, message):
    """
    Preprocess the list making sure formatting is correct
    """

    liststring = ""
    invlaid_numbers = 0
    
    for number in numlist:
        possible_number = number[0]
        parsed_number = phonenumbers.parse(possible_number, config.DEFAULT_REGION)
        if phonenumbers.is_possible_number(parsed_number):
            unicode_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            unicode_number = unicode_number.replace(' ', '') # replace the spaces
            unicode_number = unicode_number.replace('+', '') # replace the +
            unicode_number = unicode_number.replace('-', '') # replace the -
            liststring += unicode_number + "<"
        else:
            invlaid_numbers += 1

    # Remove the final "<"
    liststring = liststring[:-1]

    return plivoapi.trigger_send(liststring, message)

def interactive_send(args):

    print("--------------------------------------")
    print("|    HackNC Notification Platform    |")
    print("--------------------------------------")

    if args.group:
        group = args.group
    else:
        print("Groups available:")
        for g in config.GROUPS.keys():
            print("- " + g)
        print("--------------------------------------")

        group = input("Group.....: ")

    while group not in config.GROUPS.keys():
        print("Group invalid.")
        print("Groups available:")
        for g in config.GROUPS.keys():
            print(" - " + g)
        group = input("Group.....: ")

    print("Loading from group...")
    plist = sheetsapi.get_phone_list(group)
    count = len(plist)
    print("Group {grp} loaded with {n} recipient(s)".format(grp=group, n=count))

    if count <= 0:
        print("No entries in list...")
        print("Terminating...")

    message = input("Message...: ")
    subject = args.subject

    print("--------------------------------------")
    print("""Sending to {grp}:

    {subject} {message}
    """.format(
        n=count,
        grp=group,
        subject=subject,
        message=message))

    cost = count * config.PLIVO_SEND_RATE
    print("Count : " + str(count))
    print("Cost  : " + str(cost))
    print("--------------------------------------")

    confirm = input("OK? y/[n] : ") or "n"

    if confirm.lower() == "y":
        print("Queueing...")
        success = do_send(plist, subject + " " + message)
        if success:
            print("Send Queued!")
        else:
            print("Send Failed.")
    else:
        print("Terminating...")
        exit(1)

def main():
    args = make_parser()
    interactive_send(args)

if __name__ == "__main__": 
    main()