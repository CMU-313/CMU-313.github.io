---
layout: page
title: Recitation 8 - static analysis and continuous integration 
permalink: /recitations/8-analysis-ci
parent: Recitations
---
 
# Recitation 8: static analysis and continuous integration
Static and dynamic analysis tools help you keep the codebase healthy. In this recitation, we will learn how to set up these tools in CI (GitHub Actions). 
# Step 1: Setup your sample Python repo

First, go to [this template repo](https://github.com/CMU-313/fall-2022-recitation-7-analysis-ci) and [use it](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template) to create your own repo. The repo is very similar to the HW4 repo, except that it comes with a failing test. 

You already learned that it's a big no-no to push directly to `main`. We can actually enforce this using [branch protect rules](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/defining-the-mergeability-of-pull-requests/managing-a-branch-protection-rule). Read the docs to understand what they are, and set the following rules:

* Requires a pull request before merging to `main`: just check the box
* Requires tests to pass before merging to `main`: search for the job name in the required checks (i.e. `test` in this case)

Your setting should look like this:

![](/assets/images/reci/branch-protection.png)

# Step 2: Fix the broken CI

The ❌ really shouldn't have been there in the first place if I had these rules enabled. Now let's fix it. Branch off from `main` and create a PR to fix the broken CI. 

The fix is simple: add an `if` in `app.fibonacci` to return `0` if `position == 0`.

The `test` job should pass on your PR. Click "Squash and merge"* to merge after the status checks pass.

*: It's just a lot cleaner than the default merge.

# Step 3: Make your code pretty 

Different tab sizes driving you crazy? Let's use a tool to standardize them all. A code formatter, a static analysis tool, helps one identify and fix formatting issues in the codebase. Let's use [black](https://github.com/psf/black) as an example. 

First, create another branch for setting up a code formatter.

Then, install it locally and try running it.
* `pipenv install --dev black`: `black` is only a _development dependency_. Your package doesn't actually use it.
* `pipenv run black . --check`: runs `black` in the current directory. `--check` dry-runs `black` and don't alter any files.
  * Observe some files on the list.
* `pipenv run black .`: this will actually change the files.
  * Run `git diff` to observe the file changes.

Using CI, we can enforce formatting requirements using the same GH Actions + status checks. For popular tools, someone has done it before, and you can reuse their workflow. 

* Go to [this existing `black` Actions on GH Marketplace](https://github.com/marketplace/actions/run-black-formatter)
* Click "Use lastest version" to see what needs to be added to `.github/workflows/main.yml`
* Add another "job" to the `.yml` file called `format`
* Push your formatted files to the branch and observe `format` passes.
* Squash and merge the PR

# Step 4: Add test coverage to the CI workflow

Finally, you can also do some dynamic analysis. Since we are already using `pytest`, let's use [`pytest-cov`](https://pytest-cov.readthedocs.io/en/latest/), a plugin that reports test coverage.

First, install and try to use it locally:

* Create another branch
* `pipenv install --dev pytest-cov`: install `pytest-cov` locally 
* `pipenv run pytest --cov=app`: runs `pytest` with coverage report

Now, let's add another job in the workflow for reporting coverage:

* Copy the steps before `pytest` from the `test` workflow 
* Now, run `pipenv run pytest --cov=app` to report coverage
* Push and observe the new check running

## Bonus: report coverage in PRs

The coverage job doesn't really add much to the workflow now since it doesn't fail. Without being too strict about coverage, we can at least display the coverage status in the PR. 

[Somebody has already done it](https://github.com/marketplace/actions/pytest-coverage-commentator), so we can use it in our repo too. Here are the lines that matter:

```yml
- name: Build coverage file
  run: |
    pytest --cache-clear --cov=app test/ > pytest-coverage.txt
- name: Comment coverage
  uses: coroo/pytest-coverage-commentator@v1.0.2
```

If set up, the job will automatically comment on PRs with the coverage info:
![](/assets/images/reci/coverage-report.png)