# HackNotify

> The SMS notification system for HackNC

This Project leverages the following APIs:

* Google Sheets
* Plivo

# Installation

### Pre-requisites

* Python3
* A google account with access to the HackNC Google Drive

### Python Install

Create a copy of `config-example.py` called `config.py` and get the necessary information and API keys.

```
git clone git@github.com:hacknc/hacknotify
cd hacknotify
pip3 install .
```

### Google API setup

This step is necessary because each account must enable google sheets api.

Visit https://developers.google.com/sheets/quickstart/python and follow Step 1.

# Running the client

`usage: notify.py [-h] [--group GROUP] [--subject SUBJECT]`