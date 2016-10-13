# Attention!
# Change the variables in this file, and create a copy called config.py

PLIVO_ID="PLIVO ID HERE" # Change me!
PLIVO_KEY="PLIVO SECRET KEY HERE" # Change me!
PLIVO_SRC="PLIVO PHONE # HERE" # Change me!

SHEET_APP_NAME = 'HackNC Notify'
SHEET_ID = '1eqlklR6LsOUufQlUR7YFiRDHNTXRj1NDz9RhiDaRx-I'

# Require that the phone number is in the first selected column.
GROUPS = {
    "hackers": "Hackers!A1:B",
    "sponsors": "Sponsors!A1:B",
    "mentors": "Mentors!A1:B",
}

PLIVO_SEND_RATE=0.0035 # Price per message in USD

DEFAULT_REGION = "US"
DEFAULT_SUBJECT = "[HackNC]"