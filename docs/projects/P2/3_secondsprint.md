# Project 2C: Collaborative Development

## Deliverables

**Second Sprint** – 140 points – due Thursday, March 2nd, 11:59pm

- [Process & Implementation Final Snapshot](#process--implementation-final-60-pts) (60 pts)
- [Team Reflection](#team-reflection-50-pts) (50 pts)
- [Individual Reflection](#individual-reflection-30-pts) (30 pts)


## Process & Implementation Final (60 pts)
Continue working on the implementation of your feature(s). Be sure to continue following best practices for collaborative development similar to the previous sprint.

As you become more familiar with the codebase, we have higher expectations for the final deliverables of this sprint. Specifically, along with your feature changes, we expect to see:

- **Automated Tests**
    - Add tests to the test suite that demonstrate the functionalities you implemented
    - These should follow the acceptance criteria you set from the initial planning

- **User Documentation**
    - Create a new file `UserGuide.md` in the root directory of your repository
    - In this file, provide a detailed outline of how to use and user test your new feature(s)
    - You should also provide a link/description of where your added automated tests can be found, along with a description of what is being tested and why you believe the tests are sufficient for covering the changes that you have made

!!! note "GitHub Actions"
    GitHub Actions should be enabled. It is reasonable to have failures in feature branches, but you should do your best to make your main branch build consistently pass.

As with the first sprint, every member of your team must contribute to the implementation. One way we will evaluate this is that each team member must have at least one commit as a part of the solution. Failure to do so will result in a significant penalty to your grade.

You must commit all of your changes to the main branch of your team repository before the homework deadline. Unlike the previous assignment, you should not submit your changes to the parent NodeBB repository.

Submit a link to your repository and your Github Project board onto Gradescope. For grading, we will take a snapshot of your repository and board right at the deadline and grade based on your progress there.


## Process & Team Reflection (50 pts)

After coding is complete, reflect on your experience as a team. Again, we look for honest reflection, which will likely include reflection on failures. **We will not grade whether you predicted the effort correctly, but rather what you have learned**. 

You will see the following groups of questions on Gradescope. We recommend that your team use collaborative text editing tools like Google Docs to draft your answers, then submit your final answers to Gradescope.

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

5. **Team Experience:** Reflect on your experience working as a team. You should discuss as a team on the aspects of communication, scheduling, responsibilities and equitable contributions. Answer the following points by providing at least one concrete action for each: 
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


## Individual Reflection (30 pts)

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

## Grading
To receive full credit for the implementation, we expect:

- [ ] **Progress from Interim Snapshot**
    - [ ] Fulfillment of implementation goals as outlined by the planned milestones, **or** a clearly written justification in the milestone description of why elements fell through
    - [ ] An updated Project Board for the final progress
    - [ ] Reasonable code structure and style, including documentation where appropriate
    - [ ] Coherent commits of reasonable size with meaningful commit messages by all team members
    - [ ] High quality usage of Git/GitHub tools, such as issues, milestones, pull requests, and commits
- [ ] **Additional Requirements for Final Submission**
    - [ ] Automated test cases for the implemented functionalities
    - [ ] GitHub Actions running on the repository and passing on the main branch
    - [ ] Created `UserGuide.md` file containing user documentation of the new feature that fulfills the guidelines given above
    - [ ] A functional new feature that works when following the steps in `UserGuide.md`. Note that we aren't expecting the feature to be bug free, but it should work under general expected usage.
  
To receive full credit for the process and team reflections, we expect:

- [ ] A detailed, well written, and well structured reflection on each of the provided guiding questions
- [ ] A comparison between the planned and the actual schedule
- [ ] An analysis beyond mere descriptions and superficial statements, including supporting evidence for claims, that reflects on the causes of deviations, conflicts, and so forth, or your own experience
- [ ] Inclusion of meeting minutes(s) that adequately demonstrate your team’s meeting process
- [ ] At least three concrete actions with that your team will either start, stop, or keep doing in the future, with proper justification and supporting evidence

To receive full credit for the individual reflection, we expect:

- [ ] A detailed, well written, and well structured reflection on each of the provided guiding questions
- [ ] A comparison between current and previous experience
- [ ] A reflection on the development process, including what worked well and what did not work well
- [ ] A reflection on working in a team, with learnings about self and working with others
- [ ] At least one concrete action that you will act upon in the future, with proper justification and supporting evidence

## Resources & Documentation

### NodeBB Development

By now, you should be familiar enough with the codebase to finish making the remainder of your changes. The additional focus of this second sprint is on **testing** your code; hence, documentation related to the testing framework will be very helpful.

As with before, you will find some resources to help you with development in the `README` of the NodeBB repository. You will now want to check the testing section for resources on the Mocha test framework:

* [Mocha Documentation](https://mochajs.org/)
    * Everything from the "Getting Started" section and below is documentation on how the framework works. You can also reference existing tests!
