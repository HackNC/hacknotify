# ============================ READ ME ================================
# STEP 1: Create a COPY in the same directory called config.py
# STEP 2: Configure this application by changing the "CHANGE ME" fields
# STEP 3: RUN `pip install -e .` 
#         This will allow config changes to take immediate effect.
# TROUBLESHOOTING: Review README.md, then open a github issue
# =====================================================================

# Pick any one of ["plivo", "twilio", "bandwidth"]
PROVIDER="CHANGE ME"

# GOOGLE SHEET API INFO
# Visit https://developers.google.com/sheets/quickstart/python and follow Step 1
SHEET_APP_NAME = 'CHANGE ME: MY SHEET APP NAME'
# If your sheet URL is https://docs.google.com/spreadsheets/d/asdfghjklasdfghjklasdfghjkl/edit
# then your SHEET_ID is 'asdfghjklasdfghjklasdfghjkl'
SHEET_ID = 'CHANGE ME: asdfghjklasdfghjklasdfghjkl'

# Pair your google sheet data with your group names.
GROUPS = {
    # key: any arbitrary name for the group
    # value: a valid Google Sheets selection, including the TAB name and row/col query
    "hackers": "Hackers!A1:B",
    "sponsors": "Sponsors!A1:B",
    "mentors": "Mentors!A1:B",
    "blue": "Blue!A1:B",
    "red": "Red!A1:B",
    # A1:B means the entire column of A, not including any of B.
    # Please note that this is not introspective.  This list does not automatically populate from your google sheet.
}

# PLIVO API INFO
# Create a PLIVO account to get this info.
PLIVO_ID="CHANGE ME"
PLIVO_KEY="CHANGE ME"
PLIVO_SRC="CHANGE ME" # Your plivo phone number (starting with country code)
PLIVO_SEND_RATE=0.0035 # Price per message in USD

# TWILIO API INFO - NOT YET SUPPORTED
# Create a TWILIO account to get this info.
TWILIO_ID="CHANGE ME"
TWILIO_KEY="CHANGE ME"
TWILIO_SRC="CHANGE ME" # Your twilio phone number (starting with country code)
TWILIO_SEND_RATE=0.0075 # Price per message in USD

# BANDWIDTH API INFO
# Create a Bandwidth account to get this info.
BW_USERNAME="CHANGE ME"
BW_ID="CHANGE ME"  # Token
BW_KEY="CHANGE ME" # Key
BW_SRC="CHANGE ME" # Your bandwidth phone number (starting with + country code)
BW_SEND_RATE=0.005 # Price per message in USD

# For python phonenumbers library
DEFAULT_REGION = "US"

# EVENT_NAME is used as the message subject line
EVENT_NAME = "CHANGE ME: HackNC"
DEFAULT_SUBJECT = "["+EVENT_NAME+"]"

# The largest numbers an SMS message can have.
# Any more than this, and the message will be broken into 2 (or more)
SMS_MAX_CHARS=160