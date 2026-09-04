---
title: "1B Starter Task"
nav_order: 20
---

# Project 1B: Starter Task and Self-Directed Learning

## Deliverables

Starter Task - 95 points - due Monday, September 7th, 11:59PM

- [TypeScript Self-Directed Learning](#typescript-self-directed-learning-25-pts) (25 pts)
- [GitHub Issue](#github-issue-25-pts) (25 pts)
- [Code Refactoring and Validation](#code-refactoring-and-validation-20-pts) (20 pts)
- [GitHub Pull Request](#github-pull-request-25-pts) (25 pts)

## Onboarding

Now that you have explored the repository, the development team would like to give you an onboarding assignment.

The team has noticed an accumulation of maintainability issues detected by **[Qlty](https://github.com/qltysh/qlty)**, a multi-language code quality tool.
Qlty detects “code smells” such as high function complexity, too many parameters, deep nesting, and duplicated code.
Your task is to remove one or more Qlty-reported issues by refactoring code and validating that your change takes effect within the opencode codebase.

## Prerequisites

### Onboarding Materials

Before jumping into the codebase, please review the [course syllabus](/syllabus) and be sure you have access to each of the following:

- Course Slack - check your email for an invite link
- [Canvas]({{ canvas_course_url() }})
- [Gradescope]({{ gradescope_course_url() }})

If you run into any trouble accessing the above or have any questions, reach out to the instructors.

### Git & GitHub

In this project and throughout the rest of this course, you will be expected to work extensively with Git and GitHub. Specifically for this project, you should be familiar with:

- [x] Forking/cloning GitHub repositories
- [x] Understanding general Git flow - pulling, branching, adding, committing, pushing, merging
- [x] Creating GitHub Issues and using related features (labels, assignees, milestones)
- [x] Creating GitHub Pull Requests and using related features (linking to issues)
- [x] Creating GitHub Project Boards

If you are not familiar with any of these steps, you may refer to the [Resources & Documentation](documentation.md#git--github-documentation) section if needed. There is a [simple Git-based exercise](github.md) that you are highly recommended to complete before proceeding with this project.

### Qlty

[Qlty](https://github.com/qltysh/qlty) is a multi-language static analysis tool that supports linting, scanning, and auto-formatting across a large number of languages and technologies, including Javascript.
For this assignment, you will locally install and configure the Qlty command-line tool to identify maintainability issues within the codebase.

To get started, you will need to [install Qlty](https://github.com/qltysh/qlty?tab=readme-ov-file#-quick-start) into your DevContainer.
You will know it is installed properly when you can run 

```bash
qlty --version
```

To use Qlty to show all of the code smells within the project, you should run:

```bash
qlty smells --all
```

Note that, by default, Qlty only analyzes the files that you've modified since your last commit.
`--all` tells Qlty to scan the entire codebase.

This will return a large list of issues and likely fill up your terminal with lots of code snippets.
To make it easier to find which files have issues, you can disable code snippets in the output via the `--no-snippets` option:

```bash
qlty smells --all --no-snippets
```

Once you've narrowed in on a particular file, you can produce a list of smells for just that file as follows:

```bash
qlty smells script/path/file.ts
```

You can use the `--no-snippets` option to find the associated line number for each smell on the left.

```bash

qlty smells --no-snippets  packages/desktop/src/main/apps.ts
     [0/3] 🔍  Analyzing 1 path... 0.03s
     [1/3] 👀  Checking structure of 1 files...  1.17s
     [2/3] 🤔  Looking for duplication across 1 files...  8.61s
     [3/3] ✨  Reporting...  

packages/desktop/src/main/apps.ts
  39  Function with many returns (count = 12): resolveWindowsAppPath
 119  Deeply nested control flow (level = 5)
 126  Deeply nested control flow (level = 5)
   1  High total complexity (count = 80)
  39  Function with high complexity (count = 73): resolveWindowsAppPath
  57  Function with high complexity (count = 22): resolveCmd

```

## Tasks

### TypeScript Self-Directed Learning (25 pts)

OpenCode, like most modern web codebases, is written in TypeScript. Qlty's smell reports, the code you'll be refactoring, and the reviewers reading your pull request all assume a working knowledge of TypeScript's type system. 

Recall the activity you did [Recitation 1](../../recitations/reci1-typescript.md). You are now tasked to apply your newfound knowledge of typescript to complete this section of the assignment. From the topics that you studied:

- Basic types & type annotations (string, number, arrays, functions)
- Unions, literals, and narrowing
- Object shapes: interfaces and type aliases
- Tooling, config, and ecosystem (tsconfig.json, flags, frameworks)

Once you feel comfortable with these topics, create a short multiple-choice quiz (at least 3 questions per topic) covering them (we recommend using an AI tool for this step), to check your own understanding. This quiz is a personal learning tool — you do not need to submit the whole thing.

**Deliverable:** Submit **two** multiple-choice questions from your quiz to Gradescope. For each question, include:

- The question text
- Four answer choices (A–D)
- The correct answer
- A 1–2 sentence explanation of why that answer is correct

Pick two questions you think would meaningfully test whether a classmate understands a core TypeScript concept. We will be pulling from student-submitted questions to build a quiz that the whole class will take during a future lecture, so questions should be general TypeScript-concept questions — clear and unambiguous, not opencode-specific trivia.

??? info "Good Wrong answers"
    Good wrong answers: 1) It should look like a real, sensible answer to someone who does not know the full concept, rather than a silly or farfetched joke. 2) It should stem from a plausible student error or partial understanding. 3) It should to match the correct answer and other choices in word count, grammatical structure, and tone so it does not accidentally stand out.

### GitHub Issue (25 pts)

First, choose a single Qlty-reported “smell” in a TypeScript file and open a GitHub issue in the [class repository](https://github.com/CMU-313/opencode/issues) using the **P1B Starter Task Issue template** to declare which smell you will be working on.

![GitHub Issue Template](/assets/images/hw/p1b_issue_template.png)

For the task, the smell must:

**Be a smell that no one else in the class has picked and created an issue for.**
  We expect you to look through existing *open* issues, if any, to avoid duplication.

The Qlty smell that you pick should be a maintainability smell (e.g., high function complexity, too many parameters, deep nesting, or duplicated code) that requires real code restructuring.

You should fill out all of the fields in the provided issue template and title the issue appropriately.
Specifically, you should include both the **full file path** and **line number** (reported by Qlty) in the title to avoid ambiguity and make it easier for others to identify which smells have already been claimed (e.g., `Refactor (packages/desktop/src/main/apps.ts:39): Function with many returns (count = 12)`).

??? info "Issue Guidelines"
    **Issues titles** should provide a high-level overview of what the problem is (e.g. *"Navbar button UI bugs"*, *"Unexpected registration validation errors"*). Sometimes, issues are used to propose new features (e.g. *"Add CSV export feature"*).

    **Issue descriptions** should then elaborate on the title. For feature-level bugs, this may include providing information about how to reproduce the bug; for codebase-level changes, you can name specific files.

Then, assign yourself to the Issue by leaving a comment that says "I would like to work on this please!"

You should soon see another comment by the `github-actions` bot informing you that you have been successfully assigned to this issue.

![Bot Issue Assignment](/assets/images/hw/bot_assignment.png)

??? info "Why Bot Assignment?"
	You might be curious as to why we are using a GitHub bot instead of directly assigning yourself to the issue. As you aren’t officially recognized as a collaborator of CMU-313/opencode, GitHub adds some restrictions to your permissions for security purposes, including not being able to assign yourself to an issue. Hence, we are using a bot to work around these restrictions. This is similar to how you would request issues on an Open Source project!

	For future projects, you will have full control over these GitHub features such as managing assignees, adding labels, creating milestones, and more.

### Code Refactoring and Validation (20 pts)

#### Code Refactoring (5 pts)

For this task, you will focus on refactoring the code and removing the corresponding Qlty issue(s) from your chosen file.
As part of the task, you must validate your changes for **one Qlty-reported smell** by re-running Qlty locally.

**Back in your own fork**, create a feature branch and implement the changes needed to address the chosen Qlty smell.
You should start with the following steps:

- Review the Qlty smells for the file (via ` qlty smells <selected/file.ts>`).
- Identify the necessary code changes to address the chosen smell.
- Implement the changes and ensure that they do not introduce new Qlty warnings or issues.
- Run the linter and test suite to ensure your changes pass all checks (via `bun lint` and `bun test`).



#### Change Validation (15 pts)

You will need to validate that the code works.  To do this, you need to offer compelling evidence that the change has not broken anything.  You do this with tests.  Your changes should have tests that validate that the change did not break anything. This could include tests that were existing before your change, or you may need to write new tests.  In your PR, you should explicitly say which tests cover your changes, and a short explanation as to why those tests are sufficient to convince a reviewer that the changes did not break anything.  NOTE: The tests that you submit should execute the code changes you made. 

You can build a coverage report using the following command (in the specific package directory where you made the changes): 

```bash
bun test --coverage --coverage-dir=./coverage
```

You should start by running the tests locally, and confirm that they are passing, and that they cover the changes you made. You might need to add tests, or update existing tests. Once you are convinced that your tests are covering a correct change, you should then push your changes to your branch, and make sure they pass on CI.  

NOTE: because there are too many tests for all the students to run on every change, you should add the tests that cover your changes to the CI on your branch, to make sure they run.  

### GitHub Pull Request (25 pts)

As you work, be sure to periodically commit your changes.
Your commit message(s) must clearly describe what is changing.
If you’d like, you can also make use of branching and pull requests in your own repository to practice working with GitHub.

??? info "Branch and Commit Guidelines"
    **Branch names** should be short and provide a description of what you will be doing on that branch (e.g. *"fix-header-sizing-issue"*, *"fix-multiple-dialog-bug"*, *"add-sorting-feature"*). When working with others, you can also append your username to signal which branches are yours (e.g. *"313ta/add-sorting-feature"*).

	**Commits** should start with a verb and provide a description of what they are doing to the codebase (e.g. *"Remove faulty condition from getCustomerDetails"*, *"Fix failing CompositeTestCase"*, *"Fix issue #21"* ).

Once you are satisfied, create a pull request from your personal branch back to the class repository **using the widget below.**
This will redirect you to a pull request template for this assignment where you should fill out all of the fields, attach the required screenshots, and provide a clear PR title that includes the full path (e.g., `Refactor (packages/desktop/src/main/apps.ts): Function with many returns`).

<div class="p1b-card md-typeset">
    <form onsubmit="event.preventDefault();
      const handle = document.getElementById('handle').value.trim();
      const branch = document.getElementById('branch').value.trim();
      if (!handle || !branch) { alert('Enter your GitHub username and branch name.'); return; }
      const url = `https://github.com/CMU-313/opencode/compare/main...${encodeURIComponent(handle)}:${encodeURIComponent(branch)}?expand=1&template=p1b-starter-task.md`;
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
	If the tests are failing on GitHub but work locally, it may be caused by server overload. ~~Re-running the failing GitHub Action 1-2 times will resolve this.~~ DM a staff member on Slack or go to office hours to have one of us rerun it for you.

You should ensure that **all checks are green.**
A green checkmark on the PR signals that you’ve completed the implementation aspect of this assignment. ✅

## Submission

Finally, once you have created an issue and submitted a pull request, you should use the following Gradescope link to submit your work to be graded: [Gradescope]({{ gradescope_course_url() }}) 

## Grading

To receive full credit for this project, we expect:

- [ ] **TypeScript Self-Directed Learning (25 pts)**
	- [ ] Two multiple-choice questions submitted
 	- [ ] Each question has exactly one clearly correct answer among four choices
 	- [ ] Each question includes a brief explanation
 	- [ ] Questions test a core TypeScript concept (not trivia or opencode-specific code)

- [ ] **GitHub Issue (25 pts)**
	- [ ] TypeScript file within the opencode codebase
 	- [ ] Meaningful title with full path + line number
 	- [ ] Issue form fields completed with Qlty evidence
 	- [ ] Successful bot assignment

- [ ] **GitHub Pull Request (25 pts)**
 	- [ ] PR uses the P1B Refactoring PR template and all fields are completed
 	- [ ] PR title includes full path
 	- [ ] Commit messages are meaningful
 	- [ ] All CI checks green

- [ ] **Code Refactoring & Validation (20 pts)**
	- [ ] Target smell reduced/removed (same scope) with before/after Qlty evidence
 	- [ ] `bun lint` and `bun test` pass locally
 	- [ ] Test coverage results showing change covered
    - [ ] Test output showing tests passing.
