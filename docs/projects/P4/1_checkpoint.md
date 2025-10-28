# Project 4A: Design and Test

## Deliverables


## Architectural Design Document (40 points)

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
    Use proprities of LLMs discussed in class to discuss why an LLM may be a good solution for translating posts on NodeBB.

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

!!! note
    Diagrams should **involve suitable architectural views**; **must include a legend**; and **should involve appropriate levels of abstraction** for the components in the diagram. If necessary, use color/shape/text to differentiate between types of components and connectors. You may find it appropriate to merge more than one view into a single diagram. If you do this, **you must be explicit about what views you are merging**, and why. Otherwise, diagrams should clearly represent legitimate architectural views. Make sure that multiple views of the architecture are consistent with each other and the links are clear; if necessary provide a mapping in additional text.

!!! tip
    Drawing diagrams is much easier with the right software. Consider tools like [draw.io](https://draw.io/) (free, online, and collaborative), [Dia](http://dia-installer.de/), [OmniGraffle](https://www.omnigroup.com/omnigraffle), [MS Visio](https://www.microsoft.com/en-us/microsoft-365/visio/flowchart-software), or even just the drawing editor of [Google Docs](https://docs.google.com/). [Google Slides](https://slides.google.com/) will also likely work for this purpose. Pictures of whiteboard drawings are also acceptable, if clearly readable.

More resources to assist you with creating your design document can be found in the [Resources & Documentation](#resource-documentation) section below.

!!! warning On Generative AI
    In the past, students have utilized generative AI tools to generate diagrams with mixed success. While some diagrams have been useful and accurate, others have fallen short due to inaccuracies or oversimplifications not aligned with specific project requirements. Be cautious and review them carefully for accuracy and relevance. If we suspect you've abused generative AI and your diagrams are **inadequate**, we won't consider regrade requests. You’ve been warned.

By the checkpoint deadline, your team will submit your design document to Gradescope as a PDF.

## Basic LLM Experiment (15 points)

To explore the feasibility of LLMs for this task, your manager would like you to prototype the basic functionality of an LLM to translate text. Due to the company’s existing deal with Microsoft, your team will use the gpt-4o-mini language model from OpenAI's Platform.

Once you're all set up, open the Colab notebook using [this link](https://colab.research.google.com/drive/1ubDjMa-YhKq2kuHaiy_JfotWam_VlmSm?usp=sharing). Click on File --> Save as a copy in Drive to create your own copy that you will work on. Only one team member needs to do this, and the team should collaborate using this notebook. Click on Share and make sure the Colab notebook is **editable** by anyone in Carnegie Mellon University.

Now, you should be ready to experiment with gpt-4o-mini! Follow the instructions in the notebook through the end of the Basic LLM Experiment.

Given the unpredictable nature of LLM responses, it is crucial to test whether your application can handle a range of outcomes. Your Colab notebook should also include tests for your code. We have provided a starter code.
In this task, you are required to employ mocking techniques to test your code resilience against unexpected results from API calls to the LLM. Mocking is a method used in testing to replace real system components with mock objects that simulate the behavior of those components. This approach allows developers to emulate various scenarios, including errors or atypical responses from external services, without having to make actual API calls. Here you will be using mocking to mimic different unexpected outcomes to check if your code can handle such anomalies gracefully.

For full credit, your submission should have at least four mock tests that deal with different unexpected model behaviors. At least one of these tests should involve the model returning unexpected text. All tests should relate to the `query_llm_robust` function.

You should download and submit a .ipynb copy of your Colab notebook (with outputs) to Gradescope.

## Resource & Documentation

### Design Documents
The design document task is easy to underestimate both in terms of time needed and in terms of difficulty designing meaningful and useful descriptions. While it is easy to create a superficial solution, a good solution will likely require significant thinking, discussion, and iteration.

Feel free to seek feedback from the course staff on your solution before submission!

We recommend that you appoint someone in your team to track the accuracy and completeness of architectural representations throughout this assignment. **Do not** just divide up the views among your team members and assume they show everything needed. You only need to submit the final designs/documents, not intermediate steps on the process of getting there.

There are a few additional reference materials available in the CMU library that your team may want to consult. We do not recommend reading through all of it; instead, skip around to sections that are relevant to you.

- [Software Architecture in Practice, Third Edition](https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=30264): You may wish to review appropriate sections within Part Two to help find appropriate tactics, techniques you can use in your design to promote particular quality attributes.
- [Documenting Software Architectures: Views and Beyond, Second Edition](https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=30386): useful book to generally reference for creating architecture documentation.

### LLMs

Here is some useful information about LLMs you may want to use when comparing different architectures.
- [OpenAI pricing](https://platform.openai.com/docs/pricing)
- [Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [DeepSeek pricing](https://api-docs.deepseek.com/quick_start/pricing)
- [LLM Comparison Leaderboard](https://www.vellum.ai/llm-leaderboard)
