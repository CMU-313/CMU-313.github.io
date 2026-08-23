---
title: "3A Deployment and CI"
nav_order: 10
---

# Project 3A: Deployment and CI

## Deliverables

**Deployment & CI Design** – 35 points – due Monday, October 26, 2026, 11:59PM

- [Deployed Application (20 pts)](#deployed-application-20-pts)
- [CI/CD Pipeline Design Document (15 pts)](#cicd-pipeline-design-document-group-15-pts)

### Deployed Application (20 pts)

Your team will be using Linux Virtual Machines (VMs) hosted at CMU for the deployment of your opencode application. Further instructions on how to deploy can be found on the [Deployment & CD Pipeline Setup](deployment.md) page.

This step matters beyond just getting a link to share: following the deployment instructions generates a GitHub Actions workflow in your repository that automatically deploys on changes to `main`. That workflow **is** the CD half of this project's "CI/CD" — keep it in place, since the rest of P3 builds the CI half around it rather than replacing it.

Once you have successfully deployed your website, make sure to test within your team to ensure that your added feature(s) from Project 2 are properly integrated.

By the checkpoint deadline, you should as a group:

- Submit the link to the deployed site onto Gradescope
- Add the link to the deployed site and the link to the UserGuide.md that your team submitted for Project 2 to this [public spreadsheet](https://docs.google.com/spreadsheets/d/1Xmaqmu5MITPjy1TFDpohQFwzaPYcUNVviuc4jLDXPEY/edit?usp=sharing) next to your team name. This will be used in [Feature Review](/projects/p3/2_finalsubmission/#extra-credit-feature-review-6-pts) for extra credit.

### CI/CD Pipeline Design Document (Group) (15 pts)

Before jumping into implementation, your manager would like your team to design the CI checks that will run alongside the deploy workflow you just stood up. As a group, you will identify **at least N checks to add to your pipeline**, where N is the number of people on your team (so one per person), and each person will individually own building one of them in the final submission.

We provide a [starter list of tools](resources.md) organized by category, but you are not limited to these tools. In your selection, you should have:

- **at least one** code quality / static analysis check (lint, type-check, static analysis)
- **at least one** testing / dynamic analysis check (coverage gate, mutation testing, load/fuzz testing)
- **at least one** security / dependency check (vulnerability or secret scanning)
- **at least one** check that is not from our starter list
- **no** check that duplicates tooling opencode's pipeline already runs (e.g. Qlty, which you already used in Project 1 — pick something that adds new coverage)

You should create this document as a team in the Google Drive folder your TA shared with you, with each person authoring the subsection for the check they're committing to own. For each check, write:

- What the check does, and a link to its documentation/source
- Why your team picked it (trade-offs vs. alternatives you considered)
- Where it will run in the pipeline (e.g. on every PR, on merge to `main`) and whether it will block merges or just report
- What customization or configuration it needs, both up front and over time

!!! note "Grading Note"
    We are not grading whether the checks are implemented yet at this checkpoint — just that your team has a concrete, justified plan. Implementation happens in the final submission.

!!! note "Time Management"
    Don't spend too long researching every option exhaustively. Set deadlines within your team so everyone has enough time left to actually build and merge their check for the final deadline.

By the checkpoint deadline, your team will submit to Gradescope:

- A link to your CI/CD Pipeline Design Document.

## Grading

To receive full credit for the checkpoint, we expect:

- [ ] A link to your successfully deployed web application for your team repository, with the auto-deploy GitHub Actions workflow in place
- [ ] A link to your CI/CD Pipeline Design Document. Your team's selected checks must satisfy all the following criteria:
  - Contain at least one code quality / static analysis check
  - Contain at least one testing / dynamic analysis check
  - Contain at least one security / dependency check
  - Contain at least one check not on our starter list of tools
  - Contain no overlaps between teammates, and no duplication of tooling opencode's pipeline already runs
- [ ] Each check's subsection must contain a justification and integration plan as described above
