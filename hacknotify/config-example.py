# ----------------------------
# Configure this application.
# pip install -e will allow config changes to take immediate effect.
# ----------------------------

# Currently can be "plivo" or "twilio"
PROVIDER="plivo"

# GOOGLE SHEET API INFO
# Visit https://developers.google.com/sheets/quickstart/python and follow Step 1
SHEET_APP_NAME = 'HackNC Notify'
SHEET_ID = '1eqlklR6LsOUufQlUR7YFiRDHNTXRj1NDz9RhiDaRx-I'

# Pair your google sheet data with your group names.
GROUPS = {
   # key: any arbitrary name for the group
   # value: a valid Google Sheets selection, including the TAB name and row/col query

    "hackers": "Hackers!A1:B",
    "sponsors": "Sponsors!A1:B",
    "mentors": "Mentors!A1:B",
    "blue": "Blue!A1:B",
    "red": "Red!A1:B",
}

# PLIVO API INFO
# Create a PLIVO account to get this info.
PLIVO_ID="CHANGE ME"
PLIVO_KEY="CHANGE ME"
PLIVO_SRC="CHANGE ME" # Your plivo phone number (starting with country code)
PLIVO_SEND_RATE=0.0035 # Price per message in USD

# For python phonenumbers library
DEFAULT_REGION = "US"
# For the subject
EVENT_NAME = "HackNC"
DEFAULT_SUBJECT = "["+EVENT_NAME+"]"