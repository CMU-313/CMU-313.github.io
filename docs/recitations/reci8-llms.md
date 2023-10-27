---
title: Recitation 8 - Large Language Models
---
# Recitation 8: Large Language Models

## Setup Instructions (10 min)
For this recitation and Project 4, you'll be using Google's Vertex AI Platform in a Jupyter notebook to query a large language model. First, we need to set up our GCP project to enable the API and install the prerequisites to run the notebook. 

1.  Enable the Vertex AI API using [this link](https://console.cloud.google.com/flows/enableapi?apiid=aiplatform.googleapis.com). Make sure your NodeBB project from P3 is selected in the project selector dropdown.
    
2.  Install JupyterLab for Python following the instructions in [this link](https://jupyter.org/install).
    
3.  Install the gcloud CLI following the instructions in [this link](https://cloud.google.com/sdk/docs/install).
    
4.  In your terminal, run `gcloud auth application-default login` and open the authentication URL that is displayed. Choose the account linked to the NodeBB project, and copy the verification code and paste it into the terminal.
    
5.  In your terminal, run `gcloud config set project PROJECT_ID`, where the `PROJECT_ID` is the ID of your NodeBB project. You can find this by going to [https://console.cloud.google.com](https://console.cloud.google.com), selecting the NodeBB project
from the dropdown, and copying the Project ID.

## Overview

During this recitation, students will able to run and evaluate a large language model on an example dataset. This is an individual activity so everyone should be running the notebook; however, feel free to discuss the activity and your approach with other students!

## Activity 0: Running the Notebook and Installing Dependencies (5 min)

Download and run the notebook from [this repository](https://github.com/CMU-313/fa23-recitation-8) and run the first cell of the Jupyter notebook to install any Python dependencies and load in the dataset.

## Activity 1: Examine the Stanford Question Answering (SQuAD) Dataset (10 mins)

The dataset contains a set of questions and answers to test a system for reading comprehension. Load in the dataset and understand the format.

For one example, print out the context, question, and expected answer.

## Activity 2: Use the Vertex AI API to query the chat-bison LLM (5 min)

Now that we have loaded the dataset, let's try querying an LLM to answer one of the questions. Refer to the [Vertex Python SDK docs](https://cloud.google.com/vertex-ai/docs/generative-ai/chat/test-chat-prompts#chat-query-python_vertex_ai_sdk) to load and query the model. For this exercise, choose the "**chat-bison@001**" model. 

Try running the model on one of the examples from the SQuAD dataset. Does the output match the expected answer?

## Activity 3: Check Correctness of Output (5 min)

When using an LLM, it is important to design an evaluation strategy for the task. This involves choosing a method of evaluating the correctness of the LLM output. Since the output in our task is textual, we can choose from the many difference ways of checking similarity to an expected answer. For this recitation, we will simply use an exact string match. However, we urge you to explore other techniques for Project 4. 

Sample 10 data points from the dataset and evaluate the accuracy of the LLM on those questions. What are some limitations with this metric? Are there ways of changing the prompt to make the outputs better?
