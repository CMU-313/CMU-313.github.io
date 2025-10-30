---
title: Recitation 9 - Property-Based Testing
---

# Recitation 9: Property-Based Testing

## Overview

After covering property-based testing in lecture, you will learn how to use [fast-check](https://fast-check.dev) and practice how to apply property-based testing to an actual codebase.

Specifically, you will continue to work with [PierogIO](https://github.com/CMU-313/PierogIO), the fictional pierogi delivery service for which you wrote example-based tests in lecture last week.
The codebase is riddled with issues!
You will work in your **project teams** to write effective property-based tests, find bugs, and fix them.
I.e., you will use property-based testing to go on a bug hunt.
A small prize will be awarded to the team that finds the most bugs (using property-based tests) at the start of lecture on Thursday.

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

## Submission

TODO: ask students to individually submit some artifact to Gradescope before the end of recitation.
It could be a very short quiz (e.g., what bugs did you find? what properties did you write?).
