'''
This script downloads the match history for a given summoner account id. For every newly found match,
the match information is downloaded and stored within GCP storage. Afterwards, two SQL-tables will be updated,
one containing the last summoner account id and the last time the data was refreshed, and one containing the
match ids for the downloaded matches.

The different parts necessary are exposed separately so that a public facing web server could also call them
and only execute the parts needed.

Note that all API calls to the Riot API have to respect the corresponding rate limiting, which will be controlled
using the redis server.

This script is used within Cloud Run and starts a small webserver with flask and gunicorn. See also the
small example here: https://cloud.google.com/run/docs/quickstarts/build-and-deploy.

The server is designed the following way:
- /: Main route which accepts a summoner account id.
- /get_match_history: Route which returns the match history (complete for data collection, only partially if
                      called for a visualization)
- /get_match_information: Route which returns the match information.
'''


###
# Import packages
import logging
import os

from flask import Flask
import requests
import urllib3

from src.ressources.constants import DEBUG_FLASK, DEPLOYMENT_ENV_VARIABLE
from src.ressources.secrets import getRiotApiKey


###
# Initialize application and logger
app = Flask('Match information API')
logger = logging.getLogger('Match information API')


###
# Initialize variables and start the server
if __name__ == "__main__":
    # Set logging level
    logging.basicConfig(level = getattr(logging, os.environ.get('LOGGING', 'INFO')))

    # Import environment variables if run locally. This is determined by not having a DEPLOYMENT-ENV variable
    if os.environ.get(DEPLOYMENT_ENV_VARIABLE, None) is None:
        from dotenv import load_dotenv
        _ = load_dotenv()

    # Import the Riot API key from GCP secrets
    apiKey = getRiotApiKey()

    # Start web application
    app.run(debug = DEBUG_FLASK, host = '0.0.0.0', port = int(os.environ.get('PORT', 8080)))
