# Serverless NodeBB Deployment on GCP

This document will provide instructions to create a serverless deployment of NodeBB on GCP.

## Setup Redis Database on upstash

We'll be using a database-as-a-service called upstash to host the Redis database associated with our NodeBB deployment.

1. Visit [upstash](https://upstash.com) and create an account.
2. Make sure Redis is selected, and click "Create Database"
3. Name your database, select an appropriate region and hit "Create"

You should see a page that contains the endpoint, port, password, and other details associated with the redis instance you just created.

## Update your Dockerfile

To have all the packages we need to build NodeBB, we need to change our Dockerfile. Make the following change and push your changes to your repository.

```
- RUN npm install --only=prod && \
+ RUN npm install && \
```

## Deploy on GCP Cloud Run

Make sure you're logged into the Google account you used to redeem your GCP credits. If you haven't redeemed your GCP credits yet, follow the instructions in the [Deployment Recitation](/recitations/reci3-deployment/#task-1b-deploy-on-google-cloud-platform).

Once you're logged into the right credit-bearing Google account, use the following instructions to deploy on GCP Cloud Run.

1. Create a project called "NodeBB" using the [GCP Cloud Console](https://console.cloud.google.com/projectcreate) (you can set the location to "Students")
2. Enable the IAM API using [this link](https://console.cloud.google.com/apis/api/iam.googleapis.com/metrics). Make sure the project you just created is selected in the project selector drop down
2. Visit the [Cloud Run console](https://console.cloud.google.com/run) and select the project you just created using the project selector drop down(top-left)
3. Click on "Create Service"
4. Select "Continuously deploy new revisions from a source repository" and click "Set up with Cloud Build"
5. Set the Source repository to be your team's NodeBB repository - you may need to click on "Manage connected repositories" and authenticate with GitHub if you don't see the repository.
6. Set the Build Type to the "Dockerfile" option
7. In the "Autoscaling" section, set the minimum number of instances to 1
8. In the "Authentication" section select "Allow unauthenticated invocations"
9. Click on the "Container, Networking, and Security" dropdown, set the "Container Port" to 4567 and hit create
10. Once the deployment is complete, click on the URL of the form `*.run.app` at the top of the page to view the deployment.

You should see a form that says "NodeBB Web Installer". Keep this URL handy because you'll need it later :)

## Create Config Script

At this point, we could use the web installer to generate the `config.json` file in our container and setup NodeBB. However, since this a serverless deployment, we're not guaranteed any persistence of data generated at runtime.

Therefore, we need to change our Dockerfile to generate the `config.json` file at build time of the container.

To do so, first create a template file called `config_template.json` that looks exactly like the following, and push your changes to your repository.

```
{
  "url": "",
  "secret": "c5502d62-84a5-41f1-87eb-ee33a76fb7bc",
  "database": "redis",
  "redis": {
    "host": "",
    "port": "",
    "password": "",
    "database": "0"
  },
  "port": "4567"
}
```

!!! info "Why can't we just push a pre-populated `config.json` file?"
    This would solve the persistence problem and deploy NodeBB correctly. However, as a result, we expose secrets like the upstash redis connection details on a public GitHub repository. Injecting these secrets as environment variables at runtime gives our deployment access to them, while ensuring that the secrets remain secret. 

Configure the following environment variables by visiting the Cloud Run dashboard for your deployment, clicking on "Edit and deploy new revision" and then clicking on "Add Variable" in the "Environment Variables" section.

* `DEPLOYMENT_URL`: URL of the form `*.run.app` that your Cloud Run deployment is live at.
* `REDIS_HOST`: Endpoint value from your upstash redis database dashboard.
* `REDIS_PORT`: Port value from your upstash redis database dashboard.
* `REDIS_PASSWORD`: Password value from your upstash redis database dashboard.

Click on "Deploy" at the bottom of the page to save your changes.

We'll now add a bash script that will populate this template with environment variables defined at build time of our Docker container. Create a file called `create_config.sh` in your NodeBB repo, and populate the file with the following bash script.

```
#!/bin/bash

# Check that environment variables have been defined
if [[ -z "${REDIS_HOST+x}" ]]; then
  # var is not defined
  echo "Error: REDIS_HOST is not defined!"
  exit 1
fi

if [[ -z "${REDIS_PORT+x}" ]]; then
  # var is not defined
  echo "Error: REDIS_PORT is not defined!"
  exit 1
fi

if [[ -z "${REDIS_PASSWORD+x}" ]]; then
  # var is not defined
  echo "Error: REDIS_PASSWORD is not defined!"
  exit 1
fi

if [[ -z "${DEPLOYMENT_URL+x}" ]]; then
  # var is not defined
  echo "Error: DEPLOYMENT_URL is not defined!"
  exit 1
fi

# Read the JSON file
json_data=$(cat "/usr/src/app/config_template.json")

# Update the JSON file with the environment variables
json_data=$(jq --arg deployment_url "$DEPLOYMENT_URL" '.url = $deployment_url' <<< "$json_data")
json_data=$(jq --arg host "$REDIS_HOST" '.redis.host = $host' <<< "$json_data")
json_data=$(jq --arg port "$REDIS_PORT" '.redis.port = $port' <<< "$json_data")
json_data=$(jq --arg password "$REDIS_PASSWORD" '.redis.password = $password' <<< "$json_data")

# Write the updated JSON file to config.json
echo "$json_data" > "/usr/src/app/config.json"

cat /usr/src/app/config.json
```

Now, update your Dockerfile so that it looks like the following.

```
FROM node:lts

RUN mkdir -p /usr/src/app && \
    chown -R node:node /usr/src/app
WORKDIR /usr/src/app

RUN apt-get update && apt-get install -y jq

ARG NODE_ENV
ENV NODE_ENV $NODE_ENV

COPY --chown=node:node install/package.json /usr/src/app/package.json

USER node

RUN npm install && \
    npm cache clean --force

COPY --chown=node:node . /usr/src/app

ENV NODE_ENV=production \
    daemon=false \
    silent=false

EXPOSE 4567

RUN chmod +x create_config.sh

CMD  ./create_config.sh -n "${SETUP}" && ./nodebb setup || node ./nodebb build; node ./nodebb start
```

We're making two changes here: (1) installing the jq package to read/edit json files from our bash script, and (2) running the `create_config.sh` script on container startup.

Once you push your changes, a new deployment should get triggered and it should be good to go once complete. Congratulations! You've now setup a continuous deployment of NodeBB on GCP.

Be sure to share the application link with your teammates to ensure they can also access the application and test that all your added features from Project 2 have been successfully applied.
