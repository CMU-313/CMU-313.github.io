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

While your team had been working on deployment, your buzzword-enamored clients had hired another engineer to work on an extra ML-based feature to take in student performance data and provide a prediction of which applicants are more likely to succeed in industry. Specifically, the new career feature would:

- adds a new recruiter user type
- adds a new career tab on NodeBB, that leads to a new career page
- the new career page will
     - allow students to submit relevant information about themselves for recruiters to see
     - allow recruiters to see a list of students who have submitted their information, together with the prediction of their success in industry

However, the engineer left shortly after and the project was abandoned. They have left an unfinished draft pull request on the repository, and you have been tasked with completing the project.

Your manager wants you to:

1. **Assess the current architecture**, and decide what would be the best way to incorporate the work done by the previous engineer
2. **Reason about, document and select an appropriate architecture** for the project
3. **Finish integrating the feature** made by the previous engineer based on your team's new design

Along with architectural issues, as the feature will be evaluating student information, you are also concerned about the fairness of the model. You have been tasked with:

1. **Evaluating** the pre-trained model's performance and fairness
2. **Writing a report** on the evaluation of the model
3. **Provide a decision** on whether the model should be used in production
  
## Deliverables and Deadlines
There are two (2) deadlines for this project. This project is worth a total of 180 points.

**Checkpoint Deliverables** – 80 points - due Tuesday, April 4th, 11:59pm

- [Architectural Design Document (60 pts)](#architectural-design-document-60-points)
- [Jupyter Notebook Setup (20 pts)](#jupyter-notebook-setup-20-points)

**Final Deliverables** – 100 points - due Tuesday, April 11th, 11:59pm

- [Feature Integration Implementation (50 pts)](#feature-integration-implementation-50-points)
- [Evaluation Report (50 pts)](#evaluation-report-50-points)

## Checkpoint Deliverables

### Architectural Design Document (60 points)

To start off, your manager has requested a **concrete design document** on how you plan on integrating the new ML-based career feature into the existing codebase. One of your manager's requirements is that the career feature **should work on a deployed site**.

==You will later follow this design document in order to fully integrate this feature into NodeBB.==

Your team should start by evaluating what components of the feature have been implemented for you by the previous engineer as detailed in their [draft pull request](https://github.com/CMU-313/NodeBB/pull/186), then consider potential architectural solutions. It is **highly recommended** that at least one team member does a fresh clone and run the draft pull request locally to get a better understanding of the feature before proceeding. (Note: You can clone template repositories without forking them.)

Some initial solutions to consider include:

1.  **Rewriting the all aspects of the feature in JavaScript** and incorporating it into the monolith
2.  **Implementing a Python-based microservice** and deploying it as a separate service; then, integrating the service with your existing monolith via a REST API
3.  **Refactoring part or all of the existing monolith** into a microservices-based architecture

!!! warning "Implementation Efforts"
    Keep in mind that **your team will have to integrate the feature as part of the final deliverable**. This should be a factor that affects your final decision on which architecture to pursue.

Once you have finished evaluating the codebase, create the design document highlighting your findings and decisions. Below is a sample outline for your design document along with recommended page lengths.

1. **Feature Overview (<1 pages)**  
    Describe concisely how the career feature works and how it will be used by the relevant stakeholders, with screenshots if necessary.

2. **Current Architecture (<1 page)**  
    Provide a brief description of the current NodeBB architecture and the current state of the new career feature (i.e. unintegrated with the rest of the codebase).

    Include an **architectural diagram** to support your description.

3. **Quality Requirements (<1 page)**  
    Provide a concise, prioritized list of the overall quality requirements you considered in arguing for the integration of the feature into the system and a short justification for each. Your team should decide on **at least three** requirements to focus on.

    Rank your requirements in decreasing order of importance. This allows readers to quickly understand what you were designing for.

4. **Potential Solutions (~1 page each)**  
    Your team should consider **at least two** different potential solutions for integrating the new feature. For each, provide at least one architectural diagram, a brief description of the solution's architectural design, and a discussion of the design's tradeoffs.

    Tradeoffs must involve (but are not limited to) the quality attributes described in the previous section. Justify such arguments with reference to appropriate diagrams and concrete examples, as appropriate.

5. **Selected Architecture + Justification (<1 page)**  
    Describe which design your team decided to proceed with in architecturally integrating the feature into existing codebase. Justify your design decisions, including why your design is adequate for the quality attributes important to this system, and what assumptions you made in your design (if any).

    Within your justification, you should explicitly include a timeline demonstrating how you plan on dividing development work within your team to ensure you finish implementation before the final deadline.

!!! note "On Diagrams"
    Diagrams should **involve suitable architectural views**; **must include a legend**; and **should involve appropriate levels of abstraction** for the components in the diagram. If necessary, use color/shape/text to differentiate between types of components and connectors.
    
    You may find it appropriate to merge more than one view into a single diagram. If you do this, **you must be explicit about what views you are merging**, and why. Otherwise, diagrams should clearly represent legitimate architectural views. Make sure that multiple views of the architecture are consistent with each other and the links are clear; if necessary provide a mapping in additional text.

!!! info "Drawing Diagrams"
    Drawing diagrams is much easier with the right software. Consider tools like [draw.io](https://draw.io/) (free, online, and collaborative), [Dia](http://dia-installer.de/), [OmniGraffle](https://www.omnigroup.com/omnigraffle), [MS Visio](https://www.microsoft.com/en-us/microsoft-365/visio/flowchart-software), or even just the drawing editor of [Google Docs](https://docs.google.com/). [Google Slides](https://slides.google.com/) will also likely work for this purpose.
    
    Pictures of whiteboard drawings are also acceptable, if clearly readable.

More resources to assist you with creating your design document can be found in the [Resources & Documentation](#resource-documentation) section below.

By the checkpoint deadline, your team will submit your design document to Gradescope as a PDF.

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
The previous engineer has provided some examples on the usage of the model in the [draft pull request](https://github.com/CMU-313/NodeBB/pull/186).

You are provided with a [test dataset](/assets/project/student_data.csv), which contains a similar set of features and output (whether the student is a good candidate or not). This test dataset is a different set of students from the training dataset, and the evaluation of whether the student is a good candidate **is done by a fair panel of recruiters, so it can be considered to be unbiased. **Additionally, the panel of recruiters have provided you with **additional context on the extracurricular activities in comments** (marked with #).

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

Before doing a thorough evaluation of the fairness of the model, you will start by doing preliminary analysis on the [test dataset](/assets/project/student_data.csv), and run the model on the test dataset to get the accuracy of the model. To do so, you will need to set up a Jupyter notebook to do this, you can either:

- Set up a [JupyterLab](https://jupyter.org/install) on your local machine. Additionally, you can use [VSCode](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) to run the notebook as well.
- Or use [Google Colab](https://colab.research.google.com/) to run the notebook in the cloud. (Recommended if you do not have experience with Jupyter notebooks)

It is recommended that you use **Python 3.9 or above** when setting up the notebook.

After you have set up the notebook, you should:

1. Load the model and test dataset
2. Plot the distribution of the test dataset across all features (except Student ID) using any visualization library of your choice (e.g. pandas, matplotlib, seaborn, plotly, etc.). You should choose the appropriate visualization for each feature.
3. Predict the output of the test dataset using the model
4. Report the accuracy of the model, and the confusion matrix

Refer to the [Resources & Documentation](#resource-documentation) section if you need help with any of the above steps.

By the checkpoint deadline, your team will commit the Jupyter notebook to your repository, and submit a link to the Jupyter notebook with the basic analysis and usage of the model done. 

## Final Deliverables

### Feature Integration Implementation (50 points)

Complete the integration of the ML-based candidate recommendation feature into your team repository for NodeBB. Your implementation should follow your selected design from your checkpoint design document.

Revisiting the [project context](#project-context), the feature:
 > - adds a new recruiter user type
   - adds a new career tab on NodeBB, that leads to a new career page
   - the new career page will
      - allow students to submit relevant information about themselves for recruiters to see
      - allow recruiters to see a list of students who have submitted their information, together with the prediction of their success in industry

You may freely use any and/or all of the development progress made available in the [draft pull request](https://github.com/CMU-313/NodeBB/pull/186) in your implementation. In fact, if the draft pull request matches your proposed design, you are highly encouraged to directly integrate all code from the draft pull request as a starting point for your implementation.

On Gradescope, you should:

- **Submit a link to your deployed site** that has the career features successfully integrated
- **Answer the discussion questions** regarding your implementation and any additional design decisions made by your team

??? info "Partial Credit"
    For partial credit, you may instead submit your repository with a locally working integration of the career feature. You should then answer the presented questions on Gradescope for how to get your feature working locally.

!!! note "A Note on CD"
    While we encourage CD workflows, your deployment does **not** have to be automated for this assignment. In other words, it is acceptable to manually deploy your site without modifying your workflow from the previous project.

### Evaluation Report (50 points)

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

1. **Introduction (< 0.5 page)**  
   Provide a brief introduction to the model that you are evaluating, and the test dataset that you are using, and the context of use of the model.
2. **Description of the test data (< 1 page)**  
   Provide descriptive statistics of the test dataset (e.g. mean, median, mode, standard deviation, etc.) for each feature, preferably in a table. You should also provide a brief discussion on the distribution of the features.
3. **Model Performance (< 0.5 page)**  
   Provide the accuracy and confusion matrix of the model on the test dataset and a brief discussion on the performance of the model.
4. **Feature Exploration (< 1 page)**  
   Identify features that you think are important when it comes to evaluating the fairness of the model, and explain why.
5. **Fairness Evaluation (~ 1.5 page)**  
   Consider **three fairness strategies** that were discussed in class and then:

    1. Provide the corresponding **fairness metrics** for the model (if applicable) based on the features you selected in step 4.
    2. Determine whether the model is fair under each fairness strategy, and provide a brief discussion on why.
    3. Determine which fairness strategy is the most appropriate for the model, given the context of what the model is used for. Provide a brief discussion on why.

6. **Recommendation (< 0.5 page)**  
   Make a recommendation on whether the model should be used in production, and provide a brief discussion on why. 

On Gradescope submit the following:

- A link to your Jupyter notebook that contains your code and analysis that is committed to your GitHub repository.
- A PDF of your report

## Grading
To receive full credit for the checkpoint, we expect:

- [ ] A design document outlining your research into the existing codebase architecture, the quality requirements considered by your team, alternative solutions, and a final justification & timeline for your selected integration plan
- [ ] A link to a Jupyter notebook completing all of the setup steps outlined by the previous section

To receive full credit for the final deadline, we expect:

- [ ] A link to your successfully deployed web application for your team repository which demonstrates the integration of the ML-based career feature
- [ ] A link to a Jupyter notebook containing all research/data gathered during your evaluation of the ML model
- [ ] An uploaded PDF report discussing the fairness of the model addressing all the sections outlined above

## Resource & Documentation

### Design Documents
The design document task is easy to underestimate both in terms of time needed and in terms of difficulty designing meaningful and useful descriptions. While it is easy to create a superficial solution, a good solution will likely require significant thinking, discussion, and iteration.

Feel free to seek feedback from the course staff on your solution before submission!

We recommend that you appoint someone in your team to track the accuracy and completeness of architectural representations throughout this assignment. **Do not** just divide up the views among your team members and assume they show everything needed. You only need to submit the final designs/documents, not intermediate steps on the process of getting there.

There are a few additional reference materials available in the CMU library that your team may want to consult. We do not recommend reading through all of it; instead, skip around to sections that are relevant to you.

- [Software Architecture in Practice, Third Edition](https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=30264): You may wish to review appropriate sections within Part Two to help find appropriate tactics, techniques you can use in your design to promote particular quality attributes.
- [Documenting Software Architectures: Views and Beyond, Second Edition](https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=30386): useful book to generally reference for creating architecture documentation.

### Model Analysis

#### Jupyter Notebooks
- [How to Use Jupyter Notebooks](https://www.dataquest.io/blog/jupyter-notebook-tutorial/)
- [How to Use Jupyter Notebooks on Google Colab](https://colab.research.google.com/notebooks/intro.ipynb)

#### Pandas
- [How to Use Pandas](https://www.w3schools.com/python/pandas/default.asp)
- [Reading CSV Files](https://www.w3schools.com/python/pandas/pandas_csv.asp)
- [Dataframe](https://www.w3schools.com/python/pandas/pandas_dataframes.asp)

#### Data Analysis
- [Descriptive Statistics](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html)
- [What is Accuracy of a Model?](https://developers.google.com/machine-learning/crash-course/classification/accuracy)
- [Accuracy](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html)
- [What is a Confusion Matrix?](https://www.dataschool.io/simple-guide-to-confusion-matrix-terminology/)
- [Confusion Matrix](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html)

#### Visualization
- [Plotting with Pandas](https://pandas.pydata.org/docs/user_guide/visualization.html)
- [Matplotlib](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)
- [Seaborn](https://seaborn.pydata.org/tutorial.html)
- [Plotly](https://plotly.com/python/)