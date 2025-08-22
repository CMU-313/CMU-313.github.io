# Project 1B: Starter Task

## Deliverables

Starter Task - 95 points - due Thursday, September 4th, 11:59PM

- [GitHub Issue](#github-issue-20-pts) (20 pts)
- [Code Refactoring and Validation](#code-refactoring-and-validation-10-pts) (10 pts)
- [GitHub Pull Request](#github-pull-request-25-pts) (25 pts)
- [Gradescope Written Assignment](#written-assignment-40-pts) (40 pts)

## Onboarding

Now that you have explored the repository, the development team would like to give you an onboarding assignment.

The team has noticed an accumulation of maintainability issues detected by **[Qlty](https://github.com/qltysh/qlty)**, a multi-language code quality tool.
Qlty detects “code smells” such as high function complexity, too many parameters, deep nesting, and duplicated code.
Your task is to remove one or more Qlty-reported issues by refactoring code and validating that your change takes effect within the NodeBB codebase.

## Prerequisites

### Onboarding Materials

Before jumping into the codebase, please review the [course syllabus](/syllabus) and be sure you have access to each of the following:

- Course Slack - check your email for an invite link
- [Canvas](https://canvas.cmu.edu/courses/48397)
- [Gradescope](https://www.gradescope.com/courses/1086939)

If you run into any trouble accessing the above or have any questions, reach out to the instructors.

### Git & GitHub

In this project and throughout the rest of this course, you will be expected to work extensively with Git and GitHub. Specifically for this project, you should be familiar with:

- [x] Forking/cloning GitHub repositories
- [x] Understanding general Git flow - pulling, branching, adding, committing, pushing, merging
- [x] Creating GitHub Issues and using related features (labels, assignees, milestones)
- [x] Creating GitHub Pull Requests and using related features (linking to issues)
- [x] Creating GitHub Project Boards

If you are not familiar with any of these steps, you are **highly recommended** to first complete Recitation 2 - Git, GitHub, as it will cover the standards we are expecting in this class (which you will be graded upon). Refer to the [Resources & Documentation](/projects/P1/documentation/#git--github-documentation) section if needed.

### Qlty

[Qlty](https://github.com/qltysh/qlty) is a multi-language static analysis tool that supports linting, scanning, and auto-formatting across a large number of languages and technologies, including Javascript.
For this assignment, you will locally install and configure the Qlty command-line tool to identify maintainability issues within the codebase.

To get started, you will need to install Qlty on your machine: https://github.com/qltysh/qlty?tab=readme-ov-file#-quick-start.
If you are using the DevContainer, everything should already be installed for you.

To use Qlty to show all of the code smells within the project, you should run:

```bash
qlty smells --all
```

Note that, by default, Qlty only analyzes the files that you've modified since your last commit.
`--all` tells Qlty to scan the entire codebase.

This will a large list of issues and likely fill up your terminal with lots of code snippets.
To make it easier to find which files have issues, you can disable code snippets in the output via the `--no-snippet` option:

```bash
qlty smells --all --no-snippet
```

Once you've narrowed in on a particular file, you can produce a list of smells for just that file as follows:

```bash
qlty smells public/src/path/to/file.js
```

## Tasks

### GitHub Issue (20 pts)

First, choose a single Qlty-reported “smell” in a JavaScript file and open a GitHub issue in the [class repository](https://github.com/CMU-313/NodeBB/issues) to declare which file and issue you will be working on.

For the task, the file must:

- **Be a Javascript file.**
- **Be in the `src/` or `public/src/` directory.**
- **Be a file that no one else in the class has picked and created an issue for.** We expect you to look through existing *open* issues, if any, to avoid duplication.
  - If you really cannot find a unique file because you are late to the game, then you may pick a file that has an open issue, but identify a different Qlty-reported smell in the same file.
  Reference the other issue in your description to distinguish yourself (e.g., "this is different from #124 because...").

The Qlty issue you pick should be a maintainability smell (e.g., high function complexity, too many parameters, deep nesting, or duplicated code) that requires real code restructuring.

Title the task appropriately, such as `Refactoring code in <file name>`, and mention the file name in the description. Use the **full file path** (`src/../xx.js`) in the title and description to avoid ambiguity.

Additionally, include in the description:

- A copy/paste or screenshot of the relevant Qlty output (from `qlty smells --all`).
- A brief explanation of the issue you will address.

??? info "Issue Guidelines"
    **Issues titles** should provide a high-level overview of what the problem is (e.g. *"Navbar button UI bugs"*, *"Unexpected registration validation errors"*). Sometimes, issues are used to propose new features (e.g. *"Add CSV export feature"*).

    **Issue descriptions** should then elaborate on the title. For feature-level bugs, this may include providing information about how to reproduce the bug; for codebase-level changes, you can name specific files.

Then, assign yourself to the Issue by leaving a comment that says "I would like to work on this please!"

You should soon see another comment by the `github-actions` bot informing you that you have been successfully assigned to this issue.

![Bot Issue Assignment](/assets/images/hw/bot_assignment.png)

??? info "Why Bot Assignment?"
	You might be curious as to why we are using a GitHub bot instead of directly assigning yourself to the issue. As you aren’t officially recognized as a collaborator of CMU-313/NodeBB, GitHub adds some restrictions to your permissions for security purposes, including not being able to assign yourself to an issue. Hence, we are using a bot to work around these restrictions. This is similar to how you would request issues on an Open Source project!

	For future projects, you will have full control over these GitHub features such as managing assignees, adding labels, creating milestones, and more.

### Code Refactoring and Validation (10 pts)

For this task, you will focus on refactoring the code and removing the corresponding Qlty issue(s) from your chosen file.
As part of the task, you must validate your changes for **one Qlty-reported smell** by re-running Qlty locally.

Back in your own fork, create a feature branch and implement the changes needed to address the chosen Qlty issue(s).
You should start with the following steps:

- Review the Qlty smells for the file (via ` qlty smells --all`).
- Identify the necessary code changes to address the chosen smell.
- Implement the changes and ensure that they do not introduce new Qlty warnings or issues.
- Run the linter and test suite to ensure your changes pass all checks (via `npm run lint` and `npm run test`).

We also want you to manually test your changes in a running NodeBB instance.
The purpose is to trigger the refactored code's execution from the user interface (UI) with the following steps:

- Within your implementation, add a print statement (e.g., `console.log(YOUR_NAME)`) immediately before, after, or in the middle of your refactored code.
- Restart the NodeBB instance and watch its logs via `./nodebb log`.
- Perform any necessary UI operations that execute the refactored code (e.g., clicking buttons for an action)
- Take a screenshot of these logs and include it in your written report, along with a brief explanation of the steps you took to trigger the code.
- Remove the temporary print statement before committing your final code.

### GitHub Pull Request (25 pts)

As you work, be sure to periodically commit your changes.
Your commit message(s) must clearly describe what is changing.
If you’d like, you can also make use of branching and pull requests in your own repository to practice working with GitHub.

??? info "Branch and Commit Guidelines"
    **Branch names** should be short and provide a description of what you will be doing on that branch (e.g. *"fix-header-sizing-issue"*, *"fix-multiple-dialog-bug"*, *"add-sorting-feature"*). When working with others, you can also append your username to signal which branches are yours (e.g. *"313ta/add-sorting-feature"*).

	**Commits** should start with a verb and provide a description of what they are doing to the codebase (e.g. *"Remove faulty condition from getCustomerDetails"*, *"Fix failing CompositeTestCase"*, *"Fix issue #21"* ).

Once you are satisfied, open a pull request from your personal branch back to the **class** repository.
Similar to the Issue, your PR title should mention the full path of the file you’ve changed.
The PR body should summarize the changes you made and [use one of the linking keywords](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue) to link the issue that you previously opened (e.g. adding `resolves #313` will signal to GitHub that this PR resolves issue number 313).

??? info "Pull Request Guidelines"
	**Pull request titles** should describe what high-level changes were made to the codebase. Generally, they give a concise summary of all the commit messages.

    **Pull request descriptions** should describe what changes have been made in more detail and how the changes have been tested.

There will be automated checks that run on your pull request to ensure you meet the requirements of this assignment.
Some of them take a while to run, so be sure to check on your pull request periodically to ensure that all these actions pass and everything is working properly!

!!! note "Test Suite Failures"
	If the tests are failing on GitHub but work locally, it may be caused by server overload. Re-running the failing GitHub Action 1-2 times will resolve this.

 You should ensure that all checks are green.
 If all of the actions have passed, you will see a green checkmark next to your pull request.
 This signals that you have completed the implementation aspect of this assignment! ✅

### Written Assignment (40 pts)

After you have completed all of the above tasks, we will ask you some questions relevant to the NodeBB project and the course [syllabus](/syllabus).
Fill out and submit the HW1 Written Assignment available on Gradescope.

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
	- [ ] A green checkmark signaling that all checks have passed
- [ ] Answers to the Gradescope Written Assignment that demonstrate successful completion of the project and understanding of the benefits and limitations of software metrics in the context of NodeBB
