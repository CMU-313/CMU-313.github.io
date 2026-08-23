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
{% for recitation in released_recitations(schedule) %}
  <article class="lab-index-card">
    <div class="lab-index-card__header">
      <span class="lab-index-card__eyebrow">Recitation {{ '%02d' | format(loop.index) }}</span>
      <span class="lab-index-card__date">{{ recitation.date.strftime('%b %-d') }}</span>
    </div>
    <div class="lab-index-card__body">
      <h2><a href="{{ recitation.source_file.stem }}/">{{ recitation.title }}</a></h2>
      <p class="lab-index-card__summary">{{ recitation.description | default('A hands-on session for applying this week\'s DevOps practices.') }}</p>
      <dl class="lab-index-card__details">
        <div>
          <dt>Recitation date</dt>
          <dd>{{ recitation.date.strftime('%b %-d, %Y') }}</dd>
        </div>
        <div>
          <dt>Tools</dt>
          <dd>{% if recitation.card.tags %}{{ recitation.card.tags | join(' · ') }}{% else %}To be announced{% endif %}</dd>
        </div>
      </dl>
      <a class="lab-index-card__link" href="{{ recitation.source_file.stem }}/">Open recitation <span aria-hidden="true">→</span></a>
    </div>
  </article>
{% endfor %}
</div>
