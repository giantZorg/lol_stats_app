# GCP setup
This file explains the necessary services and how they are configured. During the initial development stages, the services are all created using gcloud, but should later be rewritten into [terraform scripts](https://cloud.google.com/architecture/managing-infrastructure-as-code) together with a split into a prod and a test system.


# Services
Frequently used constants:
```
export PROJECT_NAME=lol-stats-app
export SYSTEM=test
export REGION=europe-west1
export ZONE=europe-west1-b
export NETWORK=lol-stats-app
```


## Memstore (Redis)
This service is used as a cache for quick access for both backend functions as well as web applications. Should only be used as a cache, not as a permanent storage service.

The gcloud command is as follows:
```
gcloud redis instances create "${PROJECT_NAME}-${SYSTEM}" --size=1 \
    --region=${REGION} --zone=${ZONE} --redis-version=redis_5_0 \
    --network=${NETWORK}
```

Retrieve the IP-address of the created Redis server (listed under *host*):
```
gcloud redis instances describe "${PROJECT_NAME}-${SYSTEM}" --region=${REGION}
```
