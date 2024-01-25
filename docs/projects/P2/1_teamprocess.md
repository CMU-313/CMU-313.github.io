# Project 2A: Collaborative Development

## Deliverables

**Team Process & Planning** – 70 points – due Thursday, September 14th, 11:59pm

- **Prerequisite:** [Team Setup](#team-setup)
- [Teamwork Contract](#teamwork-contract-40-pts) (35 pts)
- [Project Planning](#project-planning-40-pts) (35 pts)
- *[Extra Credit](#extra-credit-8-pts) (7 pts)*


## Team Setup

### Slack Channel

On the 17-313 Slack workspace, create a new **private** Slack channel that includes all your team members and the two TAs who are your team mentors (these are the same TAs that run your recitation — if you are unsure of who they are, ask in `#general`).

Use this Slack channel to collectively decide on a **team name**. Your team name should be unique, pronounceable, short, and something you would be proud to shout in your team cheer on the streets of Pittsburgh in the presence of small, impressionable, multilingual children. Once you have a team name, rename your team Slack channel to `#team-<teamname>`.

You can use this Slack channel for subsequent project-team related discussions or specialized Q&A with your TA mentors for the rest of the semester.

### GitHub Repository

You will be working on your team repository for this project. Once you have decided on a team name, go to the link below to set up your team:

[https://classroom.github.com/a/_nJ1-0ds](https://classroom.github.com/a/_nJ1-0ds)

!!! warning
    After you join a team on GitHub, you cannot change teams! Make sure that **only one** of you creates the team, and make sure that the remaining teammates join the right team.

Once you enter your team name, Github will automatically create a repository for your team. You should then create a **Github Project board** for your repository (you can follow the steps from the [GitHub Exercise](/projects/P1/github/#setting-up-a-project-board) or the first recitation).

You should use this team repository for all your development, and be sure to use good development practices, including keeping your commits cohesive and your commit messages informative. The same resources mentioned above provide more details on our guidelines.

We will be grading you on how well you follow the process we used for Project 1 and utilize this Project board:

- Create issues for feature improvements or bug-fixes
- When creating issue, assign team members and tag with appropriate labels
- Create a pull request and reference the issue it will be resolving
- Provide feedback to pull requests
- Use a Kanban board to track your workflow

For this project, you will create issues or pull requests **directly in your team repository**. We will use your commit history and issue/pull request activity on Github to assess both your teamwork process and each member’s individual contributions towards the project. It is **not** acceptable for one person to commit all the work after synchronizing through other means.

For each code-based deliverable, we will look at a snapshot of your repository at the deadline. This will often be done by asking you for a screenshot or commit link submitted via Gradescope.

### Setup Activity Action

To help you to understand your contributions through the semester. We added an `activity-action` for you, which automatically pulls the commit and issue histories and updates the `README.md` file in the main branch.

To enable `activity-action`, you need to create a Github token and add that to your team repository. You can create a new token by going to your profile settings: `Developer settings` > `Personal access tokens` > `Tokens (classic)` > `Generate new token`. You do **NOT** need to select any scopes. Set the expiration date on `May 24, 2024`, and put note `17-313 Project Token`. > `Generate token`. Copy the generated token. **Do not close the page unless you finish the next step. You won't be albe to see it again!**

Next, you need to add the generated Github token to your repository secrets. Goto your repository page. Select `Settings` > `Secrets and variables` > `Actions` > `Secrets` > `New repository secret`. Name: `PERSONAL_GITHUB_TOKEN`; Value: the token you have just generated.

Once you start working on the project, you will see the action adding your contributions to the `README.md` file.

!!! warning
    Do not change anything in the  `README.md`, this file will be modified and overrided by the action. If you want to change anything, please change `README.md.tpl`.

!!! warning
    If you protect the main branch in your repository, it will prevents the action from updating the `README.md` file. To solve this issue, you you have to enable force pushes to the protected branch. See [documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule).



### Teamwork Self-Assessment

As the course moves into team-based projects, we will be releasing weekly self-assessments, each worth one participation point. These are meant to be short surveys and should not take more than a few minutes. They are intended to help you reflect on your team's process and prompt you to think about how to improve it. The first one will be released on **Friday, September 8th** and due the following **Friday, September 15th** (both at 11:59pm).


## Main Deliverables

### Teamwork Contract (35 pts)

When working with a team, it is important to discuss each team member’s background, and establish common expectations of the team. Miscommunication or the general lack of communication are often the most common causes of team conflict. 

!!! note "Team Conflict Example"
    A common conflict in working style is when there are team members who always want to get a headstart on their work, while there are team members who are fine with doing work a few days before the deadline. It causes panic in the former team members, while the latter team members feel frustrated as to why they are being rushed. 

As such, your first process task of the semester will be creating a teamwork contract with your teammates. It is a **1 - 2 page** document containing information that all teammates agree to follow. You should work on the contract **with all members present**. We recommend that you keep it to around 1 page, 2 page is a **hard limit.**

Additionally, **it is more important that you only include statements that the team will adhere to** than it is to fulfill the length requirement (quality over quantity!) You do not need to write full sentences (bullet points are okay), but your decisions must be clearly conveyed in the document.

You are free to include anything that your team deems necessary, but you should minimally address the following sections:

1. **Expectations**<br/>
How much time is each team member expected to be putting into working on projects? Punctuality? How would your team accommodate when unexpected commitments come up for a team member (e.g. interviews, sickness, competitions)?<br/><br/>
Do accommodate for the fact that project load can get heavier towards the end of the semester.<br/><br/> 

1. **Communication**<br/>
What platform (s) will your team be using to communicate? What’s the expected time to get a response? <br/><br/>
For any communication platforms you decide on, please test that everyone can receive notifications. We highly recommend using apps (Slack, Discord) over browser-based sites.<br/><br/>

1. **Meeting Schedule**<br/>
When and how will your team meet? What modality would it be? <br/><br/>
A strong recommendation would be to set up a recurring 1hr meeting blocked out for the rest of the semester, so that your team does not have to scramble to find a common meeting time each week. Teams that have recurring meetings are generally more successful in the class.<br/><br/>

1. **Responsibilities**<br/>
How will you divide responsibilities for each project? During meetings, who will be in charge of note taking, organizing & running those meetings? <br/><br/>
From past courses, we noticed the natural emergence of a project manager in teams, who ensures the project moves towards completion. We highly suggest that you consider how your team would rotate that role amongst team members over the course of the remaining projects. Throughout the semester, we will ask for documentation of your meeting notes, so be sure to keep them organized (we recommend using a shared Drive folder).<br/><br/>

1. **Equitable Contribution & Conflict Resolution**<br/>
What are the steps the team would take to address teammates who are contributing too little, and when will the team bring this up to the instructors? What are the steps to bring up and discuss potential teamwork issues? <br/><br/>
The first thing the staff will ask the student when they mention that they are facing team issues is if they have followed the steps on their team contract.<br/>

Feel free to seek the assistance of TAs and instructors in drafting this document. 

!!! note
    We will ask you to reference, reflect upon, and refine this document throughout this semester, and we will evaluate your team's process strategies and interactions through what you outline in this contract. Please ensure that everyone on your team thoroughly discusses each of the above sections and agree with the final decisions.

Once you have completed the contract itself, have all members sign and date the document as an indicator that all members have read the document and agreed to uphold all outlined items. Then, save the file as a PDF and upload it to Gradescope. Only one team member needs to make the submission; they can then add the rest of the teammates as group members for a group submission. 

We also **highly recommend** that you [bookmark](https://slack.com/help/articles/205239997-Pin-messages-and-bookmark-links) the teamwork contract in your team’s Slack channel.


### Project Planning (35 pts)

Before your team jumps into development, you must first determine what features to implement. Schedule and hold an initial project planning meeting with your team to complete the steps outlined below.

#### Functional Requirements - User Stories

During this meeting, discuss potential functional requirements of this project. Consider what possible use cases may be for this system and what features it should have to fulfill those needs. 

Then, document these functional requirements in the form of user stories that follow the guidelines discussed in lecture. All of your user stories should be in the format of "As a [role], I want [function], so that [value]".

**You should come up with at least two user stories per student in your group.**

!!! note "Formulating User Stories"
    Consider what are the different types of users that will be interacting with your system (your stakeholders) and what features they would want to have that the current NodeBB does not provide. You may want to reference features in existing Q&A systems (e.g. Piazza, Diderot) that may be desirable, or conduct interviews with your peers who could be a potential users of this system.

As a team, you should then come up with a prioritization ranking for each user story. The prioritization should be based on two factors 

- **Impact**: how essential is this user story to the overall functionality of the application to your stakeholders, how beneficial it would be to your stakeholders, and
- **Effort**: how much time/effort is required to implement this user story

Once you have your list of user stories, create a new GitHub Project board (click into Projects on your team repository). Then create two new columns to the left called **"User Stories"** and **"Backlog"**. At this point in time, you should have **"User Stories", "Backlog", "To-Do", "In Progress" and "Done"**, in that order from left to right. Feel free to add more columns if your teams decide that you need them during your development process

Add your user stories into the **"User Stories"** column using the **“+ Add item”** button at the bottom, create draft issues for each of your user stories.In the body of each of these draft issues, provide a brief but concrete justification of its prioritization ranking that your team decided on. You should order all the user stories in this column from highest to lowest priority.

#### Technical Requirements - Issues

Now that you have your prioritized list, consider the *technical requirements* of the various user stories and collectively decide on which one(s) you will be focusing on over the next two sprints. In this project (as like most projects), your team is aiming to maximize the amount of value you are delivering to your stakeholders given your constraints.

Your selected user stories should have relatively high priority based on your team's ranking, and you should actively take factors into consideration that may impact your development.

!!! note "Selecting Appropriate User Stories"
    Given the amount of variations in each team's user stories, it's hard to give concrete guideline on the number of user stories that a team needs to tackle. Teams could tackle 1 user story that requires major effort, or a few user stories that each requires lesser effort. 
    
    In general, we are expecting that user stories be selected given:

    - 2 sprints of 2 weeks each
    - number of team members on your team
    - assumption of 8 hours/week available per individual

    The course staff **is happy to discuss this with your team during OH** and we highly recommend you do so if your team is unsure. We will also be providing you with feedback during your first sprint's [checkpoint presentation](/projects/P2/2_firstsprint/#checkpoint-presentation-50-pts).

The feature(s) you plan to implement should not be purely cosmetic or arbitrary. We expect this to be a non-issue as most high priority features to make NodeBB usable in a course environment would require changes that span across the development stack.

!!! note
    An example of what would **not** be accepted is a cosmetic feature that only modifies a frontend UI component (i.e. changing the color of the navbar), or just the renaming of a field in the database.
    
    You may want to look ahead into parts 2B and 2C to check our specific requirements for your implementation.

Convert the feature(s) you decide to implement into technical requirements (i.e. what needs to be developed for this feature to work). Then, break these requirements down into manageable, assignable issues and document them on your Project board by adding them to “Backlog” column. At minimum, these issues should make use of GitHub features like milestones/labels/descriptions to denote:

- **Estimated effort** for each task
- **Dependencies** among tasks (if any)
- Initial **assignments** for team members
- **Milestones** to indicate which sprint the issue should be completed in (Sprint 1, Sprint 2, Stretch)
- **Acceptance criteria** that describes how you know this task is done - think about how you will test this feature

You should actively assign and move these issues across your Kanban board as your team makes progress. 

!!! note "A Note on Grading"
    We **will not** assess how accurately you predicted your development process, nor will we be giving points based on the complexity or quality of your changes. The focus of our evaluations will be on how you decompose the problem, how you respond to unexpected circumstances, and how you analyze and reflect on your experience later on.

    We **will** check your development progress at the end of each sprint. Please be proactive in your planning to ensure that you make notable progress in both of your sprints. We highly recommend reading ahead on what our expectations are for the end of each sprint as you plan your milestone goals.

Include a link to your GitHub board in your Gradescope submission. If you are unsure about your planned changes, you can ask for feedback from a member of the course staff!


### Extra Credit (7 pts)
Getting to know your colleagues in a friendly context can often lead to more effective collaboration; for example, healthy teams often get lunch together. To incentivize this, we will give your team extra credit for this assignment if you meet for a team bonding experience outside of a working session.

You might want to eat together, go out for boba, or hold a board game session. If someone on your team is not feeling well, you may also do a virtual activity such as an online gaming session (Drawphone, Skribbl.io, etc.) or social "Zoom lunch". 

To receive extra credit, share the photo or screenshot of your team activity with your TA mentors by sending it in your team Slack channel before the deadline. We encourage you to do these types of meetings often throughout the semester!


## Grading

To receive full credit for the teamwork contract, we expect:

- [ ] All sections listed above are addressed in a roughly 1-2 page PDF document submitted to Gradescope
- [ ] Document demonstrates a clear process outline that was discussed between and agreed upon by the teammates
- [ ] All group members’ signatures at the end of the document

To receive full credit for the project planning, we expect:

- [ ] A GitHub project board linked to your team repository with:
    - [ ] A User Story column containing at least two user stories per group member that satisfy the guidelines outlined in the sections above and in lecture
    - [ ] A Backlog column containing a series of GitHub issues describing the feature(s) that the team will tackle. Each issue makes use of GitHub features to denote all of the required information listed above
