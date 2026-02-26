# Project 3B: Tool Analysis and Integration

## Deliverables

**Final Deliverables** – 65 points – due Thursday, March 19, 2026, 11:59PM

- [Tool Analysis (Individual) (30 pts)](#tool-analysis-individual-30-pts)
- [Tool Analysis Design Doc (Group) (20 pts)](#tool-analysis-design-doc-group-20-pts)
- [Tool Integration (15 pts)](#tool-integration-15-pts)
- [_Extra Credit_ (6 pts)](#extra-credit-feature-review)

### Tool Analysis (Individual) (30 pts)

You will each individually add a comment containing answers to the following questions to your own PR that you made for Project 3A:

- What is the name and high-level description of what the tool does? Provide a link to its documentation/source.
- Is the tool used for static or dynamic analysis?
- What types of problems does this particular tool catch?
- What types of customization are possible or necessary?
- How can/should this tool be integrated into a development process?
- Are there many false positives? False negatives? True positive reports about things you don't care about?

### Tool Analysis Design Doc (Group) (20 pts)

!!! warning "Individual Grade Adjustments"
    This document is something that we expect the team to work on together. However, we will be asking who worked on what part of the document, and in the case that a sub-section of the document is low quality AI slop, we will be only penalizing the author of that section, NOT the entire team. To this end, we will be requiring that develop the document in the Google Drive folder that has be shared with your team by your TA.

As a group, create a Design Document/RFC that includes:

- A **justification section** detailing which tool(s) you are choosing to integrate in your team's workflow and why
- An **integration section** describing how the selected tool(s) shall be integrated into your process
- A **conclusion section** summarizing your work

Below, we provide more detailed instructions and page limit recommendations for each of the sections.

#### Justification (~Half a page)

After going through each of the tools, you should explicitly state the tool(s) you are choosing to integrate for this project and provide a justification for why you are selecting the tool(s). You should refer to the pro/con analysis done in the individual PRs and how they align with the goals of your team and the project overall.

You **must recommend at least one tool**, even if it’s with reservations.

#### Integration (<1 page)

This section should address the different factors to take into consideration when integrating a new tool. At minimum, you should address the following:

**Technical Questions**
  - How are you integrating the tool (high-level)? At what point in the development/deployment process shall it be integrated? What sorts of customization or configuration will you be using?
  - If you added any specific configuration to allow the main branch of your repository to pass its status checks, add the justification for those decisions in this section.
**Social Integration Questions**
  - How do you foresee the team using the tool during their development process? Consider the incentives & deterrents to the developers when it comes to using the tool, and their personal motivation to use it.

Your answers should be based on your experiences running the tool(s) on your team repository and be grounded in data from your research on different factors such as tool usability, output, and customizability.

Keep this section updated as you work on implementing the integration.

#### Conclusion (<1 page)

In this section, provide a brief summary of your findings along with items that were not addressed in the previous sections.

- Are there any open questions?
- Are there any issues you consider to be out of scope?
- What drawbacks of the proposed process/tooling are you accepting for some (good) reason?

This section should be used to wrap everything up and ensure you have a good/complete design document!

Each member should submit a link to the document on Gradescope **individually**.

### Tool Integration (15 pts)

Once you have a tool selected along with a general integration plan, you should fully integrate one of the tools into your project’s workflow. For your checkpoint research, you should have successfully run this tool locally; you should then create a new workflow within the project to run it as part of the development cycle.

Your team should discuss:

- How often should this new integration be run (on each pull request? on commits to main?)
- What level of customization is needed for this tool?
- How should the integration of this tool be enforced?

This configuration must have been justified in your design document under the Integration section.

To be considered successfully integrated, the tool must:

- Be **merged into your main branch**
- **Have been run at least once in the Git flow cycle** (i.e. either during the pull request, merge, or commit stage).
- **Pass** when run on your codebase. This is indicated by having a green checkmark.

!!! note "Ensuring Passing Checks"
    In order to ensure your checks pass successfully, you may have to make additional changes to your repository, such as fixing reported issues or tweaking tool configuration. These changes should be documented and addressed in your design document.

!!! warning "Failing CI builds"  
    Continually failing builds show you have _not_ completely integrated the tool into your workflow.

On Gradescope, submit a link to your repository and a link to one of the successful GitHub Action runs.

### Extra Credit: Feature Review (6 pts)

Now that you and your classmates have deployed your applications in 3A, you will be able to test out each other’s features and provide constructive feedback on your experience and how to improve them! Take this as an opportunity to learn about what your classmates have been working on for the past few weeks.

Note that this is an **individual** task.

For extra credit, you will conduct reviews of features developed by other teams. Pick **three** teamss' deployments from the [public spreadsheet](https://docs.google.com/spreadsheets/d/1Xmaqmu5MITPjy1TFDpohQFwzaPYcUNVviuc4jLDXPEY/edit?usp=sharing) to review--1 from your own section and 2 from other sections.

For each team, you will submit a review of their feature(s) on the appropriately titled sheet in the Google Sheet. You will need to test the feature(s) as described in their UserGuide and provide feedback on the following:

1. How was the experience of using the feature(s), would this be something you think would help enable better communication between faculty and students and why?
2. How do you think the feature can be improved? and/or What do you think the feature did well in?
3. Did you discover any bugs using the feature(s)?

To qualify for extra credit, you will have to submit your review:

- on Gradescope
- in the appropriate sheet for the group you want to review in the [public spreadsheet](https://docs.google.com/spreadsheets/d/1Xmaqmu5MITPjy1TFDpohQFwzaPYcUNVviuc4jLDXPEY/edit?usp=sharing). There should be one sheet per team, and you should add your review to the sheet for the team you are reviewing.

## Grading

To receive full credit for the extra credit, we expect:

- [ ] Your review of three different teams' features on Gradescope and on the [public spreadsheet](https://docs.google.com/spreadsheets/d/1Xmaqmu5MITPjy1TFDpohQFwzaPYcUNVviuc4jLDXPEY/edit?usp=sharing), addressing the three questions described.

## Grading

To receive full credit for the final deadline, we expect:

- [ ] A link to your successfully run CD GitHub action that deploys the website while following proper GitHub practices in handling deployment secrets
- [ ] A link to the Github comment containing your individual analysis of your tool
- [ ] A design document describing your justification for your selection of integrated tool(s), and your final integration plan
- [ ] A link to a successful run of a GitHub Action that demonstrates your integration of your selected tool(s) into your team workflow
