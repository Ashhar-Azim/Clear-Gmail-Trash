# Clear-Gmail-Trash
if you somehow don't want to use gmail provided filters but looking for more technical method

# Gmail API Email Deletion Tool

The Gmail API Email Deletion Tool is a Python script with a graphical user interface (GUI) that allows you to delete emails from your Gmail account based on various criteria. It uses the Gmail API and Tkinter for the GUI.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Logging](#logging)
- [Warning](#warning)
- [Contributions](#contributions)
## Features

- Filter emails by keyword, sender, subject, attachment presence, and email size.
- Dark theme toggle for the GUI.
- Logging of actions, including deletions, cancellations, and errors.

## Prerequisites

- Python
- Gmail API OAuth 2.0 credentials (store the JSON file as `credentials.json` in the script's directory)

## Getting Started

1. Install the necessary Python libraries:

     ```pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib ttkthemes```

2. Create a Gmail API OAuth 2.0 credentials file (credentials.json) and place it in the script's directory.

3. Run the script using Python:

     ```python gmail_api_tool.py```

4. Use the graphical interface to configure filtering criteria and delete emails.

## Usage

     Enter filtering criteria in the GUI, including keywords, sender, subject, attachment presence, and email size.
     Click "Delete Emails" to delete matching emails, and confirm the deletion when prompted.
     Use the "Toggle Dark Theme" button to switch between dark and light themes for the GUI.

## Logging

     The script logs actions to a file named gmail_api_log.txt. This log file includes timestamps, log levels, and relevant messages.

## Contributions

     This Project is in development. Please feel free to contribute

## Warning

- Use this tool responsibly and only on your own Gmail account.
- Take care not to accidentally delete important emails.
- Follow Google's terms of service and API usage guidelines.

