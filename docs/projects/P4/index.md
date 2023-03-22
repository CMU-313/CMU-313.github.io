# Project 4: Software Architecture & ML Evaluation

## Learning Goals
- Design a software architecture for software system that incorporates machine learning
- Decide the appropriate architecture for a given problem
- Assess and describe the tradeoffs of different architectures
- Integration of machine learning into a software system and reason about their implications
- Evaluate the performance and fairness of machine learning models
- Engage meaningfully with engineering ethics

## Project Context 
As you and your team continue developing the new system, your CMU contact suddenly bursts into the room shouting, “Careers! Hiring! Machine learning!”

Your manager follows closely behind and provides an explanation: a significant number of job recruiters have taken interest in your project and would like to use the platform as a means to reach out to students for career opportunities. However, the population of students is too large, and increasing annually. They are concerned by the sheer number of students to review for job applications, and recruiters want a simpler way to narrow the applicant pool.

While your team had been working on deployment, your buzzword-enamored clients had hired another engineer to work on an extra ML-based feature to take in student performance data and provide a prediction of which applicants are more likely to succeed in industry.

However, the engineer left shortly after and the project was abandoned. They have left an unfinished draft pull request on the repository, and you have been tasked with completing the project.

Your manager wants you to:

1. **Assess the current architecture**, and decide what would be the best way to incorporate the work done by the previous engineer
2. **Reason about, document and select an appropriate architecture** for the project
3. **Finish integrating the feature** made by the other team based on your team's new design

Along with architectural issues, as the feature will be evaluating student information, you are also concerned about the fairness of the model. You have been tasked with:

1. **Evaluating** the pre-trained model's performance and fairness
2. **Writing a report** on the evaluation of the model
3. **Provide a decision** on whether the model should be used in production
  
## Deliverables and Deadlines
There are two (2) deadlines for this project. This project is worth a total of 180 points.

**Checkpoint Deliverables** – 80 points - due Tuesday, April 4th at 11:59pm

- [Architectural Design Document (60 pts)](#architectural-design-document-60-points)
- [Jupyter Notebook Setup (20 pts)](#jupyter-notebook-setup-20-points)

**Final Deliverables** – 100 points - due Tuesday, April 11th at 11:59pm

- [Feature Integration Implementation (40 pts)](#feature-integration-implementation-40-points)
- [Evaluation Report (60 pts)](#evaluation-report-60-points)

## Checkpoint Deliverables

### Architectural Design Document (60 points)

Before jumping into development, your manager would like a concrete design document on how you plan on integrating the feature seamlessly into the existing repository.

Your team should start by evaluating what components of the feature have been implemented for you by the previous engineer, then consider how you would like to proceed with integration. Some potential options include:

1.  Rewriting the feature in JavaScript and incorporate it into the monolith
2.  Implementing a Python-based microservice and deploy as a seperate service; then, integrate the service with your existing monolith via REST API
3.  Refactoring part or all of the existing monolith into a microservices-based architecture

Then, create a design document highlighting your findings and decisions. Below is a sample outline for your design document along with recommended page lengths:

1.  **Feature Description** (< 0.5 pages)
    Describe concisely how the feature works and how it will be used by the relevant stakeholders. 
    <br/>

2.  **Current Architecture** (< 1 page)
    Provide a brief description of the current NodeBB architecture, along with an architectural diagram. 
    Your diagram should also demonstrate the current state of the new career feature (i.e. unintegrated with the rest of the codebase)
    <br/>

3.  **Quality Requirements** (< 0.5 pages)
    Provide a concise, prioritized list of the overall quality requirements you considered in arguing for the integration of the feature into the system. 
    Rank them in decreasing order of importance. This allows readers to quickly understand what requirements you were designing for.
    <br/>

4.  **Considered Solutions** (1-1.5 pages each)
    Your team should consider at least two different potential solutions for integrating the new feature. For each, provide a brief description, an architectural diagram, and a discussion of the pros/cons.
    Tradeoffs must involve (but are not limited to) quality attributes that will be affected by the alternative. Justify such arguments with reference to appropriate diagrams (this provides traceability) and concrete examples, as appropriate.
    <br/>
  
5.  **Selected Architecture + Justification** (<1 page)
    Describe which design your team decided to proceed with in architecturally integrating the feature into existing codebase.
    Justify your design decisions, including why your design is adequate for the quality attributes important to this system, and what assumptions you made in your design (if any).

!!! note "On Diagrams"
    Diagrams should involve suitable architectural views; must include a legend; and should involve appropriate levels of abstraction for the components in the diagram. If necessary, use color/shape/text to differentiate between types of components and connectors.
    
    You may find it appropriate to merge more than one view into a single diagram. If you do this, you must be explicit about what views you are merging, and why. Otherwise, diagrams should clearly represent legitimate architectural views. Make sure that multiple views of the architecture are consistent with each other and the links are clear; if necessary provide a mapping in additional text.

!!! note "Drawing Diagrams"
    [Documenting Software Architectures: Views and Beyond, Second Edition](https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=30386) is a useful book on creating architecture documentation. It is available (for free) as an e-book from the CMU library web site. If you use it, treat it as reference material; do not plan to read major parts of it.

    Drawing diagrams is easier with the right software. Consider tools like draw.io (free, online, and collaborative), Dia, OmniGraffle, MS Visio, or even just the drawing editor of Google Docs. Google Slides will also likely work for this purpose. Pictures of whiteboard drawings are also acceptable, if clearly readable.


Submit your design document to Gradescope. 

### OLD (IGNORE FOR NOW)
Additional Hints:

- The design document task is easy to underestimate both in terms of time needed and in terms of difficulty designing meaningful and useful descriptions. While it is easy to create a superficial solution, a good solution will likely require significant thinking, discussion, and iteration. Feel free to seek feedback from the course staff on your solution before submission.

- It may take several iterations to get your architectural views right. Appoint someone to track the accuracy and completeness of architectural representations throughout this assignment. Do not just divide up the views among your team members and assume they show everything needed. You only need to submit the final designs/documents, not intermediate steps on the process of getting there.

- As additional reference material, [Software Architecture in Practice, Third Edition](https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=30264) is a book on software architecture that is available (for free) as an e-book from the CMU library web site. You may wish to review appropriate sections within Part Two to help find appropriate tactics, techniques you can use in your design to promote particular quality attributes. Note that the book is not a reading assignment and you should not try to read it thoroughly. Instead, use it as reference material and select particular bits of advice that are relevant to your situation.

### Jupyter Notebook Setup (20 points)
As the previous engineer left in a hurry, the model that was provided to you is pre-trained and you do not have any information on how it was trained. You are tasked with evaluating the model's performance and fairness.

When it comes to training the model itself, the ML engineer who worked on the project before you had the following assumptions:

- The model is used to predict whether a student will be a good candidate for a software engineering job. It is a binary classifier, where 1 means the student is a good candidate, and 0 means the student is not a good candidate.
- The model is trained on a dataset of students who have graduated from CMU, and have been working in the industry for at least 1 year.
- In order to prevent bias, they assumed that removing `Gender (M, F)` and `Student ID` from the dataset would be sufficient when it comes to training the model. They claimed that it is now *Group Unaware*, thus the model would be fair.

The model specification is as follows:
```
X variable (input parameters)
- Age (18 - 25)
- Major (Computer Science, Information Systems, Business, Math, 
         Electrical and Computer Engineering, Statistics and Machine Learning)
- GPA (0 - 4.0)
- Extra Curricular Activities (Student Theatre, Buggy, Teaching Assistant, Student Government, 
    Society of Women Engineers, Women in CS, Volleyball, Sorority, Men's Basketball, 
    American Football, Men's Golf, Fraternity)
- Number of Programming Languages (1, 2, 3, 4, 5)
- Number of Past Internships (0, 1, 2, 3, 4)

Y variable (output)
- Good Candidate (0, 1)
```
The previous engineer has provided some examples on the usage of the model in the draft pull request. 

To begin with, you should first evaluate the model's performance. You are provided with a test dataset, which contains a similar set of features and output (whether the student is a good candidate or not). This test dataset is a different set of students from the training dataset, and the evaluation of whether the student is a good candidate **is done by a fair panel of recruiters, so it can be considered to be fair and unbiased. **Additionally, the panel of recruiters have provided you with **additional context on the extracurricular activities in comments** (marked with #).

Your test dataset is provided to you in the following format:
```
X variable
- Student ID
- Gender (M, F)
- Age (18 - 25)
- Major (Computer Science, Information Systems, Business, Math, 
         Electrical and Computer Engineering, Statistics and Machine Learning)
- GPA (0 - 4.0)
- Extra Curricular Activities (Student Theatre, Buggy, Teaching Assistant, Student Government, 
    Society of Women Engineers, Women in CS, Volleyball, Sorority, Men's Basketball, 
    American Football, Men's Golf, Fraternity)
  # Likely Co-Ed (Student Theatre, Buggy, Teaching Assistant, Student Government)
  # Likely Majority Female (Society of Women Engineers, Women in CS, Volleyball, Sorority)
  # Likely Majority Male (Men's Basketball, American Football, Men's Golf, Fraternity)
- Number of Programming Languages (1, 2, 3, 4, 5)
- Number of Past Internships (0, 1, 2, 3, 4)

Y variable
- Good Candidate (0, 1)
```

Before doing a thorough evaluation of the fairness of the model, you would do some preliminary analysis on the test dataset, and run the model on the test dataset to get the accuracy of the model. To do so, you will need to set up a Jupyter notebook to do this, you can either:

- Set up a [JupyterLab](https://jupyter.org/install) on your local machine. 
- Or use [Google Colab] to run the notebook in the cloud.

It is recommended that you use Python 3.9 or above when setting up the notebook.

After you have set up the notebook, you should:

1. Load the model and test dataset
2. Plot the distribution of the test dataset across all features (except Student ID) using any visualization library of your choice (e.g. pandas, matplotlib, seaborn, plotly, etc.). You should choose the appropriate visualization for each feature.
3. Predict the output of the test dataset using the model
4. Report the accuracy of the model, and the confusion matrix

Refer to the Resources section if you need help with any of the above steps.

By the checkpoint deadline, your team will commit the Jupyter notebook to your repository, and submit a link to the Jupyter notebook with the basic analysis and usage of the model done. 

## Final Deliverables

### Feature Integration Implementation (40 points)
@Angela - TODO, essentially asking them to implement their design from their design document

### Evaluation Report (60 points)

Now you have to decide whether the model should be used in production. You will need to evaluate the performance and the fairness of the model. You should do all your work in the Jupyter notebook that you set up in the checkpoint deliverables.

#### Performance Evaluation
You should have already evaluated the performance of the model in the checkpoint deliverables. You should now do a more thorough evaluation of the model's performance. You should:

- Evaluate the model's performance on the test dataset, and report the accuracy and confusion matrix

#### Fairness Evaluation
When evaluating the fairness of the model, you should 
- Revisit the assumptions made by the previous engineer
- Revisit the fairness discussion we had in class, and also in [ML Discrimination](https://research.google.com/bigpicture/attacking-discrimination-in-ml/)
- Consider the fairness strategies and corresponding metrics that can be used to evaluate the fairness of the model

#### Report 
After evaluating the performance and fairness of the model, you should now write a report on your findings. You will also need to provide a decision on whether the model should be used in production.

Your report should include the following sections with clear headings:

1. **Introduction** Provide a brief introduction to the model that you are evaluating, and the test dataset that you are using, and the context of use of the model.
2. **Description of the test data** Provide descriptive statistics of the test dataset (e.g. mean, median, mode, standard deviation, etc.) for each feature. You should also provide a brief discussion on the distribution of the features.
3. **Model Performance** Provide the accuracy and confusion matrix of the model on the test dataset and a brief discussion on the performance of the model.
4. **Feature Exploration** Select features that you think are important when it comes to evaluating the fairness of the model, and why.
5. **Fairness Evaluation** Consider **three fairness strategies** that were discussed in class and then 
   1. Provide the corresponding **fairness metrics** for the model (if applicable) based on the features you selected in step 4.
   2. Determine whether the model is fair under each fairness strategy, and provide a brief discussion on why.
   3. Determine which fairness strategy is the most appropriate for the model, given the context of what the model is used for. Provide a brief discussion on why.
6. **Recommendation** Make a recommendation on whether the model should be used in production, and provide a brief discussion on why. 

On Gradescope submit the following:
- A link to your Jupyter notebook that contains your code and analysis that is committed to your repository
- A PDF of your report

## Grading
To receive full credit for this project, you must meet the following requirements:

## Resource & Documentation