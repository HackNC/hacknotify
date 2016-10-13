from __future__ import print_function
import httplib2
import os
from . import config

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/sheets.googleapis.com-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = config.SHEET_APP_NAME


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python.json')

    store = Storage(credential_path)
    credentials = store.get()
    credentials_secret_file_fullpath = os.path.join(credential_dir, CLIENT_SECRET_FILE)
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(credentials_secret_file_fullpath, SCOPES)
        flow.user_agent = APPLICATION_NAME
        credentials = tools.run_flow(flow, store, None)
        print('Storing credentials to ' + credential_path)
    return credentials

def get_phone_list(list_name):
    """
    Get a list of phone numbers by their name.
    """
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4') 
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl)
    # Load these from config.
    spreadsheetId = config.SHEET_ID
    rangeName = config.GROUPS[list_name]

    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()

    values = result.get('values', [])

    if not values:
        print("No data found")
        return None
    else:
        return values