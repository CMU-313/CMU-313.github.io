---
title: Recitation 9 - Machine Learning
---


# Recitation 9:  Machine Learning


## Setup Instructions: 
1. Go to this [repo](https://github.com/CMU-313/s23-ml-recitation) and clone it 
2. Make sure you can run the jupyter notebooks 
    1. [Google Colab](https://githubtocolab.com/CMU-313/s23-ml-recitation/blob/main/model_testing.ipynb) is one option to do this (NOTE: you should be able to do this by adding tocolab to the github url for the model_testing notebook)
        1. Make sure to connect to google drive and upload the titanic data set folder, double check the file paths in the notebook to make sure they match
    2. You can also run it locally if you have jupyter setup


## Overview
During this recitation, students will have the opportunity to play with various machine learning frameworks and tools and justify a recommendation argument for using a machine learning model in practice. This is an individual activity so everyone should be running the notebook; however, feel free to discuss the activity and your approach with other students!


## Context
We can use the Titanic dataset to make predictions on whether or not passengers would survive given features in the dataset. We trained two models on the data: one that uses sex as a feature and one that does not. You’ll be working with the starter code in model_testing.ipynb.


## Activity 1: Examine the Titanic Dataset (10 mins)
1. The dataset contains detailed information on the passengers aboard the Titanic. Go through the first part of the testing notebook.
2. Then choose one feature and plot its distribution.
1. Is the distribution what you expected it to be? Was there anything surprising about it?


## Activity 2: Import and Analyze Models (5 min)
We pre-trained two models based on the Titanic training dataset. Let's import these models and review their accuracy. Note that the difference between the models is one uses sex as a feature and one does not. Run the cells in this section.

## Activity 3: Fairness Metrics Evaluation (15 mins)
An important part of evaluating an ML model is assessing its fairness. In this activity, evaluate the fairness metrics that we discussed in class with respect to sex and pclass. 
1. Fill in the notebook to compute the demographic parity metric
2. Fill in the notebook to compute the equal opportunity metric
3. Feel free to evaluate and compute any other metrics that you think would be helpful to evaluate the model. One to consider is true and false positive rates and/or true and false negative rates.


## Activity 4: Recommendation (10 mins)
Based on the analysis and evaluations we've done above (both fairness and accuracy), would you recommend that one of these models is used in practice (i.e. in a situation where the model could be used to determine who is prioritized for safety in a similar situation)


Justify your choice with evidence that you produced in previous activities. Feel free to write directly in the jupyter notebook and then add your answer to the gradescope quiz.