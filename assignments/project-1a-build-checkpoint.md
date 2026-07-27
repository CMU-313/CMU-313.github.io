---
canvas_assignments:
- canvas_id: 958737
  doc_anchor: task-a1-planning
  due_at: '2026-03-15T23:59:00-04:00'
  name: 'A1: Initial Plan'
  points: 100
  submission_types:
  - online_upload
  rubric_section: Planning
  submission_form:
  - label: Google Doc
    hint: Provide a link to your shared Google Doc with "Commenter" permissions using the comments box.
  - label: PDF
    hint: Upload a PDF export of your document.
- canvas_id: 958738
  doc_anchor: task-a2-execution-deployment
  due_at: '2026-03-22T23:59:00-04:00'
  name: 'A2: Execution & Deployment (Release Candidate)'
  points: 100
  submission_types:
  - online_url
  - online_upload
  rubric_section: Launch Readiness & Preparation
  submission_form:
  - label: GitHub Release
    hint: 'Provide the URL of your hw1-a2 release (e.g., https://github.com/your-org/your-repo/releases/tag/hw1-a2)'
  - label: Google Doc
    hint: Provide a link to your Finalized Plan with "Commenter" permissions using the comments box.
  - label: PDF
    hint: Upload a PDF export of your finalized plan document.
- canvas_id: 958739
  doc_anchor: task-a3-operations-retrospective
  due_at: '2026-03-29T23:59:00-04:00'
  name: 'A3: Operations & Retrospective (Post-Launch Report)'
  points: 100
  submission_types:
  - online_url
  - online_upload
  rubric_section: Operations & Retrospective
  submission_form:
  - label: Google Doc
    hint: Provide a link to your shared Google Doc "Commenter" permissions using the comments box.
  - label: PDF
    hint: Upload a PDF export of your document.
due_date: 2026-03-29
group_assignment: true
kind: homework
release_date: 2026-03-09
reveal_date: 2026-03-04
checkpoints:
  - date: 2026-03-10
    title: "A0: Team Formation"
    due_at: '2026-03-10T23:59:00-04:00'
    doc_anchor: task-a0-team-formation
  - date: 2026-03-15
    title: "A1: Initial Plan"
    doc_anchor: task-a1-planning
    due_at: '2026-03-15T23:59:00-04:00'
  - date: 2026-03-22
    title: "A2: Execution & Deployment"
    doc_anchor: task-a2-execution-deployment
    due_at: '2026-03-22T23:59:00-04:00'
  - date: 2026-03-29
    title: "A3: Operations & Retrospective"
    doc_anchor: task-a3-operations-retrospective
    due_at: '2026-03-29T23:59:00-04:00'
rubric:
- criteria:
  - desc: Prioritization is explicit, targets are concrete, and chosen techniques
      fit the system's highest-risk areas.
    name: Assessment & Focus
    points: 15
    tiers:
    - desc: Prioritization is explicit and defensible, targets are concrete, and chosen
        techniques clearly fit the system's highest-risk areas.
      label: Excellent
      points: 15
    - desc: Prioritization and techniques are mostly clear and reasonable, with minor
        gaps in specificity or justification.
      label: Good
      points: 13
    - desc: Plan is usable but generic in places; prioritization exists but is weakly
        justified.
      label: Satisfactory
      points: 10
    - desc: Broad, vague plan with little true prioritization or actionable targets.
      label: Poor
      points: 6
    - desc: Section missing or does not address the required prompts.
      label: Missing / Non-Responsive
      points: 0
  - desc: Residual risks are concrete, with specific logs/metrics/alerts and clear
      detection paths for high-impact failures.
    name: Monitoring & Risk Management
    points: 10
    tiers:
    - desc: Residual risks are concrete, with actionable logs/metrics/alerts and clear
        detection paths for high-impact failures.
      label: Excellent
      points: 10
    - desc: Risks and monitoring are mostly solid but miss depth on at least one key
        failure mode.
      label: Good
      points: 8
    - desc: Risks are identified, but monitoring design is high-level or weakly tied
        to concrete triggers.
      label: Satisfactory
      points: 7
    - desc: Risk statements are vague and monitoring is mostly checkbox-level.
      label: Poor
      points: 4
    - desc: Section missing or lacks usable monitoring strategy.
      label: Missing / Non-Responsive
      points: 0
  - desc: Triage workflow, PR checklist, bug-report expectations, and AI usage policy
      are clearly defined and actionable.
    name: Defect & Incident Management
    points: 10
    tiers:
    - desc: Clear triage workflow, high-quality PR checklist, actionable bug-report
        expectations, and responsible AI usage policy.
      label: Excellent
      points: 10
    - desc: Most processes are defined and usable, but one area is underdeveloped.
      label: Good
      points: 8
    - desc: Basic process exists but lacks enough detail for reliable execution under
        pressure.
      label: Satisfactory
      points: 7
    - desc: Process guidance is incomplete or too vague to follow in practice.
      label: Poor
      points: 4
    - desc: Section missing or materially non-actionable.
      label: Missing / Non-Responsive
      points: 0
  points: 35
  section: Planning
- criteria:
  - desc: Dashboards and telemetry are directly mapped to Critical User Journeys and
      provide useful operational signal.
    name: Instrumentation & Observability
    points: 10
    tiers:
    - desc: Dashboards and telemetry are directly mapped to Critical User Journeys
        and provide useful operational signal.
      label: Excellent
      points: 10
    - desc: Meaningful monitoring exists, with minor coverage/alignment gaps.
      label: Good
      points: 8
    - desc: Basic telemetry is present but weakly connected to launch risk.
      label: Satisfactory
      points: 7
    - desc: Minimal instrumentation with little operational value.
      label: Poor
      points: 4
    - desc: Monitoring evidence is absent.
      label: Missing / Non-Responsive
      points: 0
  - desc: Changes are safe, well-evidenced, reviewed, and keep `main` stable while
      respecting scope constraints.
    name: Pre-Launch Hotfixes & Stability
    points: 10
    tiers:
    - desc: Changes are safe, well evidenced, reviewed, and keep `main` stable while
        respecting scope constraints.
      label: Excellent
      points: 10
    - desc: Mostly safe execution with minor hygiene or validation gaps.
      label: Good
      points: 8
    - desc: Some useful fixes, but execution quality and/or stability evidence is
        inconsistent.
      label: Satisfactory
      points: 6
    - desc: Risky or weakly justified changes; instability or weak process control.
      label: Poor
      points: 3
    - desc: Major rewrite, unresolved build breakage, or serious rule violation.
      label: Constraint Violation / Non-Functional
      points: 0
  points: 20
  section: Launch Readiness & Preparation
- criteria:
  - desc: Critical User Journeys remained reliably available or were quickly restored
      with supporting evidence.
    name: System Operation & Reliability
    points: 13
    tiers:
    - desc: Critical User Journeys remained reliably available or were quickly restored
        with evidence.
      label: Excellent
      points: 13
    - desc: Some degradation/outages occurred, but recovery was effective and timely.
      label: Good
      points: 11
    - desc: Mixed reliability outcomes with delayed or partial recovery.
      label: Satisfactory
      points: 9
    - desc: Major reliability failures with weak recovery effectiveness.
      label: Poor
      points: 6
    - desc: No credible evidence of operation outcomes.
      label: Missing / Non-Responsive
      points: 0
  - desc: The team followed its defined process under pressure and made clear, justified
      adaptations when reality diverged from the plan.
    name: Process Adherence & Adaptation
    points: 15
    tiers:
    - desc: Team followed defined process under pressure and adapted with clear, justified
        decisions when reality diverged.
      label: Excellent
      points: 15
    - desc: Process was followed with limited lapses; adaptations were mostly reasonable.
      label: Good
      points: 13
    - desc: Process was inconsistently applied; adaptations were reactive more than
        deliberate.
      label: Satisfactory
      points: 10
    - desc: Frequent process breakdowns or unsafe execution under pressure.
      label: Poor
      points: 7
    - desc: No evidence of disciplined process execution.
      label: Missing / Non-Responsive
      points: 0
  - desc: Reflection is concrete, candid, and evidence-backed, with specific identification
      of gaps and high-value refactoring targets.
    name: Plan vs. Reality & Technical Debt Reflection
    points: 10
    tiers:
    - desc: Reflection is concrete, candid, evidence-backed, and identifies high-value
        follow-on refactoring targets.
      label: Excellent
      points: 10
    - desc: Reflection is thoughtful and specific, but depth is uneven in one area
        (testing ROI, gaps, or debt analysis).
      label: Good
      points: 8
    - desc: Reflection covers required topics but is mostly descriptive rather than
        analytical.
      label: Satisfactory
      points: 6
    - desc: Reflection is superficial and weakly tied to evidence.
      label: Poor
      points: 4
    - desc: Reflection section missing or non-substantive.
      label: Missing / Non-Responsive
      points: 0
  - desc: Incident log is complete, timestamped, and tied to concrete evidence such
      as PRs, issues, and dashboards.
    name: Incident Management & Artifacts
    points: 7
    tiers:
    - desc: Incident log is complete, timestamped, and tied to concrete evidence (PRs,
        issues, dashboards, alerts).
      label: Excellent
      points: 7
    - desc: Incident records are mostly complete with minor omissions.
      label: Good
      points: 6
    - desc: Incident tracking exists but lacks important detail, timestamps, or traceability.
      label: Satisfactory
      points: 5
    - desc: Fragmentary incident record with weak evidence linkage.
      label: Poor
      points: 3
    - desc: Incident tracking/artifacts missing.
      label: Missing / Non-Responsive
      points: 0
  points: 45
  section: Operations & Retrospective
title: 'Phase A: Deploy'
grading_component: phase_a
grading:
  raw_max: 100
  tiers:
    - { name: "Platinum", min_score: 90, points: 25 }
    - { name: "Gold",     min_score: 85, points: 23 }
    - { name: "Silver",   min_score: 80, points: 20 }
    - { name: "Bronze",   min_score: 70, points: 18 }
    - { name: "Copper",   min_score: 60, points: 15 }
    - { name: "Fail",     min_score: 0,  points: 0 }
launch_date: Monday, March 23rd
quality_plan_gdoc_id: 1O1GQ5NJfeui6O9WxM_wb_Bh7ZsKZyuMKY6wuGI6J6TE
post_launch_report_gdoc_id: 1xqcgwS5iUyRggk09li4wSMaCTJ0MfQKMHG4zyBdgZho
---

## Learning Goals

After completing this assignment, you should be able to:

* **Inherit and operate** a legacy "brownfield" system without needing to rewrite it first.
* **Strategize quality assurance** to prioritize specific components and techniques under tight time constraints.
* **Define operational distinctions** between "perfect" quality and "launchable" quality using Critical User Journeys.
* **Instrument a running system** to provide just enough evidence (logs/metrics) to prove it is working.
* **Detect and triage** production incidents in real-time.
* **Deploy hotfixes safely** under pressure without making the outage worse.
* **Critically reflect** on the effectiveness of a quality plan against actual production reality.

## Project Context

You have been told by management that you need to launch the system on **{{page.meta.launch_date}}.**
You need to quickly devise and execute a quality plan.
Do not let perfect be the enemy of good.
You need to carefully prioritize where you spend your time and how you assure the system.
Think carefully about how you will mitigate residual risk (e.g., using monitoring to quickly catch defects in production).

The infrastructure for the system mostly already exists:
The repository comes with a DevContainer and a Docker Compose file that should allow you to begin developing locally quickly.
Additionally, a continuous deployment pipeline is already in place.
Commits to `main` will be automatically deployed to production.
Your focus should be on the behavior of the system and not on environmental concerns.

### Rules of Engagement

Throughout the assignment, all members of your team must abide by the rules below.
If you break these rules, your grade may be negatively affected.
If you are unsure about the rules, don't hesitate to post on Piazza or reach out to the teaching staff during office hours.

* You cannot make major changes. No rewrites or refactoring.
* You are allowed to write tests and use analysis tools
* You are allowed to add telemetry and logging instrumentation to code
* You are allowed to make small bug fixes (if you are unsure, reach out to the teaching staff), but you must provide strong evidence for the fix

----

{{ checkpoints_list() }}

----

## Task A0: Team Formation

You will be formed into teams during the first lecture and immediately given access to your GitHub repository.
During lecture, we will demonstrate how to build and launch the code locally, then walk through a few basic user journeys on the website.

Your team must ensure that at least one teammate can run the system locally using the provided DevContainer / Docker Compose setup.
If anyone is having a problem, we will have additional office hours during the first week.
You should come to office hours before the Thursday lecture.

----

## Task A1: Planning

Your team will need to submit a plan to product management that outlines your quality plan for the system.
You are inheriting a legacy codebase with many unknowns, and you have a limited amount of time before launch.
**You cannot test everything.**
You must carefully prioritize your efforts.

### The Quality Assurance Plan

Before making any changes to the codebase, your team will complete a structured **Quality Assurance Plan** containing exactly these three top-level sections using the [provided Google Doc Template]({{ gdoc_copy(page.meta.quality_plan_gdoc_id) }}).
You must be signed into Google with your CMU account to access the template.
You should create **one document per team.**
We want specific, verifiable answers for each question rather than vague statements.
You should elaborate and provide details where possible.
**Your plan should be clear enough that another engineer could carry out your plan with little to no questions.**

Your plan must cover:

1. **Assessment & Focus:** what you will prioritize (components/CUJs), how you will evaluate them (techniques), what “passing” means (targets/evidence), and what is out of scope (pre-launch vs launch window).
2. **Monitoring & Risk Management:** key residual risks, the logs/metrics you will monitor, and an alerting plan (what triggers alerts and how your team is notified).
3. **Operational Readiness & Response:** PR quality gates, basic incident response workflow (acknowledge → mitigate → verify), GitHub Issues defect tracking (issue template fields), and responsible AI usage rules.

The document will act as a contract for the launch window. **You should be careful not to overcommit.**

### Quality Planning Workshop (Thursday, March 12th)

Instead of a traditional lecture, we will hold a quality planning workshop in class on Thursday, March 12th.
The session will be interactive and split into two major blocks, focusing on "Assessment & Focus" and "Monitoring & Risk Management".

For each section, we will:

1. **Discuss Trade-offs:** Briefly discuss options, constraints, and good/bad examples.
2. **Drafting:** Teams will spend 15-20 minutes drafting that specific section of their plan in a Google Doc.
3. **Peer Review:** Teams will swap plans with a partner team to critique and provide feedback.
4. **Debrief:** We will discuss common themes and insights as a class.

<!-- If time allows, we will also briefly cover "Defect Management & Incident Response". -->

----

## Task A2: Execution & Deployment

After finalizing your A1 plan, you will have roughly a week to execute it and make preparations ahead of the launch of the system.
You should use this time to identify and address the most pressing issues, but be aware that you cannot make larger changes to the system (that may be required by certain issues).

Simulated traffic will begin at 12:00 am ET on Monday, March 23 (i.e., immediately after the A2 deadline).
From that point onward, your system is considered “live,” and you should expect real incidents and performance issues to emerge.

The continuous deployment (CD) pipeline is already active; any pull request merged into main will be automatically deployed to your production environment.
Use this phase to ensure your deployment pipeline is stable and that your instrumentation is reporting useful signal (dashboards, logs, and any alerts you choose to configure).

----

## Task A3: Operations & Retrospective

Traffic has started hitting your server! Your goal is to keep your Critical User Journeys alive, detect incidents, and fix things as you discover issues in production.

During the operational window, you may continue to write tests and add observability (metrics/logging/dashboard improvements), but **you are still not allowed to make major functional or architectural changes.**
Hotfixes are allowed when they are narrowly scoped, well-evidenced, and reviewed.

### The Post-Launch Report

Write a **Post-Launch Report** to close the loop on your Quality Assurance Plan from Task A1 using the [provided Google Doc Template]({{ gdoc_copy(page.meta.post_launch_report_gdoc_id) }}).
You should create **one document per team.**

This report should be honest; you are graded on your analysis of the events, not on having a "perfect" launch.
If everything went wrong, explain *why* and what you would do differently — you can still get full marks.

You should ensure that your report covers the following sections as defined in the template (follow the prompts and tables in the Google Doc):

* **System Operation & Reliability:** Uptime summary + dashboard evidence, plus a brief aggregate incident summary (do not repeat per-incident details here).
* **Process Adherence & Adaptation:** What you followed from A1, what you changed (and why), and how you stayed safe under pressure (include 1–2 PR links as evidence).
* **Plan vs. Reality & Technical Debt:** Where you were surprised, highest ROI technique, biggest blind spot, and 2–3 specific debt items that made ops/hotfixing harder.
* **Incident Management & Artifacts:** Complete the Incident Log table and include explicit GitHub links (Issues + PRs).

----

## Deliverables and Submission

Please ensure your team completes the following checklists before each respective deadline.

### A0: Team Formation (Due Tuesday, March 10th)

* Ensure at least one teammate can build and run the system locally (DevContainer / Docker Compose).
* Confirm your team can access the repository and open a pull request.
* **Submission:** No Canvas submission. Completion is checked in class.

### A1: Planning (Due Sunday, March 15th)

* [ ] Complete a draft of your **Quality Assurance Plan** using the provided template.
<!-- * [ ] Ensure the document is polished and incorporates feedback from the in-class workshop. -->
* [ ] Submit the document to Canvas.

{{ canvas_submission(958737) }}

### A2: Execution & Deployment (Due Sunday, March 22nd)

By the deadline, your team must confirm that the system is ready for the traffic spike.

* [ ] **Finalize your quality plan:** You may re-submit your quality plan at this checkpoint.
  Use this opportunity to update your plans and respond to feedback from the course staff.
* [ ] **Merge into `main`:** Ensure all your hotfixes, instrumentation, and configuration changes are safely merged into the `main` branch.
* [ ] **Create a GitHub Release:** Draft a new release on your GitHub repository with the tag `hw1-a2`. Title it **"Phase A Launch Candidate"** and include a brief changelog or list of PRs in the description.
* [ ] **Submit to Canvas:** Submit the URL of your GitHub release.

{{ canvas_submission(958738) }}

### A3: Operations & Retrospective (Due Sunday, March 29th)

* [ ] Complete your **Post-Launch Report** using the provided template, ensuring all incident logs and evidence screenshots are included.
* [ ] Ensure all relevant GitHub issues and PRs created during the operation window are properly linked in the report.
* [ ] Submit the final document to Canvas.

{{ canvas_submission(958739) }}

----

{% include "partials/assignment_grading.md" %}
