---
title: "Project 5: Break and Fix"
release_date: 2026-11-05
due_date: 2026-11-12
checkpoints:
  - date: 2026-11-07
    title: "Extra Credit: Red-Team Sign-up"
    due_at: "2026-11-07T23:59:00-05:00"
    link: "1_break.md"
  - date: 2026-11-10
    title: "Extra Credit: Red-Team Mutants to Target"
    due_at: "2026-11-10T23:59:00-05:00"
    link: "1_break.md"
  - date: 2026-11-12
    title: "Mutation Testing & Red Team"
    due_at: "2026-11-12T23:59:00-05:00"
    link: "1_break.md"
---

# Project 5: Break and Fix

## Learning Goals

- Evaluate the strength of a test suite with mutation testing
- Design plausible faults that target specific requirements, and predict which tests should catch them
- Compare hand-written mutants with automatically generated ones, and understand the strengths of each
- Strengthen properties to kill surviving mutants, and argue when a mutant is equivalent
- Critically evaluate tests written or suggested by an AI agent
- Reflect on how your requirements, tests, and use of an AI agent shaped your work across the semester
- (Extra credit) Attack and defend tests across teams

## Project Context

In Project 4, you turned your requirements into properties that CI runs on your pull request, and they pass. Your manager's next question is a fair one: *would they fail if the code were wrong?* A test suite that passes no matter what the code does is worse than no test suite, because it gives you false confidence.

**Mutation testing** answers that question directly. A *mutant* is a copy of your code with one small, deliberate bug in it: a `<` flipped to `<=`, a condition negated, a line deleted. If your tests fail on the mutant, they *kill* it. If they still pass, the mutant *survives*, and you've found a bug your tests can't see.

In this project, you'll attack your own properties: first with mutants you design by hand to break specific requirements, then with [Stryker](https://stryker-mutator.io/), which generates mutants automatically. You'll strengthen your properties until they kill what they should, examine one property that opencode helped write, and look back on how your requirements, tests, and use of an AI agent held up across the semester. For extra credit, you can also attack another team's properties.

## Deliverables and Deadlines

This project is **individual**: you continue with the same target feature, branch, and traceability table from Projects 3 and 4.

This project is worth a total of 100 points, with one deadline. The optional extra-credit red team has two earlier deadlines of its own.

[**Mutation Testing & Red Team**](1_break.md) – 100 points – due Thursday, November 12, 2026, 11:59PM

- Hand-Written Mutants with Predictions (30 pts)
- Stryker Run & Comparison (35 pts)
- Agent Failure Case (20 pts)
- Retrospective (15 pts)
- Extra Credit: Cross-Team Red Team (up to 10 pts) – optional; **sign up by Saturday, November 7, 2026, and post mutants to your target by Tuesday, November 10, 2026, 11:59PM**

!!! tip
    If you sign up for the red team, its deadlines come early so your target has time to defend. Finish the required parts first; extra credit can't make up for missing them.
