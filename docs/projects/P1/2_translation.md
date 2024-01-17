# Project 1B: TypeScript Translation
## Deliverables
Starter Task - 95 points - due Thursday, January 25th, 11:59PM

- [GitHub Issue](#github-issue-20-pts) (20 pts)
- [TypeScript Translation or Code Coverage](#task-10-pts) (10 pts)
- [GitHub Pull Request](#github-pull-request-25-pts) (25 pts)
- [Gradescope Written Assignment](#written-assignment-40-pts) (40 pts)

## Onboarding
Now that you have explored the repository, the development team would like to give you an onboarding assignment.

*Types types types!* Driven by their programming language enthusiast, the team is currently undertaking a major code overhaul and converting the repository from JavaScript to [TypeScript](https://www.typescriptlang.org/). This language is a superset of JavaScript and comes with many advantages, including better support for code editors, compile time error-checking and, of course, types!

To ensure the translation is done properly, we also want all files to achieve complete code coverage with JavaScript.  If you are not up to translating to TypeScript, you can also improve the code base by increasing the code coverage.
<!-- As part of the efforts to integrate this new language into the repository, all future code will be written using TypeScript and the old files are translated as necessary. To prepare you for TypeScript development, the team would like you to contribute towards rewriting the codebase. -->

## Prerequisites
### Onboarding Materials
Before jumping into the codebase, please review the [course syllabus](/syllabus) and be sure you have access to each of the following:

- Course Slack - check your email for an invite link
- [Canvas](https://canvas.cmu.edu/courses/39244)
- [Gradescope](https://www.gradescope.com/courses/583198)

If you run into any trouble accessing the above or have any questions, reach out to the instructors.

### Git & GitHub
In this project and throughout the rest of this course, you will be expected to work extensively with Git and GitHub. Specifically for this project, you should be familiar with:

- [x] Forking/cloning GitHub repositories
- [x] Understanding general Git flow - pulling, branching, adding, committing, pushing, merging
- [x] Creating GitHub Issues and using related features (labels, assignees, milestones)
- [x] Creating GitHub Pull Requests and using related features (linking to issues)
- [x] Creating GitHub Project Boards

If you are not familiar with any of these steps, you are **highly recommended** to first complete [Recitation 1 - Git, GitHub, TypeScript](/recitations/reci1-github), as it will cover the standards we are expecting in this class (which you will be graded upon). Refer to the [Resources & Documentation](/projects/P1/documentation/#git--github-documentation) section if needed.


### GitHub Issue (20 pts)
First, choose a single JavaScript file to either translate or complete the code coverage, and open a GitHub Issue in the [class repository](https://github.com/CMU-313/NodeBB/issues) to declare which file you will be translating.

There are some restrictions on the `.js` file that you can pick. 

For the TypeScript Translation, the file must:

- **Be in the `src/` folder**
- **Contain at least 50 lines of non-import statement code** before you start translating it. Files like [`src/api/index.js`](https://github.com/CMU-313/NodeBB/blob/main/src/api/index.js) and [`src/controllers/admin.js`](https://github.com/CMU-313/NodeBB/blob/main/src/controllers/admin.js) are not allowed
- **Be a file that no one else in the class has picked for TypeScript Translation and created an issue for**. We expect you to look through existing issues, if any, to avoid such duplication (thus, there is an incentive for you to start early!)

For Completing the Code Coverage, the file must:
- **Be in the `src/` folder**
- **Contain at least 5 lines of not covered by existing tests** 
- **Be a file that no one else in the class has picked for completing code coverage and created an issue for**. We expect you to look through existing issues, if any, to avoid such duplication (thus, there is an incentive for you to start early!)


Title the task appropriately, such as `Converting <file name> from JS to TS` or `Adding code coverage for <file name>`,  and mention the file name in the description. To prevent ambiguities between similarly-named files, be sure to use the **full file path** (`src/../xx.js`) in the title and description. 

??? info "Issue Guidelines"
    **Issues titles** should provide a high-level overview of what the problem is (e.g. *"Navbar button UI bugs"*, *"Unexpected registration validation errors"*). Sometimes, issues are used to propose new features (e.g. *"Add CSV export feature"*).

    **Issue descriptions** should then elaborate on the title. For feature-level bugs, this may include providing information about how to reproduce the bug; for codebase-level changes, you can name specific files.

Then, assign yourself to the Issue by leaving a comment that says "I would like to work on this please!"

You should soon see another comment by the `github-actions` bot informing you that you have been successfully assigned to this issue.

![Bot Issue Assignment](/assets/images/hw/bot_assignment.png)

??? info "Why Bot Assignment?"
	You might be curious as to why we are using a GitHub bot instead of directly assigning yourself to the issue. As you aren’t officially recognized as a collaborator of CMU-313/NodeBB, GitHub adds some restrictions to your permissions for security purposes, including not being able to assign yourself to an issue. Hence, we are using a bot to work around these restrictions. This is similar to how you would request issues on an Open Source project!
	
	For future projects, you will have full control over these GitHub features such as managing assignees, adding labels, creating milestones, and more.

### Task (10 pts)
For this task you will chose one (1) of the following tasks:
  
  TypeScript Tranlation
  
  OR

  Complete Code Coverage

  You only need to do one (1) of these tasks. Each file can be claimed once for each task, so if someone else has claimed the TypeScript Translation, you could still claim the Complete Code Coverage.

#### TypeScript Translation 
Back in **your own fork**, create a feature branch and implement the change. You should start with the following steps:

- [Install TypeScript](https://www.typescriptlang.org/download)
- If you chose a file named `xx.js`, create a new file called `xx.ts` in the same directory
- Copy over the contents of the original file into this new file
- Make changes to `xx.ts` file as needed to translate the file into TypeScript
- Run `npx tsc` to generate a compiled JavaScript file from your changes

Your changes must still pass both the linter and the test suite, so be sure to test your changes locally!

!!! note "Dependencies on Untranslated Files"
	There will be some instances where your file may reference functions or variables from modules in other files that have not been translated yet. This may cause the linter to throw errors as these values will be of type `any`. In those situations, **and only in those situations**, you may add the following comments to suppress the linter warnings:
	
	```TypeScript
	// The next line calls a function in a module that has not been updated to TS yet
	// eslint-disable-next-line @typescript-eslint/no-unsafe-member-access, @typescript-eslint/no-unsafe-call
	```

	We will check your files to make sure you are only suppressing these warnings when absolutely necessary. For examples and more details, see the [Additional TypeScript Background](/projects/P1/documentation#additional-typescript-background) section under "Resources and Documentation".

#### Complete Code Coverage 

Back in **your own fork**, create a feature branch and implement the change. You should start with the following steps:

- Run tests to determine the initial coverage.
- Locate the tests that are currently covering that file.
- Write tests that will add coverage to at least five (5) lines that are currently uncovered in the file, as measured by line coverage.  
- All new tests added by you must pass.

**NOTE: each test should actually test something, meaning it must have at least 1 assert statement**



### GitHub Pull Request (25 pts)
As you work, be sure to periodically commit your changes. Your commit message(s) must clearly describe what is changing. If you’d like, you can also make use of branching and pull requests in your own repository to practice working with GitHub.

??? info "Branch and Commit Guidelines"
    **Branch names** should be short and provide a description of what you will be doing on that branch (e.g. *"fix-header-sizing-issue"*, *"fix-multiple-dialog-bug"*, *"add-sorting-feature"*). When working with others, you can also append your username to signal which branches are yours (e.g. *"313ta/add-sorting-feature"*).
	
	**Commits** should start with a verb and provide a description of what they are doing to the codebase (e.g. *"Remove faulty condition from getCustomerDetails"*, *"Fix failing CompositeTestCase"*, *"Fix issue #21"* ).

Once you are satisfied, open a pull request from your personal branch back to the **class** repository. Similar to the Issue, your PR title should mention the full path of the file you’ve changed. The PR body should summarize the changes you made and [use one of the linking keywords](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue) to link the issue that you previously opened (e.g. adding `resolves #313` will signal to GitHub that this PR resolves issue number 313).

??? info "Pull Request Guidelines"
	**Pull request titles** should describe what high-level changes were made to the codebase. Generally, they give a concise summary of all the commit messages.

    **Pull request descriptions** should describe what changes have been made in more detail and how the changes have been tested.

There will be automated checks that run on your pull request to ensure you meet the requirements of this assignment. Some of them take a while to run, so be sure to check on your pull request periodically to ensure that all these actions pass and everything is working properly!

!!! note "Test Suite Failures"
	If the tests are failing on GitHub but work locally, it may be caused by server overload. Re-running the failing GitHub Action 1-2 times will resolve this.

If all of the actions have passed, you will see a green checkmark next to your pull request. This signals that you have completed the implementation aspect of this assignment! ✅

### Written Assignment (40 pts)
After you have completed all of the above tasks, we will ask you some questions relevant to the NodeBB project and the course [syllabus](/syllabus). Fill out and submit the HW1 Written Assignment available on Gradescope. 

## Grading
To receive full credit for this project, we expect:

- [ ] A GitHub Issue with:
	- [ ] A selected JavaScript file that follows our requirements above
	- [ ] A meaningful title and description that includes the full path of the file
	- [ ] A successful self-assignment as an assignee
- [ ] A GitHub Pull Request with:
	- [ ] A meaningful title that includes the full path of the file
	- [ ] A description body that describes the changes made and links the pull request to the issue
	- [ ] Meaningful commit messages
	- [ ] Appropriate usage of the eslint-ignore comment
	- [ ] A green checkmark signaling that all checks have passed
- [ ] Answers to the Gradescope Written Assignment that demonstrate successful completion of the project and understanding of the benefits and limitations of software metrics in the context of NodeBB