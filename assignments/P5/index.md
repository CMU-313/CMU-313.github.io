---
title: "Project 5: Break and Fix"
release_date: 2026-11-06
due_date: 2026-11-12
checkpoints:
  - date: 2026-11-09
    title: "Extra Credit: Red-Team Mutants to Target"
    due_at: "2026-11-09T23:59:00-05:00"
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
- (Extra credit) Attack and defend tests across teams

## Project Context

In Project 4, you turned your requirements into properties that CI runs on your pull request, and they pass. Your manager's next question is a fair one: *would they fail if the code were wrong?* A test suite that passes no matter what the code does is worse than no test suite, because it gives you false confidence.

**Mutation testing** answers that question directly. A *mutant* is a copy of your code with one small, deliberate bug in it: a `<` flipped to `<=`, a condition negated, a line deleted. If your tests fail on the mutant, they *kill* it. If they still pass, the mutant *survives*, and you've found a bug your tests can't see.

In this project, you'll attack your own properties: first with mutants you design by hand to break specific requirements, then with [Stryker](https://stryker-mutator.io/), which generates mutants automatically. You'll strengthen your properties until they kill what they should, and examine one property that opencode helped write. For extra credit, you can also trade attacks with a partner team.

## Deliverables and Deadlines

This project is **individual**: you continue with the same target feature, branch, and traceability table from Projects 3 and 4.

This project is worth a total of 100 points, with one deadline. The optional extra-credit red team has an earlier deadline of its own.

[**Mutation Testing & Red Team**](1_break.md) – 100 points – due Thursday, November 12, 2026, 11:59PM

- Hand-Written Mutants with Predictions (35 pts)
- Stryker Run & Comparison (40 pts)
- Agent Failure Case (25 pts)
- Extra Credit: Cross-Team Red Team (up to 10 pts) – optional; **red-team mutants due to your target Monday, November 9, 2026, 11:59PM**

!!! tip
    If you opt into the red team, its mutants are due early so your target has time to defend. Finish the required parts first; extra credit can't make up for missing them.
