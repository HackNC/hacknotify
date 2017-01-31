# HackNotify

> An SMS notification system built for HackNC

This project leverages the following APIs:

* Google Sheets
* Plivo, Bandwidth SDK, or Twilio

# Installation

### Requirements

* Python 3
* A google account with access to a correctly formatted google sheet.
* API Credit with a Bandwidth.com, Plivo, or Twilio account.  (Bandwidth recommended)

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

Create a copy of `config-example.py` called `config.py` and get the necessary information and API keys from your chosen service.

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
>>> group = notify.get_group("group_name")
>>> notify.do_send(group, "[TEST2]", "SPAAAAACE")
True
```

Example console output:
```
--------------------------------------
|      SMS Notification Platform     |
--------------------------------------
[?] Groups available:
 - red
 - blue
 - hackers
 - sponsors
 - mentors
Group.....: mentors
[*] Loading from group... 
[*] Group "mentors" loaded with 1 recipient(s)
Message...: THIS WAS A TRIUMPH
--------------------------------------
[*] Sending to mentors:

    [HackNC] THIS WAS A TRIUMPH
    
Count : 1
Cost  : 0.005
--------------------------------------
OK? y/[n] : y
[*] Queueing...
[*] Send Queued!
```