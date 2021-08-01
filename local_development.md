# Informations for local development

## Virtual environment
For all python scripts, a virtual environment using version 3.9.6 and the requirements given in [requirements.txt](requirements.txt) are used. Linting is done using pylint with the exceptions listed in [settings.json](.vscode/settings.json).


## Local environment variables
All local environment variables are stored in the file .env which is covered by the .gitignore. Should contain the following key-value pairs (separated by a = without whitespaces):

|ENV-Variable|Value|Meaning|
|###|###|###|
|DEV_LOCALE|1|Signals that development is done on a local machine|
|GOOGLE_APPLICATION_CREDENTIALS|~|Path to the GCP service account credentials json used for local testing|
