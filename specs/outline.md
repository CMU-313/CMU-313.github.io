---
kind: lecture_spec_outline
status: draft
---

# Lecture Spec Format

Lecture specs are planning documents for turning a scheduled topic into a coherent class session.
They sit between the course calendar and the Quarto slide deck: specific enough to expose the learning arc, but early enough that slide implementation can still change.

Put one spec per lecture under `slides/specs/`.
Use the same numeric prefix as the eventual slide file when that relationship is known, for example `01-containers-and-orchestration.md`.

## Design Decisions

* Specs are Markdown, not Quarto.
  They are for instructor planning, not student-facing delivery.
* Specs should make the lecture's learning goals, conceptual throughline, timing, activities, and assessment hooks explicit before slide work begins.
* Specs should be durable across slide rewrites.
  A good spec describes what students should understand and do, not the exact text of every slide.
* Lectures should be principle-first, not technology tutorials.
  Tool names can appear when they clarify an idea, but the lecture should teach the transferable concept underneath the tool.
* Lecture examples should be small and isolated from homework systems.
  Use tiny fictional services, short scenarios, or simplified diagrams so students can reason without assignment-specific baggage.
* Specs should split lectures into digestible segments.
  A useful segment usually has one topic (its content), one main student action, and one reason it matters.
  Only the topic goes in the Lecture Plan table (the Content column); the student action and the reason it matters are developed in the Segment Notes, which lay the segment out as a slide-by-slide narrative.
* Name each segment as the question it answers, phrased for the student.
  Each segment opens with a plain-text splash slide that shows only the segment name, so the name has to stand on its own and tell a student what the segment is about.
  Prefer a concrete question the segment resolves ("What makes a secret a secret?", "How should secrets reach the code that needs them?") over an abstract or insider label ("The Breach", "Why Secrets Are Different", "Delivery Patterns").
  A good test: read the name cold, with no other context — if it does not preview what the student is about to learn, it is too abstract.
  The same name is used in three places — the Lecture Plan table, the Segment Notes heading, and the splash slide — so keep them identical. Administrivia is the one exception and stays "Administrivia".
* Specs should include active learning throughout the lecture.
  Think-pair-share, quick classification tasks, short written predictions, class discussions, and small diagnosis activities can all work.
* Activities do not need to wait until the end.
  The lecture plan should show where students think, discuss, predict, decide, or diagnose during the session.
* Lecture meetings start with 1-2 minutes of administrivia.
  Account for that in the timebox instead of treating it as free time.
* Learning goals should use observable verbs.
  Prefer "explain", "compare", "diagnose", "choose", "trace", and "justify" over "understand".
* Each lecture gets a small number of high-value goals.
  Three to five goals is usually enough for an 80-minute class.
* Each lecture should have a single throughline: the sentence that explains why these topics belong together.
* Keep Purpose, Throughline, and Non-Goals distinct so they do not restate each other.
  Purpose is course-arc context only: why this lecture exists, what it builds on, and what it sets up later.
  The Throughline carries the lesson, and Non-Goals carry the exclusions; Purpose should not duplicate either.
  One or two sentences of Purpose is plenty.
* Timeboxing is part of the spec.
  If a section has no time budget, it is too easy for the implementation to sprawl.
* Activities and checks for understanding belong in the spec.
  They should appear before slide drafting so the deck is not only exposition.
* Specs should name non-goals.
  This is especially useful for topics such as Kubernetes, cloud networking, and compliance that are easy to over-teach.
* Specs should connect to the broader course arc without becoming homework instructions.
  The spec can name concepts that will recur later, but it should not depend on a homework-specific system or walkthrough.
* Use one sentence per line where practical.
  This keeps diffs readable as plans evolve.

## Suggested File Shape

```markdown
---
kind: lecture_spec
status: draft
title: "Lecture Title"
date: YYYY-MM-DD
duration_minutes: 80
slide_file: ../NN-slide-file.qmd
---

# Lecture Title

## Purpose

One or two sentences of course-arc context: why this lecture exists, what it builds on, and what it sets up later.
Do not restate the throughline or the non-goals here.

## Throughline

One sentence that ties the lecture together.

## Learning Goals

By the end of the lecture, students should be able to:

* Goal 1
* Goal 2
* Goal 3

## Non-Goals

* Topic that will be mentioned but not taught deeply
* Common rabbit hole that should stay out of this lecture

## Prior Knowledge (optional)

Include this section only when the entry level is non-obvious or students are likely to mis-judge what they already know.
Skip it when the assumed baseline is just the standard course prerequisites.

* What students are assumed to have seen already
* What students are likely not to know yet

## Lecture Plan

| Time | Segment | Content |
| ---: | --- | --- |
| 0-2 min | Administrivia | Announcements and logistics |
| 2-10 min | What problem are we even solving? | The problem the lecture solves |

## Segment Notes

Each segment is a slide-by-slide narrative: one bullet per slide, titled with an assertion-evidence headline (a full-sentence claim) followed by a one-to-two sentence message. A later pass expands each slide into detail sub-bullets. Open with the slides that motivate the segment, build the concept, turn misconceptions into correcting-assertion slides, and end with the activity slide (prefixed 🤔).

### Segment Name

* **A full-sentence claim, not a topic label.** One or two sentences on what this slide conveys or shows.
* **The next claim the student needs to hear.** Its message, kept to the headline point — detail comes in the expansion pass.
* **🤔 The activity prompt.** What students do, and how to run it.

## Slide Implementation Notes

* Possible visuals, demos, diagrams, or title-slide ideas
```

## Open Questions

* Should specs be referenced from `slides/index.qmd`, or should they remain purely internal planning documents?
* Should specs include an optional section for later course connections, or should those connections stay inside the segment notes?
* Should specs eventually replace planning prose embedded directly in `.qmd` slide drafts?
