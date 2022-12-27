---
title: "CMU 17-313: Foundations of Software Engineering"
hide:
    - navigation
---

# Foundations of Software Engineering
Previous versions of the course website: [F20](/_old/2020), [F21](/_old/2021), [F22](/_old/F22)

## Overarching Questions

- When is a program good enough to ship? Have you built what the customer wanted?
- Why (and how) does Netflix deliberately and randomly take down its own servers?
- What can we learn from the Boeing 737 disaster?
- How did Twitter eradicate the Fail Whale? And what does it have to do with Ruby?
- How do you get a patch accepted into an open-source project?
- You can write code. Can you build software?

## Overview
Successful software projects require more than just technical expertise. Figuring out what the client wants, collaborating in a team, managing complexity, mitigating risks, staying on time and budget, and determining under various constraints when a product is good enough to be shipped are at least equally important topics that often have a significant human component. 17-313 explores these issues while broadly covering the fundamentals of modern software engineering.

Assuming reasonably solid programming skills (including unit testing and code-level design), we will explore the following topics:

- **Process consideration for software development**  
(How do avoid problems early? When and how much to design? When and how much to test? When and how to involve the customers? Agile methods...)
- **Requirements elicitation, documentation, and evaluation**  
(How to figure out what the customer really wants? Who else has an interest? How can we measure success objectively? How can we reliably document expectations? ...)
- **Design for quality attributes**  
(How can we design a system to be able to scale to millions of users? How can we design security into a system? ...)
- **Strategies for quality assurance,** including measurement, inspection, and static and dynamic analysis  
(What quality assurance strategy is best for a given system? What can we automate and when should we keep humans in the loop? How much testing and what kind of testing should we do? What qualities are important to assure beyond functional correctness? Can we evaluate usability, scalability, reliability, performance? How can we statically guarantee the absence of certain security issues? ...)
- **Empirical methods in software engineering**  
(How can we measure quality attributes such as performance, security, and reliability? How can we measure how users interact with the system? How can we know whether the difference matters? ...)
- **Time and team management**  
(How to estimate the duration and costs of a project? How to monitor progress and risks to recognize issues early? How to coordinate developers in a team? How to form and develop teams? How to select and motivate team members? How to deal with team dynamics such as social loafing? ...)
- **Economics of software development**  
(Business models, outsourcing, open source, ...)


This course has a strong technical focus, and includes assignments with and without programming. Many assignments will also have written components. Students will get experience with team management and modern software-engineering tools. The course puts students on a fast track toward project management positions. 

**Assignments** (mostly done in groups) include:

- An **introduction** assignment where individual students will learn to engage with an existing code base.
- A **requirements** assignment in which each team will interview stakeholders to elicit and document requirements for a software system.
- An **architecture** assignment in which teams will train and deploy an ML model using microservices.
- A project in which each team **contributes to an open source project** of their choice. This involves identifying an issue in the existing project, understanding the development process of that project and how to contribute, and actually making a contribution such as fixing a bug or adding a feature. Extra credit will be awarded if the contribution is merged into the project.

## Class Calendar

<iframe src="https://calendar.google.com/calendar/embed?src=c_mfu3uiuq0fktl6tmvanaoejeeg%40group.calendar.google.com&ctz=America%2FNew_York&mode=WEEK" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>

## Weekly Schedule

<div id="schedule" markdown>

<!-- Loading in schedule from schedule.yaml -->
{%- set schedule = extra.schedule -%}
{% if schedule %}

| Date         | Lecture | Recitation | Reading | Homework Deadline |
| ------------ | ------- | ---------- | ------- | ----------------- |
{% for schedule_day in schedule %}| {{schedule_day.date}} | {% if schedule_day.lecture.name != "" %} **[{{schedule_day.lecture.name}}]({{schedule_day.lecture.link}})**{: .label .label-gold } {% endif %} {% if schedule_day.recitation.name != "" %} <td rowspan="5"> **{{schedule_day.recitation.name}}** <br> **[:material-play-box: Slides]({{schedule_day.recitation.slides}})**{: .label .label-aqua } **[:material-file-document: Handout]({{schedule_day.recitation.handout}})**{: .label .label-aqua }**[:material-equalizer: Quiz]({{schedule_day.recitation.quiz}})**{: .label .label-aqua }</td> {% endif %} | {% if schedule_day.reading.name != "" %} **[{{schedule_day.reading.name}}]({{schedule_day.reading.link}})**{: .label .label-blue} {% endif %} {% if schedule_day.homework.name != "" %} <td rowspan="{{schedule_day.homework.numDays}}"> **{{schedule_day.homework.name}}** <br> {{schedule_day.homework.deadline}} <br> **[:material-file-document: Handout]({{schedule_day.homework.link}})**{: .label .label-red } </td> {% endif %}
{% endfor %}

{% else %}
Coming Soon!
{% endif %}

</div>

## Staff
### Instructors
{%- set instructors = extra.staff | selectattr("role", "==", "Instructor") | list -%}

{% for instructor in instructors %}
<div class="staffer card"> 
    <div class="container">
        <img class="staffer-image" src="/assets/images/{{instructor.photo}}" alt="">
        <div>
            <h3 class="staffer-name"> 
                {{instructor.name}}
            </h3>
            <p>
                <a href="mailto:{{instructor.email}}">
                    <span class="material-symbols-outlined">
                        mail
                    </span>
                </a>
                {% if instructor.website %}
                <a href="{{instructor.website}}">
                    <span class="material-symbols-outlined">
                        public
                    </span>
                </a>
                {% endif %}
            </p>
        </div>
    </div>
</div>
{% endfor %}

{%- set assistants = extra.staff | selectattr("role", "==", "Teaching Assistant") | list -%}
{%- set num_teaching_assistants = assistants | count -%}

{% if num_teaching_assistants > 0 %}
### Teaching Assistants
{% for assistant in assistants %}
<div class="staffer card"> 
    <div class="container">
        <img class="staffer-image" src="/assets/images/{{assistant.photo}}" alt="">
        <div>
            <h3 class="staffer-name"> 
                {{assistant.name}}
            </h3>
            <p>
                <a href="mailto:{{assistant.email}}">
                    <span class="material-symbols-outlined">
                        mail
                    </span>
                </a>
                {% if assistant.website %}
                <a href="{{assistant.website}}">
                    <span class="material-symbols-outlined">
                        public
                    </span>
                </a>
                {% endif %}
            </p>
        </div>
    </div>
</div>
{% endfor %}
{% endif %}
