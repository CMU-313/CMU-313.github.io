---
title: "Interviews & Requirements"
nav_order: 10
---

# Project 3: Interviews & Requirements

!!! warning "Updated October 23, 2026"
    This page has changed since it was first posted. Old text is ~~struck out~~, and new text is marked **Updated Oct 23:**. The main changes: you now do your work in a [P3 Workbook](#getting-started-your-workbook) and submit it as one PDF; the reflection questions are a separate Gradescope assignment; there is a new interview log; and the permission-rules example was corrected to match how opencode actually works.

## Deliverables

**Interviews & Requirements** – 55 points – due Thursday, October 29, 2026, 11:59PM

- [Target Declaration & Interview Script (15 pts)](#target-declaration-interview-script-15-pts)
- [Interviews & Notes (20 pts)](#interviews-notes-20-pts)
- [Requirements & Reflection (20 pts)](#requirements-reflection-20-pts)

## Getting Started: Your Workbook

**Updated Oct 23:** This section is new.

You'll do all of your Project 3 work in one Google Doc, the **P3 Workbook**. It has a section for each deliverable, and each section starts on its own page.

1. [Make a copy of the P3 Workbook template](https://docs.google.com/document/d/1_zzGSI3nn6P4mugiRk_xNwj5BoQzphoWMs-MqoEld9c/copy).
2. Move your copy into your team's Google Drive folder (the one your TAs shared with you at the start of the semester), and name it `P3 Workbook – <andrewid>`.
3. Fill in each section as you go. Replace the gray instructions with your own work, and don't delete the page breaks.

## Choosing a Target Feature

You will each explicitly declare **one opencode feature** to interview users about. It can be the feature you built in Project 2 or a different part of opencode.

- **Default:** the feature you built in Project 2, which you already know well.
- **Strongly recommended switch:** if your Project 2 feature is heavily non-deterministic (its behavior depends on LLM output, streaming, timing, or the network), choose a feature with more deterministic logic instead. Requirements for non-deterministic behavior are much harder to state precisely, and much harder to check later. You do not need permission to switch, but we strongly recommend talking it over with your TA first.

!!! example "Example of a deterministic feature: permission rules"
    opencode lets users control what the agent may do without asking, using rules in their config such as `"git *": "ask"` or `"rm *": "deny"` (see the [permissions docs](https://opencode.ai/docs/permissions/)). The matching logic lives in `packages/opencode/src/permission/` and `packages/opencode/src/util/wildcard.ts`. Given the same rules and the same command, it always gives the same answer, and users have strong expectations about it ("a specific rule listed after the catch-all `*` rule should take priority"). That makes it a good target. You are welcome to choose it, or use it as a model for the kind of feature to look for.

### Shared Features

Students who pick the same feature may collaborate on the interview script and run interviews together, but you must disclose it: who you worked with and which parts were shared (**Updated Oct 23:** put this in section 8 of your workbook). You still need three interviews (one of each kind below), and every student present at a shared interview can count it toward their three. Your requirements and reflection must be your own.

## Target Declaration & Interview Script (15 pts)

### Target Declaration

~~At the top of your submission, declare:~~ **Updated Oct 23:** In section 1 of your workbook, declare:

- The feature you chose
- The files or modules that implement it (link them in your team repository)
- Why you chose it
- If you switched away from your Project 2 feature: what made it a poor fit

### Interview Script

~~Write an interview script of about one page.~~ **Updated Oct 23:** In section 2 of your workbook, write an interview script of about one page. Generic questions ("What do you like about it?", "Is it easy to use?") are fine as warm-ups, but they are not enough on their own. Your script must include questions that draw out **precise expectations** about the feature's behavior, including at least one question of each of these kinds:

| Kind | Example question |
|---|---|
| **Invariants** | "What should *never* happen when you use this?" |
| **Round-trip** | "If you do X and then undo it, what do you expect to see?" |
| **Metamorphic** | "If you changed the input slightly, what should stay the same? What should change?" |
| **Oracle** | "How would you know it gave you the wrong answer?" |

Adapt these to your feature. "What should never happen?" is a starting point; "Is there any command that should *never* run, no matter what rules you've written?" is a question someone can actually answer. Plan follow-ups for when an answer is vague ("Can you give me a specific example?", "What would you expect to see instead?").

## Interviews & Notes (20 pts)

Run **three** interviews about your target feature, one with each kind of interviewee:

1. **A classmate who is not on your team.** A real opencode user who doesn't know your feature's internals.
2. **A member of course staff.** A TA or instructor. Sign up for a slot using the sign-up sheet that will be posted in Slack. Staff interviews are short (about ~~15 minutes~~ **Updated Oct 23:** 10 minutes), so come prepared.
3. **Someone outside the course.** Anyone who has used an AI coding tool (opencode, Claude Code, Cursor, Copilot, and so on), such as a developer friend, a colleague from an internship, or a student in another program. They bring the least course bias.

~~For each interview, take notes that record what the interviewee actually said, as close to their words as you can, and give each note a line number or ID (e.g. `C-12` for line 12 of your classmate interview) so you can cite it later. Your notes should also record:~~

- ~~Who you interviewed (name and role for classmates and staff; a role only, such as "backend developer, uses Copilot daily", for outside interviewees)~~
- ~~When the interview took place and how long it lasted~~
- ~~Which script questions you asked, and any follow-ups you added on the spot~~

**Updated Oct 23:** For each interview, take notes in sections 4–6 of your workbook that record what the interviewee actually said, as close to their words as you can. Number every line so you can cite it later: `C-1`, `C-2`, … for the classmate, `S-1`, … for staff, and `O-1`, … for the outside interviewee. Your notes should also show which script questions you asked, and any follow-ups you added on the spot.

**Updated Oct 23:** Fill in the **interview log** (section 3 of your workbook) with one row per interview:

- Who you interviewed (name for classmates and staff; a role only, such as "backend developer, uses Copilot daily", for outside interviewees)
- When the interview took place and how long it lasted
- Whether it was in person or remote

!!! note "Interview etiquette"
    Tell interviewees what the interview is for and ask before recording; notes alone are fine. Show them the feature (a live demo or a screen share works well) so they're reacting to real behavior and not guessing.

## Requirements & Reflection (20 pts)

### Requirements Table

Turn what you heard into **5 to 8 new or already-implemented requirements** for your feature. Each requirement must be:

- **Testable:** it should be possible to write an automated test that checks whether the requirement holds.
- **Traceable:** you should be able to point to which specific interview note(s) each requirement came from.

~~Present your requirements in a table with this format:~~ **Updated Oct 23:** Present your requirements in the table in section 7 of your workbook:

| ID | Interview evidence | Requirement | Acceptance Criteria |
|---|---|---|---|
| R1 | `C-12`, `S-4`: "I'd be furious if it ran `rm -rf` after I said deny" | When a command matches several rules, the last matching rule in the config decides the outcome. | With rules `{"*": "allow", "rm *": "deny"}`, `rm -rf /` evaluates to `deny` and `ls -la` evaluates to `allow`. |
| R2 | ... | ... | ... |

~~Keep this table somewhere you can easily update it; you will build on it.~~ **Updated Oct 23:** You will build on this table later, so keep it up to date and don't merge cells.

### Reflection

Answer the following questions ~~on Gradescope~~ **Updated Oct 23:** in the **Project 3: Reflection** assignment on Gradescope (not in your workbook):

- Which script questions worked well, and which fell flat? Why?
- What would you change about your script if you did this again?
- Which requirements came from only **one kind** of interviewee (classmate, staff, or outside)? What does that tell you about who to talk to?

## Submission

~~Submit a single PDF to Gradescope containing, in order: your target declaration, interview script, interview notes (all three), requirements table (with acceptance criteria), reflection, and (if applicable) your collaboration disclosure.~~

**Updated Oct 23:** Project 3 has **two** Gradescope submissions, both due Thursday, October 29, 2026, 11:59PM:

1. **Project 3: Elicit.** Download your workbook as a PDF (File → Download → PDF) and upload it. Tag each question to the pages of its workbook section.
2. **Project 3: Reflection.** Type your answers to the three [reflection questions](#reflection).

## Grading

To receive full credit for the target declaration and script, we expect:

- [ ] A clearly declared target feature, with the files/modules that implement it and a justification for choosing it (and for switching, if you did)
- [ ] An interview script with at least one question of each kind (invariant, round-trip, metamorphic, oracle), adapted to your feature, with planned follow-ups

To receive full credit for the interviews and notes, we expect:

- [ ] Three interviews: one classmate outside your team, one staff member, and one person outside the course who has used an AI coding tool
- [ ] Notes for each interview that capture what the interviewee said, with line IDs that can be cited
- [ ] ~~The interviewee's role, the date, the duration, and the questions asked, for each interview~~
- [ ] **Updated Oct 23:** The questions asked and any follow-ups, for each interview
- [ ] **Updated Oct 23:** An interview log covering all three interviews: interviewee, date, duration, and in person or remote

To receive full credit for the requirements and reflection, we expect:

- [ ] 5 to 8 new or already-implemented requirements, each testable against the feature's behavior
- [ ] Acceptance criteria for every requirement: a concrete situation and the expected outcome that a test could check
- [ ] Every requirement cites the interview note(s) it came from
- [ ] ~~A reflection that discusses which questions worked, what you'd change, and which requirements came from only one kind of interviewee~~
- [ ] **Updated Oct 23:** Answers on Gradescope to the three reflection questions: which questions worked, what you'd change, and which requirements came from only one kind of interviewee
- [ ] A collaboration disclosure, if you shared any part of the work
