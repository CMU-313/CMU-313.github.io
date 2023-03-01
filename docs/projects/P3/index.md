# Project 3: Quality Assurance + Deployment

## Learning Goals

- Learn how to deploy a full-stack application
- Gain hands-on experience with analysis tools, including setting up, customizing, and using them
- Practically assess and compare the costs and benefits of existing static and dynamic bug-finding tools
- Integrate CI/CD tools into development practice


## Project Context

Quality Assurance is a critical part of software development. Although you have been testing your new system this whole time, you are now setting out to establish a sustained QA practice that can be used moving forward as you iterate over and continue to improve your system.

Your CTO has assigned you two major tasks. Firstly, establishing a deployment pipeline to create a test version of the website that can be sent to beta testers who have little to no experience with code development (and therefore can not set up the developer environment by themselves). 

Secondly, evaluating existing tools & practices beyond simple linting & unit testing and producing a report on the cost/benefit tradeoffs & risks of them. You will then select and integrate one (or more!) of these tools into your development process.


## Deliverables and Deadlines
There are two (2) deliverables and two (2) deadlines. This project is worth a total of 120 points.

**Project Checkpoint** – 35 points – due Thursday, March 16th, 11:59pm

- Deployed Application (25 pts)
- Tools Checkpoint (10 pts)

**Final Deadline** - 85 points - due Tuesday, March 21st, 11:59pm

- CD Implementation (10 pts)
- Tool Analysis Design Doc (60 pts)
- CI Implementation (15 pts)

!!! note
    There are two main focuses in this project: deployment and static/dynamic analysis. For the purposes of equitable distribution of labor, we recommend that you nominate one of your members to act as the SRE for this assignment who will be primarily responsible for deployment, and have all other teammates focus on tool research and integration. 


## Deployment

### Deployed Application (25 pts)

Your team will be using the website fly.io for the deployment of the NodeBB application. Further instructions on how to deploy can be found [here](/projects/P3/deployment).

Once you have successfully deployed your website, make sure to test within your team to ensure that your added feature(s) from Project 2 are properly integrated. Then, submit a link to the deployed site onto Gradescope before the checkpoint deadline.

### CD Implementation (10 pts)
Now that you have successfully deployed your application manually, add a workflow to your team repository that will automatically deploy your application. In doing so, consider how often you would want to deploy, and if you would need to make changes to your repository to ensure best development practices.

!!! note
    You may have sensitive or secret values that will be required by your workflow in order to successfully deploy your application. As your team repository is public, be sure to follow best GitHub practice in [creating secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets) to prevent such values from being leaked.

Submit a link to a successful deployment Action run along with a brief description/justification of how you set up the workflow to Gradescope before the final deadline.


## Static and Dynamic Analysis

### Initial Research
Before jumping into tool integration, your manager would like you to research what existing analysis tools are out there that can be used with NodeBB and document your findings within a design document/RFC.

For the purposes of this RFC, you must identify and experiment with **at least N-1 potential static and dynamic analysis tools** that are applicable to your system, where N is the number of people in your team.

We provide a [starter list of tools](#starter-list-of-tools) in the resources section below to help you with your selection.

In your selection of tools, you should include **at least one static analysis tool** and **at least one dynamic analysis tool**. Additionally, you must have **at least one tool that is not from our list**. You may not use one of the existing tools within NodeBB as part of your analysis (mocha/ESLint/TSLint).

For each tool that you assess, create a separate testing branch in your repository (named appropriately for the tool you’re testing) to integrate the tool into your project and test out its capabilities. For grading purposes, you should create a pull request to the main branch from each of these testing branches.

!!! note
    We will not be grading the quality/quantity of any code you put into these testing branches/PRs, but we will be looking for **concrete evidence that you had successfully installed the tool** (i.e. through trackable file changes demonstrating that extra files/NPM packages were installed) and **at least one artifact that demonstrates you actually ran the tool on the repository.**
    
    Some acceptable artifacts include output files generated by the tool, or a text file containing the terminal output from the tool; you may also attach screenshots as additional pieces of evidence.

    These pieces of evidence **must** be attached to the Pull Request in either the description or follow-up comments. They can also be used for your design document later on.

    These branches should also provide the benefit of allowing your teammates to experiment with each of the tools by swapping between the branches.
    
In your evaluations, consider & experiment with the types of customization that are appropriate or necessary for this tool, both a priori (before they can be used in your project) and over time. Assess the strengths and weaknesses of each tool/technique, both quantitatively and qualitatively.

Consider some of the following questions: 

- What types of problems are you hoping your tooling will catch?  What types of problems does this particular tool catch? 
- What types of customization are possible or necessary? 
- How can/should this tool be integrated into a development process?
- Are there many false positives? False negatives? True positive reports about things you don’t care about?

!!! info "Tool Evaluation"
    As you can see from above, there are a lot of different factors to consider when evaluating a tool. We recommend discussing with your teammates and deciding on a group of metrics to focus on when performing evaluations.

!!! note
    Don’t spend too long during this exploration phase! Set deadlines within your team to ensure that you have enough time for both the design document and final integration deliverables described below.


### Tools Checkpoint (10 pts)

By the checkpoint deadline, your team should have decided on your **initial list of the N-1 tools** that you plan on exploring, and you must have **successfully installed and run at least one tool on your repository.**

On Gradescope, submit your list of tools and a link to the PR that provides evidence to the tool that was successfully installed.

### Tool Analysis Design Doc (60 pts)

Create a Design Document/RFC that includes:

- A **tools evaluations section** detailing your team’s analysis on each of the tools you experimented with
- A **justification section** explaining which tool(s) you think the project should use moving forward
- An **integration section** describing how the selected tool(s) shall be integrated into your process
- A **conclusion section** summarizing your work

Below, we provide more detailed instructions and page limit recommendations for each of the sections.

#### Tool Evaluations (~N pages)

For each of the N-1 tools explored by your team, you must provide:

- Name and high-level description of what the tool does and a link to its documentation/source
- Whether the tool is used for static or dynamic analysis
- A link to the pull request made from the testing branch for this tool
- A pro/con analysis of the tool and appropriate evidence to support your claims (i.e. screenshots). You can use the questions provided in the exploration phase above to shape your analysis.

Each of these sections should take up approximately 1 page (including screenshots) and no more than 2 pages.

#### Justification (~Half a page)

After going through each of the tools, you should explicitly state the tool you are choosing to integrate for this project and provide a justification for why you are selecting this tool. You should refer to the pro/con analysis done in the prior sections and how they align with the goals of your team and the project overall.

You must recommend at least one tool, even if it’s with reservations.

#### Integration (<1 page)

This section should address the different factors to take into consideration when integrating a new tool. At minimum, you should address the following:

- **Technical Questions:** how are you integrating the tool (high-level)? At what point in the development/deployment process shall it be integrated? What sorts of customization or configuration will you be using?
- **Developer Questions:** how should the team use this new tool within their development process?

Your answers should be based on your experiences running the tools and, as much as possible, be grounded in data (such as tool usability, output, and customizability).

Keep this section updated as you work on implementing the integration.

#### Conclusion (<1 page)

In this section, provide a brief summary of your findings along with items that were not addressed in the previous sections. Are there any open questions? Issues you consider out of scope? Drawbacks of the proposed process/tooling that you are accepting for some (good) reason? 

This section should be used to wrap everything up and ensure you have a good/complete design document!

Submit the Design Document as a single PDF to Gradescope.

### Tool Integration (15 pts)

Once you have a tool selected along with a general integration plan, you should fully integrate one of the tools into your project’s workflow. In the exploration phase, you should have successfully run this tool locally; you should then create a new workflow within the project to run it as part of the development cycle.

Your team should discuss how often this new integration should run (on each pull request? on commits to main?), what level of customization is needed, how it should be enforced, etc. This configuration must have been justified in your design document under the Integration section.

This integration should be **merged into your main branch** and **must have run at least once in the Git flow cycle** (i.e. either during the pull request, merge, or commit stage). Additionally, by the end of this project, your build on main **must pass successfully**; this is indicated by having a green checkmark.

!!! note
    In order to ensure your checks pass successfully, you may have to make additional changes to your repository, such as fixing reported issues or tweaking tool configuration. These changes should be documented and addressed in your design document. Continually failing builds show you have not completely integrated the tool into your workflow.

On Gradescope, submit a link to your repository and a link to one of the successful Action runs.

## Grading
To receive full credit for this project, we expect:

- [ ] [TODO: ADD GRADING DETILAS]


## Resources & Documentation

### Starter List of Tools

NodeBB is built in Javascript/Typescript using Node.js and uses Benchpress for its frontend templating. Below are non-exhaustive lists of analysis tools that are available. 

For other resources, [Awesome Static Analysis page](https://github.com/david-a-wheeler/awesome-static-analysis) and [Awesome Dynamic Analysis page](https://github.com/analysis-tools-dev/dynamic-analysis) have extensive listings of available static and dynamic analysis tools for a pretty hefty list of programming languages.

Some of the tools already have existing GitHub Actions workflows on GitHub Marketplace; use your Googling skills, and see what you find!

#### Static Tools

- [flow](https://flow.org/): Static type checker for JavaScript
- [JScent](https://github.com/moskirathe/JScent): Program analyzer for detecting “code smells”
- [JSHint](https://jshint.com/docs/): Used to flag suspicious usage in JavaScript programs
- [StandardJS](https://standardjs.com/)/[ts-standard](https://github.com/standard/ts-standard): Static analysis tool for code quality within JavaScript/TypeScript projects
- [Retire.js](https://retirejs.github.io/retire.js/): Finds library/node module vulnerabilities within your project

#### Dynamic Tools

- [Iroh](https://maierfelix.github.io/Iroh/): Runtime code tracking and visualization
- [Jalangi](https://github.com/Samsung/jalangi2): Framework for dynamic analyses in JavaScript
- [Fast-Fuzz](https://www.npmjs.com/package/fast-fuzz): Fuzzing framework for TypeScript
- [Stryker Mutator](https://stryker-mutator.io/): Mutation testing tool for JavaScript
