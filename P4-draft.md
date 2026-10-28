<!-- ===== source: assignments/P4/index.md ===== -->
*Site metadata (frontmatter):*

```yaml
title: "Project 4: Specify and Fix"
release_date: 2026-10-30
due_date: 2026-11-05
checkpoints:
  - date: 2026-11-05
    title: "Properties & Fixes"
    due_at: "2026-11-05T23:59:00-05:00"
    link: "1_specify.md"
```

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

There is one (1) deadline for this project. This project is worth a total of 65 points.

[**Properties & Fixes**](1_specify.md) – 65 points – due Thursday, November 5, 2026, 11:59PM

- Properties Tied to Requirements (Individual) (30 pts)
- Failure Triage & Fixes (Individual) (25 pts)
- CI Slice (Team) (10 pts)

<!-- !!! tip "Resources" -->
> **Tip: Resources**
>
> [Recitation 7](/recitations/reci7-pbt/) introduced fast-check and the kinds of properties you'll use here. Its [problem set](https://github.com/CMU-313/F26-reci-7/blob/main/PROBLEM_SET.md) is a good warm-up if you haven't finished it.

<!-- ===== source: assignments/P4/1_specify.md ===== -->
*Site metadata (frontmatter):*

```yaml
title: "4A Properties & Fixes"
nav_order: 10
```

# Project 4: Properties & Fixes

## Deliverables

**Properties & Fixes** – 65 points – due Thursday, November 5, 2026, 11:59PM

- [Properties Tied to Requirements (Individual) (30 pts)](#properties-tied-to-requirements-individual-30-pts)
- [Failure Triage & Fixes (Individual) (25 pts)](#failure-triage-fixes-individual-25-pts)
- [CI Slice (Team) (10 pts)](#ci-slice-team-10-pts)

## Setup

### Your Branch

Each team member works on **their own branch** in the team repository for this project, named so it's clear who owns it (e.g. `<andrewid>/properties`). Keep using this branch after this project; don't delete it once your PR merges.

### Installing fast-check

Add fast-check as a dev dependency of the package that contains your target feature. For most students, that's `packages/opencode`:

```bash
cd packages/opencode
bun add -d fast-check
```

<!-- !!! tip "One teammate adds the dependency" -->
> **Tip: One teammate adds the dependency**
>
> If everyone on your team runs `bun add` on their own branch, every PR will conflict on `package.json` and `bun.lock`. Have **one** teammate add fast-check in a small PR, merge it, and have everyone else bring that into their branch before starting.

Put your property tests next to the package's existing tests (e.g. `packages/opencode/test/<feature>/<feature>.property.test.ts`) and run them with `bun test` from inside the package. fast-check works with any test runner; you call `fc.assert(fc.property(...))` inside an ordinary `test(...)` block.

<!-- !!! warning "Make sure your tests run in CI" -->
> **Warning: Make sure your tests run in CI**
>
> opencode's CI only runs `bun test` for the packages listed in `turbo.json`. If your feature lives in a package that isn't listed, your tests will pass locally and **silently never run** in CI. Read the "Unit tests" section of `TESTING.md` in the repository and add your package if needed.

### Your Traceability Table

Copy your requirements table from Project 3 into your branch as `traceability/<andrewid>.md`, using the template below, and add two columns.

<!-- !!! note "About the examples" -->
> **Note: About the examples**
>
> The examples on this page use a made-up feature, a **request rate limiter**, so that they don't match anyone's target. Don't copy them; your requirements and properties must come from your own feature and interviews.

| ID | Interview evidence | Requirement | Acceptance Criteria | Property (kind) | Test |
|---|---|---|---|---|---|
| R1 | `I-3`, `S-7`: "If I'm at my limit, the next call should wait, not fail" | Once a user has made the maximum number of requests in a window, further requests are delayed until the window resets, never rejected. | With a limit of 3 per minute, a 4th request at 0:30 completes after 1:00 and does not throw. | No request is ever rejected (invariant) | `rate-limit.property.test.ts` |

<!-- ??? example "Traceability file template (copy into `traceability/<andrewid>.md`)" -->
> **Example: Traceability file template (copy into `traceability/<andrewid>.md`) (collapsible on the site)**
>
> ```markdown
> # Traceability: <your name> (<andrewid>)
>
> **Target feature:** <feature, and the main source files it lives in>
>
> ## Requirements
>
> | ID | Interview evidence | Requirement | Acceptance Criteria | Property (kind) | Test |
> |---|---|---|---|---|---|
> | R1 | | | | | |
>
> Properties written or suggested by opencode or another AI tool: <list by requirement ID, or "none">
>
> ## Triage log
>
> | Property | Shrunk counterexample | Outcome (real bug / wrong property / requirements conflict) | Why | Fix commit |
> |---|---|---|---|---|
> ```

Your acceptance criteria are a starting point for each property: a property should check the criteria for every generated input, not just the one example you wrote down. You may revise a requirement or its acceptance criteria if writing its property shows it was ambiguous, but keep the interview evidence and note what changed.

## Properties Tied to Requirements (Individual) (30 pts)

Write **at least 4** fast-check properties for your target feature. Each property must:

- Be tied to a specific requirement from your table (the Test column links to it, and the test's name or a comment cites the requirement ID)
- Be labeled with its kind:

| Kind | The idea | Example for a rate limiter |
|---|---|---|
| **Round-trip** | Doing then undoing (or encoding then decoding) gets you back where you started | Saving the limiter's state and loading it back gives a limiter that makes the same decisions |
| **Invariant** | Something that is true for every input | For any sequence of requests, no window ever contains more than the limit |
| **Model / oracle** | Compare against a simpler implementation that is obviously correct | The limiter agrees with a slow version that keeps a full list of timestamps |
| **Metamorphic** | Changing the input in a known way changes the output in a predictable way | Raising the limit never causes a request that was allowed to be delayed |

Your properties must use **at least two different kinds**.

A property is only as good as the inputs it sees. Write generators (arbitraries) that actually reach the interesting cases for your feature, such as the boundaries your interviewees worried about, not just random strings. Briefly explain your generator choices in a comment.

<!-- !!! note "Using opencode" -->
> **Note: Using opencode**
>
> You may use opencode (or any AI tool) to help write properties and generators. If you do, note which properties it wrote or suggested in your traceability table. You are responsible for every property being correct and tied to a real requirement.

## Failure Triage & Fixes (Individual) (25 pts)

Run your properties. For **every** property that fails, decide which of these it is, and act:

| Outcome | What it means | What you do |
|---|---|---|
| **Real bug** | The code violates a requirement users actually have | Fix the code |
| **Wrong property** | Your property doesn't say what the requirement means (or the requirement was stated imprecisely) | Fix the property (and the requirement, if needed) |
| **Requirements conflict** | Two interviewees wanted incompatible things | Decide which behavior wins, document the call and why, and update the requirement |

Add a **Triage log** section to your traceability file with one entry per failure: the property, the shrunk counterexample fast-check reported, which outcome you chose, why, and a link to the commit that fixed it.

If none of your properties fail, that's fine. Say so in your triage log, and describe how you checked that your properties are actually exercising the feature (for example, the range of inputs your generators produce).

### Landing Your Work

Open a pull request from your branch to `main` containing your properties, fixes, and traceability file. At least one teammate must review and approve it before it merges. Your PR must be **merged into `main`** by the deadline.

## CI Slice (Team) (10 pts)

As a team, make sure your properties are enforced on every change:

- **Properties run on every PR.** opencode's existing `test` workflow runs on pull requests; confirm that every teammate's properties actually run in it (see the warning in [Setup](#installing-fast-check)). If your team prefers, you may add a separate workflow just for properties.
- **`main` is branch-protected.** In your team repository's settings, add a branch protection rule (or ruleset) for `main` that requires a pull request before merging, at least one approving review, and the test check to pass.

## Submission

**Individually**, submit to Gradescope:

- A link to your merged pull request
- A link to `traceability/<andrewid>.md` on `main`

**As a team**, one member submits to Gradescope:

- A link to a GitHub Actions run on a pull request in which your team's properties ran
- A screenshot of your branch protection settings for `main`

## Grading

To receive full credit for the properties, we expect:

- [ ] At least 4 fast-check properties for your declared target feature, using at least two different kinds
- [ ] Each property tied to a requirement in your traceability table and labeled by kind
- [ ] Generators that reach meaningful inputs for the feature, with a brief explanation
- [ ] A traceability table that links every property to its requirement and its test

To receive full credit for the triage and fixes, we expect:

- [ ] A triage log entry for every failing property, with its counterexample, outcome, and justification
- [ ] Code fixes for real bugs, corrected properties for wrong properties, and a documented decision for each requirements conflict
- [ ] A PR from your own branch, reviewed and approved by a teammate, and merged into `main`

To receive full credit for the CI slice, we expect:

- [ ] Every teammate's properties running in CI on pull requests
- [ ] Branch protection on `main` requiring a PR, an approving review, and passing tests
