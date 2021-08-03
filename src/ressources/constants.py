'''
File containing various constants for the different scripts.
'''

# Environment variables
DEPLOYMENT_ENV_VARIABLE = 'DEPLOYMENT-ENV'

# Flask
DEBUG_FLASK = True

# GCP-Paths
GCP_SECRETS_PATH = 'projects/{}/secrets/{}/versions/latest'

# Riot API
API_KEY_SECRET_NAME = '{applName}-api-key-{deplEnv}'
URL_ID_FOR_NAME = 'https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{userName}?api_key={apiKey}'
