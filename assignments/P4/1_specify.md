---
title: "4A Properties & Fixes"
nav_order: 10
---

# Project 4: Properties & Fixes

## Deliverables

**Properties & Fixes** – 65 points – due Monday, November 2, 2026, 11:59PM

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

Put your property tests next to the package's existing tests (e.g. `packages/opencode/test/permission/permission.property.test.ts`) and run them with `bun test` from inside the package. fast-check works with any test runner; you call `fc.assert(fc.property(...))` inside an ordinary `test(...)` block.

!!! warning "Make sure your tests run in CI"
    opencode's CI only runs `bun test` for the packages listed in `turbo.json`. If your feature lives in a package that isn't listed, your tests will pass locally and **silently never run** in CI. Read the "Unit tests" section of `TESTING.md` in the repository and add your package if needed.

### Your Traceability Table

Copy your requirements table from Project 3 into your branch as `traceability/<andrewid>.md`, and add two columns:

| ID | Interview evidence | Requirement | Property (kind) | Test |
|---|---|---|---|---|
| R1 | `C-12`, `S-4`: "I'd be furious if it ran `rm -rf` after I said deny" | A command matching a `deny` rule is never executed, regardless of other matching rules. | Deny always wins (invariant) | `permission.property.test.ts` |

You may revise a requirement if writing its property shows it was ambiguous, but keep the interview evidence and note what changed.

## Properties Tied to Requirements (Individual) (30 pts)

Write **at least 4** fast-check properties for your target feature. Each property must:

- Be tied to a specific requirement from your table (the Test column links to it, and the test's name or a comment cites the requirement ID)
- Be labeled with its kind:

| Kind | The idea | Example for permission rules |
|---|---|---|
| **Round-trip** | Doing then undoing (or encoding then decoding) gets you back where you started | Serializing a rule set to config and parsing it back gives the same rules |
| **Invariant** | Something that is true for every input | A command that matches a `deny` rule is never allowed |
| **Model / oracle** | Compare against a simpler implementation that is obviously correct | The matcher agrees with a slow, hand-written matcher on every command |
| **Metamorphic** | Changing the input in a known way changes the output in a predictable way | Adding an unrelated rule never changes the decision for a command it doesn't match |

Your properties must use **at least two different kinds**.

A property is only as good as the inputs it sees. Write generators (arbitraries) that actually reach the interesting cases for your feature, such as the boundaries your interviewees worried about, not just random strings. Briefly explain your generator choices in a comment.

!!! note "Using opencode"
    You may use opencode (or any AI tool) to help write properties and generators. If you do, note which properties it wrote or suggested in your traceability table. You are responsible for every property being correct and tied to a real requirement.

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
