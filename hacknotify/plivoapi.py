import plivo
import math
from . import config

def _parse_list(num_list):
    """
    takes a list of valid parsed numbers
    returns a string formatted for plivo
    separated by <
    """
    list_string = ""
    for num in num_list:
        list_string += num + "<"
    
    # remove the final '<'
    return list_string[:-1]

def trigger_send(num_list, message):
    """
    Queues the messages.
    Returns the success/fail status.
    """
    auth_id = config.PLIVO_ID
    auth_token = config.PLIVO_KEY

    p = plivo.RestAPI(auth_id, auth_token)

    params = {
        'src': config.PLIVO_SRC, # Sender's phone number with country code
        'dst' : _parse_list(num_list), # Receivers' phone numbers with country code. The numbers are separated by "<" delimiter.
        'text' : message # Your SMS Text Message
    }

    # response = p.send_message(params)

    if response[0] >= 200 and response[0] <= 299:
        # 2XX Message.  Probably ok.
        return True
    else:
        print("Send Failed...")
        print(response)
        return False

def calculate_cost(count, message):
    return math.ceil(len(message) / 160) * count * config.PLIVO_SEND_RATE