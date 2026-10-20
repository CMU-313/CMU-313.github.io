---
title: "3A Interviews & Requirements"
nav_order: 10
---

# Project 3: Interviews & Requirements

## Deliverables

**Interviews & Requirements** – 25 points – due Monday, October 26, 2026, 11:59PM

- [Target Declaration & Interview Script (7 pts)](#target-declaration-interview-script-7-pts)
- [Interviews & Notes (10 pts)](#interviews-notes-10-pts)
- [Requirements & Reflection (8 pts)](#requirements-reflection-8-pts)

## Choosing a Target Feature

You will each explicitly declare **one opencode feature** to interview users about. It can be the feature you built in Project 2 or a different part of opencode.

- **Default:** the feature you built in Project 2, which you already know well.
- **Strongly recommended switch:** if your Project 2 feature is heavily non-deterministic (its behavior depends on LLM output, streaming, timing, or the network), choose a feature with more deterministic logic instead. Requirements for non-deterministic behavior are much harder to state precisely, and much harder to check later. You do not need permission to switch, but we strongly recommend talking it over with your TA first.

!!! example "Example of a deterministic feature: permission rules"
    opencode lets users control what the agent may do without asking, using rules in their config such as `"git *": "ask"` or `"rm *": "deny"` (see the [permissions docs](https://opencode.ai/docs/permissions/)). The matching logic lives in `packages/opencode/src/permission/` and `packages/opencode/src/util/wildcard.ts`. Given the same rules and the same command, it always gives the same answer, and users have strong expectations about it ("a `deny` rule should never be overridden by a broader `allow`"). That makes it a good target. You are welcome to choose it, or use it as a model for the kind of feature to look for.

### Shared Features

Students who pick the same feature may collaborate on the interview script and run interviews together, but you must disclose it: who you worked with and which parts were shared. You still need three interviews (one of each kind below), and every student present at a shared interview can count it toward their three. Your requirements and reflection must be your own.

## Target Declaration & Interview Script (7 pts)

### Target Declaration

At the top of your submission, declare:

- The feature you chose
- The files or modules that implement it (link them in your team repository)
- Why you chose it
- If you switched away from your Project 2 feature: what made it a poor fit

### Interview Script

Write an interview script of about one page. Generic questions ("What do you like about it?", "Is it easy to use?") are fine as warm-ups, but they are not enough on their own. Your script must include questions that draw out **precise expectations** about the feature's behavior, including at least one question of each of these kinds:

| Kind | Example question |
|---|---|
| **Invariants** | "What should *never* happen when you use this?" |
| **Round-trip** | "If you do X and then undo it, what do you expect to see?" |
| **Metamorphic** | "If you changed the input slightly, what should stay the same? What should change?" |
| **Oracle** | "How would you know it gave you the wrong answer?" |

Adapt these to your feature. "What should never happen?" is a starting point; "Is there any command that should *never* run, no matter what rules you've written?" is a question someone can actually answer. Plan follow-ups for when an answer is vague ("Can you give me a specific example?", "What would you expect to see instead?").

## Interviews & Notes (10 pts)

Run **three** interviews about your target feature, one with each kind of interviewee:

1. **A classmate who is not on your team.** A real opencode user who doesn't know your feature's internals.
2. **A member of course staff.** A TA or instructor. Sign up for a slot using the sign-up sheet that will be posted in Slack. Staff interviews are short (about 15 minutes), so come prepared.
3. **Someone outside the course.** Anyone who has used an AI coding tool (opencode, Claude Code, Cursor, Copilot, and so on), such as a developer friend, a colleague from an internship, or a student in another program. They bring the least course bias.

For each interview, take notes that record what the interviewee actually said, as close to their words as you can, and give each note a line number or ID (e.g. `C-12` for line 12 of your classmate interview) so you can cite it later. Your notes should also record:

- Who you interviewed (name and role for classmates and staff; a role only, such as "backend developer, uses Copilot daily", for outside interviewees)
- When the interview took place and how long it lasted
- Which script questions you asked, and any follow-ups you added on the spot

!!! note "Interview etiquette"
    Tell interviewees what the interview is for and ask before recording; notes alone are fine. Show them the feature (a live demo or a screen share works well) so they're reacting to real behavior and not guessing.

## Requirements & Reflection (8 pts)

### Requirements Table

Turn what you heard into **5 to 8 new or revised requirements** for your feature. Each requirement must be:

- **Precise:** someone could check whether it holds by looking at the feature's behavior. "Permissions should be intuitive" is not a requirement; "a command matching a `deny` rule is never executed, even if a broader rule allows it" is.
- **Traceable:** it cites the specific interview note(s) it came from.

Present your requirements in a table with this format:

| ID | Interview evidence | Requirement |
|---|---|---|
| R1 | `C-12`, `S-4`: "I'd be furious if it ran `rm -rf` after I said deny" | A command matching a `deny` rule is never executed, regardless of other matching rules. |
| R2 | ... | ... |

Keep this table somewhere you can easily update it; you will build on it.

### Reflection

Write a short reflection (about half a page) addressing:

- Which script questions worked well, and which fell flat? Why?
- What would you change about your script if you did this again?
- Which requirements came from only **one kind** of interviewee (classmate, staff, or outside)? What does that tell you about who to talk to?

## Submission

Submit a single PDF to Gradescope containing, in order: your target declaration, interview script, interview notes (all three), requirements table, reflection, and (if applicable) your collaboration disclosure.

## Grading

To receive full credit for the target declaration and script, we expect:

- [ ] A clearly declared target feature, with the files/modules that implement it and a justification for choosing it (and for switching, if you did)
- [ ] An interview script with at least one question of each kind (invariant, round-trip, metamorphic, oracle), adapted to your feature, with planned follow-ups

To receive full credit for the interviews and notes, we expect:

- [ ] Three interviews: one classmate outside your team, one staff member, and one person outside the course who has used an AI coding tool
- [ ] Notes for each interview that capture what the interviewee said, with line IDs that can be cited
- [ ] The interviewee's role, the date, the duration, and the questions asked, for each interview

To receive full credit for the requirements and reflection, we expect:

- [ ] 5 to 8 new or revised requirements, each precise enough to be checked against the feature's behavior
- [ ] Every requirement cites the interview note(s) it came from
- [ ] A reflection that discusses which questions worked, what you'd change, and which requirements came from only one kind of interviewee
- [ ] A collaboration disclosure, if you shared any part of the work
