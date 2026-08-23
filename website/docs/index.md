---
title: "CMU 17-313: Foundations of Software Engineering"
hide:
  - navigation
---

# 17-313 Foundations of Software Engineering

## Class Calendar

<iframe src="https://calendar.google.com/calendar/embed?src=c_7faee93d8ab8b1502e08769d87482816823afd63153be61d111ec8356e3ed185%40group.calendar.google.com&ctz=America%2FNew_York" style="border: 0" width="800" height="600" frameborder="0" scrolling="no"></iframe>

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
