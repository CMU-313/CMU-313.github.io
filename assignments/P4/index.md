---
title: "Project 4: Specify and Fix"
release_date: 2026-10-27
due_date: 2026-11-02
checkpoints:
  - date: 2026-11-02
    title: "Properties & Fixes"
    due_at: "2026-11-02T23:59:00-05:00"
    link: "1_specify.md"
---

# Project 4: Specify and Fix

## Learning Goals

- Translate natural-language requirements into executable property-based tests
- Recognize and apply common kinds of properties: round-trip, invariant, model/oracle, and metamorphic
- Write generators that explore a feature's input space
- Triage a failing test: decide whether the code, the test, or the requirements are wrong
- Gate merges on automated checks with continuous integration and branch protection

## Project Context

In Project 3, you interviewed users and turned what you heard into precise requirements for one opencode feature. Your manager is pleased, but a requirements table only helps if someone checks it. Requirements that live in a document drift away from the code the moment the next pull request lands.

Your manager now wants each requirement to become something the build checks automatically, on every change. Example-based unit tests only check the handful of inputs you thought of. Instead, you'll write **property-based tests** with [fast-check](https://fast-check.dev): each test states a rule that should hold for *every* input, and fast-check generates hundreds of inputs looking for one that breaks it.

When a property fails, the work begins: is the code wrong, is your property wrong, or did two of your interviewees actually want incompatible things? You'll decide, fix what needs fixing, and land the result through your team's pipeline.

## Deliverables and Deadlines

The properties, triage, and fixes are **individual**: you continue with the same target feature and requirements you declared in Project 3. The CI slice is a **team** deliverable.

There is one (1) deadline for this project. This project is worth a total of 30 points.

[**Properties & Fixes**](1_specify.md) – 30 points – due Monday, November 2, 2026, 11:59PM

- Properties Tied to Requirements (Individual) (15 pts)
- Failure Triage & Fixes (Individual) (10 pts)
- CI Slice (Team) (5 pts)

!!! tip "Resources"
    [Recitation 7](/recitations/reci7-pbt/) introduced fast-check and the kinds of properties you'll use here. Its [problem set](https://github.com/CMU-313/F26-reci-7/blob/main/PROBLEM_SET.md) is a good warm-up if you haven't finished it.
