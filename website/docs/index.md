---
title: "CMU 17-313: Foundations of Software Engineering"
hide:
  - navigation
---

# 17-313 Foundations of Software Engineering

## This Week

<div id="this-week">

{%- set this_week = extra.this_week -%}

<div class="card"> 
    <div class="header">
        Lectures & Readings
    </div>
    <div class="content">
        {% if this_week.lectures %}
            {% for lecture in this_week.lectures %}
                <div class="lecture-name">
                    {{ lecture.name }}
                </div>
                <div class="lecture-date">
                    <span class="material-symbols-outlined">calendar_month</span> 
                    {{ lecture.date }}
                </div>

                {% if lecture.link != "" %}
                <a class="label label-gold" href="{{lecture.link}}" target="_blank">
                    <span class="material-symbols-outlined">slideshow</span>
                    Slides
                </a>
                {% endif %}

                {% if lecture.reading %}
                    <a class="label label-blue" href="{{lecture.reading.link}}" target="_blank">
                        <span class="material-symbols-outlined">link</span>
                        {{lecture.reading.name}}
                    </a>
                {% endif %}
                {% if not loop.last %}
                <hr/>
                {% endif %}
            {% endfor %}
        {% else %}
            None!
        {% endif %}
    </div>

</div>

<div class="card"> 
    <div class="header">
        Recitation
    </div>
    <div class="content">
        {% if this_week.recitation %}
            <div class="recitation-name">
                {{ this_week.recitation.name }}
            </div>

            {% if this_week.recitation.slides != "" %}
            <a class="label label-aqua" href="{{this_week.recitation.slides}}" target="_blank">
                <span class="material-symbols-outlined">slideshow</span>Slides
            </a>
            {% endif %}

            {% if this_week.recitation.handout != "" %}
            <a class="label label-aqua" href="{{this_week.recitation.handout}}">
                <span class="material-symbols-outlined">description</span>Handout
            </a>
            {% endif %}

            {% if this_week.recitation.quiz != "" %}
            <a class="label label-aqua" href="{{this_week.recitation.quiz}}" target="_blank">
                <span class="material-symbols-outlined">equalizer</span>Quiz
            </a>
            {% endif %}
        {% else %}
            None!
        {% endif %}
    </div>

    <div class="header">
        Office Hours
    </div>
    <div class="content">
        Held on the first floor lobby of TCS. See <a href="#class-calendar">class calendar</a> below for exact times!
    </div>

</div>

<div class="card"> 
    <div class="header">
        Projects
    </div>
    <div class="content">
        {% if this_week.projects %}
            {% for project in this_week.projects %}
                <div class="homework-name">
                    {{ project.name }}
                </div>

                <div class="homework-date">
                    <span class="material-symbols-outlined">calendar_month</span>
                    Released {{ project.date }}
                </div>

                {% if project.deadline != "" %}
                <div class="homework-date">
                    <span class="material-symbols-outlined">calendar_month</span>
                    {{ project.deadline }}
                </div>
                {% endif %}

                {% if project.link != "" %}
                <a class="label label-red" href="{{project.link}}">
                    <span class="material-symbols-outlined">description</span>Handout
                </a>
                {% endif %}
                {% if not loop.last %}
                <hr/>
                {% endif %}
            {% endfor %}
        {% else %}
            None!
        {% endif %}
    </div>

</div>

</div>

## Class Calendar

<iframe src="https://calendar.google.com/calendar/embed?src=c_6ff178194982fe3e4cba4c28641acbb98c8c493febf2d427b07c4259d3c49a1f%40group.calendar.google.com&ctz=America%2FNew_York&mode=WEEK" style="border: 0" width="1000" height="600" frameborder="0" scrolling="no"></iframe>

## Weekly Schedule
{%- macro render_staffer(person) -%}
<div class="staffer card">
    <div class="container">
        {% if person.photo %}
        <img class="staffer-image" src="/assets/images/{{person.photo}}" alt="">
        {% else %}
        <div class="staffer-image-placeholder"></div>
        {% endif %}
        <div>
            <h3 class="staffer-name">
                {{person.name}}
            </h3>
            <div class="staffer-links">
                <a href="mailto:{{person.email}}"><span class="material-symbols-outlined">
                    mail
                </span></a>
                {% if person.website %}
                <a href="{{person.website}}" target="_blank"><span class="material-symbols-outlined">
                    public
                </span></a>
                {% endif %}
            </div>
        </div>
    </div>
</div>
{%- endmacro -%}


## Schedule

{{ schedule_table(schedule) | safe }}

## Staff

### Instructors

<div id="course-instructors">
{%- set instructors = staff | selectattr("role", "==", "instructor") | list -%}
{% for instructor in instructors %}
{{ render_staffer(instructor) }}
{% endfor %}
</div>

{%- set assistants = staff | selectattr("role", "==", "teaching-assistant") | list -%}

{% if assistants %}

### Teaching Assistants

<div id="course-assistants">
{% for assistant in assistants %}
{{ render_staffer(assistant) }}
{% endfor %}
</div>
{% endif %}
