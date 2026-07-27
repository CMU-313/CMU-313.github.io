---
title: Recitations
hide:
- navigation
- toc
---

<div class="lab-index-intro">
  <p>Labs are designed to give you practice with the tools used to build, secure, deploy, and operate software in the real world.
  Each session prepares you for the following week's assignment, so you can apply its techniques with confidence when the work expands.</p>
</div>

<div class="lab-index-grid">
{% for lab in released_labs(schedule) %}
  <article class="lab-index-card">
    <div class="lab-index-card__header">
      <span class="lab-index-card__eyebrow">Lab {{ '%02d' | format(loop.index) }}</span>
      <span class="lab-index-card__date">{{ lab.date.strftime('%b %-d') }}</span>
    </div>
    <div class="lab-index-card__body">
      <h2><a href="{{ lab.source_file.stem }}/">{{ lab.title }}</a></h2>
      <p class="lab-index-card__summary">{{ lab.description | default('A hands-on session for applying this week\'s DevOps practices.') }}</p>
      <dl class="lab-index-card__details">
        <div>
          <dt>Lab date</dt>
          <dd>{{ lab.date.strftime('%b %-d, %Y') }}</dd>
        </div>
        <div>
          <dt>Tools</dt>
          <dd>{% if lab.card.tags %}{{ lab.card.tags | join(' · ') }}{% else %}To be announced{% endif %}</dd>
        </div>
      </dl>
      <a class="lab-index-card__link" href="{{ lab.source_file.stem }}/">Open lab <span aria-hidden="true">→</span></a>
    </div>
  </article>
{% endfor %}
</div>
