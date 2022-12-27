---
title: HW02 Learning the Codebase
---

# Homework 2: Learning the Codebase

## Learning Goals

- Learn about the design and implementation of an existing software project that you will build upon this semester
- Collaborate with your teammates to design and implement a small feature addition or modification to that software project
- Practice version control and development best practices within the context of a group assignment


## Specification

Now that you have onboarded to 17-313, setup your development environment, and met your team, upper management has tasked you with building a graduate student admissions system over the course of the semester (described below).
Rather than creating a new admissions system from scratch, management has decided that you and your team will repurpose and adapt an existing document management system, Teedy.
Beyond being a pretty good document management platform, Teedy provides complex features that you expect will be useful, like tagging, workflows, and fine-grained permissions and ACLs (access control lists).

Despite its considerable functionality, Teedy is still missing many of the basic features that you expect to find in the most rudimentary of admissions systems and needs changes to be better fit for purpose.
Your goal in this homework assignment is to dig into the implementation of Teedy to better understand how it's designed and fits together, and to learn more about its associated technologies.
To that end, your team has been tasked with implementing a small feature change or addition that requires you to make a change in each of the following layers of Teedy's stack:

* Java backend: `docs-core/src/main/java/com/sismics/docs`
* REST middleware: `docs-web/src/main/java/com/sismics/docs/rest`
* Angular.js frontend: `docs-web/src/main/webapp`

## Team and GitHub repository.

You will be working on your team repository for this project. First,
collectively choose a **team name.** Your team name should be unique,
pronounceable, short, and something you would be proud to shout in your
team cheer on the streets of Pittsburgh in the presence of small,
impressionable, multi-lingual children. Then, go to the link below to
set up your team: once you provide your team name, it will automatically create
a repository for your team.

**WARNING: After you join a team, you cannot change teams! Make sure
that only one of you creates the team, and make sure that the remaining
teammates join the right team.**

After you have read the above warning, go here to set up your team:

**[https://classroom.github.com/a/ZjoPJFMC](https://classroom.github.com/a/ZjoPJFMC)**

Use the team repository for all your development, and be sure to use
good development practices, including keeping your commits cohesive and
your commit messages informative.

We will be grading you on how well you follow the process we used for HW1 and the recitation activity:
- create issues for feature improvements or bug-fixes,
- when creating issue, assign team members and tag with appropriate labels,
- and create a pull request and reference the issue to merge the changes.

In this project, however, you will not create an issue or a pull request in the parent repository,
but in your team repository, like what you did in the recitation 1.
It is not acceptable for one person to
commit all work after synchronizing through other means. This will
factor into your grade.

The *code, testing, and documentation deliverables* below will be taken
by snapshotting your repository at the deadline.


## Project Description

CMU has over 7,000 graduate students.
The university uses a software system to manage the graduate student admissions process, including collecting relevant information from applicants, accepting recommendation letters from third-parties, showing this information to the admissions committee and accepting ratings and commentary from the admissions committee to support decisions, and notifying applicants of the decision.
This system is old, clunky, and universally disliked.

You and your team are developing a new system.
Requirements for this new system remain a bit vague, and we are looking for you to put your own expereince and creativity into developing a better solution.
Your point of contact insists primarily that the new system needs to be "less garbage" than the current system.
When pressed for details, she elaborates that faculty complain that the current system makes it too difficult to evaluate the applicants; students (applicants) and their letter writers complain that the system is hard to use.
Everyone finds configuration and management difficult.


## Deadlines and deliverables

This homework has two (2) deadlines and two (3) deliverables. The
deliverables are described below: 




### **Planning---Team (due Thursday, Sept 22, 23:59) -- 20 points** 
You must create an issue in your group's Teedy repository that:

  - Describes the new feature (or change to an existing feature) that you will implement for this assignment.
    The feature/change does not need to be large, but it **must require code changes across the entire Teedy stack.**
    The goal of this assignment is not to maximize value for your project client but instead to learn as much as possible about the existing codebase.

  - Roughly outlines the changes that need to be made at each level in the Teedy stack and specifies which team member(s) are responsible for implementing those changes. 

  - **If you are unsure about your planned changes, ask for feedback on your issue from a member of the course staff!**

### **Implementation:--Team (due Thursday, Sept 22, 23:59)  -- 80 points**
  - You should follow best practices for collaborative development such as using feature branches, pull requests, and code review (e.g., tackling each layer of the stack in a separate PR).  Specifically your team should collaborate on this feature by committing changes to a branch named for the feature you are implementing. 
  - Every member of your team must contribute to the implementation. One way we will evalute this is that each team member must have at least one commit as a part of the solution.
    Failure to do so will result in a significant penalty to your grade.
  - You must commit all of your changes to the `main` branch of your repository before the homework deadline.
    Unlike the previous assignment, you should not submit your changes to the parent Teedy repository.

### **Group Presentation:--Team (due Tuesday, Sept 27, 23:59, presentation uploaded to gradescope)  -- 30 points**
During the Week 5 recitation slot, your group will give a short 10-minute presentation describing your changes (e.g., what you changed, how you changed the code, how you tested your changes) and what you learned about the codebase.  Each team member should be prepared to describe the changes they made.  In order to make the deadline fair across all sections, the presentation should be submitted to gradescope by Tuesday Sept 27th, 11:59pm. 

### **Individual Reflection:--Team (due Tuesday, Sept 27, 23:59)  -- 30 points**
 You will answer individual reflection questions on Gradescope (HW2 Individual Reflection).  We will ask you to describe the changes that you personally made, how you made those changes, and what you would do differently if given more time.

### **Extra credit:--Team (due Tuesday, Sept 27, 23:59)  -- 8 pts (5% of the overall assignment grade)**
 
Getting to know your colleagues in a friendly context can often lead to more effective collaboration; healthy teams often get lunch together, for example.  To incentivize this, we will give your team 5% extra credit for this assignment if you meet for a team outside of a working session.  You might want to eat together, or go out for boba.  If someone on your team is not feeling well, you may also do a virtual activity such as an online gaming session (drawasaurus?) or social "zoom lunch". On the 17-313 Slack workspace, create a new **private channel** (name it `team-<teamname>`) that includes all your team members and the two TAs who are your team mentors (these are the same TAs that run your recitation---if you are unsure, ask on `#general`). Share the photo or screenshot of your team activity on the slack channel with your TA mentors to receive the 5% extra credit. You can also use this slack channel for subsequent project-team related discussions or specialized Q&A with your TA mentors for the rest of the semester.


## Grading

You will be graded as a team, with an individual component. This
homework is worth 160 points, with an additional 8 points of extra credit available. 
