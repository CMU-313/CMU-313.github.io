----
-layout: page
-title: HW01 Joining the team
-permalink: /assignments/hw1
-parent: Assignments
----

# 17-313: Foundations of Software Engineering

## Homework 1: Joining the team

### Learning goals

-   Familiarize yourself with an existing software project

-   Download, install and run an existing software project.

-   Run an evaluation tool and collect metrics

-   Evaluate the results of these metrics

### Background

Git and GitHub:
- [Git Documentation](https://git-scm.com/docs/gittutorial)
- [Git Flow](https://datasift.github.io/gitflow/IntroducingGitFlow.html)
- [GitHub Basics](https://guides.github.com/activities/hello-world/)
- [GitHub's Flow](https://guides.github.com/introduction/flow/)
- [GitHub Cross-Referencing](https://docs.github.com/en/github/writing-on-github/working-with-advanced-formatting/autolinked-references-and-urls#issues-and-pull-requests)

Docker:
- [Overview](https://docs.docker.com/get-started/overview/)
- [Images vs Containers](https://stackify.com/docker-image-vs-container-everything-you-need-to-know/)
- [Mounting Volumes](https://monkelite.com/how-to-mount-volumes-into-a-docker-container/)

### Specification

Welcome to the team! To start your journey on this project, your first
task is to become familiar with an existing piece of software.
Eventually you will be adding new features, but the first step is to
simply download, run, evaluate, and explore the current software
product. The project we will be building on this semester is an open
source document management system, the Mayan EDMS
([https://www.mayan-edms.com/](https://www.mayan-edms.com/))
system. 

We will be using a class-specific fork of Mayan, whose repository is
located at: https://github.com/CMU-313/Mayan-EDMS. This fork is based
off [v4.0.7](https://docs.mayan-edms.com/releases/4.0.7.html) 
(released June 11, 2021), and contains minor tweaks to make it easier
to modify and debug. Forking from this repository will also allow you
to send pull requests to the instructors, which is the primary way
of submitting code deliverables.

Your first step should be to read the documentation from Mayan EDMS, and
review the contents of the repository. There is documentation both
for users, and for developers.

Your next task is to simply download and run the system. There are
several ways to do this, but we strongly suggest that you build a Docker
container. While you may install locally, that is almost always
significantly more work then using Docker. The documentation for this is
available here:
([https://docs.mayan-edms.com/chapters/docker/building.html](https://docs.mayan-edms.com/chapters/docker/building.html)).
Be sure to use the CMU-313 repository on GitHub instead of the official
repository on GitLab.

Once you build a Docker image, you should run Mayan EDMS in a Docker
container. You may first need to set up containers for dependencies
such as Postgresql and Redis. Refer to the [Docker installation 
instructions](https://docs.mayan-edms.com/chapters/docker/install_simple.html), but
make sure to use the Mayan image that you just built instead of
pulling it from Docker Hub. We recommend [using Docker 
compose](https://docs.mayan-edms.com/chapters/docker/docker_compose.html),
which automates some of these tasks using a handy compose file.

If you ran Mayan EDMS successfully, you should be able to navigate to
`http://localhost` and see a web page with a login screen. 
You may customize the port number that Mayan will be deployed to (default is `80`).

**Troubleshooting**: If you have trouble building things locally, try pulling a
pre-built Docker image as shown in the [docs](https://docs.mayan-edms.com/chapters/docker/install_simple.html)
or using the upstream repository in order to precisely isolate the issue.
If it takes you more than a few hours to set all this up, STOP and ask for help
on Slack.

Once you have Mayan EDMS up and running locally, proceed to evaluate it
using the Google Lighthouse tool:
[https://developers.google.com/web/tools/lighthouse/](https://developers.google.com/web/tools/lighthouse/)).
You can run Lighthouse as a stand alone application, or using the audit
tab of google developer tools. After you run Lighthouse, it will give
you a score for various dimensions: Performance, Accessibility, Best
Practices, and SEO.

After looking over the metrics, pick one metric to improve. The
Lighthouse reports will give you some suggestions as to how to
accomplish this. The only requirements are that your change should
affect the top level score, and that the change should involve a commit
to the repo. HINT: Because of this, you might want to avoid trying to
change the performance score.

First, open an issue in the [parent 
repository](https://github.com/CMU-313/Mayan-EDMS) to declare
what aspect of Mayan you will be improving. You should look through
existing issues, if any, to avoid duplicates. In the issue
description, mention the current lighthouse score you observed
and the warning that you are targeting. 
Tag the issue with one or more of the existing labels
as appropriate, add it to milestone "HW1", and assign yourself.

In your own fork of Mayan, create a feature branch, implement the change,
test it out locally, and commit your changes. Your commit message(s) must
clearly describe what's changing.

Once you are satisfied, open a pull request in the parent repository. The PR
should [link the issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue) that you previously opened (e.g. using the
"resolve(s)" keyword), summarize the changes, and describe 
how much the Lighthouse score improved by due to your change.

After you have completed this task, we will ask you to reflect on the
nature of metrics. To do this, you will answer the following questions
about metrics, specifically in the context of Mayan EDMS. You should
focus your answers for each of these questions on the one top level
metric in Lighthouse that you chose to improve.

-   What properties do we care about, and how do we measure them?

-   What is being measured? Does it (to what degree) capture the thing you care about? What are its limitations?

-   How should this metric be incorporated into process? Check in gate? Once a month? Etc.

-   What are potentially negative side effects or incentives?

### Deliverables and Deadlines

There are three (3) deliverables and one (1) deadline for this homework.

*Individual Component -- 100 points -- due Thursday, September 9th, 23:59*

1. Create an issue in the parent repository, which must:
	- Mention the current Lighthouse scores.
	- Mention the Lighthouse-reported problem being targeted.
	- Be assigned to yourself.
	- Be tagged with at least one appropriate label.
	- Be associated with the HW1 milestone.

2. Create a pull request in the parent repository, which must:
	- Reference the issue created above.
	- Describe the fix and improvement to the Lighthouse score.

3. Create and submit a single **PDF document** to Gradescope, containing the following:

	-   A link to the pull request where you improved one of the lighthouse scores.

	-   A prose description of which metric you chose to improve, why you chose that metrics, and how you went about improving it.

	-   You should then answer the following questions about the metric you chose:

	    -   What properties do we care about, and how do we measure it?

	    -   What is being measured? Does it (to what degree) capture the thing you care about? What are its limitations?

	    -   How should it be incorporated into process? Check in gate? Once a month? Etc.

	    -   What are potentially negative side effects or incentives?

Your reflection document should be under two pages (soft limit).

### Grading

This homework is worth 100 points. Running the project, making the
change, and committing it properly constitutes 50 points (50%), and the
reflection document constitutes 50 points (50%).

To receive full credit for the group component, we expect:

-   The correct use of tools and technology, including Docker, Git, GitHub, and Lighthouse.

-   Answers to the questions that demonstrate understanding of the benefits and limitations of software metrics, specifically in the context of Mayan EDMS. This analysis should go beyond superficial statements, mere descriptions, and truisms, which ties specifically to the context of this assignment.
