---
title: "2B First Sprint"
nav_order: 20
---

# Project 2B: First Sprint

## Deliverables

**First Sprint** – 95 points – due Monday, September 28th, 11:59pm

- [Individual Process & Implementation Interim](#individual-process--implementation-interim-50-pts) (50 pts) - due Monday, September 28th, 11:59pm
- [Checkpoint Presentation](#checkpoint-presentation-45-pts) (45 pts) - due Sunday, September 27th, 11:59pm, **Presentation held during Recitation on Monday, September 28th**
- *[Extra Credit](#extra-credit-2-pts) (2 pts)*


## Individual Process & Implementation Interim (50 pts)

For this sprint, **each team member is individually responsible for implementing one issue from your Backlog** — this can be a standalone feature, or your slice of a larger feature the team is jointly building (see the note on scoping issues in [2A Team Process & Planning](1_teamprocess.md#project-planning-35-pts)). Pick up (or confirm) your assigned issue on the Project board and move it to "In Progress." Specifically, your issue should be assigned to you in the GitHub Project board using the assign feature.

Implement your issue on your own feature branch, named so it's clear who owns it (e.g. `<andrewid>/<short-description>`, following the branch naming guidance from Project 1). Once you have a working implementation, open a pull request from your branch back to the team repository, referencing the issue it resolves, so your teammates can start reviewing.

!!! note "Merging happens in Sprint 2"
    You do **not** need to merge your branch into `main` by the end of this sprint. Thoroughly testing and verifying your implementation, then merging it into `main`, is the core requirement of the [Second Sprint](3_secondsprint.md). For this checkpoint, we're looking at the state of your individual branch and PR, not `main`.  However, if you're collaborating with someone else on a related issue, you might want to pull their changes into your branch (or vice-versa) to ensure your progress is on the right track.

You should still follow best practices for collaborative development, such as using pull requests and code review, even at this stage — early, asynchronous feedback on an in-progress PR is valuable even if it isn't ready to merge yet.

A helpful resource for naming commits to practice best habits and make it easier for your teammates to review your code is [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/). Consider using this format to ensure your PRs have atomic, well named commits.

!!! tip
    We highly encourage taking a look at both [GitHub Exercise](https://github.com/CMU-313/CMU-313.github.io/blob/p2_f26/assignments/P1/github.md) and this (REALLY USEFUL) [guide](https://docs.google.com/document/d/1X490SwaJbtus0KPBsjKlnNZOxUs30upkSyIvWykXkrA/edit?usp=sharing) for making good issues, commits and PRs.

Be sure to **review each other’s code** - both from a quality assurance standpoint, but also so you have a better understanding of the codebase. Although code reviews can be done asynchronously, we encourage the first few to be done synchronously so you can discuss the changes with your teammates and learn more about the codebase.

Every member of your team **must** contribute to the implementation. One way we will evaluate this is that each team member must have their own named feature branch containing commits that implement their assigned issue. Failure to do so will result in a significant penalty to your grade.

You must push all of your changes to your feature branch in the **team repository** before the homework deadline. Unlike the previous assignment (P1), you should **not** submit your changes to the parent opencode repository.

Submit a link to your repository and your Github Project board onto Gradescope. For grading, we will take a snapshot of your repository (including open branches and PRs) and board right at the deadline and grade based on your progress there.


## Checkpoint Presentation (45 pts)

During the Week 5 recitation slot (**Monday, September 28th**), your group will give a 10-minute presentation describing your current progress, followed by a short 1-2 minute Q&A session where you can get feedback from the TAs and your peers.

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

The presentation slides should be exported into a PDF and submitted to Gradescope by the Sunday deadline. The original copy should also be in your team folder created by your TAs in Recitation 2. 

## Extra Credit (2 pts)
Getting to know your colleagues in a friendly context can often lead to more effective collaboration; for example, healthy teams often get lunch together. To incentivize this, we will give your team extra credit for this assignment if you meet for a team bonding experience outside of a working session.

You might want to eat together, go out for boba, or hold a board game session. Nearly anything outside of class, libraries and campus would work. (If you are unsure, feel free to ask a TA)

To receive extra credit, submit a photo of your team activity as part of the P2B EC gradescope submission before the deadline and include it in a folder in your shared google drive. We encourage you to do these types of meetings often throughout the semester!


## Grading

To receive full credit for the individual process and implementation, we expect:

- [ ] Your own named feature branch with a working implementation of your individually assigned issue
- [ ] You have opened a well-written pull request from your branch to the team repository, referencing your issue, with at least some teammate review/comments — the PR does not need to be merged yet (see Second Sprint)
- [ ] Fulfillment of implementation goals as outlined by the planned milestones, **or** a clearly written justification in the milestone description of why elements fell through
- [ ] An updated Project Board for the current progress
- [ ] Reasonable code structure and style, including documentation where appropriate
- [ ] Coherent commits of reasonable size with meaningful commit messages by all team members
- [ ] High quality usage of Git/GitHub tools, such as issues, milestones, pull requests, and commits
- [ ] Links to Commits and PRs individual you participated in

To receive full credit for the presentation, we expect:

- [ ] All team members to be present for the presentation (or have contacted their TAs ahead of time to request an absence) and to contribute towards presenting their team’s progress
- [ ] All of the material described above covered in the presentation
- [ ] PDF Slides uploaded to Gradescope for grading & feedback
- [ ] Google Slides located in shared Google Folder to confirm equal division of work


## Resources & Documentation

### opencode Development

We highly recommend that, before starting development, you take the time to analyze the codebase with your team using the code archaeology techniques you have learned. One good place to start is figuring out which package (e.g. `cli`, `desktop`, or the core agent/server logic) owns the feature area you're touching, and trying to make a small change in each.

You will find some resources to help you with development in the `README` of the opencode repository. Here are a few specific links to get you started:

* [opencode Documentation](https://opencode.ai/docs)
* [Bun Documentation](https://bun.sh/docs)
* [TypeScript Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)

!!! tip
    Different parts of the codebase may have their own package-level `README` with more specific setup or architecture notes (e.g. the desktop app's UI framework) — check for one in the package you're working in.
