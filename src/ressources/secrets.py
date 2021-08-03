'''
This file contains functions used to download information from GCP secrets.
'''

###
# Import packages
import logging
import os

from google.cloud import secretmanager

from src.ressources.constants import API_KEY_SECRET_NAME, DEPLOYMENT_ENV_VARIABLE, GCP_SECRETS_PATH


###
# Initialize logger
logger = logging.getLogger(__name__)


###
# Function to download the Riot API key
def getRiotApiKey() -> str:
    '''
    Download Riot API key from GCP secret.
    '''

    logger.info('Get Riot API key')


    ###
    # Create secrets client and extract the project ID from it
    secretsClient = secretmanager.SecretManagerServiceClient()
    projectId = secretsClient._transport._credentials._project_id   # pylint: disable=protected-access


    ###
    # Retrieve the secret from the secret manager
    apiKey = secretsClient.access_secret_version(request = {'name': GCP_SECRETS_PATH.format(
        projectId, API_KEY_SECRET_NAME.format(applName = os.environ['PROJECT_NAME'], deplEnv =
        os.environ[DEPLOYMENT_ENV_VARIABLE]))})


    ###
    # Return the extracted API key
    return(apiKey.payload.data.decode("UTF-8"))
