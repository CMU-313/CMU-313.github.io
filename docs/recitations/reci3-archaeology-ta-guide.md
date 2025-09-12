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
- [ ] NodeBB fork repository: [NodeBB-F25-R3](https://github.com/CMU-313/NodeBB)
- [ ] Issue link ready to share: [Feature request issue](https://github.com/CMU-313/NodeBB-S24-R3/issues/1)

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

## Common Student Challenges & Solutions

### Technical Issues
**Problem**: Students can't get NodeBB running locally
- **Solution**: Check Node.js version compatibility, verify all dependencies installed
- **Prevention**: Send setup instructions day before recitation

**Problem**: Students unfamiliar with the technology stack
- **Solution**: Emphasize they don't need to understand everything, focus on following data flow
- **Reassurance**: "You're not expected to know all of this - that's why we're learning archaeology!"

**Problem**: Search results are overwhelming
- **Solution**: Show how to narrow searches, look for recent/relevant files first
- **Tip**: Start with error messages - they're easier to trace

### Conceptual Difficulties
**Problem**: Students don't know where to start
- **Solution**: Guide them to search for the exact error text first
- **Follow-up**: Then work backwards to understand the flow

**Problem**: Confusion about frontend vs backend
- **Solution**: Quick explanation: Frontend = what user sees, Backend = server logic
- **Rule of thumb**: If it's user-facing styling/interaction → frontend; if it's data/validation → backend

**Problem**: Students want to over-engineer the solution
- **Solution**: Remind them this is about learning the process, not creating perfect code
- **Focus**: Getting something working is more valuable than optimization

### Process Issues
**Problem**: Students try to implement immediately without exploring
- **Solution**: Emphasize the investigation phase is crucial
- **Analogy**: "You wouldn't perform surgery without understanding anatomy first"

**Problem**: Students get frustrated with not understanding everything
- **Solution**: Normalize this feeling - professional developers experience this daily
- **Reframe**: Focus on finding what they *need* to know, not everything

## Assessment & Participation

### What to Look For
- **Active exploration**: Are students systematically investigating the codebase?
- **Good questions**: Do they ask about code structure, data flow, or implementation approaches?
- **Collaboration**: Are they helping each other or sharing discoveries?
- **Problem-solving process**: Are they breaking down the task logically?

### Red Flags
- Students jumping straight to random code changes
- Complete silence or disengagement
- Obvious copy-pasting without understanding
- Not following the repository setup instructions

## Extension Activities (If Time Permits)

### For Fast Finishers
1. **Code Quality Discussion**: What makes this codebase easy or hard to navigate?
2. **Architecture Analysis**: How is the user registration flow organized?
3. **Testing Exploration**: Find and understand the existing tests

### Advanced Challenges
1. **Multiple Suggestions**: Instead of just adding a number, suggest multiple creative alternatives
2. **Real Uniqueness Check**: Implement server-side checking for truly unique suggestions
3. **UI Enhancement**: Improve the user experience of the suggestion display

## Post-Recitation Follow-up

### For Students
- [ ] Complete the implementation and create PR
- [ ] Fill out recitation quiz on Gradescope
- [ ] Optional: Attempt the advanced uniqueness checking feature

### For TAs
- [ ] Review student PRs and provide feedback
- [ ] Note common implementation patterns for next recitation discussion
- [ ] Document any recurring issues for future recitation improvements

## Common Code Locations (Spoiler-Free Hints)

*Use these only if students are completely stuck after 10+ minutes of searching*

- User registration logic: Look in `src/controllers/` or `src/user/` directories
- Client-side forms: Check `public/src/client/` areas
- Error message handling: Search for the specific error text
- API endpoints: Look for routes that handle user creation

## Resources & Links
- [Main Recitation Page](reci3-archaeology.md)
- [Slides](https://docs.google.com/presentation/d/19ym2ZT1t6W4942ayiTozBwoFtsEOPANeRBH1UB7g9k4/edit?slide=id.g2d896fab132_0_194#slide=id.g2d896fab132_0_194)
- [GitHub Repository](https://github.com/CMU-313/NodeBB-S24-R3)
- [Feature Request Issue](https://github.com/CMU-313/NodeBB-S24-R3/issues/1)
- [Gradescope Quiz](https://www.gradescope.com/courses/1086939/assignments/6689436/)

---

*Remember: The goal is teaching software archaeology skills, not just completing the feature. Focus on the process and investigation techniques that will serve students throughout their careers.*
