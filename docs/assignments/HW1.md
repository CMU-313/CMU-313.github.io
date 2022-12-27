---
title: HW01 Hello Teedy
---

# Homework 1: Hello, Teedy!

## Learning Goals

-   Familiarize yourself with an existing software project
-   Download, install and run an existing software project
-   Run an evaluation tool and collect metrics
-   Evaluate the results of these metrics

## Background

Git and GitHub:

- [Git Documentation](https://git-scm.com/docs/gittutorial)
- [Git Flow](https://datasift.github.io/gitflow/IntroducingGitFlow.html)
- [GitHub Basics](https://guides.github.com/activities/hello-world/)
- [GitHub's Flow](https://guides.github.com/introduction/flow/)
- [GitHub Cross-Referencing](https://docs.github.com/en/github/writing-on-github/working-with-advanced-formatting/autolinked-references-and-urls#issues-and-pull-requests)

## Specification

Welcome to the team! To start your journey on this project, your first
task is to become familiar with an existing piece of software.
Eventually you will be adding new features, but the first step is to
simply download, run, evaluate, and explore the current software
product. The project we will be building on this semester is an open
source document management system, [Teedy](https://teedy.io/).

We will be using a class-specific fork of Teedy, whose repository is located at: [https://github.com/CMU-313/Teedy](https://github.com/CMU-313/Teedy)
This fork is based off https://github.com/sismics/docs and contains minor tweaks to make the project easier to modify and debug.
Forking from the class repository will  allow you to send pull requests to the instructors, which is the primary way of submitting code deliverables for this homework.

**Getting Started:**
Your first step should be to fork the repository and then follow the installation instructions in README.md.
You must build and run Teedy **natively** on your machine (via the manual installation instructions) rather than following the Docker instructions. After building Teedy and its dependencies, you should follow the rest of the Getting Started instructions to run a Teedy instance on your machine.
![teedy screenshot](https://cmu-313.github.io/assets/images/teedy.png)



Once you have run Teedy successfully, you should be able to navigate to  [`http://localhost:8080/src`](http://localhost:8080/src) (if this doesn't work, try navigating to [`http://localhost:8080`](http://localhost:8080) ) and see a web page with a login screen.
By default, Teedy will be deployed to port `8080` on your machine.
You may change this port number (e.g., to avoid conflict with another process running on your machine).

**If the process of installing and running Teedy takes you more than a few hours, STOP and ask for help on Slack.**

**Collecting Metrics:**
Once you have Teedy up and running locally, proceed to evaluate it using [Google Lighthouse](https://developers.google.com/web/tools/lighthouse).
You can run Lighthouse as a stand alone application, or using the audit tab of Google Developer Tools.
After you run Lighthouse, it will give you a score for various dimensions: Performance, Accessibility, Best Practices, and SEO.
Additionally, you can measure test coverage.  This will be done every time you run the tests via maven `mvn test`, using the [Jacoco](https://www.eclemma.org/jacoco/) tool. 
After looking over the metrics, pick one metric to improve (Performance, Accessibility, Best Practices, SEO, or Code Coverage).
The Lighthouse reports will give you some suggestions as to how to improve a score.
The only requirements are that your change should affect the metric's score, and that the change should involve a commit to the repo.
HINT: Because of this, you might want to avoid trying to
change the performance score.

First, open an issue in the [https://github.com/CMU-313/Teedy/issues](https://github.com/CMU-313/Teedy/issues) to declare what aspect of Teedy you will be improving.
You should look through existing issues, if any, to avoid duplicates. 
In the issue description, mention the current score you observed and the warning that you are targeting.
~~Tag the issue with one or more of the existing labels as appropriate, add it to milestone "HW1", and~~ assign yourself (do this by commenting "I would like to work on this please!").

In your own fork, create a feature branch, implement the change, test it out locally, and commit your changes.
Your commit message(s) must clearly describe what's changing.

Once you are satisfied, open a pull request in the parent repository.
The PR should [link the issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue) that you previously opened (e.g. using the "resolve(s)" keyword), summarize the changes, and describe how much the score improved by due to your change.

After you have completed this task, we will ask you to reflect on the nature of metrics.
To do this, you will answer the following questions about metrics, specifically in the context of Teedy.
You should focus your answers for each of these questions on the metric that you chose to improve.

- What properties do we care about, and how do we measure them?
- What is being measured? Does it (to what degree) capture the thing you care about? What are its limitations?
- How should this metric be incorporated into process? Check in gate? Once a month? Etc.
- What are potentially negative side effects or incentives?

## Deliverables and Deadlines

There are three (3) deliverables and one (1) deadline for this homework.

*Individual Component -- 100 points -- due Thursday, September 9th, 23:59*

1. Create an issue in the parent repository, which must:
	- Mention the metric you are targeting.
	- Mention the current metric scores.
	- Be assigned to yourself.
	- ~~Be tagged with at least one appropriate label.
	- Be associated with the HW1 milestone.~~

2. Create a pull request in the parent repository, which must:
	- Reference the issue created above.
	- Describe the fix and improvement to the score.

3. Answer the following questions on Gradescope about the metric you chose:

	    -   What properties do we care about, and how do we measure it?

	    -   What is being measured? Does it (to what degree) capture the thing you care about? What are its limitations?

	    -   How should it be incorporated into process? Check in gate? Once a month? Etc.

	    -   What are potentially negative side effects or incentives?

## Grading

This homework is worth 100 points. Running the project, making the
change, and committing it properly constitutes 50 points (50%), and the reflection questions constitutes 50 points (50%).

To receive full credit for the group component, we expect:

- The correct use of tools and technology, including Git, GitHub, and Lighthouse.

- Answers to the questions that demonstrate understanding of the benefits and limitations of software metrics, specifically in the context of Teedy. This analysis should go beyond superficial statements, mere descriptions, and truisms, which ties specifically to the context of this assignment.
