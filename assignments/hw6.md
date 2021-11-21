---
layout: page
title: HW06 Open Source Excursion
permalink: /assignments/hw6
parent: Assignments
---

# 17-313: Foundations of Software Engineering

## Homework 6: Open Source Excursion

In this assignment, your high-level goal is to produce and submit a non-trivial modification or extension to an open-source project in a way that maximizes the chances that the project maintainers accept it. 

If you demonstrate to us that your change has been accepted and integrated into the project’s code base, you will get **20 (6%) bonus points**. Your team will select an open source project, select a change to implement, actually contribute to the project, and present your insights to the class. You will individually reflect on your teamwork and open source experience.

| Part | Deliverable               | Points | Due Date |
|------|---------------------------|--------|------|
| A    | **[Project & Task Selection](#part-a-project--task-selection)**{: .label .label-red } | 60    |  23-Nov    |
| B    | **[Project Presentations](#part-b-project-presentations)**{: .label .label-red }       | 80     |  6-Dec    |
| C    | **[Project Report](#part-c-project-report)**{: .label .label-red }            | 100    |  9-Dec    |
| D    | **[Individual Reflection](#part-d-individual-reflection)**{: .label .label-red }     | 80     |   9-Dec   |
| Bonus   | **If changes get accepted**    | 20     | 16-Dec    |

<details>
    <summary> Learning Objectives </summary>
    <ul>
    <li>Holistically apply software engineering methods in the context of a real-world problem, including process, requirements, architecture, measurement, and quality assurance.</li>
    <li>Gain broad and deep exposure to the culture and practices of open-source communities</li>
    <li>Understand commonly used infrastructure used in open-source, and how to choose infrastructure when starting a new open-source project.</li>
    <li>Engage with an open-source community.</li>
    <li>Identify process issues and suggest improvements in real-world projects, including communication, collaboration, tooling, quality assurance, formal and informal rules and policies.</li>
    <li>Coordinate within a team and adopt practices for efficient teams.</li>
    <li>Understand a project’s architecture and design and make a decision about the feasibility of a proposed task.</li>
    <li>Divide and schedule work within a project.</li>
    <li>Discuss how agile practices affect development.</li>
    <li>Discuss business concerns and business models of software development.</li>
     </ul>
</details>

## Teamwork
This assignment is to be done in your assigned teams. All parts except the reflection should be done in a team context and submitted on behalf of the team. You are highly encouraged to openly discuss all issues that may arise in the process of working within the teams. If severe teamwork issues arise please contact the course staff.

## Overview

### 1. Select an open source project
You may select any active open source project in any language. You might find the following helpful: 

- [Trending on Github](https://github.com/trending)
- [Software Quality Awards](https://www.yegor256.com/award.html)
- [Issues that are labeled “up-for-grabs”](https://up-for-grabs.net)
- [goodfirstissue.dev](https://goodfirstissue.dev/)
- [A list of beginner friendly projects](https://github.com/MunGell/awesome-for-beginners)
- [Apache projects](http://www.apache.org/)
- [Mozilla projects](https://firefox-source-docs.mozilla.org/contributing/contributing_to_mozilla.html)
- Or any project you have used before!

The open source project you pick should be _active, with multiple contributors._ Previous students have lamented choosing dead or maintenance projects without sufficient community support. Do not make this mistake. 

If you have questions on if we would consider a project active, contact the course staff.

### 2. Select one or more bug fixes / feature extensions

*For the rest of this assignment, we will refer to bug fixes and feature extensions as tasks.* You are free to chose the task, as long as they:

* are taken from a bug report or feature request in a public database or message board. **Do not invent a task. Address a documented project need.**
* make changes to the project’s source code. **Pure documentation or design tasks are not appropriate**
* benefit from teamwork and are appropriate for your team size (i.e., do not select one small independent task per team member). You may choose one large task or several smaller, related tasks. The tasks should be scoped such that each team member spends **one week of development effort**

Communicate with the project owners the task you are trying to do so that they would be more likely to accept your request in the future. If you have questions on these criteria, contact the course staff.

### 3. Plan the task

As per Homework 2, plan before you start coding. You should identify risks and requirements, and develop a collaboration plan and schedule.

### 4. Perform the task

You should perform adequate quality assurance activities when writing code.

1. **Take further steps to understand the project’s code.**  
You might find it useful to engage in intra-team discussions using static or dynamic diagrams. You might also find it useful to elicit feedback on your ideas by communicating with members of the open-source community.

1. **Submit your changes to the project**  
Create any necessary documentation to enable acceptance of your code. Common contribution mechanisms include pull requests, emails to a project lead, or discussion board posts. You may also need to update the bug database. The project owners will review and evaluate your pull request, and you might need more work to get it approved.  
**You are required to submit your work to the open-source project**

1. **BONUS: Get your changes accepted**  
You will get a bonus **20 (6%) bonus points** upon acceptance. If your code is accepted after the homework deadline but before the final exam, inform the course staff.

### 5. Report, Presentation and reflection
You will report on your project and task selection, work, and experience in several ways (see below). This will include a group video presentation to the class.

## Deliverable Details

### Part A: Project & Task Selection

**Points**: 60  
**Due Date**: 23 November 2021

You will deliver an initial summary report on the project and task(s) your team have chosen to work on.

Start by researching candidate open source projects.  Refer to the open source recitation for resources and the consideration that you want to make. Communication with the maintainers of the open source projects is highly encouraged.
 
Once your team has settled on a project and one or more candidate tasks, build and execute the source code, and try to read/understand the codebase. Once again, your task should make changes to the project’s source code, **Pure documentation or design tasks are not appropriate**. You should explore the code to the point that you understand how your modification fits in the overall picture, and that you are convinced that it is both non-trivial but doable with the resources (time, team members) available.
 
In selecting a task, consider the functional and non-functional implications and requirements of your proposed task(s), as well as how it fits in the larger project structure.

Once you have selected a project and task(s), break them down into subtasks, consider their priority (must-haves & good-to-haves) and assign work to each team member. It is completely acceptable if you do not complete all your tasks, as long as you provide reasoning why that is not the case. You should anticipate and plan for the main risks.

**This deliverable will serve as a check-in to determine if the open source project and task chosen was reasonable**

Your report should include:
1.	**Overview and justification** (< 1 page)  
A report on the project you selected, summarizing the relevant characteristics you considered when making your selection. Beyond whatever additional information you collect in your research, include at least a name, a website link, and a brief description of the project (what it does, who uses it, etc). 
2.	**Successful build**  
Evidence that you can build and run the software (e.g., a screenshot or text output from a successful build, a screenshot of the running program). Getting an open-source project to build/run can be a huge effort, and we want to mitigate this risk.
3.	**Task(s) description** (< 1 page)  
- A brief textual description of your proposed change(s). In addition to your core task(s), you may choose to include a stretch task, depending on how difficult the changes end up being, you may not need to implement it. Note that if your actual changes deviate from the plan, we expect a short explanation with the final submission. 
- Explain why the task(s) is benefit from teamwork and are appropriate for your team size. 
4.	**Task link(s)**  
Evidence that the task(s) is/are requested by the community (links suffices).
5.	**Subtasks & assignments** (< 1 page)  
Use a table to summarize the following
- description of each subtask 
- priorities (must-haves & good-to-haves) & justification of priorities of the subtasks
- best-effort assignment of subtasks to team members.  
6. **Risk & Mitigation Strategies** (< 0.5 page)  
Provide a list of at least two relevant risks when it comes to working on the tasks in the open source project and corresponding mitigation strategies 

Submit the initial report covering the 6 points listed above as a **single PDF** file per team to **Gradescope**. Include the names of all team members on the title page and **ensure the document is structured to make it easy to find the 6 points.** Page limits are provided for guidance; we will not enforce them.

### Part B: Project Presentations
**Points**: 80  
**Due Date**: 6th December 2021, During Final Exam Timeslot

The Final Exam time is dedicated to group presentations **(in-person)** about your open source contributions. We will randomly assign the presentation order and put all the slide decks on a laptop. We expect all team members to take an active role in the presentation. We will provide feedback sheets (see appendix). There will be 3 minutes of questions from the class following each presentation. Presentation times **should not exceed 7 minutes (hard limit).**

The goal of the presentation is primarily to teach the class about the project to which you contributed, and your experiences. You should mention your contribution (the actual tasks), but we do not expect you to include, for example, any code or diagrams from your report, unless they’re helpful for supporting a point about your interactions with the project. Your presentation should cover the following three topics (in any order and structure you deem appropriate):

1.	**High-level project and task description**  
Describe the project in terms of its high-level goals and the context in which it operates. This may include a brief history and the business context, if interesting or relevant. For example, it may be interesting to note that a project was spawned from a closed-source operation, or that it competes primarily with a closed-source counterpart. Include a brief description of the task(s) you performed, such that the audience has sufficient context to understand your explanation of your experiences, below. You should not spend more than 1/2 of the video describing the project and your task(s).

2.	**Project governance and communication**  
Describe the processes and tools the project uses to coordinate among contributors. For example: Are these processes formal or informal? Provide an explicit description (possibly with a diagram) of the acceptance process used for efforts like the task you completed. If applicable, include standards or expectations regarding software engineering activities including requirements, architecture, and quality assurance; alternatively mention that no such standards exist.

3.	**Your experiences**  
Summarize your experiences (and what you learned!) interacting with this community of open source developers, focusing on any surprising or unusual aspects of the process or interaction. For example: Did you run into any trouble understanding, changing, or contributing to a large, pre-existing project? Were there unanticipated challenges in either implementing your change, or in getting the change submitted to and accepted by the project maintainers? Did the project collaboration process or culture help or hinder your effort in any way? Characterize any interaction you had with the team leadership and community, highlighting especially any useful/useless input you received. You may (but are not required to) also relate the experience from this homework assignment with relevant experience from internships or other projects.

Participation from all team members during the presentation is required. At the same time, every individual will be asked to provide constructive feedback for other presentations in class via an electronic form (which we will provide day-of).

Your summary of your experiences can be at whatever level of detail you think is interesting or informative. Given the time limit, selecting and highlighting the two or three most important or interesting observations is likely more useful than trying to be complete.

You must upload your slides as **a single PDF document** (separate from the report) to Gradescope.

### Part C: Project Report
**Points**: 100  
**Due Date**: 9 December 2021

After completing and submitting the modification, write a report about the tasks you have performed.

Your report should include:
1.	**Selected project** (1 paragraph)  
A brief description of the open source system to which you contributed. You may reuse text from Part A.
2.	**Project context and business model**  (<0.5 page)   
An analysis of the open-source project’s context and business model. This may include a short history of the project, competing open- and closed-source projects, or a discussion of the developers’ motivations to build this system. Essentially, we want to know why this project exists and why it is important.
3.	**Task description (per task)** (<0.5 page)    
A description of the tasks you have implemented and a high-level description of how you implemented them.
4.	**Submitted artifacts (per task)**  
Evidence of the code, documentation, or other artifacts you produced for the task, and evidence that you submitted them to the project. We prefer links to publicly available resources (repository, email, pull request, etc), but will accept a zip file of your artifacts with a screenshot documenting the submission.
5.	**QA strategy** (<1 page)  
Describe which QA activities you performed and justify why you selected these QA activities over others. Describe metrics if appropriate. The justification will likely refer to relevant requirements as well as to the project’s practices. 
6.	**QA evidence**  
Evidence of your quality assurance activities described above. For example, provide source code or links to source code of tests, provide test protocols, comments or protocols from code reviews, reports from static analysis tools, links to or screenshots from a continuous integration platform, and so forth.
7.	**Plan updates** (<1 page)  
A description and justification of deviations between your initial plans and your performed activities (as in Homework 2). Changes are expected, but they should be tracked and explained. Describe changes in scope (e.g., fewer tasks) and in the schedule and work allocation. Provide an updated schedule and note differences. Explain the causes of the changes, such as unanticipated risks. 
8.	**BONUS**  
Evidence that your changes have been accepted into the code base of the open source project in forms of links or screenshots.

Page limits are provided for guidance; we will not enforce them. Collect all parts in a **single PDF document with clear subsections** and the names of all team members and submit that file to **Gradescope**.

### Part D: Individual Reflection
**Points**: 80  
**Due Date**: 9 December 2021

Your indiviudal reflection should include:
1.	**Teamwork**  
You have been in the same team over the course of this semester (HW 2-6). Look back on the entire semester and reflect on your team experiences. The following questions may guide you: 
- What has worked, what hasn’t? 
- If you could start 313 or another course over with the same team, what would you change? 
- What have you learned about teamwork and your role in teamwork?
- (Optional) Do you have any feedback on what we can do next year to help students work more effectively in teams? Bear in mind that the instructor-assigned heterogeneous teams of 3-5 students is non-negotiable. We anticipate problems as part of the learning experience, but would like to avoid unduly frustrating situations.
2. **Testing**  
You have done testing in the past homeworks. Compare the testing you have done in the past homework, and what was done in the open-source project.
- What testing did they do in the open source project, what was surprising or different?
- What was similar to what we did in class?
- Were there automated testing in the open source project? If so, how was it done?
3.	**Open source**  
Reflect on your view of the open source movement and its ideals and related business models. In our initial survey, most of you indicated that you had very limited prior experience with open source. Have your views changed? The following questions may guide your reflection:
- Why have/haven’t you contributed previously? 
- Which claims of the open source movement are supported by your experience in this (and other) projects? 
- Do you expect to contribute to open source in the future?

Aim not to exceed 3 pages (soft limit). A good reflection document will include concrete statements about lessons learned, with clear supporting evidence, such as examples, to support them. You should cover all three topics, but the questions within the three topics are provided as initial guidance; you do not need to cover them all. A good document will discuss a few issues in depth instead of superficially answering the questions above. Submit your reflection document as a **single PDF with three clear subsections** to **Gradescope**.

