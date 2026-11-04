---
title: "5A Mutation Testing & Red Team"
nav_order: 10
---

# Project 5: Mutation Testing & Red Team

## Deliverables

**Mutation Testing & Red Team** – 100 points – due Thursday, November 12, 2026, 11:59PM

- [Hand-Written Mutants with Predictions (30 pts)](#hand-written-mutants-with-predictions-30-pts)
- [Stryker Run & Comparison (35 pts)](#stryker-run-comparison-35-pts)
- [Agent Failure Case (20 pts)](#agent-failure-case-20-pts)
- [Retrospective (15 pts)](#retrospective-15-pts)
- [Extra Credit: Cross-Team Red Team (up to 10 pts)](#extra-credit-cross-team-red-team-up-to-10-pts) – optional; mutants due to your target Monday, November 9, 11:59PM

All of your work for this project continues on **your own branch** from Project 4 (e.g. `<andrewid>/properties`), and you keep pushing to the **same pull request** you opened in Project 4. Bring your branch up to date with `main` before you start, and again once a teammate merges the Stryker dependency.

## Hand-Written Mutants with Predictions (30 pts)

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

## Stryker Run & Comparison (35 pts)

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

## Agent Failure Case (20 pts)

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

## Retrospective (15 pts)

This is the last project on opencode, so take stock of what you built and how you built it. Answer the questions below in the **Project 5: Retrospective** assignment on Gradescope (not in your traceability file). Each answer should be **2–4 sentences**.

Be specific: name the requirement (R#), interview note (e.g. `C-4`), mutant (e.g. H2), or project you mean. Answers that could have been written without doing the work won't get credit. You're graded on specificity and honesty, not on whether you liked opencode or whether things went well.

### Requirements, properties, and mutants (Projects 3–5)

1. Pick one requirement you revised or dropped in Project 4, Step 1. Quote its Project 3 wording and the interview note it came from. What did you learn while writing properties that the interview didn't tell you?
2. Which of your requirements was hardest to write as a property? Name it, and say what made it hard: vague wording, behavior that depends on state or timing, or no clear way to check the answer. Rewrite the requirement the way you'd write it now.
3. Which requirement had the most surviving mutants before you strengthened your properties? Was the weakness in the requirement itself, the generator, or the assertion? How do you know?
4. Did any mutant (hand-written, Stryker, or red-team) change behavior that none of your requirements covered? Describe it and write the requirement you would add. If none did, explain why you think your requirements covered everything the mutants touched.
5. Write one question you would add to your Project 3 interview script now, knowing what Projects 4 and 5 showed you. Which requirement would the answer have sharpened?

### Working with an AI agent (Projects 1–5)

6. Describe one specific time opencode saved you real time this semester. Name the project and the task. What did you check before trusting its output?
7. Apart from your agent failure case above, describe one time opencode's output was wrong or misleading and you didn't notice right away. How did you find out, and how long did it go unnoticed?
8. Based on your agent failure case, state one rule you would give a teammate for reviewing tests an agent wrote. Name a mutant from this project that the rule would have caught.
9. Name one task you would no longer hand to an agent, and one you would hand off sooner than you did at the start of the semester. Give a one-sentence reason for each.

## Extra Credit: Cross-Team Red Team (up to 10 pts)

This part is **optional**. Teams that opt in will be paired with another team that opted in, and each of you will be assigned one member of that team as your **target**. Do the required parts first: extra credit can't make up for missing them.

### Attack (5 pts) – due to your target Monday, November 9, 11:59PM

Study your target's declared feature, requirements, and properties. They're in your target's traceability file on their branch, which their Project 4 pull request links to. Their branch keeps changing during this project, so note the commit you studied and write your mutants against that commit so the patches still apply. Write **3 mutants** against their feature, each aiming to slip past their properties. Each mutant should:

- Target one of their stated requirements (name it)
- Be plausible: a bug a real developer might write, not an obviously broken line
- Come with a short explanation of which property you expect it to slip past, and why

Send your three patch files, your explanations, and the commit you wrote them against to your target by Monday at 11:59PM, through the channel your TA sets up for your pairing. Also commit them to your own branch at `mutants/<andrewid>/redteam/`.

Attack mutants are graded on **plausibility and how well they target a requirement**, not on whether they survive.

### Defend (5 pts)

Apply each mutant you receive and run your properties. For every mutant that survives, strengthen your properties until it is killed (or argue that it is equivalent). Record each received mutant, its result, and your fix in a **Red team** section of your traceability file, and credit who sent it.

## Landing Your Work

Push your strengthened properties, mutant patches, Stryker configuration and report, and updated traceability file to your branch, so they appear in the pull request you opened in Project 4. When you're done, at least one teammate must review and approve it, and it must be **merged into `main`** by the deadline, with all of your properties passing in CI.

## Submission

**Individually**, submit to Gradescope:

- A link to your pull request (the one from Project 4, now merged)
- A link to `traceability/<andrewid>.md` on `main`

Answer the retrospective questions in the separate **Project 5: Retrospective** assignment on Gradescope.

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

To receive full credit for the retrospective, we expect:

- [ ] An answer to every question, each 2–4 sentences
- [ ] Each answer names the specific requirement, interview note, mutant, or project it's about

To receive the red-team extra credit, we expect:

- [ ] Three plausible attack mutants, each targeting a named requirement of your target, delivered by Monday, November 9
- [ ] Every mutant you received recorded with its result, and every survivor either killed by strengthened properties or argued equivalent

To receive full credit overall, we expect:

- [ ] Your Project 4 PR, updated with this project's work, reviewed and approved by a teammate, and merged into `main` with all properties passing in CI
