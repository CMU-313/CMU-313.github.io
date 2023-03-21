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

Your manager follows closely behind and provides an explanation: a significant number of job recruiters have taken interest in your project and would like to use the platform as a means to reach out to students for career opportunities. However, the population of students is too large, and increasing annually. They are concerned at the sheer number of students to review for job applications, and recruiters want a simpler way to narrow the applicant pool. While your team had been working on the service, your buzzword-enamored clients had hired another engineer to work on an extra ML-based feature to take in student performance data and provide a prediction of which applicants are more likely to succeed.

However, the engineer left shortly after and the project was abandoned. They have left an unfinished draft pull request on the repository, and you have been tasked with completing the project.

Your manager wants you to:

1. Assess the current architecture, and decide what's the best way to incorporate the work done by the previous engineer.
2. Reason about, document and select an appropriate architecture for the project.
3. Finish to re-integrate the feature made by the other team based on your team's new design

At the same time, given the nature of the project of evaluating students, you are also concerned about the fairness of the model. You have been tasked with:

1. Evaluating the pre-trained model's performance and fairness
2. Writing a report on the evaluation of the model
3. Provide a decision on whether the model should be used in production
  
## Deliverables and Deadlines
There are two (2) deadlines for this project. This project is worth a total of 180 points.

**Checkpoint Deliverables** – 80 points - due Tuesday, April 4th at 11:59pm

- [Architectural Design Document (60pts)](#architectural-design-document-60-points)
- [Jupyter Notebook Setup (20pts)](#jupyter-notebook-setup-20-points)

**Final Deliverables** – 100 points - due Tuesday, April 11th at 11:59pm

- [Feature Integration Implementation (40 pts)](#feature-integration-implementation-40-points)
- [Evaluation Report (60 pts)](#evaluation-report-60-points)

## Checkpoint Deliverables

### Architectural Design Document (60 points)

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

To begin with, you should first evaluate the model's performance. You are provided with a test dataset, which contains a similar set of features and output (whether the student is a good candidate or not). This test dataset is a different set of students from the training dataset, and the evaluation of whether the student is a good candidate **is done by a fair panel of recruiters, so it can be considered to be fair and unbiased.** Additionally, the panel of recruiters have provided you with **additional context on the extracurricular activities in comments #**

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
2. Plot the distribution of the test dataset across all features (except Student ID) using any visualization library of your choice (e.g. matplotlib, seaborn, plotly, etc.). You should choose the appropriate visualization for each feature.
3. Predict the output of the test dataset using the model
4. Report the accuracy of the model, and the confusion matrix

Refer to the Resources section if you need help with any of the above steps.

By the checkpoint deadline, your team will submit a link to the Jupyter notebook with the basis analysis and usage of the model done.
## Final Deliverables

### Feature Integration Implementation (40 points)

### Evaluation Report (60 points)

## Grading
To receive full credit for this project, you must meet the following requirements:

## Resource & Documentation