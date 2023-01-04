---
title: HW06 Open Source Excursion
---

# Homework 6: Open Source Excursion

In this assignment, your high-level goal is to produce and submit a non-trivial modification or extension to an open-source project in a way that maximizes the chances that the project maintainers accept it. 

If you demonstrate to us that your change has been accepted and integrated into the project’s code base, you will get **20 bonus points**. Your team will select an open source project, select a change to implement, actually contribute to the project, and present your insights to the class. You will individually reflect on your teamwork and open source experience.

| Part | Deliverable               | Steps | Points | Due Date |
|------|---------------------------|-------|--------|------|
| A    | **[Project & Task Selection](#part-a-project--tasks-selection-check-in)**{: .label .label-red } | 1 - 3 | 80    |  29-Nov    |
| B    | **[Project Presentations](#part-b-project-presentations)**{: .label .label-red }       |4 - 5| 100     |  12-Dec    |
| C    | **[Project Report](#part-c-project-report)**{: .label .label-red }             |4 - 5| 120 |  15-Dec    |
| D    | **[Individual Reflection](#part-d-individual-reflection-peer-evaluations)**{: .label .label-red }     | 5 | 20     |   15-Dec   |
| Bonus   | **If changes get accepted**    | 4 | 20     | 15-Dec    |

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
This assignment is to be done in your assigned teams. All parts except the reflection should be done in a team context and submitted on behalf of the team. You are highly encouraged to openly discuss all issues that may arise in the process of working within the teams. 

**Important Note**:
- We want to make sure that everyone is participating fully in the final project. For this project, we will be assessing participation in a variety of ways, including: artifact evaluation, self & peer evaluation (done as part of [individual reflection](#part-d-individual-reflection--peer-evaluations))
- Credit due for the team will be awarded based on evidence of full participation in the team. Partial participation will receive partial credit.

If severe teamwork issues arise please contact the course staff.

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

The open source project you pick should be _active, with multiple contributors._ Generally you want to pick projects that are **quick at reviewing & accepting PRs from external contributors** for a better chance of getting your bonus. Previous students have lamented choosing dead or maintenance projects without sufficient community support. Do not make this mistake. 

If you have questions on if we would consider a project active, contact the course staff.

### 2. Select one or more bug fixes / feature extensions

*For the rest of this assignment, we will refer to bug fixes and feature extensions as tasks.* You are free to chose the task, as long as they:

* are taken from a bug report or feature request in a public database or message board. **Do not invent a task. Address a documented project need.**
* make changes to the project’s source code. **Pure documentation or design tasks are not appropriate**
* benefit from teamwork and are appropriate for your team size (i.e., do not select one small independent task per team member). You may choose one large task or several smaller, related tasks. The tasks should be scoped such that each team member spends **one week of development effort**

**Communicate with the project owners the task you are trying to do so that they would be more likely to accept your request in the future.** If you have questions on these criteria, contact the course staff.

### 3. Plan the task

Once you have selected a project and task(s), break them down into subtasks, consider their priority and assign them to each team member. Identify a set of tasks as your core goal for this project, and another set of tasks as stretch goals.

You are expected to achieve your core goal for this project, and stretch goals as much as possible. We will work with you to adjust your goals during the check-in to ensure that they are appropriate your team size and timeframe.

As per previous homeworks, plan before you start coding. You should identify risks and requirements, and develop a collaboration plan and schedule. 

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
You will report on your project and task selection, work, and experience in several ways (see below). This will include a group presentation to the class.

## Deliverable Details

### Part A: Project & Tasks Selection Check-In 

**Points**: 80  
**Presentation Slide Deck Due Date**: 29th November 2022, 11:59pm  
**Presentation Date**: 30th November 2022 / 2nd December 2022 (Recitation after Thanksgiving) 

The recitation after thanksigiving will be dedicated to an **in-person** group presentation about your project and task selection.

- Presentations are **6 minutes, with 3 minutes feedback and Q&A**.
- The order of presentations will be randomly determined.
- Participation from all team members during the presentation is **required**.
- For full credit, you would have to be on time for the presentation session (within 5 minutes of recitation start time). If you are unable to attend in-person, you have to send a slack message to your TA with justifications **24 hours before the start of your recitation** else you will receive **no credit** for this part of the assignment. You will then present by recording your segment of the presentation, which your teammate will play during the presentation.

#### Guidance
- Pick a project following [Step 1](#1-select-an-open-source-project) and the open source recitation
- Select tasks following [Step 2](#2-select-one-or-more-bug-fixes--feature-extensions)
- Plan your tasks following [Step 3](#3-plan-the-task)

**Your group presentation will serve as a check-in to determine if the open source project and task chosen was reasonable**

Your **6-minute** check-in presentation should include (the recommended slides amount is in parenthesis):

1.	**Overview and justification** (~1 slide)  
An overview on the project you selected, summarizing the relevant characteristics you considered when making your selection. Beyond whatever additional information you collect in your research, include at least a name, a website link, and a brief description of the project (what it does, who uses it, etc). 

2.	**Successful build** (~1 slide)  
Evidence that you can build and run the software (e.g., a screenshot or text output from a successful build, a screenshot of the running program). Getting an open-source project to build/run can be a huge effort, and we want to mitigate this risk.

3.	**Task(s) description** (~ 2-3 slides)  
    - A brief textual description of your proposed change(s). In addition to your core task(s), you may choose to include a stretch task, depending on how difficult the changes end up being, you may not need to implement it. Note that if your actual changes deviate from the plan, we expect a short explanation with the final submission. 
    - A justification why the task(s) benefit(s) from teamwork and are appropriate for your team size. 

4.	**Task link(s)**  (~ 1 slide)    
Evidence that the task(s) is/are requested by the community (links suffices).

5.	**Subtasks & assignments** (~ 1 slide)  
A table to summarize for each subtask
    - description of each subtask 
    - priorities & justification of priorities of the subtasks (and if it's part of core goals or stretch goals)
    - assignment of subtasks to team members.  

6. **Risk & Mitigation Strategies** (~ 1 slide)   
A list of at least two relevant risks when it comes to working on the tasks in your selected open source project and corresponding mitigation strategies 

Submit the presentation deck listed above as a **single PDF** file per team to **Gradescope**. You will be presenting this in the recitation after Thanksgiving break. 

### Part B: Project Presentations
**Points**: 100  
**Presentation Slides Due Date**: 12th December 2022, 11:59pm  
**Presentation Date**: 13th / 15th December 2022, 5.30pm - 8.30pm. (During final exam timeslot)

The Final Exam time is dedicated to group presentations **(in-person)** about your open source contributions.

- Presentations are **7 minutes long, with 3 minutes Q&A**.
- The order of presentations is randomly determined.
- Participation from all team members during the presentation is **required**.
- Every individual will be asked to provide constructive feedback for other presentations in class via an paper form (which we will provide day-of).
- For full credit, you would have to be on time for the presentation session (within 10 minutes of start time). If you are unable to attend in-person, you have to send an email with justification to all instructors and cc your recitation TAs, a **week before** your final exam timeslot, so that appropriate arrangements can be made. Exceptions to notification deadline will only be made for unforseeable circumstances.

The goal of the presentation is primarily to share with the class the project to which you contributed, and your experiences. Your presentation should cover the following topics (the recommended slides amount is in parenthesis):

1.	**High-level project overview** (~1 slide) 
    - Describe the project in terms of its high-level goals and the context in which it operates. This may include a brief history and the business context. E.g. it may be interesting to note that a project was spawned from a closed-source operation, or that it competes primarily with a closed-source counterpart. 

2. **Brief description of the task you performed** (~2 slides)
    - **Brief** description of the task(s) you performed, such that the audience has sufficient context to understand your explanation of your experiences.
    - We **do not expect you to include, for example, any code or diagrams from your report**, unless they’re helpful for supporting a point about your interactions with the project.
    - A demo is appreciated, but please do a screen recording instead of a live demo.

3.	**Project processes and communication** (~2 slides)  
Describe the processes and tools the project uses to coordinate among contributors. For example: Are these processes formal or informal? Provide an explicit description (possibly with a diagram) of the acceptance process used for efforts like the task you completed. If applicable, include standards or expectations regarding software engineering activities including requirements, architecture, and quality assurance; alternatively mention that no such standards exist.

4.	**Your experiences** (~2 slides)  
Summarize your experiences (and what you learned!) interacting with this community of open source developers, focusing on any surprising or unusual aspects of the process or interaction. For example: 
    - Did you run into any trouble understanding, changing, or contributing to a large, pre-existing project?
    - Were there unanticipated challenges in either implementing your change, or in getting the change submitted to and accepted by the project maintainers?
    - Did the project collaboration process or culture help or hinder your effort in any way? Characterize any interaction you had with the team leadership and community, highlighting especially any useful/useless input you received. You may (but are not required to) also relate the experience from this homework assignment with relevant experience from internships or other projects.

Your summary of your experiences can be at whatever level of detail you think is interesting or informative. Given the time limit, selecting and highlighting the two or three most important or interesting observations is likely more useful than trying to be complete.

You must upload your slides as **a single PDF document** to Gradescope.

### Part C: Project Report
**Points**: 120  
**Due Date**: 15 December 2022, 11:59pm

After completing and submitting the modification, write a report about the tasks you have performed.

Your report should include:

1.	**Selected project** (1 paragraph)  
A brief description of the open source system to which you contributed. You may reuse text from Part A.

2.	**Project context and business model**  (<0.5 page)   
An analysis of the open-source project’s context and business model. This may include a short history of the project, competing open- and closed-source projects, or a discussion of the developers’ motivations to build this system. Essentially, we want to know why this project exists and why it is important.

3.	**Task description (per task)** (<0.5 page)    
A description of the tasks you have implemented and a high-level description of how you implemented them.

4.	**Submitted artifacts (per task)**  
Evidence of the code, documentation, or other artifacts you produced for the task, and evidence that you submitted them to the project. This would likely be links to publicly available resources (repository, email, pull request, etc).

5.	**QA strategy** (<1 page)  
Describe which QA activities you performed and justify why you selected these QA activities over others. Describe metrics if appropriate. The justification will likely refer to relevant requirements as well as to the project’s practices. 

6.	**QA evidence**  
Evidence of your quality assurance activities described above. For example, provide source code or links to source code of tests, provide test protocols, comments or protocols from code reviews, reports from static analysis tools, links to or screenshots from a continuous integration platform, and so forth.

7.	**Plan updates** (<1 page)  
A description and justification of deviations between your initial plans and your performed activities (as in Homework 2). Changes are expected, but they should be tracked and explained. Describe changes in scope (e.g., fewer tasks) and in the schedule and work allocation. Provide an updated schedule and note differences. Explain the causes of the changes, such as unanticipated risks. 

8.	**BONUS**  
Evidence that your changes have been accepted into the code base of the open source project in forms of links or screenshots.

Page limits are provided for guidance; we will not enforce them. Collect all parts in a **single PDF document with clear subsections** and the names of all team members and submit that file to **Gradescope**.

### Part D: Individual Reflection & Peer Evaluations
**Points**: 20  
**Due Date**: 15 December 2022, 11:59pm

Your indiviudal reflection should include:

1. **Self Evaluation**   
Describe the work you have done in this project (e.g. code artifacts, documentation) as well as efforts towards helping your team towards completing this project (e.g. research, organizing meetings, running meetings).

2. **Peer Evaluations**  
Describe the specific work **each of your team members** have contributed towards this project. Describe both tangible (e.g. code artifacts, report & slides making, documentation) and intangible (e.g. organizing & running meetings, communicating expectations) contributions. Do point out teammates that you think are exceptional to work with in this project as well.

3.	**Teamwork**  
You have been in the same team over the course of this semester (HW 2-6). Look back on the entire semester and reflect on your team experiences. The following questions may guide you: 
    - What has worked, what hasn’t? 
    - If you could start 313 or another course over with the same team, what would you change? 
    - What have you learned about teamwork and your role in teamwork?
    - (Optional) Do you have any feedback on what we can do next year to help students work more effectively in teams? Bear in mind that the instructor-assigned heterogeneous teams of 3-5 students is non-negotiable. We anticipate problems as part of the learning experience, but would like to avoid unduly frustrating situations.

A good reflection document will include concrete statements about lessons learned, with clear supporting evidence, such as examples, to support them. Submit your reflection on **Gradescope**.

