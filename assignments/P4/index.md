---
title: "Project 4: Specify and Fix"
release_date: 2026-10-30
due_date: 2026-11-05
checkpoints:
  - date: 2026-11-05
    title: "Properties & Fixes"
    due_at: "2026-11-05T23:59:00-05:00"
    link: "1_specify.md"
---

# Project 4: Specify and Fix

## Learning Goals

- Judge whether a requirement is feasible to implement, and revise it without losing what users actually asked for
- Translate natural-language requirements into executable property-based tests
- Recognize and apply common kinds of properties: round-trip, invariant, model/oracle, and metamorphic
- Write generators that explore a feature's input space
- Triage a failing test: decide whether the code or the test is wrong
- Land changes through a pull request whose automated tests pass

## Project Context

In Project 3, you interviewed users and turned what you heard into precise requirements for one opencode feature. Your manager is pleased, but a requirements table only helps if someone checks it. Requirements that live in a document drift away from the code the moment the next pull request lands.

Your manager now wants the build to check your requirements automatically, on every change, starting with at least four of them. Before that, though, you need to look at your requirements with an engineer's eye: some of what users want can't actually be built as stated, and needs to become something that can. Then you'll write **property-based tests** with [fast-check](https://fast-check.dev): each test states a rule that should hold for *every* input, and fast-check generates hundreds of inputs looking for one that breaks it.

When a property fails, you decide whether the code or the test is wrong, fix it, and keep going until every property passes. Then you open a pull request and get your properties passing there too.

## Deliverables and Deadlines

This project is **individual**: you continue with the same target feature and requirements you declared in Project 3.

There is one (1) deadline for this project. This project is worth a total of 65 points.

[**Properties & Fixes**](1_specify.md) – 65 points – due Thursday, November 5, 2026, 11:59PM

- Step 1: Review Your Requirements (Individual) (10 pts)
- Step 2: Write Properties for Your Requirements (Individual) (40 pts)
- Step 3: Run, Triage, and Fix (Individual) (15 pts)

!!! tip "Resources"
    [Recitation 7](/recitations/reci7-pbt/) introduced fast-check and the kinds of properties you'll use here. Its [problem set](https://github.com/CMU-313/F26-reci-7/blob/main/PROBLEM_SET.md) is a good warm-up if you haven't finished it.
