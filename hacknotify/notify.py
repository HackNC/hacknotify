#!/usr/bin/python3

import argparse
import phonenumbers

from . import sheetsapi
from . import plivoapi
from . import config

def make_parser():
    parser = argparse.ArgumentParser(description="Send notifications to a list @ HackNC")
    parser.add_argument("--group", "-g", required=False, help="The list from config to send notification to")
    parser.add_argument("--subject", "-s", required=False, default=config.DEFAULT_SUBJECT, help="a subject to prepend to the message body")
    parser.add_argument("--message", "-m", required=False, default=None, help="Message body")
    args = parser.parse_args()
    return args

def safe_input(string):
    try:
        reply = input(string)
        return reply
    except EOFError:
        print("\nEOF")
        exit(1)
    except KeyboardInterrupt:
        print("")
        exit(1)

def api_send(group, subject, message):
    """
    API call for sending from code
    :param group: a string group name from config
    :param subject: a subject line string
    :param message: message body string
    :return: True/False for success/fail
    """
    plist = sheetsapi.get_phone_list(group)
    success = do_send(plist, subject + " " + message)
    return success

def do_send(numlist, message):
    """
    Preprocess the list making sure formatting is correct
    """

    liststring = ""
    invlaid_numbers = 0
    
    for number in numlist:
        try:
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
        except:
            invlaid_numbers+= 1

    # Remove the final "<"
    print("Invalid count " + str(invlaid_numbers))
    liststring = liststring[:-1]

    return plivoapi.trigger_send(liststring, message)

def interactive_send(args):

    print("--------------------------------------")
    print("|    "+config.EVENT_NAME+" Notification Platform    |")
    print("--------------------------------------")

    if args.group:
        group = args.group
    else:
        print("Groups available:")
        for g in config.GROUPS.keys():
            print("- " + g)
        print("--------------------------------------")

        group = safe_input("Group.....: ")

    while group not in config.GROUPS.keys():
        print("Group invalid.")
        print("Groups available:")
        for g in config.GROUPS.keys():
            print(" - " + g)
        group = safe_input("Group.....: ")

    print("Loading from group...")
    plist = sheetsapi.get_phone_list(group)
    count = len(plist)
    print("Group {grp} loaded with {n} recipient(s)".format(grp=group, n=count))

    if count <= 0:
        print("No entries in list...")
        print("Terminating...")

    if args.message:
        message = args.message
    else:
        message = safe_input("Message...: ")
    
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

    confirm = safe_input("OK? y/[n] : ") or "n"

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
