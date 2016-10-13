# HackNotify

> The SMS notification system for HackNC

This Project leverages the following APIs:

* Google Sheets
* Plivo

# Installation

### Pre-requisites

* Python3
* A google account with access to the HackNC Google Drive

### Google API setup

This step is necessary because each account must enable google sheets api.

Visit https://developers.google.com/sheets/quickstart/python and follow Step 1.

Instead of putting `client_secret.json` in your development directory, do this:

```
mkdir ~/.credentials
mv /path/to/client_secret_download.json ~/.credentials/client_secret.json
```

### Python Install

```
git clone git@github.com:hacknc/hacknotify
cd hacknotify
```

Create a copy of `config-example.py` called `config.py` and get the necessary information and API keys.

```
pip3 install .
```

# Running the client

`usage: notify.py [-h] [--group GROUP] [--subject SUBJECT]`

### Examples:

Fully automate send:

`echo "y" | hacknotify --message "This was a triumph" --subject [TEST] --group hackers`

Automate input, but allow interactive confirm:

`hacknotify -m "I'm making a note here - Huge Success" -s [TEST] -g hackers`

Do it all from a python interpreter:

```
>>> from hacknotify import notify
>>> notify.api_send("hackers", "[TEST2]", "SPAAAAACE")
True
```