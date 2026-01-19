# Project 2B: Collaborative Development

## Deliverables

**First Sprint** – 95 points - **Presentation held in Recitation on Monday, September 22nd**

- [Process & Implementation Interim](#process-and-implementation-interim-50-pts) (50 pts) - due Friday, September 26th, 11:59pm
- [Checkpoint Presentation](#checkpoint-presentation-45-pts) (45 pts) - due Sunday, September 21st, 11:59pm
- *[Extra Credit](#extra-credit-2-pts) (2 pts)*


## Process and Implementation Interim (50 pts)

Start by cloning the team repository and merging your individual changes from Project 1 into your team repository using proper git flow. This can mean using git cherry-pick or just copying and pasting your individual changes and writing appropriate commit messages. Once everyone has properly set up the repository on their local machines and committed their changes, you can now start development.

You should follow best practices for collaborative development such as using feature branches, pull requests, and code review. Individual changes should be committed to properly named branches for each core feature being implemented and make use of pull requests to merge changes together. 

A helpful resource for naming commits to practice best habits and make it easier for your teammates to review your code is [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/). Consider using this format to ensure your PRs have atomic, well named commits.

!!! tip
    We highly encourage taking a look at both [GitHub Exercise](/projects/P1/github/#setting-up-a-project-board) and this (REALLY USEFUL) [guide](https://docs.google.com/document/d/1X490SwaJbtus0KPBsjKlnNZOxUs30upkSyIvWykXkrA/edit?tab=t.0#heading=h.9lgvngivw7vj) for making good issues, commits and PRs.

Be sure to **review each other’s code** - both from a quality assurance standpoint, but also so you have a better understanding of the codebase. Although code reviews can be done asynchronously, we encourage the first few to be done synchronously so you can discuss the changes with your teammates and learn more about the codebase.

Every member of your team **must** contribute to the implementation. One way we will evaluate this is that each team member must have at least one commit as a part of the solution. Failure to do so will result in a significant penalty to your grade.

You must commit all of your changes to the main branch of your **team repository** before the homework deadline. Unlike the previous assignment (P1), you should **not** submit your changes to the parent NodeBB repository.

Submit a link to your repository and your Github Project board onto Gradescope. For grading, we will take a snapshot of your repository and board right at the deadline and grade based on your progress there.


## Checkpoint Presentation (45 pts)

During the Week 5 recitation slot (**Monday, September 22nd**), your group will give a 10-minute presentation describing your current progress, followed by a short 1-2 minute Q&A session where you can get feedback from the TAs and your peers.

Your slides should include the following information (the recommended slides amount is in parentheses):

1. **Title Slide (1 slide)** <br/>
Include your team name & the names of each team member<br/><br/>

2. **Project Planning (~1-2 slides)** <br/>
What user stories did your team choose to focus on? What feature(s) did you plan on implementing to fulfill them?<br/><br/>

3. **Development Progress (~1-2 slides per person)** <br/>
What have you changed so far? How did you test your changes? What have you learned about the codebase? How does this compare with your original milestone goals? If your team did not meet your goals, why? <br/><br/>
Each team member should describe the contributions they made. In this section, you must include a video demo of your current progress; if you were not able to make a working build, include screenshots that show your current progress and clearly explain what factors impeded your progress.<br/><br/>

4. **Process Overview (~1-2 slides)** <br/>
What process strategies (i.e. meeting frequency, code reviews) did your team use for the first sprint? Was it effective? Did you encounter any difficulties or have to make any changes?<br/><br/>

5. **Looking Ahead (~2-4 slides)** <br/>
What are some current risks and/or questions that your team has after completing the first sprint? Has your experience with the first sprint affected your planning of the second sprint? Do you need to rescope? Do you need to reevaluate your process?<br/><br/>
If you did not meet your development goals, you should outline what you plan to proactively change for this upcoming sprint.<br/>

!!! note "A Note on Participation"
    **Participation from all team members during the presentation is required.** If you are unable to attend in-person, send a Slack message to your recitation TAs with justifications **at least 24 hours before the start of your recitation**. You will then be permitted to present by submitting a recording of your segment of the presentation, which your teammate will play during the presentation.

The presentation slides should be exported into a PDF and submitted to Gradescope by the Sunday deadline.

### Extra Credit (2 pts)
Getting to know your colleagues in a friendly context can often lead to more effective collaboration; for example, healthy teams often get lunch together. To incentivize this, we will give your team extra credit for this assignment if you meet for a team bonding experience outside of a working session.

You might want to eat together, go out for boba, or hold a board game session. Nearly anything outside of class, libraries and campus would work. (If you are unsure, feel free to ask a TA)

To receive extra credit, submit a photo of your team activity as part of the P2B EC gradescope submission before the deadline and include it in a folder in your shared google drive. We encourage you to do these types of meetings often throughout the semester!


## Grading

To receive full credit for the implementation, we expect:

- [ ] Fulfillment of implementation goals as outlined by the planned milestones, **or** a clearly written justification in the milestone description of why elements fell through
- [ ] An updated Project Board for the current progress
- [ ] Reasonable code structure and style, including documentation where appropriate
- [ ] Coherent commits of reasonable size with meaningful commit messages by all team members
- [ ] High quality usage of Git/GitHub tools, such as issues, milestones, pull requests, and commits
- [ ] Well written and meaningful GitHub Pull Requests

To receive full credit for the presentation, we expect:

- [ ] All team members to be present for the presentation (or have contacted their TAs ahead of time to request an absence) and to contribute towards presenting their team’s progress
- [ ] All of the material described above covered in the presentation
- [ ] PDF Slides uploaded to Gradescope for grading & feedback


## Resources & Documentation

### NodeBB Development

We highly recommend that, before starting development, you take the time to analyze the codebase with your team using the code archaeology techniques you have learned. One good place to start is determining where the MVC (or frontend/middleware/backend) split is and trying to make a small change in each section.

You will find some resources to help you with development in the `README` of the NodeBB repository. Here are a few specific links to get you started:

* [NodeBB Documentation](http://docs.nodebb.org)
* **Frontend Development:**
    * [Benchpress Documentation](https://github.com/benchpressjs/benchpressjs)
    * [Bootstrap 3 Documentation ](http://getbootstrap.com/)
* **Server Development:**
    * [Node.js Documentation](https://nodejs.org/en/docs/)
* **Database/Backend:**
    * [Redis Documentation](https://redis.io/docs/)
    * [Redis CLI](https://redis.io/docs/manual/cli/)
