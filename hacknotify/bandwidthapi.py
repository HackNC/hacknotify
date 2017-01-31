import math
from bandwidth_sdk import Message
from bandwidth_sdk import Client
from . import config


def trigger_send(num_list, message):
    """
    Queues the messages.
    Returns the success/fail status.
    """
    bw_client = Client(config.BW_USERNAME, config.BW_ID, config.BW_KEY)

    send_from_number = config.BW_SRC
    if not '+' in send_from_number:
        send_from_number = '+' + send_from_number

    sender = Message.send_batch()
    for num in num_list:
        # Bandwidth likes the leading '+'
        sender.push_message(config.BW_SRC, '+' + num, message)

    sender.execute()

    if sender.errors:
        for e in sender.errors:
            print("BW ERROR:" + str(e))
        return False
    return True

def calculate_cost(count, message):
    return math.ceil(len(message) / config.SMS_MAX_CHARS) * count * config.BW_SEND_RATE