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
    """
    Input function with safety for 
    ^C (CTRL C)
    ^D (CTRL D)
    """
    try:
        reply = input(string)
        return reply
    except EOFError:
        print("\nEOF")
        exit(1)
    except KeyboardInterrupt:
        print("")
        exit(1)


def get_groups():
    """
    Return a list of the possible groups to send to
    """
    return config.GROUPS.keys()


def get_group(group_name):
    """
    Get the actual list of numbers in a group
    """
    return sheetsapi.get_phone_list(group_name)


def do_send(dirty_list, subject, message):
    """
    API call for sending from code
    :param group: a string group name from config
    :param subject: a subject line string
    :param message: message body string
    :return: True/False for success/fail
    """
    valid_list = do_number_parse(dirty_list)
    return plivoapi.trigger_send(valid_list, subject + " " + message)


def do_number_parse(numlist):
    """
    Preprocess the list making sure formatting is correct
    Return a valid list
    """
    invalid_list = []
    valid_list = []
    
    for number in numlist:
        
        try:
            
            possible_number = number[0]
            parsed_number = phonenumbers.parse(possible_number, config.DEFAULT_REGION)
            
            if phonenumbers.is_possible_number(parsed_number):
                unicode_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
                unicode_number = unicode_number.replace(' ', '') # remove the spaces
                unicode_number = unicode_number.replace('+', '') # remove the +
                unicode_number = unicode_number.replace('-', '') # remove the -
                valid_list.append(unicode_number)
            else:
                invalid_list.append(number)
        
        except IndexError:
            invalid_list.append(number)

    return valid_list


def enter_interactive_send(args):
    """
    Walk the user through creating and sending a message
    """

    print("--------------------------------------")
    print("|      SMS Notification Platform     |")
    print("--------------------------------------")

    # ==========================
    # Determine group to send to
    # ==========================

    group = None
    if args.group:
        group = args.group
    else:   
        tries = 0 
        while group not in config.GROUPS.keys():
            
            if tries > 0:
                print("[!] Group invalid.")
            tries += 1
            
            print("[?] Groups available:")
            for g in config.GROUPS.keys():
                print(" - " + g)
            group = safe_input("Group.....: ")

    print("[*] Loading from group... ")
    plist = get_group(group)
    count = len(plist)
    print("[*] Group \"{grp}\" loaded with {n} recipient(s)".format(grp=group, n=count))

    if count <= 0:
        print("[!] No entries in list")
        print("[!] Terminating")
        exit(1)

    # =======================
    # Build the message
    # =======================

    if args.message:
        message = args.message
    else:
        message = safe_input("Message...: ")
    
    subject = args.subject

    print("--------------------------------------")
    print("""[*] Sending to {grp}:

    {subject} {message}
    """.format(
        n=count,
        grp=group,
        subject=subject,
        message=message))

    if config.PROVIDER.lower() == "plivo":
        cost = plivoapi.calculate_cost(count, message)
    elif config.PROVIDER.lower() == "twilio":
        raise NotImplementedError("Twilio not implemented")

    print("Count : " + str(count))
    print("Cost  : " + str(cost))
    print("--------------------------------------")

    # ======================
    # Trigger send
    # ======================

    confirm = safe_input("OK? y/[n] : ") or "n"

    if confirm.lower() == "y":
        
        print("[*] Queueing...")
        success = do_send(plist, subject, message)
        
        if success:
            print("[*] Send Queued!")
        else:
            print("[!] Send Failed!")
    else:
        print("[!] Terminating")
        exit(1)


def main():
    """
    The entry point for 'hacknotify' command
    """

    args = make_parser()
    enter_interactive_send(args)


if __name__ == "__main__": 
    main()
