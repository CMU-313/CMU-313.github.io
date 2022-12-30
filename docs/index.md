---
title: "CMU 17-313: Foundations of Software Engineering"
hide:
    - navigation
---

# 17-313 Foundations of Software Engineering
## Spring 2023
Previous versions of the course: [F20](/_old/2020), [F21](/_old/2021), [F22](/_old/F22)

## Class Calendar

<iframe src="https://calendar.google.com/calendar/embed?src=c_mfu3uiuq0fktl6tmvanaoejeeg%40group.calendar.google.com&ctz=America%2FNew_York&mode=WEEK" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>

## Weekly Schedule

<div id="schedule" markdown>

<!-- Loading in schedule from schedule.yaml -->
{%- set schedule = extra.schedule -%}

{% if schedule %}
{% set ns = namespace(recitation_days_left=0, homework_days_left=0) %}
<table style="border-collapse: collapse; font-size:90%;">
    <thead>
        <th><b>Date</b></th>
        <th><b>Lecture</b></th>
        <th><b>Recitation</b></th>
        <th><b>Reading</b></th>
        <th><b>Homework Deadline</b></th>
    </thead>
    <tbody>
        {% for schedule_day in schedule %}
        <tr>
            <td style="position: relative;"><span class="schedule-day">{{schedule_day.date}}</span></td>

            <td><span class="schedule-lecture">
                {% if schedule_day.lecture.name != "" %}
                    <a class="label label-gold" href="{{schedule_day.lecture.link}}">
                        {{schedule_day.lecture.name}}
                    </a>
                {% endif %}
            </span></td>

            {% if schedule_day.recitation.name != "" %} 
                <td rowspan="5"><span class="schedule-recitation">
                    <b>{{schedule_day.recitation.name}}</b>
                    <br/>

                    <a class="label label-aqua" href="{{schedule_day.recitation.slides}}">
                        <span class="material-symbols-outlined">slideshow</span> Slides
                    </a>

                    <a class="label label-aqua" href="{{schedule_day.recitation.handout}}">
                        <span class="material-symbols-outlined">description</span> Handout
                    </a>

                    <a class="label label-aqua" href="{{schedule_day.recitation.quiz}}">
                        <span class="material-symbols-outlined">equalizer</span> Quiz
                    </a>
                </span></td>
                {% set ns.recitation_days_left = 4 %}
            {% else %}
                {% if ns.recitation_days_left > 0 %}
                    {% set ns.recitation_days_left = ns.recitation_days_left - 1 %}
                {% else %}
                    <td><span class="schedule-recitation"></span></td>
                {% endif %}
            {% endif %}

            <td><span class="schedule-reading">
                {% if schedule_day.reading.name != "" %}
                    <a class="label label-blue" href="{{schedule_day.reading.link}}">
                        {{schedule_day.reading.name}}
                    </a>
                {% endif %}
            </span></td>

            {% if schedule_day.homework.name != "" %} 
                <td rowspan="{{schedule_day.homework.numDays}}"><span class="schedule-homework">
                    <b>{{schedule_day.homework.name}}</b>
                    <br/>
                    {{schedule_day.homework.deadline}}
                    <br/>
                    <a class="label label-red" href="{{schedule_day.homework.link}}">
                        <span class="material-symbols-outlined">description</span> Handout
                    </a>
                </span></td> 
                {% set ns.homework_days_left = schedule_day.homework.numDays - 1 %}
            {% else %}
                {% if ns.homework_days_left > 0 %}
                    {% set ns.homework_days_left = ns.homework_days_left - 1 %}
                {% else %}
                    <td><span class="schedule-homework"></span></td>
                {% endif %}
            {% endif %}
        </tr>
        {% endfor %}
    </tbody>
</table>

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
