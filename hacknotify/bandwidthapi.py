import math
import bandwidth
from . import config

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

def _send_50(api, send_from_number, num_list, message):

    sendlist = []

    for num in num_list:
        # Bandwidth likes the leading '+'
        if len(num) == 10:
            sendlist.append({
                "from": send_from_number,
                "to": num,
                "text": message
            })

    results = api.send_message(sendlist)
    sleep(2)


def trigger_send(num_list, message):
    """
    Queues the messages.
    Returns the success/fail status.
    """
    api = bandwidth.client('catapult', config.BW_USERNAME, config.BW_ID, config.BW_KEY)

    send_from_number = config.BW_SRC
    if not '+' in send_from_number:
        send_from_number = '+' + send_from_number

    chks = chunks(num_list, 40)

    for l in chks:
        _send_50(api, send_from_number, l, message)
    
    return True

def calculate_cost(count, message):
    return math.ceil(len(message) / config.SMS_MAX_CHARS) * count * config.BW_SEND_RATE