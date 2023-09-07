# Project 2B: Collaborative Development

## Deliverables

**First Sprint** – 95 points – due Tuesday, September 26th, 11:59pm

- [Process & Implementation Interim Snapshot](#process--implementation-interim-50-pts) (50 pts)
- [Checkpoint Presentation](#checkpoint-presentation-50-pts) (45 pts) - **Held in Recitation on Wednesday September 27th / Friday September 29th**


## Process & Implementation Interim (50 pts)

Start by cloning the team repository and merging your individual changes from Project 1 into your team repository using proper git flow. You may also delete the `hw1.yaml` workflow found in `.github/workflows`. Once everyone has properly set up the repository on their local machines and committed their changes, you can now start development.

!!! question "What if I did not successfully translate my file in Project 1?"
    If you do not need to modify that file in order to implement your team's feature, then you do not need to merge your file into your repository. You will not be penalized for not merging in your Project 1 file.

You should follow best practices for collaborative development such as using feature branches, pull requests, and code review. Individual changes should be committed to properly named branches for each core feature being implemented and make use of pull requests to merge changes together. 

Be sure to **review each other’s code** - both from a quality assurance standpoint, but also so you have a better understanding of the codebase. Although code reviews can be done asynchronously, we encourage the first few to be done synchronously so you can discuss the changes with your teammates and learn more about the codebase.

To fit with the translation efforts described in Project 1, **any new code introduced to the codebase should be in TypeScript**. This does mean that you may need to translate existing files to fulfill this requirement.

!!! note "Using Translations from Project 1"
    Most of the existing files should have been translated by your classmates in Project 1! Feel free to reference their translations for your own uses - for citation purposes, include a short comment at the top of your file that cites the original translator and a link to where you found the translation, for example:

    ```
    // Referenced @student’s TypeScript translation from P1: [PR link]
    ```

Every member of your team **must** contribute to the implementation. One way we will evaluate this is that each team member must have at least one commit as a part of the solution. Failure to do so will result in a significant penalty to your grade.

You must commit all of your changes to the main branch of your **team repository** before the homework deadline. Unlike the previous assignment, you should **not** submit your changes to the parent NodeBB repository.

Submit a link to your repository and your Github Project board onto Gradescope. For grading, we will take a snapshot of your repository and board right at the deadline and grade based on your progress there.


## Checkpoint Presentation (45 pts)

During the Week 5 recitation slot (**Wednesday September 27th / Friday September 29th**), your group will give a 10-minute presentation describing your current progress, followed by a short 1-2 minute Q&A session where you can get feedback from the TAs and your peers.

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

The presentation slides should be exported into a PDF and submitted to Gradescope by the Tuesday deadline.


## Grading

To receive full credit for the implementation, we expect:

- [ ] Fulfillment of implementation goals as outlined by the planned milestones, **or** a clearly written justification in the milestone description of why elements fell through
- [ ] An updated Project Board for the current progress
- [ ] Reasonable code structure and style, including documentation where appropriate
- [ ] Coherent commits of reasonable size with meaningful commit messages by all team members
- [ ] High quality usage of Git/GitHub tools, such as issues, milestones, pull requests, and commits

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
