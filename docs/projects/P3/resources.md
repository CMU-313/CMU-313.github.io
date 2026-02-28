## Resources & Documentation

### Starter List of Tools

NodeBB is built in Javascript/Typescript using Node.js and uses Benchpress for its frontend templating. Below are non-exhaustive lists of analysis tools that are available.

For other resources, [Software Testing Magazine - Open Source JavaScript Code Analysis](https://www.softwaretestingmagazine.com/tools/open-source-javascript-code-analysis/), [Awesome Static Analysis page](https://github.com/david-a-wheeler/awesome-static-analysis), and [Awesome Dynamic Analysis page](https://github.com/analysis-tools-dev/dynamic-analysis) have extensive listings of available static and dynamic analysis tools for a pretty hefty list of programming languages.

Some of the tools already have existing GitHub Actions workflows on GitHub Marketplace; use your Googling skills, and see what you find!

#### Static Tools

- [flow](https://flow.org/): Static type checker for JavaScript
- [jshint](https://jshint.com/docs/): Used to flag suspicious usage in JavaScript programs
- [StandardJS](https://standardjs.com/)/[ts-standard](https://github.com/standard/ts-standard): Static analysis tool for code quality within JavaScript/TypeScript projects
- [Retire.js](https://retirejs.github.io/retire.js/): Finds library/node module vulnerabilities within your project

#### Dynamic Tools

- [Jalangi](https://github.com/Samsung/jalangi2): Framework for dynamic analyses in JavaScript
- [Fast-Fuzz](https://www.npmjs.com/package/fast-fuzz): Fuzzing framework for TypeScript
- [Stryker Mutator](https://stryker-mutator.io/): Mutation testing tool for JavaScript
- [k6](https://github.com/grafana/k6): Open source tool for load testing
