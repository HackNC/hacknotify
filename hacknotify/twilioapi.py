import math
from twilio.rest import TwilioRestClient
from . import config


def trigger_send(num_list, message):
    """
    Queues the messages.
    Returns the success/fail status.
    """

    # To find these visit https://www.twilio.com/user/account
    client = TwilioRestClient(config.TWILIO_ID, config.TWILIO_KEY)

    send_from_number = config.TWILIO_SRC
    if not '+' in send_from_number:
        send_from_number = '+' + send_from_number

    # Twilio does not allow bulk creation. Iterate over all.

    for num in num_list:
        message = client.messages.create(
            body=message,
            to="+" + num,
            from_=send_from_number,
        )
    return True
    
    # API Docs are bad.  No idea how to detect failures, so I'll just let those go to
    # console and hope they are helpful...


def calculate_cost(count, message):
    return math.ceil(len(message) / config.SMS_MAX_CHARS) * count * config.TWILIO_SEND_RATE