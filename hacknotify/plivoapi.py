import plivo
from . import config

def trigger_send(liststring, message):
    """
    Queues the messages.
    Returns the success/fail status.
    """
    auth_id = config.PLIVO_ID
    auth_token = config.PLIVO_KEY

    p = plivo.RestAPI(auth_id, auth_token)

    params = {
        'src': config.PLIVO_SRC, # Sender's phone number with country code
        'dst' : liststring, # Receivers' phone numbers with country code. The numbers are separated by "<" delimiter.
        'text' : message # Your SMS Text Message
    }

    response = p.send_message(params)

    if response[0] >= 200 and response[0] <= 299:
        # 2XX Message.  Probably ok.
        return True
    else:
        print("Send Failed...")
        print(response)
        return False