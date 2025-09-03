# Project 1B: Starter Task

## Deliverables

Starter Task - 95 points - due Thursday, September 4th, 11:59PM

- [GitHub Issue](#github-issue-20-pts) (20 pts)
- [Code Refactoring and Validation](#code-refactoring-and-validation-35-pts) (35 pts)
- [GitHub Pull Request](#github-pull-request-40-pts) (40 pts)

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
To make it easier to find which files have issues, you can disable code snippets in the output via the `--no-snippets` option:

```bash
qlty smells --all --no-snippets
```

Once you've narrowed in on a particular file, you can produce a list of smells for just that file as follows:

```bash
qlty smells public/src/path/to/file.js
```

You can use the `--no-snippets` option to find the associated line number for each smell on the left.

```bash
qlty smells --no-snippets src/controllers/mods.js
...

src/controllers/mods.js
 236  Complex binary expression
   1  High total complexity (count = 55)
  22  Function with high complexity (count = 23): list
 131  Function with high complexity (count = 20): detail
 214  Function with high complexity (count = 14): postQueue
```

## Tasks

### GitHub Issue (20 pts)

First, choose a single Qlty-reported “smell” in a JavaScript file and open a GitHub issue in the [class repository](https://github.com/CMU-313/NodeBB/issues) using the **P1B Starter Task Issue template** to declare which smell you will be working on.

![GitHub Issue Template](/assets/images/hw/p1b_issue_template.png)

For the task, the smell must:

- **Be in a Javascript file.**
- **Be in the `src/` or `public/src/` directory.**
- **Be a smell that no one else in the class has picked and created an issue for.**
  We expect you to look through existing *open* issues, if any, to avoid duplication.

The Qlty smell that you pick should be a maintainability smell (e.g., high function complexity, too many parameters, deep nesting, or duplicated code) that requires real code restructuring.

You should fill out all of the fields in the provided issue template and title the issue appropriately.
Specifically, you include both the **full file path** and **line number** (reported by Qlty) in the title to avoid ambiguity and make it easier for others to identify which smells have already been claimed (e.g., `Refactor (src/controllers/groups.js:70): Function with high complexity (details)`).

??? info "Issue Guidelines"
    **Issues titles** should provide a high-level overview of what the problem is (e.g. *"Navbar button UI bugs"*, *"Unexpected registration validation errors"*). Sometimes, issues are used to propose new features (e.g. *"Add CSV export feature"*).

    **Issue descriptions** should then elaborate on the title. For feature-level bugs, this may include providing information about how to reproduce the bug; for codebase-level changes, you can name specific files.

Then, assign yourself to the Issue by leaving a comment that says "I would like to work on this please!"

You should soon see another comment by the `github-actions` bot informing you that you have been successfully assigned to this issue.

![Bot Issue Assignment](/assets/images/hw/bot_assignment.png)

??? info "Why Bot Assignment?"
	You might be curious as to why we are using a GitHub bot instead of directly assigning yourself to the issue. As you aren’t officially recognized as a collaborator of CMU-313/NodeBB, GitHub adds some restrictions to your permissions for security purposes, including not being able to assign yourself to an issue. Hence, we are using a bot to work around these restrictions. This is similar to how you would request issues on an Open Source project!

	For future projects, you will have full control over these GitHub features such as managing assignees, adding labels, creating milestones, and more.

### Code Refactoring and Validation (35 pts)

For this task, you will focus on refactoring the code and removing the corresponding Qlty issue(s) from your chosen file.
As part of the task, you must validate your changes for **one Qlty-reported smell** by re-running Qlty locally.

Back in your own fork, create a feature branch and implement the changes needed to address the chosen Qlty smell.
You should start with the following steps:

- Review the Qlty smells for the file (via ` qlty smells <selected/file.js>`).
- Identify the necessary code changes to address the chosen smell.
- Implement the changes and ensure that they do not introduce new Qlty warnings or issues.
- Run the linter and test suite to ensure your changes pass all checks (via `npm run lint` and `npm run test`).

We also want you to manually test your changes in a running NodeBB instance.
The purpose is to trigger the refactored code's execution from the user interface (UI) with the following steps:

- Within your implementation, add a print statement (e.g., `console.log(YOUR_NAME)`) immediately before, after, or in the middle of your refactored code.
- Restart the NodeBB instance.
- If you refactored a public/src/ file (front-end related file), watch logging via DevTools (`Ctrl+Shift+I` to open and then navigate to the 'Console' tab). If you refactored a src/ file, watch logging via `./nodebb log`.
- Perform any necessary UI operations that execute the refactored code (e.g., clicking buttons for an action)
- Take a screenshot of these logs and include it in your pull request description, along with a brief explanation of the steps you took to trigger the code.
- Remove the temporary print statement before committing your final code.

### GitHub Pull Request (40 pts)

As you work, be sure to periodically commit your changes.
Your commit message(s) must clearly describe what is changing.
If you’d like, you can also make use of branching and pull requests in your own repository to practice working with GitHub.

??? info "Branch and Commit Guidelines"
    **Branch names** should be short and provide a description of what you will be doing on that branch (e.g. *"fix-header-sizing-issue"*, *"fix-multiple-dialog-bug"*, *"add-sorting-feature"*). When working with others, you can also append your username to signal which branches are yours (e.g. *"313ta/add-sorting-feature"*).

	**Commits** should start with a verb and provide a description of what they are doing to the codebase (e.g. *"Remove faulty condition from getCustomerDetails"*, *"Fix failing CompositeTestCase"*, *"Fix issue #21"* ).

Once you are satisfied, create a pull request from your personal branch back to the class repository **using the widget below.**
This will redirect you to a pull request template for this assignment where you should fill out all of the fields, attach the required screenshots, and provide a clear PR title that includes the full path (e.g., `Refactor (public/src/client/categories.js): reduce nesting in render()`).

<div class="p1b-card md-typeset">
    <form onsubmit="event.preventDefault();
      const handle = document.getElementById('handle').value.trim();
      const branch = document.getElementById('branch').value.trim();
      if (!handle || !branch) { alert('Enter your GitHub username and branch name.'); return; }
      const url = `https://github.com/CMU-313/NodeBB/compare/main...${encodeURIComponent(handle)}:${encodeURIComponent(branch)}?expand=1&template=p1b-starter-task.md`;
      window.open(url, '_blank');
    ">
        <label>
            <span>GitHub Username</span>
            <input id="handle" required placeholder="your-username">
        </label>
        <label>
            <span>Branch</span>
            <input id="branch" required placeholder="main">
        </label>
        <button type="submit" class="md-button md-button--primary">Create pull request with template</button>
    </form>
</div>

??? info "Pull Request Guidelines"
	**Pull request titles** should describe what high-level changes were made to the codebase. Generally, they give a concise summary of all the commit messages.

    **Pull request descriptions** should describe what changes have been made in more detail and how the changes have been tested.

Automated checks (lint/tests) will run on your PR.
If CI fails but your local machine passes, try re-running the job once; if it still fails, comment in the PR and ping the staff.

!!! note "Test Suite Failures"
	If the tests are failing on GitHub but work locally, it may be caused by server overload. Re-running the failing GitHub Action 1-2 times will resolve this.

You should ensure that **all checks are green.**
A green checkmark on the PR signals that you’ve completed the implementation aspect of this assignment. ✅

## Submission

Finally, once you have created an issue and submitted a pull request, you should use the following Gradescope link to submit your work to be graded [Gradescope](https://www.gradescope.com/courses/1086939) 

## Grading

To receive full credit for this project, we expect:

- [ ] **GitHub Issue (20 pts)**
	- [ ] JavaScript file under src/ or public/src/
 	- [ ] Meaningful title with full path + line number
 	- [ ] Issue form fields completed with focused Qlty before evidence
 	- [ ] Successful bot assignment

- [ ] **Code Refactoring & Validation (35 pts)**
	- [ ] Target smell reduced/removed (same scope) with before/after Qlty evidence
 	- [ ] `npm run lint` and `npm run test` pass locally
 	- [ ] Runtime trigger demonstrated (logs + UI screenshot)

- [ ] **GitHub Pull Request (40 pts)**
 	- [ ] PR uses the P1B Refactoring PR template and all fields are completed
 	- [ ] PR title includes full path
 	- [ ] Commit messages are meaningful
 	- [ ] All CI checks green
