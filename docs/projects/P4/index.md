# Project 4: Architecting an LLM Integration

## Learning Goals
- Design a software architecture for a software system that incorporates a foundational large language model
- Decide the appropriate architecture for a given problem
- Address and describe the tradeoffs of different architectures
- Host and integrate pre-trained foundational large language models into an existing software system
- Evaluate the performance/quality of LLM powered features
- Design test suites that include unit, integration, and mock testing, to ensure robustness and reliability
- Engineer techniques to improve the performance of pre-trained models on application-specific tasks
- Decide whether an LLM powered solution is production ready

## Project Context

The development of the new Q&A forum system for CMU is in full swing when your CEO suddenly bursts into the room shouting, “LLMs! AI! Why are we building a Q&A forum without integrating LLMs?!”

Once your CEO has finally calmed down, your manager calls an all-hands meeting. At the meeting, everyone agrees that you don’t have the resources to build a completely new Q&A forum and also automate the whole question-answering problem.

But, to better compete with Piazza, your CEO and manager decide to put your team in charge of exploring using an LLM to implement a translation feature. This feature will automatically translate posts written in languages other than English into English. This initiative aims to foster inclusivity and ensure that language barriers do not hinder participation in the forum.

In light of this new direction, your manager wants you to:

1. **Architect the feature** - reason about, document and select an appropriate architecture for integrating this feature into the existing system.
2. **Build an experimental integration** with the existing NodeBB codebase to evaluate feasibility.
3. **Evaluate the feature** and decide whether the feature should be fully implemented.

As everything is just settling down, your CEO bursts back into the room!! There's a new catch: the company is strapped for funding and must be very careful with its spending. As a result, your team is now required to conduct all experimentation and implementation of the LLM-powered translation feature **using an LLM hosted on the company's servers**. There will be hardware overhead in this solution, but, in the long run, will be cheaper in this use case than having to pay an external LLM provider (ex. OpenAI) for every query.

<!-- FOR LATER POSSIBLY: Your boss will be extra happy and give you a salary raise (bonus points) if you are able to make a NodeLingo model for the company: a pre-trained LLM that you build and customize with a prompt specifically for translation (fewer points), or fine-tune the model (more points). This is discussed in more depth in checkpoint 1. -->

## Deliverables and Deadlines
There are three (3) deadlines for the project. This project is worth a total of 125 points.

[**Checkpoint #1 (Design and Test)**](./1_checkpoint.md) – 65 pts - due Thursday, November 6, 11:59pm

- [Architectural Design Document (40 pts)](./1_checkpoint.md#architectural-design-document-40-points)
- [Basic LLM Experiment (15 pts)](./1_checkpoint.md#basic-llm-experiment-15-points)
- [LLM Experiment Integration Checkpoint (10 pts)](./1_checkpoint.md#llm-experiment-integration-checkpoint-10-points)

[**Checkpoint #2 (Implementation and Evaluation)**](./2_checkpoint.md) - 60 pts - due Tuesday, November 11, 11:59pm

- [Final LLM Experiment Implementation (30 pts)](./2_checkpoint.md#final-llm-experiment-implementation-30-points)
- [Evaluation Report (30 pts)](./2_checkpoint.md#evaluation-report-30-points)
