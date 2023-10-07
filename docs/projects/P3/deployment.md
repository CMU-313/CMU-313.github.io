# Serverless NodeBB Deployment on GCP

This document will provide instructions to create a serverless deployment of NodeBB on GCP.

## Setup Redis Database on upstash

We'll be using a database-as-a-service called upstash to host the Redis database associated with our NodeBB deployment.

1. Visit [upstash](upstash.com) and create an account.
2. Make sure Redis and selected, and click "Create Database"
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

1. Create a project called "NodeBB" using the [GCP Cloud Console](https://console.cloud.google.com/projectcreate?previousPage=%2Fwelcome%3Fproject%3Dextreme-startup&organizationId=703967796528) (you can set the location to "Students")
2. Visit the [Cloud Run console](https://console.cloud.google.com/run) and select the project you just created using the project selector drop down(top-left)
3. Click on "Create Service"
4. Select "Continuously deploy new revisions from a source repository" and click "Set up with Cloud Build"
5. Set the Source repository to be your team's NodeBB repository - you may need to click on "Manage connected repositories" and authenticate with GitHub if you don't see the repository.
6. Set the Build Type to the "Dockerfile" option
7. In the "Autoscaling" section, set the minimum number of instances to 1
8. In the "Authentication" section select "Allow unauthenticated invocations" and hit "Create"
9. Click on the "Container, Networking, and Security" dropdown and set the "Container Port" to 4567
10. Once the deployment is complete, click on the URL of the form `*.run.app` at the top of the page to view the deployment.

You should see a form that says "NodeBB Web Installer".

## Create Config Script

At this point, we could use the web installer to generate the `config.json` file in our container and setup NodeBB. However, since this a serverless deployment, we're not guaranteed any persistence of data generated at runtime.

Congratulations, you have now successfully deployed NodeBB!

Be sure to share the application link with your teammates to ensure they can also access the application and test that all your added features from Project 2 have been successfully applied.
