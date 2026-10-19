---
kind: recitation
title: Recitation 7 - Property Based Testing
date: 2026-10-19
reveal_date: 2026-10-16
---

# Recitation 7: Property-Based Testing

In lecture you designed Wordle properties on paper. Today you'll write them
in [fast-check](https://fast-check.dev), run them, and measure how good they
are.

- **Part 1 (TA-led, ~20 min):** `matchGuess` from lecture. Follow along in
  `test/wordle.test.ts`.
- **Part 2 (groups of 2–3, ~25 min):** a new function, `mergeIntervals`. Work
  in `test/intervals.test.ts`.
- **At home:** [the problem set](https://github.com/CMU-313/F26-reci-7/blob/main/PROBLEM_SET.md) finishes both.

After the recitation, remember to complete the [Gradescope assignment](https://www.gradescope.com/courses/1356702/assignments/8417897) to receive credit!

## Before recitation: setup (5 min)

For this activity, create a fork of [this repository](https://github.com/CMU-313/F26-reci-7/tree/main) and clone it to your local machine.

You need Node.js 20, 22, or 24+ (`node --version`).

```bash
git clone <your repo URL>
cd <repo>
npm install
npm test        # one intervals test fails. That's on purpose (Part 2)
```

## Commands

| Command | What it does |
|---|---|
| `npm run test:wordle` | Run your Wordle properties against the real `matchGuess` |
| `npm run test:intervals` | Run your interval properties against the real `mergeIntervals` |
| `npm run mutants:wordle` | Run your Wordle properties against the planted bugs |
| `npm run mutants:intervals` | Run your interval properties against the planted bugs |

## How you'll know your properties are any good

A property that passes tells you very little on its own. A property that
checks nothing passes too. So every function here comes with **mutants**:
copies of the code with a realistic bug planted in them. A good set of
properties

1. **passes** on the real implementation (no false alarms), and
2. **fails** on every mutant ("kills" it).

After every new property, run `test:` first, then `mutants:`.

The mutants runner runs everything 5 times with fresh random seeds. For each
mutant it says which property killed it and shows the counterexample:

```
  ✔ allBlack       killed  by: guessing the secret gives all greens
      Counterexample: ["AAAAA"]
      AssertionError: expected [ 'B', 'B', 'B', 'B', 'B' ] to deeply equal [ 'G', 'G', 'G', 'G', 'G' ]
```

A mutant killed in only some runs is **flaky**. That means your generator
only *sometimes* produces an input that exposes the bug, so improve the
generator.

Rules of the game:

- Import only from `../src/<subject>` (for example `../src/wordle`). The
  runner rejects tests that import the implementation file directly, because
  then the mutants could never be swapped in.
- Write properties from the **specification** (the doc comment at the top of
  each implementation file), not by reading `mutants.ts`. After the deadline
  you'll get more mutants to try your properties against.
- Label every property with its pattern, on the line above its `it(`:
  `// Pattern: invariant. The output is sorted.`

## Part 1: Wordle (follow along)

Your TA will live-code these. Type along in `test/wordle.test.ts`.

1. Build a generator for five-letter words.
2. Two invariants: the output has length 5, and every color is G/Y/B. Then
   run the mutants. How many does it kill?
3. A conditional property: guessing the secret gives all greens.
4. The "never credits a letter more often than the secret has it" invariant.
   Is the kill reliable? Your TA will explain why not.
5. Read a counterexample.

Finished early? One Wordle mutant still survives at the end of Part 1. Try
to kill it. (It's Task 1 of the problem set anyway.)

## Part 2: Merging intervals (groups of 2–3)

Read the specification at the top of `src/intervals/mergeIntervals.ts`
**carefully**. Several mutants are about one sentence of it.

`test/intervals.test.ts` has one property and a first-draft generator to
start from.

**Checkpoint 1: make the starter honest (~5 min).**
Run `npm run test:intervals`. The test fails *on the correct
implementation*. Read the counterexample: what's wrong, the property or the
generator? Fix it by **constructing** valid inputs, not by filtering
(`.filter` or `fc.pre`).

**Checkpoint 2: one property per pattern (~10 min).**
Use the toolbox from lecture. For each pattern, write one property in
English first, then in code:

| Pattern | Question to ask about `mergeIntervals` |
|---|---|
| Invariant | What must *always* be true of the output's shape? |
| Differential | Can you write a tiny, obviously correct check of "is point *p* covered?" and compare input with output? |
| Metamorphic | What change to the input should *not* change the output? |
| Algebraic | What happens if you merge something that's already merged? |
| Conditional | If the input intervals already don't overlap or touch, what should the output be? (Generate such inputs directly.) |

After each property, run `npm run test:intervals`, then
`npm run mutants:intervals`, and note which mutants it kills.

**Checkpoint 3: hunt the survivors (~8 min).**
For each surviving mutant, decide whether you are missing a **property**
(the bug is never checked) or a **generator** (the bug is checked, but the
inputs never reach it). For the second, ask: could your generator even
produce an input that triggers this bug, like two intervals sharing an
endpoint exactly? How often?

At the end of recitation, your TA will ask each group for its mutation score
and its hardest mutant.

## fast-check cheat sheet

```ts
import fc from 'fast-check';

// Running a property: check it with expect() inside the callback.
fc.assert(
  fc.property(arbA, arbB, (a, b) => {
    expect(f(a, b)).toEqual(/* ... */);
  }),
);

// Generators ("arbitraries")
fc.integer({ min: -20, max: 20 })
fc.nat(10)                                     // 0..10
fc.constantFrom('A', 'B', 'C')
fc.array(arb, { minLength: 1, maxLength: 5 })
fc.tuple(arbA, arbB)
fc.oneof(arbA, arbB)                           // sometimes one, sometimes the other
fc.shuffledSubarray(xs, { minLength: xs.length, maxLength: xs.length }) // a shuffle of xs

// Building new generators from old ones
arb.map(x => f(x))                             // transform each value
arb.chain(x => otherArbBuiltFrom(x))           // second value depends on the first
arb.filter(x => ok(x))                         // discards values; use sparingly
fc.pre(ok(x))                                  // same idea, inside the property
```

Docs: <https://fast-check.dev/docs/introduction/>