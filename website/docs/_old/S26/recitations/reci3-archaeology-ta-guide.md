# Recitation 3: Software Archaeology - TA Guide

## Overview
This recitation introduces students to software archaeology - the practice of understanding and navigating unfamiliar codebases. Students will work hands-on with the NodeBB codebase to implement a username suggestion feature when registration fails due to duplicate usernames.

## Learning Objectives
By the end of this recitation, students should be able to:
- Navigate and understand the structure of a large, unfamiliar codebase
- Use search tools and IDE features to locate relevant code sections
- Differentiate between frontend and backend code
- Implement small features by extending existing functionality
- Understand the importance of software archaeology skills in professional development

## Preparation (Before Recitation)
### Required Materials
- [ ] Slides: [Software Archaeology Slides](https://docs.google.com/presentation/d/19ym2ZT1t6W4942ayiTozBwoFtsEOPANeRBH1UB7g9k4/edit?usp=sharing)
- [ ] NodeBB fork repository: [NodeBB-F25-R3](https://github.com/CMU-313/NodeBB-F25-R3)
- [ ] Issue link ready to share: [Feature request issue](https://github.com/CMU-313/NodeBB-F25-R3/issues/1)

### Setup Check
- [ ] Ensure all students have access to the repository
- [ ] Test that the NodeBB instance runs properly in the dev environment
- [ ] Verify that students can fork and clone repositories

## Recitation Timeline (50 minutes)

### Introduction (10 minutes)
1. **Welcome & Context Setting** (3 min)
   - Explain software archaeology concept
   - Real-world relevance: Most developers spend significant time reading existing code
   - Today's goal: Learn systematic approach to understanding unfamiliar code

2. **Feature Overview** (4 min)
   - Show current NodeBB registration behavior
   - Demonstrate the "username already exists" error
   - Explain desired feature: suggest alternative usernames

3. **Task Overview** (3 min)
   - Walk through the GitHub issue
   - Emphasize this is about *process* not just implementation
   - Remind about PR requirement

### Guided Exploration (15 minutes)
4. **Repository Structure Tour** (8 min)
   - Navigate through key directories together
   - Point out `src/` (backend) vs `public/` (frontend)
   - Highlight important files: `package.json`, `README.md`, etc.
   - Show how to use IDE's file explorer effectively

5. **Search Strategies Demo** (7 min)
   - Demonstrate different search approaches:
     - Searching for error messages
     - Searching for "username" or "register" keywords
     - Using IDE's "Go to Definition" features
   - Show how to filter search results
   - Demonstrate git grep vs IDE search

### Hands-on Work (20 minutes)
6. **Task 0: Repository Setup** (5 min)
   - Students fork and clone repository
   - Follow README setup instructions
   - Verify NodeBB runs locally
   - **TA Action**: Circulate to help with setup issues

7. **Task 1: Reproduce Behavior** (5 min)
   - Students test current registration flow
   - Try registering with existing username
   - Document current error behavior
   - **TA Action**: Ensure all students see the error message

8. **Task 2: Code Investigation** (10 min)
   - Students search for relevant code sections
   - Identify whether changes needed in frontend/backend
   - Locate error message sources
   - **TA Action**: Guide students who are stuck, ask probing questions

### Implementation & Wrap-up (5 minutes)
9. **Implementation Guidance** (3 min)
   - Brief discussion of findings as a group
   - Hint at general approach without giving away solution
   - Remind about i18n complexity (English only for this task)

10. **Next Steps** (2 min)
    - Explain they should complete implementation after recitation
    - Review PR requirements
    - Mention optional advanced task
    - Preview next recitation


## Common Code Locations (Spoiler-Free Hints)

*Use these only if students are completely stuck after 10+ minutes of searching*

- User registration logic: Look in `src/controllers/` or `src/user/` directories
- Client-side forms: Check `public/src/client/` areas
- Error message handling: Search for the specific error text
- API endpoints: Look for routes that handle user creation

## Locate the files to change

Help students find the relevant files using these search strategies:

### Step 1: Initial Search
Run `grep -r "Username taken"` in the public folder. This returns all files containing the string "Username taken" and will list several JavaScript files.

### Step 2: Follow the Breadcrumbs  
The files from Step 1 don't contain the actual implementation code. Instead, they reference a placeholder string called "username-taken".

### Step 3: Search for the Placeholder
Run `grep -r "username-taken"` in the public folder. This returns many files, most of which are translation-related.

### Step 4: Filter Out Translation Files
Run `grep -r "username-taken" --exclude-dir=language` to exclude translation files. This should return a single target file: `src/client/register.js`, which needs to be modified.

## Make a string template

The goal is to change the error message from 'Account taken' to 'Account taken. Maybe try ${currentUsername}suffix'. This requires converting a static error message into a dynamic template.

### Understanding Message Templates
Guide students to examine existing templated error messages in `public/language/en-US/error.json`. Look for examples like:
```
'wrong-parameter-type': 'A value of type %3 was expected for property \%1`, but %2 was received instead'
```

This format shows how the project uses message templates with placeholder variables (`%1`, `%2`, `%3`).

### Implementation Steps
1. **Modify the error message**: In `public/language/en-US/error.json`, find line 34:
   ```
   "username-taken": "Username taken",
   ```
   
2. **Add template placeholder**: Change it to:
   ```
   "username-taken": "Username taken. Maybe try %1",
   ```

3. **Update the error call**: In `src/client/register.js`, modify the showError call from:
   ```
   [[error:username-taken]]
   ```
   to:
   ```
   [[error:username-taken, "${username}suffix"]]
   ```

### How It Works
The `%1` placeholder takes the value from the second argument passed to the showError function. When calling `showError(username_notify, [[error:username-taken, "${username}suffix"]])`, the `${currentUsername}suffix` gets passed as the second argument and replaces `%1` in the template.

## Resources & Links
- [Main Recitation Page](reci3-archaeology.md)
- [Slides](https://docs.google.com/presentation/d/19ym2ZT1t6W4942ayiTozBwoFtsEOPANeRBH1UB7g9k4/edit?usp=sharing)
- [GitHub Repository](https://github.com/CMU-313/NodeBB-F25-R3)
- [Feature Request Issue](https://github.com/CMU-313/NodeBB-F25-R3/issues)
- [Gradescope Quiz](https://www.gradescope.com/courses/1086939/assignments/6689436/)

---

*Remember: The goal is teaching software archaeology skills, not just completing the feature. Focus on the process and investigation techniques that will serve students throughout their careers.*
