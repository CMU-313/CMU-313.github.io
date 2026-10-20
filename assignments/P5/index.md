---
title: "Project 5: Break and Fix"
release_date: 2026-11-03
due_date: 2026-11-09
checkpoints:
  - date: 2026-11-05
    title: "Red-Team Mutants to Partner"
    due_at: "2026-11-05T23:59:00-05:00"
    link: "1_break.md"
  - date: 2026-11-09
    title: "Mutation Testing & Red Team"
    due_at: "2026-11-09T23:59:00-05:00"
    link: "1_break.md"
---

# Project 5: Break and Fix

## Learning Goals

- Evaluate the strength of a test suite with mutation testing
- Design plausible faults that target specific requirements, and predict which tests should catch them
- Compare hand-written mutants with automatically generated ones, and understand the strengths of each
- Strengthen properties to kill surviving mutants, and argue when a mutant is equivalent
- Critically evaluate tests written or suggested by an AI agent
- Attack and defend tests across teams

## Project Context

In Project 4, you turned your requirements into properties that run on every pull request, and they pass. Your manager's next question is a fair one: *would they fail if the code were wrong?* A test suite that passes no matter what the code does is worse than no test suite, because it gives you false confidence.

**Mutation testing** answers that question directly. A *mutant* is a copy of your code with one small, deliberate bug in it: a `<` flipped to `<=`, a condition negated, a line deleted. If your tests fail on the mutant, they *kill* it. If they still pass, the mutant *survives*, and you've found a bug your tests can't see.

In this project, you'll attack your own properties: first with mutants you design by hand to break specific requirements, then with [Stryker](https://stryker-mutator.io/), which generates mutants automatically. You'll strengthen your properties until they kill what they should, examine one property that opencode helped write, and then trade attacks with a partner team.

## Deliverables and Deadlines

Most of this project is **individual**: you continue with the same target feature, branch, and traceability table from Projects 3 and 4. The TA check-in is a **team** meeting.

There are two (2) deadlines for this project. This project is worth a total of 45 points.

[**Mutation Testing & Red Team**](1_break.md) – 45 points – due Monday, November 9, 2026, 11:59PM

- Hand-Written Mutants with Predictions (8 pts)
- Stryker Run & Comparison (8 pts)
- Agent Failure Case (5 pts)
- Cross-Team Red Team (12 pts) – **red-team mutants due to your partner Thursday, November 5, 2026, 11:59PM**
- TA Check-in (Team) (12 pts) – held between November 4 and November 9

!!! tip
    The red-team mutants are due early so your partner has time to defend. Get your own mutants and Stryker run done early in the week, so you have time to respond to the mutants your partner sends you.
