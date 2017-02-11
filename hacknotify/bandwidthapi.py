import math
from bandwidth_sdk import Message
from bandwidth_sdk import Client
from . import config

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def _send_50_this_is_trash(send_from_number, num_list, message):
    sender = Message.send_batch()

    for num in num_list:
        # Bandwidth likes the leading '+'
        sender.push_message(send_from_number, '+' + num, message)

    sender.execute()

    return sender


def trigger_send(num_list, message):
    """
    Queues the messages.
    Returns the success/fail status.
    """
    bw_client = Client(config.BW_USERNAME, config.BW_ID, config.BW_KEY)

    send_from_number = config.BW_SRC
    if not '+' in send_from_number:
        send_from_number = '+' + send_from_number

    chks = chunks(num_list, 40)

    for l in chks:
        sender = _send_50_this_is_trash(send_from_number, l, message)
        if sender.errors:
            for e in sender.errors:
                print("BW ERROR:" + str(e))
            return False
    
    return True

def calculate_cost(count, message):
    return math.ceil(len(message) / config.SMS_MAX_CHARS) * count * config.BW_SEND_RATE