# Project 4: Architecting an LLM Integration

## Learning Goals
- Design a software architecture for a software system that incorporates a foundational large language model
- Decide the appropriate architecture for a given problem
- Address and describe the tradeoffs of different architectures
- Integrate pre-trained foundational large language models into an existing software system
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

As everything is just settling down, your CEO bursts back into the room!! There's a new catch: the company is strapped for funding and must be very careful with its spending. As a result, your team is now required to conduct all experimentation and implementation of the LLM-powered translation feature **using only the Azure credits currently at your disposal**. If your team successfully stays within your available credits and doesn't need to request any more, you’ll earn **bonus points** for your ingenuity and efficiency.

Some of you may think that it’s unfair for this change to come up unexpectedly, especially since we didn’t inform you before P3, but keep in mind that this is just like real life! Working in a company means having to deal with unexpected circumstances, which more often than not contain some aspect concerning money. We're looking to see how well you can adapt to this new situation, and we want you to have this experience before you're dealing with the pressure of real company money. Rest assured, if your team needs more credits to finish the project, we will not be taking off points.

## Deliverables and Deadlines
There are three (3) deadlines for the project. This project is worth a total of 125 points.

**Checkpoint #1 Deliverables** – 55 pts - due Thursday, November 14, 11:59pm

- [Architectural Design Document (40 pts)](#architectural-design-document-40-points)
- [Basic LLM Experiment (15 pts)](#basic-llm-experiment-15-points)

**Checkpoint #2 Deliverables** – 10 pts - due Monday, November 18, 11:59pm

- [LLM Experiment Integration Checkpoint (10 pts)](#llm-experiment-integration-checkpoint-10-points)

**Final Deliverables** - 60 pts - due Thursday, November 21, 11:59pm

- [Final LLM Experiment Implementation (30 pts)](#final-llm-experiment-implementation-30-points)
- [Evaluation Report (30 pts)](#evaluation-report-30-points)

## Checkpoint #1 Deliverables

### Architectural Design Document (40 points)

To start, your manager has requested a concrete design document outlining how you plan to integrate the new LLM-powered translation feature into the existing codebase. One of your manager's requirements is that this feature should work on a deployed site.

If the team decides to go ahead with the feature, this design document will be followed in order to fully integrate this feature into NodeBB.

Two initial solutions to consider are:

1.  **Implementing a Python-based microservice** and deploying it as a separate service; then, integrating the service with your existing monolith via a REST API
2.  **Refactoring part or all of the existing monolith** into a microservices-based architecture

Your design document must discuss both of these approaches and **include a third approach of your choosing**. You must advocate for one of these three approaches as the best solution.

Once you have finished evaluating the codebase, create the design document highlighting your findings and decisions. Below is a sample outline for your design document along with recommended page lengths.

1. **Feature Overview (<1 pages)**
    Describe concisely how the translation feature works and how it will be used by the relevant stakeholders, with screenshots if necessary.

2. **Assessing LLM Suitability (<1 page)**
    Use the framework discussed in class to discuss why an LLM may be a good solution for translating posts on NodeBB.

3. **Current Architecture (<1 page)**
    Provide a brief description of the current NodeBB architecture. Include an **architectural diagram** to support your description.

4. **Quality Requirements (<1 page)**
    Provide a concise, prioritized list of the overall quality requirements you considered in arguing for the integration of the feature into the system and a short justification for each. Your team should decide on **at least three** requirements to focus on.

    Rank your requirements in decreasing order of importance. This allows readers to quickly understand what you were designing for.

5. **Potential Solutions (~1 page each)**
    Your team should consider **three** different potential solutions for integrating the new feature. For each, provide at least one architectural diagram, a brief description of the solution's architectural design, and a discussion of the design's tradeoffs.

    Tradeoffs must involve (but are not limited to) the quality attributes described in the previous section. Justify such arguments with reference to appropriate diagrams and concrete examples, as appropriate.

6. **Selected Architecture + Justification (<1 page)**
    Describe which design your team decided to proceed with in architecturally integrating the feature into existing codebase. Justify your design decisions, including why your design is adequate for the quality attributes important to this system, and what assumptions you made in your design (if any).

> [!NOTE]
> Diagrams should **involve suitable architectural views**; **must include a legend**; and **should involve appropriate levels of abstraction** for the components in the diagram. If necessary, use color/shape/text to differentiate between types of components and connectors. You may find it appropriate to merge more than one view into a single diagram. If you do this, **you must be explicit about what views you are merging**, and why. Otherwise, diagrams should clearly represent legitimate architectural views. Make sure that multiple views of the architecture are consistent with each other and the links are clear; if necessary provide a mapping in additional text.

> [!INFO] "Drawing Diagrams"
> Drawing diagrams is much easier with the right software. Consider tools like [draw.io](https://draw.io/) (free, online, and collaborative), [Dia](http://dia-installer.de/), [OmniGraffle](https://www.omnigroup.com/omnigraffle), [MS Visio](https://www.microsoft.com/en-us/microsoft-365/visio/flowchart-software), or even just the drawing editor of [Google Docs](https://docs.google.com/). [Google Slides](https://slides.google.com/) will also likely work for this purpose. Pictures of whiteboard drawings are also acceptable, if clearly readable.

More resources to assist you with creating your design document can be found in the [Resources & Documentation](#resource-documentation) section below.

!!! warning "On Generative AI"
    In the past, students have utilized generative AI tools to generate diagrams with mixed success. While some diagrams have been useful and accurate, others have fallen short due to inaccuracies or oversimplifications not aligned with specific project requirements. Be cautious and review them carefully for accuracy and relevance. If we suspect you've abused generative AI and your diagrams are **inadequate**, we won't consider regrade requests. You’ve been warned.

By the checkpoint deadline, your team will submit your design document to Gradescope as a PDF.

### Basic LLM Experiment (15 points)

To explore the feasibility of LLMs for this task, your manager would like you to prototype the basic functionality of an LLM to translate text. Due to the company’s existing deal with Microsoft, your team will use the gpt-4o-mini language model from OpenAI's Platform.

To get setup, you will need to setup your Azure NodeBB instance and set up LLM use through Azure. You should already have done both of these for recitations 7 and 8, but for completeness, you should refer to these two documents if you don't have something set up.

1. [Recitation 7 instructions](https://docs.google.com/document/d/1cC95F2752ZNmAJ_VPjZmEd8UoUhBi7-lQElx6OaZFd0) on setting up NodeBB instance on Azure
2. [Recitation 8 instructions](https://docs.google.com/document/d/1cTvANh2R6WChDXFz3HDXepcIeciUasAZhB9jScGRdJ4/edit?usp=sharing) on setting up Azure for LLM use

Once you're all set up, open the Colab notebook using [this link](). Click on File --> Save as a copy in Drive to create your own copy that you will work on. Only one team member needs to do this, and the team should collaborate using this notebook. Click on Share and make sure the Colab notebook is **editable** by anyone in Carnegie Mellon University.

Now, you should be ready to experiment with gpt-4o-mini! Follow the instructions in the notebook through the end of the Basic LLM Experiment.

Given the unpredictable nature of LLM responses, it is crucial to test whether your application can handle a range of outcomes. Your Colab notebook should also include tests for your code. We have provided a starter code.
In this task, you are required to employ mocking techniques to test your code resilience against unexpected results from API calls to the LLM. Mocking is a method used in testing to replace real system components with mock objects that simulate the behavior of those components. This approach allows developers to emulate various scenarios, including errors or atypical responses from external services, without having to make actual API calls. Here you will be using mocking to mimic different unexpected outcomes to check if your code can handle such anomalies gracefully.

For full credit, your submission should have at least four mock tests that deal with different unexpected model behaviors. At least one of these tests should involve the model returning unexpected text. All tests should relate to the `query_llm_robust` function.

You should download and submit a .ipynb copy of your Colab notebook (with outputs) to Gradescope.

## Checkpoint #2 Deliverables

### LLM Experiment Integration Checkpoint (10 points)

For this checkpoint, you are expected to have successfully integrated the provided UI code into your project. Additionally, you must implement and deploy a server-side functionality that returns a hardcoded response. This step is crucial to ensure you are on track. We have provided some initial code on [this repo](https://github.com/CMU-313/translator-service).

Furthermore, your server-side code must include unit and mock tests. To accomplish this, you must move the tests you wrote in the previous checkpoint to the repo and integrate them into the CI pipeline.

## Final Deliverables

### Final LLM Experiment Implementation (30 points)

The final step is to implement this LLM feature into your team's NodeBB project. Your implementation should include the UI code you integrated in Checkpoint #2. You should also integrate the code you developed as a part of the LLM experiment, but you may modify it as needed to successfully integrate the functionality into your code.
**Because this is the last Project to use NodeBB, commit to your repo, and we will grade your final repository state**  Reach out to your TA if you have any questions. 

### Evaluation Report (30 points)

Now that you’ve experimented with an LLM integration, write a report that summarizes your findings for the rest of the team. In particular, you will need to decide whether your findings justify completing and shipping this feature.

Your report should include the following with clear headings:

**1. Introduction (&lt;0.5 pages)**

Provide a brief introduction to the LLM integration you’re evaluating, and the context of its use, i.e. the translation feature.

**2. LLM integration (&lt;1 page)**

Describe the end-to-end implementation of your final solution to translating posts. Given an arbitrary post in any language, how do you integrate with an LLM to return an answer? Feel free to include any prompts and diagrams.

**4. Evaluation Results (&lt;0.5  page)**

Provide a summary of the results from applying the evaluation strategy on your final LLM experiment. Feel free to include any evidence/output from your notebook.

**5. Operational Costs (&lt;0.5 pages)**

Based on the pricing of your chosen LLM, how much will it cost to provide users with this feature? How long does it take to translate a post? State any assumptions made in making these estimates. Is the cost associated with providing this feature reasonable?

**6. Final Recommendation (&lt;0.5 pages)**

Provide a final decision on whether the translation feature should be implemented based on the evaluation results, operational costs and other relevant factors.

On Gradescope submit the following:

* Link to your Colab notebook (with output) that contains your code, analysis. Make sure it is editable so that we can run the notebook if necessary.
* PDF of your evaluation report

## Grading
To receive full credit for the first checkpoint, we expect:

- [ ] An uploaded PDF design document outlining your research into the existing codebase architecture, the quality requirements considered by your team, alternative solutions, and a final justification & timeline for your selected integration plan
- [ ] A link to your Colab notebook completing all of the setup and basic LLM experiment steps outlined by the previous section

To receive full credit for the second checkpoint, we expect:

- [ ] A functional integration of the UI code into your NodeBB application.
- [ ] A preliminary implementation of the translation feature using the starter code, including CI with unit and mock tests.
- [ ] An integrated deployment of your NodeBB and the translation service on GCP.

To receive full credit for the final deadline, we expect:

- [ ] A functional translation feature, as described in your design document, integrated into your NodeBB application and deployed on GCP.
- [ ] An uploaded PDF report discussing your evaluation findings addressing all the sections outlined above

## Resource & Documentation

### Design Documents
The design document task is easy to underestimate both in terms of time needed and in terms of difficulty designing meaningful and useful descriptions. While it is easy to create a superficial solution, a good solution will likely require significant thinking, discussion, and iteration.

Feel free to seek feedback from the course staff on your solution before submission!

We recommend that you appoint someone in your team to track the accuracy and completeness of architectural representations throughout this assignment. **Do not** just divide up the views among your team members and assume they show everything needed. You only need to submit the final designs/documents, not intermediate steps on the process of getting there.

There are a few additional reference materials available in the CMU library that your team may want to consult. We do not recommend reading through all of it; instead, skip around to sections that are relevant to you.

- [Software Architecture in Practice, Third Edition](https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=30264): You may wish to review appropriate sections within Part Two to help find appropriate tactics, techniques you can use in your design to promote particular quality attributes.
- [Documenting Software Architectures: Views and Beyond, Second Edition](https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=30386): useful book to generally reference for creating architecture documentation.

### LLMs

- [Azure OpenAI docs](https://learn.microsoft.com/en-us/azure/ai-services/openai/overview)
- [Azure OpenAI Service pricing](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/openai-service/g)
- [SBert Cosine Similarity Documentation](https://www.sbert.net/docs/quickstart.html#comparing-sentence-similarities)
- [SBert Semantic Search Documentation](https://www.sbert.net/examples/applications/semantic-search/README.html)
