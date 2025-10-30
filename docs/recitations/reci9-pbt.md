---
title: Recitation 9 - Property-Based Testing
---

# Recitation 9: Property-Based Testing

## Overview

In this recitation, you will use [fast-check](https://fast-check.dev) to write property-based tests for [PierogIO](https://github.com/CMU-313/PierogIO), the pierogi delivery service you tested in lecture last week.
The codebase is riddled with bugs!
Working in your **project teams**, you'll write property-based tests to find and fix as many bugs as possible.
A small prize will be awarded to the team that finds the most bugs at the start of Thursday's lecture.

## Setup

1.  **One person in your team** should go to the PierogIO repository and click the "Use this template" button in the top right corner before selecting the "Create repository" option, as shown below.

    ![Use the PierogIO repo as a template for your team's repository](/assets/images/reci/template-create-repo.png)

    That person should then choose to create a **private repository**, select "CMU-313" as the owner, and name it "pierogio-**your-team-name**" before hitting the "Create repository" button.

    ![Use the following settings (described above) to create your repo](/assets/images/reci/template-settings.png)

2.  After creating the repository, that person should **invite the rest of the team as collaborators.**
    To do so, go to the **Settings** page for your repository, then select **"Collaborators and teams"** from the menu on the left.
    You can then either click the **Add team** button and type in / select your team, or you can click **Add people** and manually add the rest of your team to the repository.

    ![Share the repository with the rest of your team](/assets/images/reci/repo-settings.png)

3.  Finally, everyone should be able to access the repository.
    You can then use Codespaces to open up the repository or you can clone it to your machine and install it as a DevContainer (CMD+SHIFT+P: "Rebuild and Reopen in Dev Container").
    You should now be able to interact with the codebase.

    ![Create a codespace](/assets/images/reci/create-codespace.png)

    !!! info "Codespaces is just an IDE in the Cloud"
        Be aware that any changes you make within the Codespace won't be saved to GitHub unless and until you push your changes.
        Similarly, you won't see any changes that your team members make until you pull those changes.

## Background: fast-check

To write property-based tests in fast-check, you need two things: (1) **a way to generate inputs** at random (known as an arbitrary), and (2) a predicate that **checks whether the property holds** on a given input.
To help get you started, we have provided starter test code in `./tests/properties/`.
Below is an example of a property-based test from `./tests/properties/order.properties.spec.js`:

```js
// we describe our property in natural language
it('total should always be non-negative integer', () => {

  // we call fc.assert to assert that a given property should be true for all generated inputs
  fc.assert(

    // we use fc.property to construct the property we want to test
    // fc.property takes n + 1 arguments
    fc.property(
        // the first n arguments specify the arbitraries that
        // should be used to construct inputs (n=2 in this case)
        orderArb, contextArb,

        // the last argument to fc.property is a predicate that takes n arguments
        // and returns true if the property is satisfied on that input
        // each argument corresponds to a concrete value that is generator by the i-th arbitrary
        (order, context) => {

            // we supply the generated inputs to the function that we want to test
            const result = total(order, context);

            // we check our property over the result
            // in this case, we don't find any bugs!
            // but we can verify that our property works by intentionally breaking the code
            // (temporarily) and having it negate the price before returning the value
            return result >= 0 && Number.isInteger(result);

        }
    ),

    // below, we provide extra optional arguments to `fc.assert`
    // numRuns specifies the number of attempts
    { numRuns: 50 }

  );

});
```

#### Generating Inputs via Arbitraries

[Arbitraries](https://fast-check.dev/docs/introduction/getting-started/#arbitrary) are responsible for generating random inputs to the function that you would like to test.
To help get you started, we have provided several arbitraries in `./tests/properties/arbitraries.js`, including `orderArb`, which will create random orders.
**TODO: do we want students to write a contextArb?**

#### Verifying Properties with Predicates


The predicate is a function that returns `true` if the property holds for the given inputs, and `false` otherwise.
In the example above, our predicate checks two things:

```js
(order, context) => {
    const result = total(order, context);
    return result >= 0 && Number.isInteger(result);
}
```

This predicate verifies that:

1. The total is non-negative (`result >= 0`)
2. The total is an integer (`Number.isInteger(result)`)

When writing predicates, think about what should **always** be true about your function's output, regardless of the input. Common properties include:

- **Range properties**: The output is within expected bounds (e.g., non-negative, less than a maximum)
- **Type properties**: The output has the expected type (e.g., integer, string, array)
- **Relationship properties**: The output relates to the input in a predictable way (e.g., output length equals input length)
- **Invariant properties**: Certain conditions never change (e.g., sorted arrays stay sorted after filtering)

If fast-check finds an input where your predicate returns `false`, it will report a test failure and show you the counterexample.

#### Running Tests

To run the property-based tests:

```bash
npm test -- tests/properties/
```

To run a specific test file:

```bash
npm test -- tests/properties/delivery.test.js
```

**TODO: add screenshot of running tests from inside IDE.**

## Activity: Bug Hunt Challenge

Your team's goal is to **find as many bugs as possible** using property-based testing.
For each bug you find:

1. Write a property-based test that fails due to the bug
2. Document the bug by adding a comment above the test explaining what property is violated
3. Fix the bug in the source code and push your changes to `main`
4. Verify that your test now passes

### Getting Started

Since you already wrote example-based tests for PierogIO during lecture, you're familiar with the codebase. Follow these steps to make the most of your recitation time:

1. **Set up your environment** (5 minutes): Clone your team's repository and run `npm test` to ensure everything works
2. **Pick a module** (2 minutes): Have each pair in your team claim a different module to focus on (e.g., delivery, tax, discounts, total)
3. **Write 2-3 properties** (35 minutes): Start with simple properties, then get more creative.
    Think about edge cases and invariants!
4. **Hunt for bugs** (20 minutes): Run your tests, find failures, fix bugs in the source code
5. **Share findings** (5 minutes): Gather as a team and share what bugs you found

!!! tip "Working as a Team"
    - **Pair up**: Work in pairs of 2 on different modules to cover more ground
    - **Rotate**: Consider switching pairs halfway through to share knowledge
    - **Share findings**: Use the last 5 minutes to discuss what each pair discovered
    - **Push often**: Commit and push your changes regularly so teammates can see your progress

## Submission

Before leaving recitation, **each student** should submit individually to Gradescope:

1. **A brief reflection** (3-5 sentences) answering:
    * What bugs did your team find?
    * What was the most interesting property you wrote?
    * What was challenging about property-based testing?

2. **Your team's repository URL**

**The team with the most bugs found wins a prize!** Winners will be announced at the start of Thursday's lecture.
