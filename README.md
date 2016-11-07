# HackNotify

> An SMS notification system built for HackNC

This project leverages the following APIs:

* Google Sheets
* Plivo

# Installation

### Requirements

* Python 3
* A google account with access to a correctly formatted google sheet.

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
pip3 install -e .
```

You're done!

# Running the client

`usage: hacknotify [-h] [--group GROUP] [--subject SUBJECT] [--message MESSAGE]`

### Examples:

Fully automate send:

`echo "y" | hacknotify --message "This was a triumph" --subject [TEST] --group hackers`

Automate input, but allow interactive confirm:

`hacknotify -m "I'm making a note here - Huge success" -s [TEST] -g hackers`

Do it all from a python interpreter:

```
>>> from hacknotify import notify
>>> notify.api_send("hackers", "[TEST2]", "SPAAAAACE")
True
```