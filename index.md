---
layout: home
title: "CMU 17-313: Foundations of Software Engineering"
nav_exclude: true
seo:
  type: Course
  name: Just the Class
---

# {{ site.tagline }}
{: .mb-2 }
{{ site.description }}
{: .fs-6 .fw-300 }
<!-- 
{% if site.announcements %}
{{ site.announcements.last }}
[Announcements](announcements.md){: .btn .btn-outline .fs-3 }
{% endif %} -->

Previous versions of the class website are archived here: [F20](/2020), [F21](/2021)

## Questions

- When is a program good enough to ship? Have you built what the customer wanted?
- Why (and how) does Netflix deliberately and randomly take down its own servers?
- What can we learn from the Boeing 737 disaster?
- How did Twitter eradicate the Fail Whale? And what does it have to do with Ruby?
- How do you get a patch accepted into an open-source project?
- You can write code. Can you build software?




## Overview
Successful software projects require more than just technical expertise. Figuring out what the client wants, collaborating in a team, managing complexity, mitigating risks, staying on time and budget, and determining under various constraints when a product is good enough to be shipped are at least equally important topics that often have a significant human component. 17-313 explores these issues broadly covering the fundamentals of modern software engineering.

Assuming reasonably solid programming skills (including unit testing and code-level design), we will explore the following topics:

- **Process consideration for software development**
(How do avoid problems early? When and how much to design? When and how much to test? When and how to involve the customers? Agile methods...)

- **Requirements elicitation, documentation, and evaluation**
(How to figure out what the customer really wants? Who else has an interest? How can we measure success objectively? How can we reliably document expectations? ...)
- **Design for quality attributes**
(How can we design a system to be able to scale to millions of users? How can we design security into a system? ...)
- **Strategies for quality assurance,** including measurement, inspection, and static and dynamic analysis(What quality assurance strategy is best for a given system? What can we automate and when should we keep humans in the loop? How much testing and what kind of testing should we do? What qualities are important to assure beyond functional correctness? Can we evaluate usability, scalability, reliability, performance? How can we statically guarantee the absence of certain security issues? ...)
- **Empirical methods in software engineering**
(How can we measure quality attributes such as performance, security, and reliability? How can we measure how users interact with the system? How can we know whether the difference matters? ...)
- **Time and team management**
(How to estimate the duration and costs of a project? How to monitor progress and risks to recognize issues early? How to coordinate developers in a team? How to form and develop teams? How to select and motivate team members? How to deal with team dynamics such as social loafing? ...)
- **Economics of software development**
(business models, outsourcing, open source, ...)


This course has a strong technical focus, and includes assignments with and without programming. Assignments also include written components. Students will get experience with team management and modern software-engineering tools. The course puts students on a fast track toward project management positions.

Assignments (mostly done in groups) include:

- An introduction assignment where individual students will learn to engage with an existing code base.
- A requirements assignment in which each team will interview stakeholders to elicit and document requirements for a software system.
- An architecture assignment in which teams will train and deploy an ML model using microservices.
- A project in which each team contributes to an open source project of their choice. This involves identifying an issue in the existing project, understanding the development process of that project and how to contribute, and actually making a contribution such as fixing a bug or adding a feature. Extra credit will be awarded if the contribution is merged into the project.



<!-- ## Just the Class

Just the Class is a GitHub Pages template developed for the purpose of quickly deploying course websites. In addition to serving plain web pages and files, it provides a boilerplate for:

- a [course calendar](calendar.md),
- a [staff](staff.md) page,
- and a weekly [schedule](schedule.md).

Just the Class is built on top of [Just the Docs](https://github.com/pmarsceill/just-the-docs), making it easy to extend for your own special use cases while providing sane defaults for most everything else. This means that you also get:

- automatic [navigation structure](https://pmarsceill.github.io/just-the-docs/docs/navigation-structure/),
- instant, full-text [search](https://pmarsceill.github.io/just-the-docs/docs/search/) and page indexing,
- and a small but powerful set of [UI components](https://pmarsceill.github.io/just-the-docs/docs/ui-components) and authoring [utilities](https://pmarsceill.github.io/just-the-docs/docs/utilities).

## Getting Started

Getting started with Just the Class is simple.

1. Create a [new repository based on Just the Class](https://github.com/kevinlin1/just-the-class/generate).
1. Update `_config.yml` and `index.md` with your course information.
1. Configure a [publishing source for GitHub Pages](https://help.github.com/en/articles/configuring-a-publishing-source-for-github-pages). Your course website is now live!
1. Edit and create `.md` [Markdown files](https://guides.github.com/features/mastering-markdown/) to add your content.

For a few open-source examples, see the following course websites and their source code.

- [CSE 390HA](https://courses.cs.washington.edu/courses/cse390ha/20au/) ([source code](https://gitlab.cs.washington.edu/cse390ha/20au/website)) is an example of a single-page website that centers modules.
- [CSE 143](https://courses.cs.washington.edu/courses/cse143/20au/) ([source code](https://gitlab.cs.washington.edu/cse143/20au/website)) hosts an entire online textbook with full-text search.
- [CSE 373](https://courses.cs.washington.edu/courses/cse373/21su/) ([source code](https://gitlab.cs.washington.edu/cse373-root/21su/website) is an example of a simple website combining Markdown pages with generated HTML files.

Share your website with us in the [show and tell discussion](https://github.com/kevinlin1/just-the-class/discussions/categories/show-and-tell)!

Continue reading to learn how to setup a development environment on your local computer. This allows you to make incremental changes without directly modifying the live website.

### Local development environment

Just the Class is built for [Jekyll](https://jekyllrb.com), a static site generator. View the [quick start guide](https://jekyllrb.com/docs/) for more information. Just the Docs requires no special Jekyll plugins and can run on GitHub Pages' standard Jekyll compiler.

1. Follow the GitHub documentation for [Setting up your GitHub Pages site locally with Jekyll](https://help.github.com/en/articles/setting-up-your-github-pages-site-locally-with-jekyll).
1. Start your local Jekyll server.
```bash
$ bundle exec jekyll serve
```
1. Point your web browser to [http://localhost:4000](http://localhost:4000)
1. Reload your web browser after making a change to preview its effect.

For more information, refer to [Just the Docs](https://pmarsceill.github.io/just-the-docs/). -->
