---
title: Recitation 3 - Software Archaeology
---

# Recitation 3: Software Archaeology

## Overview

In today’s recitation, we will practice getting to know an unknown codebase specifically in the context of fixing bugs in an open-source software system. We will do this by exploring bugs in OpenRefine, a Java tool for loading, cleaning, and augmenting data. 

## Pre-requisites

You may optionally wish to peruse [these docs](https://docs.openrefine.org) to introduce yourself to how to use OpenRefine.

**Let's fix some bugs!**

Consider the following open bug:
[https://github.com/OpenRefine/OpenRefine/issues/5034](https://github.com/OpenRefine/OpenRefine/issues/5034)

## Task 0: Clone the repo

- Clone the repository at [https://github.com/OpenRefine/OpenRefine](https://github.com/OpenRefine/OpenRefine) 
- Run with `./refine` in the project directory

## Task 1: Reproduce the bug

- Look at the issue above and reproduce it manually as in the description

## Task 2: Diving into the code

Let’s learn more about this bug! Your high level goal is to identify the code that is implicated in the bug and learn more about the bug en route to fixing it. Note that we don’t expect you to actually fix it, it’s open for a reason, but we’d like you to learn about the code being executed and learn a little bit about what’s going on.

(It’s okay if you don’t get to all of these tasks.) 

Try some or all of the following tasks:

- Explore the tests directory
- Can you find a test that looks like it might test the same code you’ve been exploring in these bugs? (hint: the bug involves importing an Excel file)
- Use your IDE to jump to a definition implicated in the code you’re debugging 
- Find similar code to the code that’s involved in the error (hint: the code adds a column called File, and one of the cells involves the file source)
- Try making a change! It will reflect in the UI. Can you fix the bug?

If you’ve finished all that, practice playing around with [testing with Maven](https://mkyong.com/maven/how-to-run-unit-test-with-maven/):
- Write a test that fails due to the bug
- Change the code so that that your new test pass
- Change the code so that a different error is thrown
- Change your tests such that an error isn’t thrown 