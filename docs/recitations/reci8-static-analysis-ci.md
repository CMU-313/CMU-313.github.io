---
title: Recitation 8 - static analysis and continuous integration
---

# Recitation 8: static analysis and continuous integration

Static and dynamic analysis tools help you keep the codebase healthy. In this recitation, we will learn how to set up these tools in CI (GitHub Actions). 
## Step 1: Setup your sample Python repo

First, go to [this template repo](https://github.com/CMU-313/fall-2022-recitation-8-analysis-ci) and [use it](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) to create your own repo. The repo is very similar to the HW4 repo, except that it comes with a failing test. 

You already learned that it's a big no-no to push directly to `main`. We can actually enforce this using [branch protect rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/managing-a-branch-protection-rule). Read the docs to understand what they are, and set the following rules:

* Requires a pull request before merging to `main`
* Requires tests to pass before merging to `main`: 
  * Search for the job name in the required checks (i.e. `test` in this case.) You may need to save the settings first before this search box appears.

Your setting should look like this:

![](/assets/images/reci/branch-protection.png)

The failing test cases ❌ wouldn’t have been there if I had these rules enabled in the first place. Now, let's fix our failing test. 
## Step 2: Fix the broken CI

The ❌ really shouldn't have been there in the first place if I had these rules enabled. Now let's fix it. Branch off from `main` and create a PR to fix the broken CI. 

Take a look in the Actions page to see which test is failing. Branch off from `main` and create a PR to fix the broken CI. (the fix should be VERY simple!)

The `test` job should pass on your PR. Click "Squash and merge"* to merge after the status checks pass.

*: It's just a lot cleaner than the default merge.

**HINT:** If you are _really_ stuck on how to fix, click [here](https://www.youtube.com/watch?v=dQw4w9WgXcQ)

## Step 3: Make your code pretty 

Different tab sizes driving you crazy? Let's use a tool to standardize them all. A code formatter, a static analysis tool, helps one identify and fix formatting issues in the codebase. Let's use [black](https://github.com/psf/black) as an example. 

First, create another branch for setting up a code formatter.

Then, run the following commands to install it locally and try running it:

* `pipenv install --dev black`: `black` is only a _development dependency_. Your package doesn't actually use it.
* `pipenv run black . --check`: 
  * Runs `black` in the current directory. `--check` dry-runs `black` and don't alter any files.
  * Observe some files on the list.
* `pipenv run black .`: 
  * This will actually change the files.
  * Run `git diff` to observe the file changes.

Using CI, we can enforce formatting requirements using the same GH Actions + status checks. For popular tools, someone has done it before, and you can reuse their workflow. 

* Go to [this existing `black` Actions on GH Marketplace](https://github.com/marketplace/actions/run-black-formatter)
* Click "Use lastest version" to see what needs to be added to `.github/workflows/main.yml`
* Add another job called “format” to the `main.yml` file to use `black` to check the file formatting 
* Push your formatted files to the branch and observe `format` passes.
* Squash and merge the PR

## Step 4: Add test coverage to the CI workflow

Finally, you can also do some dynamic analysis. Since we are already using `pytest`, let's use [`pytest-cov`](https://pytest-cov.readthedocs.io/en/latest/), a plugin that reports test coverage.

First, install and try to use it locally:

* Create another branch
* Install `pytest-cov` locally: `pipenv install --dev pytest-cov` 
* Runs `pytest` with coverage report: `pipenv run pytest --cov=app`

Now, let's add another job in the workflow for reporting coverage:

* From the `test` workflow, copy the steps before `pytest` 
* Now, run `pipenv run pytest --cov=app` to report coverage
* Push and observe the new check running

## Bonus: report coverage in PRs

The coverage job doesn't really add much to the workflow now since it doesn't fail. Without being too strict about coverage, we can at least display the coverage status in the PR. 

[Somebody has already done it](https://github.com/marketplace/actions/pytest-coverage-commentator), so we can use it in our repo too. __Hint__: you should only need the last two steps in the workflow.

Note that this action will only run on pull request-based workflows, so you will need to modify your triggers. 

If set up, the job will automatically comment on PRs with the coverage info:
![](/assets/images/reci/coverage-report.png)