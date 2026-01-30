---
title: Recitation 3 - Software Archaeology
---

# Recitation 3: Software Archaeology

## Overview

In today’s recitation, we will practice implementing a new feature for the NodeBB codebase.


**Let's implement a new feature!**

Check out [this issue](https://github.com/CMU-313/NodeBB-S26-R3/issues/1) of the feature request. The user wants NodeBB to suggest a new username if an existing username is taken. (Don't worry about searching through all the users currently registered to suggest a new name, just make it suggest the current name the user wanted but with a suffix attached to it. Querying the backend server again is harder and is part of the optional task.)

## Task 0: Clone the repo

- Fork [this repository](https://github.com/CMU-313/NodeBB-S26-R3) and clone it. Follow the README to install the necessary modules and run NodeBB.

## Task 1: Reproduce the existing behaviour

- After you've successfully ran the program, go through it to reproduce the current behaviour.

## Task 2: Diving into the code and implement the new behaviour

Let’s learn more about the current implementation! Your high-level goal is to identify the code that implements current implementation and extends it to add the new feature. We’d like you to dive into the codebase and “excavate” the code.

Try some or all of the following tasks:

- Explore the NodeBB directory
- Understand how current features are implemented.
- Can you identify whether to modify the front-end or back-end code of the program?
    - Frontend code is located in `public` directory
    - Backend code is located in `src` directory
- Can you identify the keywords that you would like to search in the repository?
    - Maybe try searching for part of the error message that is currently showing.
- Use your IDE to jump to a definition implicated in the code you’re debugging

!!! warning
    Since error message involves [i18n and l10n](https://en.wikipedia.org/wiki/Internationalization_and_localization), please implement only the English version.

## Task 3: Making a Pull Request

If you’ve finished all that,

- Add and commit your changes
- Push the code to your forked repository.
- Create a pull request that links the issue.

## Task 4 (Optional): Suggest a unique username

Can you suggest a unique username by querying the backend server again? For example, if `test123` is taken, you should check if `test1231` is taken, then `test1232`, etc. You should display a username that has not yet been registered by anyone.
