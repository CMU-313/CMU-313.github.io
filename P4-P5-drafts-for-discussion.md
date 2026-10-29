# P4 and P5 Drafts: For Team Discussion

*Drafted Oct 23, 2026. Neither project has been released; both drafts are in the course site repo under `assignments/P4` and `assignments/P5`.*

P3, P4 and P5 replace the old P3 (deployment/CI) and P4 (LLM integration). They form one thread on a single opencode feature that each student picks in P3: **interview users → turn requirements into property-based tests → attack those tests with mutants.** Each part is released only after the previous one is due, so students never see what's coming next.

| | P3: Elicit | P4: Specify and Fix | P5: Break and Fix |
|---|---|---|---|
| Status | **Live** | Draft | Draft |
| Release | Tue Oct 20 | Fri Oct 30 | Tue Nov 3 |
| Due | Thu Oct 29 | Mon Nov 2 | Mon Nov 9 (red-team mutants Thu Nov 5) |
| Points | 55 | 65 | 100 |
| Individual / team | Individual | Individual, plus a 10-pt team CI slice | Individual, plus a 26-pt team TA check-in |
| Main artifact | Google Doc workbook → PDF | `traceability/<andrewid>.md` + property tests, merged PR | Mutant patches, Stryker report, merged PR |

All three total **220 points**.

## How the parts connect

Each student keeps one traceability table that gains columns in each part:

| Interview evidence | Requirement | Acceptance criteria | Property (kind) | Test | Mutants it kills |
|---|---|---|---|---|---|
| P3 | P3 | P3 | P4 | P4 | P5 |

In P3 the table lives in the student's Google Doc workbook. In P4 they copy it into their team repo as `traceability/<andrewid>.md`, and it stays there for P5.

## Decisions we need to make

Most important first.

1. **P4 has only four days.** P3 is due Thu Oct 29 and P4 releases Fri Oct 30, so P4 runs Fri–Mon over a weekend. Writing properties, triaging failures, fixing code and getting a reviewed PR merged is a lot for that. Options:
    - Keep it as is.
    - Push P4's due date to Wed Nov 4, and shift P5 to Thu Nov 5 – Wed Nov 11.
    - Shrink P4's scope, for example 3 properties instead of 4, or dropping the merge requirement.
2. **Stryker hasn't been tested with opencode.** P5's Stryker section assumes Stryker's "command" runner can drive `bun test`. Nobody has run it yet, and all of P5 depends on it. Someone needs to try it on the permission feature before Nov 3. If it doesn't work, fall back to hand-written mutants only and move Stryker's 18 points elsewhere.
3. **Can students turn on branch protection?** P4's team CI slice asks students to protect `main` in their team repo. If students don't have admin rights on their CMU-313 team repos, they can't. Then either staff turn it on for every team, or we drop that requirement.
4. **Red-team logistics (P5).** We need to:
    - pair each team with a partner team, and assign every student a target on that team;
    - pick a channel for sending mutants (Slack DM? GitHub issue? Gradescope?);
    - accept that attack mutants are due Nov 5, two days after release.

    Is that too tight?
5. **TA check-in load (P5, 26 points).** Each team gets a 10-minute meeting between Nov 4 and Nov 9. For each meeting, the TA has to read one student's feature and write a plausible bug in it beforehand. That's real prep per team. Is 26 points the right weight for a 10-minute meeting?
6. **Where students learn this material.** The schedule has no lecture on property-based or mutation testing during P4/P5 (Oct 27 – Nov 10 are a workshop and guest lectures).
    - Recitation 7 (Oct 19) covered fast-check and briefly mentioned mutation score.
    - Recitation 9 (property-based testing with PierogIO) is **Nov 2, the day P4 is due**.

    Should Recitation 9 move earlier? Should we add a short mutation-testing primer before P5?
7. **Gradescope setup.** P3 has two assignments with full rubrics. Nothing exists yet for P4 or P5. Both drafts currently collect links: the merged PR and the traceability file. Do we want rubrics built before release, as we did for P3?

## Smaller questions

- **No failing properties (P4).** If none of a student's properties fail, the draft says that's fine as long as they show their generators actually exercise the feature. Is that enough for 25 points of "triage and fixes"?
- **"At least two kinds" of property (P4).** Is that the right minimum, or should we require three?
- **Per-item deductions.** In the P3 rubric, items like "−1 per untestable requirement" are applied once, with extras added as a point adjustment. Is that OK for P4/P5 too?
- **Agent failure case (P5, 12 points).** Students who never used opencode for properties are told to ask it for one now. Is that acceptable, or does it defeat the point?
- **Equivalent mutants (P5).** Students give a 2–3 sentence argument and report the score both raw and with equivalent mutants excluded. Which score do we grade on?
- **Students who switched targets.** If a student's P3 target isn't the feature they built in P2, their P4/P5 work is in a part of opencode their team didn't build. Any problem with that, for example merge conflicts or review burden on teammates?
- **Example feature.** Every worked example uses the permission-rules feature. Do we want a second example from a different feature, so students don't over-index on it?

---

The full current drafts follow. They are copied from the site source. Admonition boxes are shown as quotes, and some formatting may differ from the live site.

# Appendix A: Project 4 draft

## Project 4: Specify and Fix

### Learning Goals

- Translate natural-language requirements into executable property-based tests
- Recognize and apply common kinds of properties: round-trip, invariant, model/oracle, and metamorphic
- Write generators that explore a feature's input space
- Triage a failing test: decide whether the code, the test, or the requirements are wrong
- Gate merges on automated checks with continuous integration and branch protection

### Project Context

In Project 3, you interviewed users and turned what you heard into precise requirements for one opencode feature. Your manager is pleased, but a requirements table only helps if someone checks it. Requirements that live in a document drift away from the code the moment the next pull request lands.

Your manager now wants each requirement to become something the build checks automatically, on every change. Example-based unit tests only check the handful of inputs you thought of. Instead, you'll write **property-based tests** with [fast-check](https://fast-check.dev): each test states a rule that should hold for *every* input, and fast-check generates hundreds of inputs looking for one that breaks it.

When a property fails, the work begins: is the code wrong, is your property wrong, or did two of your interviewees actually want incompatible things? You'll decide, fix what needs fixing, and land the result through your team's pipeline.

### Deliverables and Deadlines

The properties, triage, and fixes are **individual**: you continue with the same target feature and requirements you declared in Project 3. The CI slice is a **team** deliverable.

There is one (1) deadline for this project. This project is worth a total of 65 points.

**Properties & Fixes** – 65 points – due Monday, November 2, 2026, 11:59PM

- Properties Tied to Requirements (Individual) (30 pts)
- Failure Triage & Fixes (Individual) (25 pts)
- CI Slice (Team) (10 pts)

> **Resources:** [Recitation 7](https://cmu-313.github.io/recitations/reci7-pbt/) introduced fast-check and the kinds of properties you'll use here. Its [problem set](https://github.com/CMU-313/F26-reci-7/blob/main/PROBLEM_SET.md) is a good warm-up if you haven't finished it.

## Project 4: Properties & Fixes

### Deliverables

**Properties & Fixes** – 65 points – due Monday, November 2, 2026, 11:59PM

- Properties Tied to Requirements (Individual) (30 pts)
- Failure Triage & Fixes (Individual) (25 pts)
- CI Slice (Team) (10 pts)

### Setup

#### Your Branch

Each team member works on **their own branch** in the team repository for this project, named so it's clear who owns it (e.g. `<andrewid>/properties`). Keep using this branch after this project; don't delete it once your PR merges.

#### Installing fast-check

Add fast-check as a dev dependency of the package that contains your target feature. For most students, that's `packages/opencode`:

```bash
cd packages/opencode
bun add -d fast-check
```

Put your property tests next to the package's existing tests (e.g. `packages/opencode/test/permission/permission.property.test.ts`) and run them with `bun test` from inside the package. fast-check works with any test runner; you call `fc.assert(fc.property(...))` inside an ordinary `test(...)` block.

> **Make sure your tests run in CI:** opencode's CI only runs `bun test` for the packages listed in `turbo.json`. If your feature lives in a package that isn't listed, your tests will pass locally and **silently never run** in CI. Read the "Unit tests" section of `TESTING.md` in the repository and add your package if needed.

#### Your Traceability Table

Copy your requirements table from Project 3 into your branch as `traceability/<andrewid>.md`, and add two columns:

| ID | Interview evidence | Requirement | Acceptance Criteria | Property (kind) | Test |
|---|---|---|---|---|---|
| R1 | `C-12`, `S-4`: "I'd be furious if it ran `rm -rf` after I said deny" | When a command matches several rules, the last matching rule in the config decides the outcome. | With rules `{"*": "allow", "rm *": "deny"}`, `rm -rf /` evaluates to `deny` and `ls -la` evaluates to `allow`. | Last match decides (model/oracle) | `permission.property.test.ts` |

Your acceptance criteria are a starting point for each property: a property should check the criteria for every generated input, not just the one example you wrote down. You may revise a requirement or its acceptance criteria if writing its property shows it was ambiguous, but keep the interview evidence and note what changed.

### Properties Tied to Requirements (Individual) (30 pts)

Write **at least 4** fast-check properties for your target feature. Each property must:

- Be tied to a specific requirement from your table (the Test column links to it, and the test's name or a comment cites the requirement ID)
- Be labeled with its kind:

| Kind | The idea | Example for permission rules |
|---|---|---|
| **Round-trip** | Doing then undoing (or encoding then decoding) gets you back where you started | Serializing a rule set to config and parsing it back gives the same rules |
| **Invariant** | Something that is true for every input | If the last rule matching a command is `deny`, the command is never allowed |
| **Model / oracle** | Compare against a simpler implementation that is obviously correct | The matcher agrees with a slow, hand-written matcher on every command |
| **Metamorphic** | Changing the input in a known way changes the output in a predictable way | Adding an unrelated rule never changes the decision for a command it doesn't match |

Your properties must use **at least two different kinds**.

A property is only as good as the inputs it sees. Write generators (arbitraries) that actually reach the interesting cases for your feature, such as the boundaries your interviewees worried about, not just random strings. Briefly explain your generator choices in a comment.

> **Using opencode:** You may use opencode (or any AI tool) to help write properties and generators. If you do, note which properties it wrote or suggested in your traceability table. You are responsible for every property being correct and tied to a real requirement.

### Failure Triage & Fixes (Individual) (25 pts)

Run your properties. For **every** property that fails, decide which of these it is, and act:

| Outcome | What it means | What you do |
|---|---|---|
| **Real bug** | The code violates a requirement users actually have | Fix the code |
| **Wrong property** | Your property doesn't say what the requirement means (or the requirement was stated imprecisely) | Fix the property (and the requirement, if needed) |
| **Requirements conflict** | Two interviewees wanted incompatible things | Decide which behavior wins, document the call and why, and update the requirement |

Add a **Triage log** section to your traceability file with one entry per failure: the property, the shrunk counterexample fast-check reported, which outcome you chose, why, and a link to the commit that fixed it.

If none of your properties fail, that's fine. Say so in your triage log, and describe how you checked that your properties are actually exercising the feature (for example, the range of inputs your generators produce).

#### Landing Your Work

Open a pull request from your branch to `main` containing your properties, fixes, and traceability file. At least one teammate must review and approve it before it merges. Your PR must be **merged into `main`** by the deadline.

### CI Slice (Team) (10 pts)

As a team, make sure your properties are enforced on every change:

- **Properties run on every PR.** opencode's existing `test` workflow runs on pull requests; confirm that every teammate's properties actually run in it (see the warning in Setup). If your team prefers, you may add a separate workflow just for properties.
- **`main` is branch-protected.** In your team repository's settings, add a branch protection rule (or ruleset) for `main` that requires a pull request before merging, at least one approving review, and the test check to pass.

### Submission

**Individually**, submit to Gradescope:

- A link to your merged pull request
- A link to `traceability/<andrewid>.md` on `main`

**As a team**, one member submits to Gradescope:

- A link to a GitHub Actions run on a pull request in which your team's properties ran
- A screenshot of your branch protection settings for `main`

### Grading

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

---

# Appendix B: Project 5 draft

## Project 5: Break and Fix

### Learning Goals

- Evaluate the strength of a test suite with mutation testing
- Design plausible faults that target specific requirements, and predict which tests should catch them
- Compare hand-written mutants with automatically generated ones, and understand the strengths of each
- Strengthen properties to kill surviving mutants, and argue when a mutant is equivalent
- Critically evaluate tests written or suggested by an AI agent
- Attack and defend tests across teams

### Project Context

In Project 4, you turned your requirements into properties that run on every pull request, and they pass. Your manager's next question is a fair one: *would they fail if the code were wrong?* A test suite that passes no matter what the code does is worse than no test suite, because it gives you false confidence.

**Mutation testing** answers that question directly. A *mutant* is a copy of your code with one small, deliberate bug in it: a `<` flipped to `<=`, a condition negated, a line deleted. If your tests fail on the mutant, they *kill* it. If they still pass, the mutant *survives*, and you've found a bug your tests can't see.

In this project, you'll attack your own properties: first with mutants you design by hand to break specific requirements, then with [Stryker](https://stryker-mutator.io/), which generates mutants automatically. You'll strengthen your properties until they kill what they should, examine one property that opencode helped write, and then trade attacks with a partner team.

### Deliverables and Deadlines

Most of this project is **individual**: you continue with the same target feature, branch, and traceability table from Projects 3 and 4. The TA check-in is a **team** meeting.

There are two (2) deadlines for this project. This project is worth a total of 100 points.

**Mutation Testing & Red Team** – 100 points – due Monday, November 9, 2026, 11:59PM

- Hand-Written Mutants with Predictions (18 pts)
- Stryker Run & Comparison (18 pts)
- Agent Failure Case (12 pts)
- Cross-Team Red Team (26 pts) – **red-team mutants due to your partner Thursday, November 5, 2026, 11:59PM**
- TA Check-in (Team) (26 pts) – held between November 4 and November 9

> **Tip:** The red-team mutants are due early so your partner has time to defend. Get your own mutants and Stryker run done early in the week, so you have time to respond to the mutants your partner sends you.

## Project 5: Mutation Testing & Red Team

### Deliverables

**Mutation Testing & Red Team** – 100 points – due Monday, November 9, 2026, 11:59PM

- Hand-Written Mutants with Predictions (18 pts)
- Stryker Run & Comparison (18 pts)
- Agent Failure Case (12 pts)
- Cross-Team Red Team (26 pts) – mutants due to your partner Thursday, November 5, 11:59PM
- TA Check-in (Team) (26 pts)

All of your work for this project continues on **your own branch** from Project 4 (e.g. `<andrewid>/properties`). Bring it up to date with `main` before you start.

### Hand-Written Mutants with Predictions (18 pts)

Before running any tool, design about **5 mutants** by hand. Each one should be designed to break a **specific requirement** in your traceability table while still looking plausible, the kind of bug that could survive a code review. For example:

- An off-by-one at a boundary
- An undo that restores everything except one field
- An error that is silently swallowed instead of reported
- A rule-matching loop that stops one rule too early

For each mutant, **before you run it**, predict which property (if any) should kill it, and why.

Save each mutant as a patch file in your branch at `mutants/<andrewid>/H1.patch`, `H2.patch`, and so on. One way to make one: edit the source, run `git diff > mutants/<andrewid>/H1.patch`, then `git checkout -- <file>` to undo the edit. To run a mutant later, `git apply` the patch, run your tests, and revert.

Record your results in a **Hand-written mutants** section of your traceability file:

| ID | Requirement targeted | Change | Predicted killer | Actual result |
|---|---|---|---|---|
| H1 | R1 | `permission/index.ts`: `findLast` changed to `find`, so the first matching rule wins instead of the last | "Last match decides" (R1) | Survived: the generator never produced two rules matching the same command |

Then fill in the **Mutants it kills** column of your main traceability table.

### Stryker Run & Comparison (18 pts)

#### Running Stryker

[Stryker](https://stryker-mutator.io/) generates mutants automatically and runs your tests against each one. Install it in the package containing your feature:

```bash
cd packages/opencode
bun add -d @stryker-mutator/core
```

Create a `stryker.config.json` in that package. Use the **command** test runner so Stryker runs `bun test`, and limit both the mutated files and the tests to your target feature. Mutating all of opencode would take hours. For example:

```json
{
  "testRunner": "command",
  "commandRunner": { "command": "bun test test/permission" },
  "mutate": ["src/permission/**/*.ts", "src/util/wildcard.ts"],
  "coverageAnalysis": "off",
  "reporters": ["html", "clear-text", "progress"]
}
```

Run it with `bunx stryker run`, and commit the HTML report (`reports/mutation/mutation.html`) to `mutants/<andrewid>/`.

#### Comparison

In a **Stryker comparison** section of your traceability file, report your mutation score and answer:

- Which of your hand-written mutants did Stryker **never** generate? Why not?
- Which Stryker survivors would you **never** have thought of? Are any of them bugs a real developer might plausibly write?
- What does each approach find that the other doesn't?

#### Strengthening

Kill surviving mutants (hand-written and Stryker) by **improving your properties** where possible: better generators, stronger assertions, or a new property for a requirement you hadn't fully captured. Do not kill survivors by adding example-based tests.

Some mutants are **equivalent**: the change doesn't alter the program's behavior in any observable way, so no test can kill them. For each mutant you claim is equivalent, give a 2–3 sentence argument why. Report your final mutation score both as Stryker reports it and with equivalent mutants excluded.

### Agent Failure Case (12 pts)

AI agents are good at producing tests that *look* thorough. Find **one property written or suggested by opencode** that let a hand-written or Stryker mutant survive. Common reasons:

- A **weak oracle**: the property checks something that is true no matter what (e.g. "the result is a boolean")
- An **always-passing property**: the assertion restates the implementation, so it can't disagree with it
- A **generator that never reaches the bug**: inputs too narrow, too random, or missing the boundary

If none of your existing properties came from opencode, ask opencode now to write a property for one of your requirements, and run your mutants against it.

In an **Agent failure case** section of your traceability file, include:

- An excerpt of the opencode transcript where the property was written or suggested
- The mutant it let survive
- An explanation of why the property was too weak
- Your strengthened version, and evidence that it kills the mutant

### Cross-Team Red Team (26 pts)

Your TA will pair your team with a **partner team**, and assign each of you one member of that team as your **target**.

#### Attack (13 pts) – due to your target Thursday, November 5, 11:59PM

Study your target's declared feature, requirements, and properties (they're in their traceability file on `main`). Write **3 mutants** against their feature, each aiming to slip past their properties. Each mutant should:

- Target one of their stated requirements (name it)
- Be plausible: a bug a real developer might write, not an obviously broken line
- Come with a short explanation of which property you expect it to slip past, and why

Send your three patch files and explanations to your target by Thursday at 11:59PM, through the channel your TA sets up for your pairing. Also commit them to your own branch at `mutants/<andrewid>/redteam/`.

Attack mutants are graded on **plausibility and how well they target a requirement**, not on whether they survive.

#### Defend (13 pts)

Apply each mutant you receive and run your properties. For every mutant that survives, strengthen your properties until it is killed (or argue that it is equivalent). Record each received mutant, its result, and your fix in a **Red team** section of your traceability file, and credit who sent it.

### TA Check-in (Team) (26 pts)

Sign up for a **10-minute** check-in with your TA between November 4 and November 9 using the sign-up sheet that will be posted in Slack. Your **whole team** must attend.

During the check-in, your TA will plant a bug in one team member's feature. That is a live mutant. A team member chosen by the TA will:

1. Predict which of their properties, if any, will catch it, and why
2. Run the tests
3. Discuss the result with the TA: if the mutant survived, what would kill it?

You are graded on the **quality of your reasoning**, not on whether the mutant was killed. Every member should be ready to talk about their own feature and properties.

### Landing Your Work

Open a pull request from your branch to `main` containing your strengthened properties, mutant patches, Stryker configuration and report, and updated traceability file. At least one teammate must review and approve it, and it must be **merged into `main`** by the deadline.

### Submission

**Individually**, submit to Gradescope:

- A link to your merged pull request
- A link to `traceability/<andrewid>.md` on `main`

There is no separate submission for the TA check-in.

### Grading

To receive full credit for the hand-written mutants, we expect:

- [ ] About 5 plausible mutants, each targeting a named requirement, saved as patch files
- [ ] A prediction for each mutant, recorded before running it, and the actual result
- [ ] An updated **Mutants it kills** column in your traceability table

To receive full credit for the Stryker run and comparison, we expect:

- [ ] A Stryker configuration scoped to your feature, and a committed HTML report
- [ ] A comparison of hand-written and Stryker mutants that answers each question above
- [ ] Survivors killed by improved properties rather than example tests, with a short argument for each claimed equivalent mutant
- [ ] Your mutation score reported both raw and with equivalent mutants excluded

To receive full credit for the agent failure case, we expect:

- [ ] A transcript excerpt showing where opencode wrote or suggested the property
- [ ] The surviving mutant and a clear explanation of why the property was too weak
- [ ] A strengthened property with evidence that it kills the mutant

To receive full credit for the red team, we expect:

- [ ] Three plausible attack mutants, each targeting a named requirement of your target, delivered by Thursday, November 5
- [ ] Every mutant you received recorded with its result, and every survivor either killed by strengthened properties or argued equivalent

To receive full credit for the TA check-in, we expect:

- [ ] All team members present
- [ ] A clear, well-reasoned prediction and discussion of the planted mutant

To receive full credit overall, we expect:

- [ ] A PR from your own branch, reviewed and approved by a teammate, and merged into `main`
