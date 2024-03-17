---
title: Recitation 7 - Large Language Models
---
# Recitation 7: Large Language Models

## Overview 

During this recitation, students will be able to run and evaluate a large language model on an example question/answer dataset. This is an individual activity so everyone should be running the notebook; however, feel free to discuss the activity and your approach with other students!

## Setup Instructions (5 min)
For this recitation, you'll be using Google's Vertex AI Platform in a Colab notebook to query a large language model on a question/answer dataset. First, we need to set up our GCP project to enable the API and create a copy of the Colab notebook.
Note: if you have not yet created a GCP project and redeemed your credits, please refer to the instructions in Task 1B of [Recitation 6](https://cmu-313.github.io/recitations/reci6-deployment/). 

1.  Enable the Vertex AI API using [this link](https://console.cloud.google.com/flows/enableapi?apiid=aiplatform.googleapis.com). Make sure your NodeBB project from P3 or the basic web app from Recitation 6 is selected in the project selector dropdown.
    
2.  Open the Colab notebook using [this link](https://colab.research.google.com/drive/1KKD9nQV_Ahm-XUNSViMlwspU_BqTRSgI?usp=sharing). Click on File --> Save as a copy in Drive to create your own copy that you will work on.
    
3.  Click on Share and make sure the Colab notebook is editable by anyone in Carnegie Mellon University. You will submit a link to this notebook for Gradescope.

## Activity 0: Install Dependencies and Authenticate GCP (5 min)

Run the first cell of the notebook to install any Python dependencies. Follow the rest of the instructions in the notebook to authenticate GCP.

## Activity 1: Examine the Stanford Question Answering (SQuAD) Dataset (10 mins)

The dataset contains a set of questions and answers to test a system for reading comprehension. Load in the dataset and understand the format.

For one example, print out the context, question, and expected answer.

## Activity 2: Use the Vertex AI API to query the chat-bison LLM (10 min)

Now that we have loaded the dataset, let's try querying an LLM to answer one of the questions. Refer to the [Vertex Python SDK docs](https://cloud.google.com/vertex-ai/docs/generative-ai/chat/test-chat-prompts#chat-query-python_vertex_ai_sdk) to load and query the model. For this exercise, choose the "**chat-bison@001**" model. 

Try running the model on one of the examples from the SQuAD dataset. Does the output match the expected answer?

## Activity 3: Check Correctness of Output (10 min)

When using an LLM, it is important to design an evaluation strategy for the task. This involves choosing a method of evaluating the correctness of the LLM output. Since the output in our task is textual, there are many difference ways of checking similarity to an expected answer. For now we will proceed with simply taking the percent of correct asnwers given by the LLM.

Follow the notebook instructions to calculate cosine similarity for a sample of 10 questions. What are some limitations with this metric? Are there ways of changing the prompt to make the outputs better?

Once you are done, submit the link to your Colab notebook to gradescope at [this link](https://www.gradescope.com/courses/583198/assignments/3599220/).
