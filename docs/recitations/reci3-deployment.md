
# Recitation 6: Deployment

  

## Overview

Throughout this recitation, students will:

  

* Understand the fundamental steps involved in deployment

* Learn about CI/CD and the basics of how to set it up in a Github repo

* Get hands on experience deploying with Fly.io (or Vercel as a backup)

* Set up the Extreme Startup web app for use in Tuesday's (3/14) lecture

  

## Definitions

  

Before we begin, we have to understand our goals with CI/CD. It is a software development approach that utilizes frequent, automated testing and deployment to ensure that changes to the codebase can be rapidly and safely incorporated into the production environment.

  

**Continuous Integration (CI)** refers to the practice of automatically building and testing the codebase whenever new changes are introduced. This involves integrating code changes from multiple developers into a shared repository and running automated tests to ensure that the changes do not break the existing functionality.

  

**Continuous Deployment/Delivery (CD)** refers to the practice of automatically deploying code changes to the production environment after they have been tested and approved. Continuous Deployment involves automatically deploying changes to the production environment as soon as they pass automated tests, while Continuous Delivery involves deploying changes to a staging environment for further testing and approval before being deployed to production.

  

Together, CI/CD enables software teams to rapidly and safely develop, test, and deploy changes to the codebase, improving the speed and quality of software delivery while reducing the risk of errors and downtime.

  

There's quite a lot to learn about CI/CD. If you're interested in learning more, [click here!](https://about.gitlab.com/topics/ci-cd/)

  

## Task 0: Prep

  

For this recitation, we'll be working with a basic web app built on Next.js that responds to HTTP requests. Your job on Tuesday during the ~Extreme Startup~ game will be to parse these requests and figure out what the correct response is. Today we'll focus on setting up the app so that everything is in place for the game.

  

The steps to do this are as follows:

!!! warning
	Do not use codespaces for this task, and the rest of the recitation. Everything must be done locally.

1. Fork this repo: [https://github.com/CMU-313/basic-web-app](https://github.com/CMU-313/basic-web-app).

2. Follow the instructions in the readme to run the development server locally.

3. Install the Fly.io CLI and set up the Fly.io account that you'll use to host your app. Complete steps 1-3 of the instructions [here](https://fly.io/docs/hands-on/).

4. In your local basic-web-app repo, run `fly launch` followed by `fly open`

  

Now check your [fly.io dashboard](https://fly.io/dashboard) to monitor your app deployment.

  

This has already been a lot of instructions, so good job for getting this far!!!

  

**Note: Fly.io offers a free tier and you should not be required to enter any credit card info for the purposes of this recitation. If you get a message saying that a credit card is required, you can complete the recitation using Vercel instead. See the backup instructions below.**

  

## Task 1: Continuous Deployment

  

Next, we'll setup CD. Our goal is to set up a GitHub action that links to our Fly.io account and automatically redeploys a new version of our app whenever a new change is pushed into the main branch.

  

The steps to do this are as follows:

  

1. Get a Fly API token with `flyctl auth token`.

2. Go to your fork on GitHub and click Settings.

3. Go to Secrets and Variables > Actions and create a repository secret called `FLY_API_TOKEN` with the value of the token from the previous step. This is how GitHub will link to your Fly.io account.

4. Double check that `fly.toml` (the config file fly.io uses for deployment) is not listed in your `.gitignore`.

5. Create a new file `.github/workflows/fly.yml`.This is the file that will outline instructions for the GitHub action.

6. Fill the file with the contents listed under step 8 [here](https://fly.io/docs/app-guides/continuous-deployment-with-github-actions/).

7. Commit and push your changes!

  

Now let's take a step back and understand what we've done. First, we generated an authorization token and used it to connect Fly.io to our GitHub repo. Then, we created a `fly.yml` file setting up a GitHub action that automatically runs the deployment commands whenever a push is made to the main branch. See if you can figure out which lines do what in the code above!

  

Now, look through the codebase and try to change the header on your app's frontend while testing with the local development server. Once you have made your changes, commit and push them. Back on GitHub, you should see the Action trigger and your app will redeploy!

  

With this complete, you'll be able to quickly iterate and any changes you make and push to your fork will be automatically deployed. Cool!

  

## Bonus Task: Continuous Integration

  

While the steps above are all that is required for the ~Extreme Startup~ game, we'll spend the rest of the recitation setting up CI for our repo as well. For our purposes, we'll set up an action that runs ESLint and our Jest tests whenever we push to the repo.

  

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

  

**Note: In an ideal world, you would condition the deployment action on this action, such that your app is only deployed if the linter and tests pass. Sadly, our world is not ideal :(, but if you want to learn more, click [here](https://docs.github.com/en/actions/using-jobs/using-conditions-to-control-job-execution) and [here](https://docs.github.com/en/actions/learn-github-actions/expressions)!**

  

Once this is complete, you will be ready for the game tomorrow. Good job and good luck!

  

Remember to do Recitation 6 Quiz on Gradescope!

  

## Vercel Backup Instructions

  

### Task 0

See the instructions [here](https://docs.google.com/document/d/1FINHlDBRLeBjR65KyJ1zDtObvQC8ydjqV36-w6Zwex0/edit#heading=h.xbhcc8nupq1s) to setup a Vercel deployment.

### Task 1

To learn how to setup a deployment GitHub action for Vercel, see [here](https://vercel.com/guides/how-can-i-use-github-actions-with-vercel).

### Task 2

Same as above!
