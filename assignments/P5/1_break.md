---
title: "5A Mutation Testing & Red Team"
nav_order: 10
---

# Project 5: Mutation Testing & Red Team

## Deliverables

**Mutation Testing & Red Team** – 100 points – due Thursday, November 12, 2026, 11:59PM

- [Hand-Written Mutants with Predictions (18 pts)](#hand-written-mutants-with-predictions-18-pts)
- [Stryker Run & Comparison (18 pts)](#stryker-run-comparison-18-pts)
- [Agent Failure Case (12 pts)](#agent-failure-case-12-pts)
- [Cross-Team Red Team (26 pts)](#cross-team-red-team-26-pts) – mutants due to your partner Monday, November 9, 11:59PM
- [TA Check-in (Team) (26 pts)](#ta-check-in-team-26-pts)

All of your work for this project continues on **your own branch** from Project 4 (e.g. `<andrewid>/properties`), and you keep pushing to the **same pull request** you opened in Project 4. Bring your branch up to date with `main` before you start, and again once a teammate merges the Stryker dependency.

## Hand-Written Mutants with Predictions (18 pts)

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
| H1 | R1 | `rate-limit.ts`: window reset check changed from `>=` to `>`, so a request exactly at the reset time is still delayed | "No window exceeds the limit" (R1) | Survived: the generator never produced a request landing exactly on a window boundary |

As in Project 4, this example uses a made-up feature. Your mutants must target your own requirements.

Then add a **Mutants it kills** column to your main traceability table and fill it in for each requirement.

## Stryker Run & Comparison (18 pts)

### Running Stryker

[Stryker](https://stryker-mutator.io/) generates mutants automatically and runs your tests against each one. Install it in the package containing your feature:

```bash
cd packages/opencode
bun add -d @stryker-mutator/core
```

As with fast-check in Project 4, have **one** teammate add Stryker in a small PR so your branches don't conflict on `package.json` and `bun.lock`.

Each team member needs their own configuration, so name yours `stryker.<andrewid>.config.json` and put it in that package. Use the **command** test runner so Stryker runs `bun test`, and limit both the mutated files and the tests to your target feature. Mutating all of opencode would take hours. For example:

```json
{
  "testRunner": "command",
  "commandRunner": { "command": "bun test test/<feature>" },
  "mutate": ["src/<feature>/**/*.ts"],
  "coverageAnalysis": "off",
  "reporters": ["html", "clear-text", "progress"]
}
```

Run it with `bunx stryker run stryker.<andrewid>.config.json`.

!!! warning "Fix your fast-check seed"
    fast-check generates different inputs on every run, so a mutant can be killed in one run and survive the next. Before running Stryker, fix the seed for your property tests (for example, `fc.configureGlobal({ seed: 42 })` at the top of your test file, or `{ seed: 42 }` as the second argument to `fc.assert`). Record the seed in your Stryker comparison section.

Stryker writes its report to `reports/mutation/mutation.html` in the package, and every teammate's run writes to the same place. **Copy** your report to `mutants/<andrewid>/mutation.html` and commit that copy. Add `reports/` to the package's `.gitignore` so the shared output folder never ends up in a PR.

### Comparison

In a **Stryker comparison** section of your traceability file, report your mutation score and answer:

- Which of your hand-written mutants did Stryker **never** generate? Why not?
- Which Stryker survivors would you **never** have thought of? Are any of them bugs a real developer might plausibly write?
- What does each approach find that the other doesn't?

### Strengthening

Kill surviving mutants (hand-written and Stryker) by **improving your properties** where possible: better generators, stronger assertions, or a new property for a requirement you hadn't fully captured. Do not kill survivors by adding example-based tests.

Some mutants are **equivalent**: the change doesn't alter the program's behavior in any observable way, so no test can kill them. For each mutant you claim is equivalent, give a 2–3 sentence argument why. Report your final mutation score both as Stryker reports it and with equivalent mutants excluded.

## Agent Failure Case (12 pts)

AI agents are good at producing tests that *look* thorough. Find **one property written or suggested by opencode** that let a hand-written or Stryker mutant survive. Common reasons:

- A **weak oracle**: the property checks something that is true no matter what (e.g. "the result is a boolean")
- An **always-passing property**: the assertion restates the implementation, so it can't disagree with it
- A **generator that never reaches the bug**: inputs too narrow, too random, or missing the boundary

If none of your existing properties came from opencode, ask opencode now to write a property for one of your requirements, and run your mutants against it.

In an **Agent failure case** section of your traceability file, include:

- An excerpt of the opencode transcript where the property was written or suggested: paste the relevant prompt and response into the file (a screenshot is fine), and if you can, add a share link from opencode's `/share` command
- The mutant it let survive
- An explanation of why the property was too weak
- Your strengthened version, and evidence that it kills the mutant

## Cross-Team Red Team (26 pts)

Your TA will pair your team with a **partner team**, and assign each of you one member of that team as your **target**.

### Attack (13 pts) – due to your target Monday, November 9, 11:59PM

Study your target's declared feature, requirements, and properties. They're in your target's traceability file on their branch, which their Project 4 pull request links to. Their branch keeps changing during this project, so note the commit you studied and write your mutants against that commit so the patches still apply. Write **3 mutants** against their feature, each aiming to slip past their properties. Each mutant should:

- Target one of their stated requirements (name it)
- Be plausible: a bug a real developer might write, not an obviously broken line
- Come with a short explanation of which property you expect it to slip past, and why

Send your three patch files, your explanations, and the commit you wrote them against to your target by Monday at 11:59PM, through the channel your TA sets up for your pairing. Also commit them to your own branch at `mutants/<andrewid>/redteam/`.

Attack mutants are graded on **plausibility and how well they target a requirement**, not on whether they survive.

### Defend (13 pts)

Apply each mutant you receive and run your properties. For every mutant that survives, strengthen your properties until it is killed (or argue that it is equivalent). Record each received mutant, its result, and your fix in a **Red team** section of your traceability file, and credit who sent it.

## TA Check-in (Team) (26 pts)

Sign up for a **10-minute** check-in with your TA between November 9 and November 12 using the sign-up sheet that will be posted in Slack. Your **whole team** must attend.

During the check-in, your TA will plant a bug in one team member's feature. That is a live mutant. A team member chosen by the TA will:

1. Predict which of their properties, if any, will catch it, and why
2. Run the tests
3. Discuss the result with the TA: if the mutant survived, what would kill it?

You are graded on the **quality of your reasoning**, not on whether the mutant was killed. Every member should be ready to talk about their own feature and properties.

## Landing Your Work

Push your strengthened properties, mutant patches, Stryker configuration and report, and updated traceability file to your branch, so they appear in the pull request you opened in Project 4. When you're done, at least one teammate must review and approve it, and it must be **merged into `main`** by the deadline, with all of your properties passing in CI.

## Submission

**Individually**, submit to Gradescope:

- A link to your pull request (the one from Project 4, now merged)
- A link to `traceability/<andrewid>.md` on `main`

There is no separate submission for the TA check-in.

## Grading

To receive full credit for the hand-written mutants, we expect:

- [ ] About 5 plausible mutants, each targeting a named requirement, saved as patch files
- [ ] A prediction for each mutant, recorded before running it, and the actual result
- [ ] A **Mutants it kills** column added to your traceability table and filled in

To receive full credit for the Stryker run and comparison, we expect:

- [ ] A Stryker configuration (`stryker.<andrewid>.config.json`) scoped to your feature, a recorded seed, and a committed copy of the HTML report
- [ ] A comparison of hand-written and Stryker mutants that answers each question above
- [ ] Survivors killed by improved properties rather than example tests, with a short argument for each claimed equivalent mutant
- [ ] Your mutation score reported both raw and with equivalent mutants excluded

To receive full credit for the agent failure case, we expect:

- [ ] A transcript excerpt showing where opencode wrote or suggested the property
- [ ] The surviving mutant and a clear explanation of why the property was too weak
- [ ] A strengthened property with evidence that it kills the mutant

To receive full credit for the red team, we expect:

- [ ] Three plausible attack mutants, each targeting a named requirement of your target, delivered by Monday, November 9
- [ ] Every mutant you received recorded with its result, and every survivor either killed by strengthened properties or argued equivalent

To receive full credit for the TA check-in, we expect:

- [ ] All team members present
- [ ] A clear, well-reasoned prediction and discussion of the planted mutant

To receive full credit overall, we expect:

- [ ] Your Project 4 PR, updated with this project's work, reviewed and approved by a teammate, and merged into `main` with all properties passing in CI
