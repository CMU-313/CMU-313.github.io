
# Recitation 3: Deployment

  

## Overview

Throughout this recitation, students will:

  

* Understand the fundamental steps involved in deployment

* Learn about CI/CD and the basics of how to set it up in a Github repo

* Get hands on experience deploying with multiple cloud providers - Render and Google Cloud Platform.

* Set up and get familiarized with the _Extreme Startup_ web app for use in Tuesday's (9/19) lecture

  

## Definitions

  

Before we begin, we have to understand our goals with CI/CD. It is a software development approach that utilizes frequent, automated testing and deployment to ensure that changes to the codebase can be rapidly and safely incorporated into the production environment.

  

**Continuous Integration (CI)** refers to the practice of automatically building and testing the codebase whenever new changes are introduced. This involves integrating code changes from multiple developers into a shared repository and running automated tests to ensure that the changes do not break the existing functionality.

  

**Continuous Deployment/Delivery (CD)** refers to the practice of automatically deploying code changes to the production environment after they have been tested and approved. Continuous Deployment involves automatically deploying changes to the production environment as soon as they pass automated tests, while Continuous Delivery involves deploying changes to a staging environment for further testing and approval before being deployed to production.

  

Together, CI/CD enables software teams to rapidly and safely develop, test, and deploy changes to the codebase, improving the speed and quality of software delivery while reducing the risk of errors and downtime.

  

There's quite a lot to learn about CI/CD. If you're interested in learning more, [click here!](https://about.gitlab.com/topics/ci-cd/)

  

## Task 0: Setting up your repository

  

For this recitation, we'll be working with a basic web app built on Next.js that responds to HTTP requests. Your job on Tuesday during the _Extreme Startup_ game will be to parse these requests and figure out what the correct response is. Today we'll focus on setting up the app so that everything is in place for the game.

  

The steps to do this are as follows:

!!! Warning
	Do not use codespaces for this task, and the rest of the recitation. Everything must be done locally.

1. Fork this repo: [https://github.com/CMU-313/basic-web-app](https://github.com/CMU-313/basic-web-app).

2. Follow the instructions in the readme to run and test the development server locally.

3. Once you have it running locally visit [http://localhost:3000](http://localhost:3000) and try different queries like "Who was Shakespeare?" and "What is your Andrew ID?"

4. Also visit [http://localhost:3000/api?q=shakespeare](http://localhost:3000/api?q=shakespeare) - this is the API endpoint that our game server will use at next week's lecture.
  

## Task 1: Continuous Deployment

To start off, you'll be deploying the app you just forked on two cloud platforms - Render and Google Cloud Platform. The goal here is to make your app accessible over the internet via two platforms. You'll also be setting up continuous deployment such that both of these deployments are updated with the latest version of the app, whenever you push code to the main branch of your repository.

### Task 1A: Deploy on Render
  
1. Create an account on [Render](https://render.com)
2. Create a new Web Service
3. Choose "Build and deploy from a Git repository"
4. Click on Configure account under GitHub, to give Render access to your GitHub repositories - this is necessary to setup continuous deployment.
5. Connect your basic-web-app fork to the Web Service you just created
6. Name your web server `<andrewID>-313`
7. Set the Runtime to "Node", Build Command to `npm install; npm run build` and Start Command to `npm start`
8. Make sure that the "Free" Instance Type is selected, and click "Create Web Service"
9. When the build completes, click on the link of the form `*.onrender.com` at the top of the page to view the deployment.

### Task 1B: Deploy on Google Cloud Platform

First, you need to redeem your GCP credits using the following instructions.

1. Fill out the [this form](https://gcp.secure.force.com/GCPEDU?cid=jNiJXsspdHxisefhvWgRB4vlYgFHf25hnlxWcQ9A4B7TORUD40BjE6%2F6DBVwqQwL/) link with your first/last name, and Andrew ID
2. Go to your school email and click the link in an email from "Google Cloud Notifications" to verify your email address
3. Go back to your email, click on the link ("click here to redeem") within a second email from "Google Cloud Notifications," and copy the provided code into the field within the new link

Once you submit, a $50 credit should be applied to your GCP billing account.

!!! Warning "Do not misuse!"
	We've been awarded enough credits such that each student in 17-313 can redeem one coupon. We'll be closely monitoring coupon redemption. Any and all misuse including sharing redemption instructions, redeeming multiple times, etc. will be punished.

Now that you've redeemed your coupon, use the following instructions to deploy on GCP.

1. Create a project called "Extreme Startup" using the [GCP Cloud Console](https://console.cloud.google.com/projectcreate?previousPage=%2Fwelcome%3Fproject%3Dextreme-startup&organizationId=703967796528) (you can set the location to "Students")
2. Visit the [Cloud Run console](https://console.cloud.google.com/run) and select the project you just created using the project selector drop down(top-left)
3. Click on "Create Service"
4. Select "Continuously deploy new revisions from a source repository" and click "Set up with Cloud Build"
5. Set the Source repository to be your basic-web-app fork - you may need to click on "Manage connected repositories" and authenticate with GitHub if you don't see the repository.
6. Set the Build Type to the "Go, Node.js, Python, ..." option
7. Set the Entrypoint to be `npm install; npm run build; npm start`
8. In the "Authentication" section select "Allow unauthenticated invocations" and hit "Create"
9. Once the deployment is complete, click on the URL of the form `*.run.app` at the top of the page to view the deployment.

With this complete, you'll be able to quickly iterate and any changes you make and push to your fork will be automatically deployed on both Render and GCP. Cool!

## Task 2: Implement "What is your Andrew ID?"

To test that the continuous deployments are working as expected, and familiarize yourself with the basic web app codebase, let's implement support for the query "What is your Andrew ID?"

1. Extend the `QueryProcessor` function to support this question in `utils/QueryProcessor.tsx` - this is where all the Query Processing logic exists
2. Verify that the implementation is correct by running the app locally and testing manually.
2. Write a test for the query you just implemented in `__tests__/utils/QueryProcess.test.ts`
3. Verify that the tests function correctly by running `npm run test`.
5. Commit and push your changes
6. Once pushed, verify that CD is functioning correctly by checking that a new deployment is triggered on the GCP and Render dashboards.
7. Once the deployments are complete manually verify that both support the query you just implemented.

## Bonus Task: Continuous Integration

  

While the steps above are all that is required for the _Extreme Startup_ game, we'll spend the rest of the recitation setting up CI for our repo as well. For our purposes, we'll set up an action that runs ESLint and our Jest tests whenever we push to the repo.

  

The process will be similar to above.

  

1. Create a new `.github/workflows/test.yml`

2. Copy the following into the files and fill in the blanks appropriately!

```

name: __BLANK 1__

on:

push:

branches:

- main

jobs:

__BLANK 2__:

    runs-on: ubuntu-latest

    name: __BLANK 3__

    steps:

    - uses: actions/checkout@v3

    - uses: bahmutov/npm-install@v1

    - run: npm run __BLANK 4__ (Run ESLint)

    - run: __BLANK 5__ (Run Jest)

```

  

Hint: Look at the readme of the basic-web-app repo!

!!! note "Conditional CD"
    In an ideal world, you would condition the deployment action on this action, such that your app is only deployed if the linter and tests pass. Sadly, our world is not ideal :(, but if you want to learn more, click [here](https://docs.github.com/en/actions/using-jobs/using-conditions-to-control-job-execution) and [here](https://docs.github.com/en/actions/learn-github-actions/expressions)!


Once this is complete, you will be ready for the game next week. Good job and good luck!

  

Remember to do Recitation 3 Quiz on Gradescope!

