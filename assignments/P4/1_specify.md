---
title: "4A Properties & Fixes"
nav_order: 10
---

# Project 4: Properties & Fixes

## Deliverables

**Properties & Fixes** – 65 points – due Thursday, November 5, 2026, 11:59PM

- [Step 1: Review Your Requirements (Individual) (10 pts)](#step-1-review-your-requirements-individual-10-pts)
- [Step 2: Write Properties for Your Requirements (Individual) (40 pts)](#step-2-write-properties-for-your-requirements-individual-40-pts)
- [Step 3: Run, Triage, and Fix (Individual) (15 pts)](#step-3-run-triage-and-fix-individual-15-pts)

The project has three steps, done in order:

1. **Review** your Project 3 requirements and decide which to keep as they are and which to change.
2. **Write** property-based tests for at least 4 of your requirements.
3. **Run** the tests against the code. When one fails, decide whether to fix the code or the test. Get all the tests to pass correctly, then open a PR and get them passing there too.

## Setup

### Your Branch

Each team member works on **their own branch** in the team repository for this project, named so it's clear who owns it (e.g. `<andrewid>/properties`). The PR will not need to be merged yet, and will be used for the following project as well. 

### Installing fast-check

Add fast-check as a dev dependency of the package that contains your target feature. For most students, that's `packages/opencode`:

```bash
cd packages/opencode
bun add -d fast-check
```

!!! tip "One teammate adds the dependency"
    If everyone on your team runs `bun add` on their own branch, every PR will conflict on `package.json` and `bun.lock`. Have **one** teammate add fast-check in a small PR, merge it, and have everyone pull that commit into their branch before starting.

Put your property tests next to the package's existing tests (e.g. `packages/opencode/test/<feature>/<feature>.property.test.ts`) and run them with `bun test` from inside the package. fast-check works with any test runner; you call `fc.assert(fc.property(...))` inside an ordinary `test(...)` block.

!!! warning "Make sure your tests run on your PR"
    opencode's `test` workflow runs on every pull request, but it only runs `bun test` for the packages listed in `turbo.json`. If your feature lives in a package that isn't listed, your tests will pass locally and **silently never run** on your PR. Read the "Unit tests" section of `TESTING.md` in the repository and add your package if needed.

### Your Traceability File

Copy your requirements table from Project 3 into your branch as `traceability/<andrewid>.md`, using the template below. You'll fill it in as you go through the three steps.

!!! note "About the examples"
    The examples on this page use a made-up feature, a **request rate limiter**, so that they don't match anyone's target. Don't copy them; your requirements and properties must come from your own feature and interviews.

??? example "Traceability file template (copy into `traceability/<andrewid>.md`)"
    ```markdown
    # Traceability: <your name> (<andrewid>)

    **Target feature:** <feature, and the main source files it lives in>

    ## Requirements

    | ID | Interview evidence | Requirement | Acceptance Criteria | Changed in P4? | Property (kind) | Test |
    |---|---|---|---|---|---|---|
    | R1 | | | | | | |

    Properties written or suggested by opencode or another AI tool: <list by requirement ID, or "none">

    ## Requirement changes

    | ID | Original requirement (P3) | Revised requirement | Why it changed |
    |---|---|---|---|
    ```

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

!!! note "Using opencode"
    You may use opencode (or any AI tool) to help write properties and generators. If you do, note which properties it wrote or suggested in your traceability table. You are responsible for every property being correct and tied to a real requirement.

## Step 3: Run, Triage, and Fix (Individual) (15 pts)

Run your properties against the code. If a property passes, good: the code meets that requirement for every input fast-check tried.

When a property fails, fast-check reports a **shrunk counterexample**, the smallest input it found that breaks the property. Use it to decide what's wrong, and fix it:

| Outcome | What it means | What you do |
|---|---|---|
| **Code bug** | The code violates the requirement | Fix the code |
| **Wrong test** | Your property doesn't say what the requirement means | Fix the property |
| **Requirement problem** | The failure shows the requirement itself isn't feasible, or conflicts with another one | Go back to Step 1: revise the requirement, record it in Requirement changes, then update the property |

Keep going until **every property passes**. That's when your requirements are implemented: each requirement you wrote a property for is checked automatically, and the code meets all of them.

If your properties all pass the first time you run them, that's fine: you're done with this step.

### Landing Your Work

Commit your properties, fixes, and traceability file to your branch, then open a pull request from your branch to `main` and ask at least one teammate to review it. **Don't merge it yet**: you'll keep working on this branch and PR in the next project.

By the deadline, the `test` check on your PR must **pass**, and its log must show your properties running (not just the existing tests). If a property passes locally but fails on the PR, treat it like any other failure and triage it.

## Submission

Submit to Gradescope:

- A link to your pull request
- A link to `traceability/<andrewid>.md` on your branch
- A link to the passing GitHub Actions `test` run on your PR in which your properties ran

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

- [ ] For any property that failed: a code fix for a code bug, a corrected property for a wrong test, or a recorded requirement change for a requirement problem
- [ ] An open PR from your own branch to `main`, reviewed by a teammate
- [ ] A passing `test` check on your PR whose log shows all of your properties running
