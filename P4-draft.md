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

- Judge whether a requirement is feasible to implement, and revise it without losing what users actually asked for
- Translate natural-language requirements into executable property-based tests
- Recognize and apply common kinds of properties: round-trip, invariant, model/oracle, and metamorphic
- Write generators that explore a feature's input space
- Triage a failing test: decide whether the code or the test is wrong
- Run tests automatically on every pull request with continuous integration

## Project Context

In Project 3, you interviewed users and turned what you heard into precise requirements for one opencode feature. Your manager is pleased, but a requirements table only helps if someone checks it. Requirements that live in a document drift away from the code the moment the next pull request lands.

Your manager now wants the build to check your requirements automatically, on every change, starting with at least four of them. Before that, though, you need to look at your requirements with an engineer's eye: some of what users want can't actually be built as stated, and needs to become something that can. Then you'll write **property-based tests** with [fast-check](https://fast-check.dev): each test states a rule that should hold for *every* input, and fast-check generates hundreds of inputs looking for one that breaks it.

When a property fails, you decide whether the code or the test is wrong, fix it, and keep going until every property passes. Then you open a pull request and let your team's CI check it.

## Deliverables and Deadlines

The requirements review, properties, and fixes are **individual**: you continue with the same target feature and requirements you declared in Project 3. The CI slice is a **team** deliverable.

There is one (1) deadline for this project. This project is worth a total of 65 points.

[**Properties & Fixes**](1_specify.md) – 65 points – due Thursday, November 5, 2026, 11:59PM

- Step 1: Review Your Requirements (Individual) (10 pts)
- Step 2: Write Properties for Your Requirements (Individual) (40 pts)
- Step 3: Run, Triage, and Fix (Individual) (10 pts)
- CI Slice (Team) (5 pts)

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

- [Step 1: Review Your Requirements (Individual) (10 pts)](#step-1-review-your-requirements-individual-10-pts)
- [Step 2: Write Properties for Your Requirements (Individual) (40 pts)](#step-2-write-properties-for-your-requirements-individual-40-pts)
- [Step 3: Run, Triage, and Fix (Individual) (10 pts)](#step-3-run-triage-and-fix-individual-10-pts)
- [CI Slice (Team) (5 pts)](#ci-slice-team-5-pts)

The project has three steps, done in order:

1. **Review** your Project 3 requirements and decide which to keep as they are and which to change.
2. **Write** property-based tests for at least 4 of your requirements.
3. **Run** the tests against the code. When one fails, decide whether to fix the code or the test. Get all the tests to pass correctly.

## Setup

### Your Branch

Each team member works on **their own branch** in the team repository for this project, named so it's clear who owns it (e.g. `<andrewid>/properties`). The PR will not need to be merged yet, and will be used for the following project as well. 

### Installing fast-check

Add fast-check as a dev dependency of the package that contains your target feature. For most students, that's `packages/opencode`:

```bash
cd packages/opencode
bun add -d fast-check
```

<!-- !!! tip "One teammate adds the dependency" -->
> **Tip: One teammate adds the dependency**
>
> If everyone on your team runs `bun add` on their own branch, every PR will conflict on `package.json` and `bun.lock`. Have **one** teammate add fast-check in a small PR, merge it, and have everyone pull that commit into their branch before starting.

Put your property tests next to the package's existing tests (e.g. `packages/opencode/test/<feature>/<feature>.property.test.ts`) and run them with `bun test` from inside the package. fast-check works with any test runner; you call `fc.assert(fc.property(...))` inside an ordinary `test(...)` block.

<!-- !!! warning "Make sure your tests run in CI" -->
> **Warning: Make sure your tests run in CI**
>
> opencode's CI only runs `bun test` for the packages listed in `turbo.json`. If your feature lives in a package that isn't listed, your tests will pass locally and **silently never run** in CI. Read the "Unit tests" section of `TESTING.md` in the repository and add your package if needed.

### Your Traceability File

Copy your requirements table from Project 3 into your branch as `traceability/<andrewid>.md`, using the template below. You'll fill it in as you go through the three steps.

<!-- !!! note "About the examples" -->
> **Note: About the examples**
>
> The examples on this page use a made-up feature, a **request rate limiter**, so that they don't match anyone's target. Don't copy them; your requirements and properties must come from your own feature and interviews.

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
> | ID | Interview evidence | Requirement | Acceptance Criteria | Changed in P4? | Property (kind) | Test |
> |---|---|---|---|---|---|---|
> | R1 | | | | | | |
>
> Properties written or suggested by opencode or another AI tool: <list by requirement ID, or "none">
>
> ## Requirement changes
>
> | ID | Original requirement (P3) | Revised requirement | Why it changed |
> |---|---|---|---|
> ```

## Step 1: Review Your Requirements (Individual) (10 pts)

Start with the requirements you wrote in Project 3. Before you test anything, go through them one at a time and decide whether to **implement it as is** or **change it**.

A requirement can accurately describe what users want and still not be something you can build. Look for requirements that:

- **Aren't feasible.** The system can't do it, or can't do it without unreasonable cost. Users may want something the platform, an upstream service, or the laws of physics won't allow.
- **Conflict with each other.** Two interviewees wanted incompatible things, and both made it into your table.
- **Can't be checked.** The requirement is too vague to tell whether the code meets it ("should feel fast", "should be easy").

When you change a requirement, keep what the user actually needed and change the part that can't be built. For example, in a rate limiter:

| | Requirement |
|---|---|
| **Original (P3)** | A user's requests are never delayed. |
| **Why it can't be built as is** | The upstream API enforces its own limit. Once you're over it, some delay is unavoidable. |
| **What the user actually needed** | Interviewees were frustrated by *unexplained* waits and by requests that silently failed. |
| **Revised (P4)** | When a request is over the limit, it is delayed no longer than the time left in the current window, never rejected, and the user is shown how long the wait will be. |

For every requirement you change, add a row to the **Requirement changes** section of your traceability file with the original wording, the revised wording, and why it changed. Mark the requirement as changed in the **Changed in P4?** column of the main table. Keep the original interview evidence: the revised requirement should still trace back to what you heard.

If every requirement can be built as written, that's fine. Write one or two sentences in the Requirement changes section explaining why you kept them all.

## Step 2: Write Properties for Your Requirements (Individual) (40 pts)

Write fast-check properties for **at least 4** of the requirements in your table. Each property must:

- Check the requirement's acceptance criteria for every generated input, not just the one example you wrote down in Project 3
- Have a **comment that names the requirement it checks**, by ID and wording
- Be listed in the Property and Test columns of your traceability table
- Be labeled with its kind:

| Kind | The idea | Example for a rate limiter |
|---|---|---|
| **Round-trip** | Doing then undoing (or encoding then decoding) gets you back where you started | Saving the limiter's state and loading it back gives a limiter that makes the same decisions |
| **Invariant** | Something that is true for every input | For any sequence of requests, no window ever contains more than the limit |
| **Model / oracle** | Compare against a simpler implementation that is obviously correct | The limiter agrees with a slow version that keeps a full list of timestamps |
| **Metamorphic** | Changing the input in a known way changes the output in a predictable way | Raising the limit never causes a request that was allowed to be delayed |

Your properties must use **at least two different kinds**.

For example:

```ts
// R1: When a request is over the limit, it is delayed no longer than the time
// left in the current window, and never rejected.
// Kind: invariant
test("R1: over-limit requests are delayed, never rejected", () => {
  fc.assert(
    fc.property(requestSequence, (requests) => {
      // ...
    }),
  )
})
```

A property is only as good as the inputs it sees. Write generators (arbitraries) that actually reach the interesting cases for your feature, such as the boundaries your interviewees worried about, not just random strings. Briefly explain your generator choices in a comment.

<!-- !!! note "Using opencode" -->
> **Note: Using opencode**
>
> You may use opencode (or any AI tool) to help write properties and generators. If you do, note which properties it wrote or suggested in your traceability table. You are responsible for every property being correct and tied to a real requirement.

## Step 3: Run, Triage, and Fix (Individual) (10 pts)

Run your properties against the code. If a property passes, good: the code meets that requirement for every input fast-check tried.

When a property fails, fast-check reports a **shrunk counterexample**, the smallest input it found that breaks the property. Use it to decide what's wrong, and fix it:

| Outcome | What it means | What you do |
|---|---|---|
| **Code bug** | The code violates the requirement | Fix the code |
| **Wrong test** | Your property doesn't say what the requirement means | Fix the property |
| **Requirement problem** | The failure shows the requirement itself isn't feasible, or conflicts with another one | Go back to Step 1: revise the requirement, record it in Requirement changes, then update the property |

Keep going until **every property passes**. That's when your requirements are implemented: each requirement you wrote a property for is checked automatically, and the code meets all of them.

If your properties all pass the first time you run them, that's fine. Say so in your traceability file, and describe how you checked that your properties actually exercise the feature (for example, the range of inputs your generators produce, or temporarily breaking the code and watching a property fail).

### Landing Your Work

Open a pull request from your branch to `main` containing your properties, fixes, and traceability file, and ask at least one teammate to review it. **Don't merge it yet**: you'll keep working on this branch and PR in the next project. By the deadline, all of your properties must pass in CI on the PR.

## CI Slice (Team) (5 pts)

As a team, make sure your properties are enforced on every change:

- **Properties run on every PR.** opencode's existing `test` workflow runs on pull requests; confirm that every teammate's properties actually run in it (see the warning in [Setup](#installing-fast-check)). If your team prefers, you may add a separate workflow just for properties.  You should either run all the properties, or pick a select set to run if they are taking too long for CI. If you do this, include a justification for which properties you are checking as a comment in the workflow file.

## Submission

**Individually**, submit to Gradescope:

- A link to your pull request
- A link to `traceability/<andrewid>.md` on your branch

**As a team**, one member submits to Gradescope:

- A link to a GitHub Actions run on a pull request in which your team's properties ran

## Grading

To receive full credit for reviewing your requirements, we expect:

- [ ] Every Project 3 requirement either kept or revised, with the Changed in P4? column filled in
- [ ] For each revised requirement, the original wording, the revised wording, and a reason grounded in feasibility, a conflict, or checkability
- [ ] Revised requirements that still trace back to the interview evidence

To receive full credit for the properties, we expect:

- [ ] Fast-check properties for at least 4 requirements in your traceability table, using at least two different kinds
- [ ] A comment on each property naming the requirement it checks, and its kind
- [ ] Generators that reach meaningful inputs for the feature, with a brief explanation
- [ ] A traceability table that links each property to its requirement and its test

To receive full credit for running, triaging, and fixing, we expect:

- [ ] Code fixes for code bugs, corrected properties for wrong tests, and a recorded requirement change for each requirement problem
- [ ] All of your properties passing in CI on your PR
- [ ] An open PR from your own branch to `main`, reviewed by a teammate

To receive full credit for the CI slice, we expect:

- [ ] Every teammate's properties running in CI on pull requests: all of them, or a selected set with a justification in the workflow file
