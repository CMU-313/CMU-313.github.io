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

However, your firm had a bad experience last month where an intern racked up too many API charges, so your CEO manager insists that you must use a locally hosted model.

In light of this new direction, your manager wants you to:

1. **Design the feature** - reason about, document and select an appropriate design for integrating this feature into the existing system.
2. **Evaluate different models** Evaluate different models and compare their performance.
3. **Implement the feature** Implement the translation feature.

## Deliverables and Deadlines
There are two (2) deadlines for the project. This project is worth a total of 125 points.

[**Checkpoint #1 Deliverables (Design and Test)**](./1_checkpoint.md) – 65 pts - due ~~Thursday, November 6, 11:59pm~~ Friday, November 7, 11:59pm

- [Architectural Design Document (40 pts)](./1_checkpoint.md#architectural-design-document-40-points)
- [Basic LLM Experiment (15 pts)](./1_checkpoint.md#basic-llm-experiment-15-points)
- [LLM Experiment Integration Checkpoint (10 pts)](./1_checkpoint.md#llm-experiment-integration-checkpoint-10-points)

[**Final Deliverables (Implementation and Evaluation)**](./2_checkpoint.md) - 60 pts - due Tuesday, November 11, 11:59pm

- [Final LLM Experiment Implementation (30 pts)](./2_checkpoint.md#final-llm-experiment-implementation-30-points)
- [Individual Reflection (30 pts)](./2_checkpoint.md#evaluation-report-30-points)
