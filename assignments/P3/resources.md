---
title: "Resources & Documentation"
nav_order: 40
---

## Resources & Documentation

### Starter List of Tools

opencode is built in TypeScript, using Bun as its runtime, package manager, and test runner. Below are non-exhaustive lists of checks that are available, organized by the categories your team's [CI/CD Pipeline Design Document](1_checkpoint.md#cicd-pipeline-design-document-group-15-pts) needs to cover.

For other resources, [Software Testing Magazine - Open Source JavaScript Code Analysis](https://www.softwaretestingmagazine.com/tools/open-source-javascript-code-analysis/), [Awesome Static Analysis page](https://github.com/david-a-wheeler/awesome-static-analysis), and [Awesome Dynamic Analysis page](https://github.com/analysis-tools-dev/dynamic-analysis) have extensive listings of available static and dynamic analysis tools for a pretty hefty list of programming languages.

Some of the tools already have existing GitHub Actions workflows on GitHub Marketplace; use your Googling skills, and see what you find!

#### Code Quality / Static Analysis

- [flow](https://flow.org/): Static type checker for JavaScript
- [jshint](https://jshint.com/docs/): Used to flag suspicious usage in JavaScript programs
- [StandardJS](https://standardjs.com/)/[ts-standard](https://github.com/standard/ts-standard): Static analysis tool for code quality within JavaScript/TypeScript projects

#### Testing / Dynamic Analysis

- [Jalangi](https://github.com/Samsung/jalangi2): Framework for dynamic analyses in JavaScript
- [Fast-Fuzz](https://www.npmjs.com/package/fast-fuzz): Fuzzing framework for TypeScript
- [Stryker Mutator](https://stryker-mutator.io/): Mutation testing tool for JavaScript
- [k6](https://github.com/grafana/k6): Open source tool for load testing

#### Security / Dependency Scanning

- [Retire.js](https://retirejs.github.io/retire.js/): Finds library/dependency vulnerabilities within your project

!!! note "Already in use"
    opencode's own pipeline already runs [Qlty](https://qlty.sh/) for static analysis (you used it in Project 1). Pick something that adds new coverage rather than overlapping with it.
