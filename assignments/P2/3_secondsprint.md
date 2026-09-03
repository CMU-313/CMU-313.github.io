---
title: "2C Second Sprint"
nav_order: 30
---

# Project 2C: Second Sprint

## Deliverables

**Second Sprint** – 110 points – due Friday, October 9th, 11:59pm

- [Individual Final Implementation](#individual-final-implementation-60-pts) (60 pts)
- [Team Integration](#team-integration-30-pts) (30 pts)
- [Process & Team Reflection](#process-and-team-reflection-10-pts) (10 pts)
- [Individual Reflection](#individual-reflection-10-pts) (10 pts)
- *[Extra Credit](#extra-credit-2-pts) (2 pts)*

## Individual Final Implementation (60 pts)

This sprint is where your individual Sprint 1 branch gets finished and thoroughly verified. Be sure to continue following best practices for collaborative development similar to the previous sprint.

As you become more familiar with the codebase, we have higher expectations for the final deliverables of this sprint. Specifically, for **your individual issue from Sprint 1**, we expect to see:

- **Thorough Testing & Verification**
    - Before merging, thoroughly test your implementation and add tests to the test suite that demonstrate the functionality you implemented. Your tests should cover the changes you made. They should also follow the acceptance criteria you set from the initial planning in 2A. 
    - Your PR should clearly explain why your testing and verification are enough to ensure your code is correct.
    - CI should pass for your feature branch.

- **User Documentation**
    - Contribute a section to your team's `UserGuide.md` (create it in the root directory of your repository if it doesn't already exist) describing how to use and user test the feature you implemented.
    - Provide a link/description of where your added automated tests can be found, along with a description of what is being tested and why you believe the tests are sufficient for covering the changes that you have made.

As with the first sprint, **you must individually contribute to the team's overall implementation**. Failure to do so will result in a significant penalty to your grade.

## Team Integration (30 pts)

Once each team member's issue is implemented and verified, the team is responsible for integrating everyone's work into a single, working `main` branch.

- **Merge into `main`**
    - Open (or update) a pull request from each individual branch back to your team repository's `main` branch, get it reviewed by a teammate, and merge it
    - **Full credit requires every team member's Sprint 1 issue which has passing CI to be merged into the team repository's `main` branch by this deadline.** Work that is complete and tested but still sitting on an unmerged feature branch will not receive full credit for this requirement
    - Resolve any conflicts or integration issues that come up as everyone's features are combined — this is a normal and expected part of teamwork, and how you handle it is part of what we're evaluating

!!! warning "Incomplete Individual PRs"
    If a team member's feature branch is NOT passing CI, your team is not responsible for merging it in, and that team member will receive zero points for Team Integration, but the rest of the team is still eligible for full points.

!!! note "GitHub Actions"
    GitHub Actions should be enabled on your repository. By this deadline, CI passing on your individual branch is required for full credit (see above) — this isn't the "reasonable to have red feature branches" leniency from earlier in the project. Your team should also keep `main`'s build passing consistently as branches get merged in.

You must merge all of your changes into the main branch of your team repository before the homework deadline. Unlike Project 1, you should not submit your changes to the parent opencode repository.

Submit a link to your repository and your Github Project board onto Gradescope. For grading, we will take a snapshot of your repository and board right at the deadline and grade based on your progress there.

## Process and Team Reflection (10 pts)

!!! warning "Use of Generative AI discouraged"
    Historically, we have found the use of generative AI tools for this part of the assignment has resulted in poor work being submitted. However, if only part of the assignment has low quality AI text, we will use the google drive edit history to determine individual scores for participation in the reflection.

After coding is complete, reflect on your experience as a team. Again, we look for honest reflection, which will likely include reflection on failures. **We will not grade whether you predicted the effort correctly, but rather what you have learned**. 

You will see the following groups of questions on Gradescope. **We are expecting you to create a Google Doc inside of your team folder to draft your answers, then submit your final answers to Gradescope.** In Gradescope, you should attach a link to the Google Doc. It is expected that there should be an even distribution of work done by team members and we may take a look at the documents history if we feel there is a need to confirm that. 

1. **Actual Schedule:** Document the actual schedule of your development process into either an organized list or table. You should include all of the tasks that each team member actually performed and the approximate amount of time each took. Your commit history and other documentation should help you with this.

2. **Schedule Deviations:** Reflect on the differences between your planned and actual schedule, and answer the following questions:
    - Which milestones were predicted correctly and what was re-planned? 
    - Was there anything you did not plan for initially or that you had to drop in the end? 
    - What were the reasons for the above changes and could they have been foreseen with better planning?

3. **Development Process:** Reflect on the process (specifically, the steps each team member took to contribute to the codebase) you followed during the project, and answer the following questions: 
    - What was the process you initially planned to follow? What was the process you actually followed?
    - Was the process effective? Why or why not?
    - Did you skip steps or adopt additional techniques during the project? What were they and why did you do so?

4. **Meeting Minutes:** Attach all meeting minutes kept throughout the project, which should include information about the agenda/topics discussed, decisions made, and work assignments.

5. **Team Experience:** Reflect on your experience working as a team. You should discuss as a team on the aspects of communication, scheduling, responsibilities and equitable contributions. Answer the following points by providing at least three actions that your team will take to improve in the future (feel free to have more than one in category and zero in another, they should just add up to three):
      - What should your team **keep doing?** What worked well, and why? 
      - What should your team **start doing?** What didn't work so well, and why? What will you do differently?
      - What should your team **stop doing?** What are some bad habits that your team should avoid in the future and why?

    !!! warning "Support your claims"
        You should reference your meeting minutes to support your claims and provide examples. A weakly supported statement would be as follows:
        > “We will communicate better, because miscommunication caused issues" 
        
        You should support your statements with examples from the development experience. For example: 
        > "In the future, we will try to use [such-and-such a process] for clearly documenting and communicating such design decisions, rather than [the process we did follow/failed to follow]. One of our [main challenges/development slowdown/quality problems] was the integration of components A and B, because the API for A was not well-understood by the developer of B. "

6. **Teamwork Contract:** Based on the process and team reflection above, update your teamwork contract. Did you encounter any issues or unexpected experiences that your original contract did not foresee? Feel free to add in any other clauses if necessary to your team contract. Upload your new teamwork contract (be sure to sign and date it), and **highlight the changes you made in yellow.**

Being able to communicate effectively is an important software engineering skill. As such, your reflection should be well-written and easy to read. Be sure to leave time after writing for revision and proofreading.

!!! note "Reflection Grading"
    One of the main purposes of this project is to encourage in-depth analysis of the reasons for good or bad time estimation, scheduling, and teamwork coordination. Doing poorly in these is not unusual (as numerous reports from real-life projects show). 

    We will not evaluate how well (or badly) the project went, but instead how well you understood the reasons **why** the project went as it did, and what lessons you drew from your experience to inform your future work. A good reflection document will include concrete statements about lessons learned, with clear supporting evidence, such as examples, to support the claims. 


## Individual Reflection (10 pts)

!!! warning "Use of Generative AI discouraged"
    Historically, we have found the use of generative AI tools for this part of the assignment has resulted in poor work being submitted. It is your responsibility to make sure that you feel comfortable with the work you submit and are putting in your best effort.

In addition to the team reflection, you will also be submitting an individual reflection on Gradescope. 

We want you to connect this project's experience with your previous experience with collaborative development. Your previous experience may be from an academic or non-academic setting, such as internships, hackathons, or personal projects.

Your reflection should address the following questions (and sub-questions): 

1. What previous collaborative projects have you done before? 
    - How does this project experience compare with your previous experience? What was similar and what was different?
2. What did you personally learn from this project’s development process? Process here refers to the steps you took to contribute to the codebase. 
    - What did you think worked well? What did you think did not work well?
    - Was there anything unexpected?
3. What did you learn about working in a team? 
    - What did you learn about yourself?
    - What did you learn about working with others?
4. What are you planning to do differently or improve upon in your future projects? What would you like to keep doing? Provide at least one concrete action that you plan on acting upon in the next project.

Similar to the team reflection task, we will grade the quality and depth of your reflection.

## Extra Credit (2 pts)
Getting to know your colleagues in a friendly context can often lead to more effective collaboration; for example, healthy teams often get lunch together. To incentivize this, we will give your team extra credit for this assignment if you meet for a team bonding experience outside of a working session.

You might want to eat together, go out for boba, or hold a board game session. Nearly anything outside of class, libraries and campus would work. (If you are unsure, feel free to ask a TA)

To receive extra credit, submit a photo of your team activity as part of the P2C EC gradescope submission before the deadline and include it in a folder in your shared google drive. We encourage you to do these types of meetings often throughout the semester!

## Grading
To receive full credit for the Individual Final Implementation, we expect:

- [ ] Fulfillment of your individual implementation goals as outlined by the planned milestones, **or** a clearly written justification in the milestone description of why elements fell through
- [ ] Reasonable code structure and style, including documentation where appropriate
- [ ] Coherent commits of reasonable size with meaningful commit messages
- [ ] Automated test cases for your implemented functionality, following the acceptance criteria set during planning
- [ ] CI passing on your feature branch
- [ ] Your PR clearly explains why your testing/verification is sufficient to trust the change
- [ ] A contribution to `UserGuide.md` documenting your feature and its tests
- [ ] A functional feature that works when following the steps in `UserGuide.md`. Note that we aren't expecting the feature to be bug free, but it should work under general expected usage.

To receive full credit for Team Integration, we expect:

- [ ] Every team member's individually assigned issue from Sprint 1 that has passing CI is merged into `main` (see the note above on incomplete individual PRs)
- [ ] An updated Project Board reflecting the team's final progress
- [ ] High quality usage of Git/GitHub tools, such as issues, milestones, pull requests, and commits, across the whole team
- [ ] GitHub Actions running on the repository and passing on the main branch
- [ ] Evidence that integration issues (merge conflicts, incompatible changes between teammates' features, etc.) were identified and resolved

To receive full credit for the Process and Team Reflection, we expect:

- [ ] A detailed, well written, and well structured reflection on each of the provided guiding questions
- [ ] A comparison between the planned and the actual schedule
- [ ] An analysis beyond mere descriptions and superficial statements, including links to GitHub project board items, PRs, commits, and meeting minutes as supporting evidence for claims that reflects on the causes of deviations, conflicts, and your team’s experience
- [ ] All meeting minutes throughout the project (with agenda/topics, decisions made, work assignments) that adequately demonstrate your team’s meeting process
- [ ] At least three concrete actions that your team will either start, stop, or keep doing in the future, each labeled as Keep/Start/Stop with specific justification and supporting evidence from meeting minutes or development artifacts

To receive full credit for the Individual Reflection, we expect:

- [ ] A detailed, well written, and well structured reflection on each of the provided guiding questions with concrete examples
- [ ] A comparison between current and previous experience
- [ ] A reflection on the development process, including what worked well and what did not work well
- [ ] A reflection on working in a team, with learnings about self and working with others
- [ ] At least one concrete action that you will act upon in the future, with proper justification and supporting evidence
- [ ] Links to some Sprint 2 commits/PRs with short explanations of your commit message/branch naming choices

## Resources & Documentation

### opencode Development

By now, you should be familiar enough with the codebase to finish making the remainder of your changes. The additional focus of this second sprint is on **testing** your code; hence, documentation related to the testing framework will be very helpful.

As with before, you will find some resources to help you with development in the `README` of the opencode repository. You will now want to check the testing section for resources on Bun's built-in test runner, which you've already used in Project 1:

* [Bun Test Runner Documentation](https://bun.sh/docs/cli/test)
    * You can also reference existing tests in the packages you're working in for examples of the conventions this codebase follows!
