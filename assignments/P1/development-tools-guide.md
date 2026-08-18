---
title: "Development Tools Guide"
nav_order: 30
release_date: 2026-01-01
---

# Development Tools & Concepts Guide

## Overview

This guide explains the fundamental tools and concepts you'll encounter in Project 1. Understanding these technologies will help you succeed not just in this assignment, but throughout your software engineering career.

!!! info "Learning Goals"
    By the end of this guide, you should understand:
    
    - What each tool does and why we use it
    - How the tools work together in a development workflow
    - The benefits of modern development practices
    - Common terminology used in software engineering

## Core Technologies

### Docker

**What it is**: Docker creates "containers" - lightweight, portable environments that package your application with all its dependencies.

**Think of it like**: Shipping containers that work the same way on any truck, train, or ship. A Docker container runs the same way on any computer.

**Why we use it**: 

- **Consistency**: Everyone runs the exact same environment
- **Isolation**: Your project won't conflict with other software on your machine
- **Reproducibility**: Eliminates "it works on my machine" problems
- **Easy setup**: Pre-configured with all necessary tools

**Example**: Instead of manually installing Node.js, Redis, and configuring everything, Docker gives you a pre-built environment ready to go.

### Dev Containers

**What it is**: A VS Code extension that uses Docker to create development environments automatically.

**How it works**: When you open a project with a `.devcontainer` folder, VS Code asks if you want to "Reopen in Container" - this builds and launches a Docker container with all development tools pre-installed.

**Benefits**:

- **Zero manual setup**: No need to install Node.js, databases, or other dependencies
- **Identical environments**: Everyone in the class has the exact same setup
- **Fast onboarding**: Get coding in minutes, not hours
- **Consistent experience**: Course staff can better help you since we all use the same environment

**Workflow**: 

1. Clone repository
2. Open in VS Code
3. Click "Reopen in Container"
4. Start coding!

### VS Code

**What it is**: A popular code editor (like Microsoft Word, but designed for writing code).

**Key features**:

- **Syntax highlighting**: Colors code to make it easier to read
- **IntelliSense**: Auto-completion and error detection
- **Integrated terminal**: Command line built right into the editor
- **Extensions**: Add functionality like Dev Containers, Git tools, etc.
- **Debugging**: Step through code to find and fix bugs

**Why developers love it**: Free, fast, powerful, and works with almost any programming language.

## Project Codebase

### opencode

**What it is**: [opencode](https://github.com/cmu-313/opencode) is an open source AI coding agent, built with a terminal UI for driving development work. It ships with a "build" agent (full access, for making changes) and a "plan" agent (read-only, for exploration and analysis).

**Built with**: TypeScript, running on Bun (this course's fork uses Bun as the runtime/package manager).

**Why we chose it**: Real-world, actively maintained open source project with complex features that demonstrate software engineering challenges.

!!! warning "TBD: opencode migration"
    This section previously described NodeBB (forum software). The framing above reflects opencode's actual README, but hasn't been reviewed against the CMU-313 fork specifically.

### Bun

**Bun**: JavaScript/TypeScript runtime and package manager (this project's equivalent of Node.js + npm).

**Common commands** (see [Project 1A](1_checkpoint.md) for the full list):

- `bun install` - Downloads all packages your project needs
- `bun dev` - Runs the app
- `bun lint` - Runs the linter
- `bun test` - Runs the test suite

### Localhost and Ports

**Localhost**: Your own computer acting as a web server.

- **Port numbers**: Like apartment numbers - different services use different ports

!!! warning "TBD: opencode migration"
    This section previously documented NodeBB's default port (4567). opencode's TUI doesn't run as a traditional localhost web server in the same way — needs a rewrite once we confirm what (if anything) this applies to for the CMU-313 fork.

**Why localhost**: Lets you test your application privately before sharing it with the world.

## Quality Assurance Tools

### Linting

**What it is**: A tool that analyzes your code for style issues and potential errors.

**Like**: Grammar and spell-check for code.

**What it catches**:

- Missing semicolons
- Unused variables
- Inconsistent formatting (spaces vs tabs)
- Potential logic errors
- Style guide violations

**Example**: 
```javascript
// Linter would flag these issues:
var unusedVariable = 'hello'  // unused variable
console.log( 'world' )        // inconsistent spacing
```

**Why important**: Keeps code clean, readable, and consistent across team members.

**Command**: `bun lint`

### Testing

**What it is**: Automated checks that verify your code works correctly.

**Types**:

- **Unit tests**: Test individual functions in isolation
- **Integration tests**: Test how different parts work together
- **End-to-end tests**: Test the entire application flow

**Example**:
```javascript
// A simple test
test('addition works correctly', () => {
  expect(2 + 2).toBe(4);
});
```

**Why crucial**: 

- **Catch bugs early**: Before users encounter them
- **Prevent regressions**: Ensure new changes don't break existing features
- **Enable refactoring**: Safely improve code knowing tests will catch mistakes

**Command**: `bun test`

### Code Coverage

**What it is**: Measurement of what percentage of your code is executed by tests.

**Coverage report**: Visual display showing:

- **Green lines**: Covered by tests
- **Red lines**: Not covered by tests
- **Percentage**: Overall coverage score

**Good coverage**: Generally 70-90% for most projects (opencode should show high coverage).

**Why it matters**: Higher coverage = more confidence that your code works correctly.

**Important note**: 100% coverage doesn't mean perfect code - quality of tests matters more than quantity.

## Development Workflow

### Version Control with Git

**Git**: Tool that tracks changes to files over time, like a "save game" system for code.

**Key concepts**:

- **Repository (repo)**: Folder containing all project files + change history
- **Commit**: Snapshot of your code at a specific point in time
- **Branch**: Parallel version of your code for working on features
- **Merge**: Combining changes from different branches

**GitHub**: Website that hosts Git repositories online and adds collaboration features.

!!! info "Detailed Git Commands"
    For a comprehensive reference of Git commands specific to this project, see our [Git Commands Reference Guide](git-commands-reference.md).

### Forking and Cloning

**Forking**: Making your own copy of someone else's repository on GitHub.

- Original repo → Fork to your account → You can make changes safely

**Cloning**: Downloading a repository from GitHub to your computer.

- `git clone <url>` downloads the code so you can work on it locally

**Why fork first**: So you can make changes without affecting the original project.

### Development vs Production Environments

**Development environment**: 

- Where you write and test code
- Usually on `localhost`
- Can break things safely
- Has debugging tools enabled

**Production environment**: 

- Where real users access your application
- Public website with real domain name
- Must be stable and fast
- Has monitoring and security features

**Why separate**: You can experiment and make mistakes in development without affecting real users.

## Modern Development Practices

### Containerization Benefits

**Traditional development problems**:

- "It works on my machine" syndrome
- Hours spent configuring environments
- Version conflicts between projects
- Difficult to onboard new team members

**Container solutions**:

- **Consistency**: Same environment for everyone
- **Isolation**: Projects don't interfere with each other
- **Portability**: Works on Windows, Mac, Linux
- **Quick setup**: Ready to code in minutes

### Automated Quality Checks

**Why automate**:

- **Consistency**: Tools don't have "off days" like humans
- **Speed**: Check entire codebase in seconds
- **Catch issues early**: Before they become expensive to fix
- **Enable collaboration**: Maintain code quality as team grows

**Industry standard**: Most professional projects use linting, testing, and continuous integration.

### Real-time Development

**Hot reload**: Changes appear in browser automatically when you save files.

**Live debugging**: See errors and logs in real-time.

**Instant feedback**: Know immediately if something breaks.

**Why it matters**: Faster development cycle means more time for building features, less time waiting.

## Common Issues and Solutions

### Container Problems

**Problem**: "Reopen in Container" option doesn't appear

**Solution**: Ensure `.devcontainer` folder is at project root level

**Problem**: Container build fails

**Solution**: Check Docker is running, try "Dev Containers: Rebuild Container"

### Port Conflicts

**Problem**: `localhost:4567` doesn't work

**Solutions**: 

- Check opencode is running (`bun dev`)
- Try different port in VS Code Ports tab
- Restart container if ports are conflicted

### Test and Lint Failures

**Problem**: Tests fail on first run

**Solution**: Run `bun install` to fetch dependencies

!!! warning "TBD: opencode migration"
    The old NodeBB-specific advice (checking `config.json`) is removed above pending confirmation of what, if anything, opencode needs configured.

**Problem**: Linter shows many errors

**Solution**: This is normal for learning - fix one error at a time, ask for help if overwhelmed

## Connection to Professional Development

### Industry Relevance

These aren't just academic exercises - they're industry standard practices:

- **Docker**: Used by companies like Netflix, Uber, Spotify for deploying applications
- **Testing**: Critical for companies like banks, healthcare, aerospace where bugs have serious consequences
- **Linting**: Standard at Google, Facebook, Microsoft for maintaining code quality
- **CI/CD**: How companies like Amazon deploy code hundreds of times per day safely

### Career Preparation

Understanding these tools prepares you for:

- **Internships**: You'll recognize and use similar tools
- **Job interviews**: Demonstrate knowledge of professional development practices
- **Open source contributions**: Most projects use similar workflows
- **Personal projects**: Build applications the "right way" from the start

## What's Next

Now that you understand these foundational concepts, you're ready to:

1. **Complete the Build Checkpoint**: Set up your environment with confidence
2. **Explore opencode**: Navigate the codebase with better understanding
3. **Use the tools effectively**: Leverage linting, testing, and debugging
4. **Collaborate successfully**: Work with teammates using professional practices

Remember: If any step takes more than a few hours, ask for help! These tools are designed to make development faster and easier, not to create roadblocks.

## Glossary

| Term | Definition |
|------|------------|
| **API** | Application Programming Interface - how different software components communicate |
| **CLI** | Command Line Interface - text-based way to interact with programs |
| **Container** | Packaged application with all its dependencies |
| **Dependency** | External library or package your project needs to function |
| **Environment** | The setup where your code runs (development, testing, production) |
| **Framework** | Pre-built structure that provides common functionality |
| **Full-stack** | Both frontend (user interface) and backend (server) development |
| **Repository** | Storage location for your project files and version history |
| **Runtime** | Environment where your code executes (like Node.js for JavaScript) |
| **Localhost** | Your own computer acting as a server for testing |

---

*This guide was created to help students understand the foundational tools and concepts in modern software development. For additional help, reach out on Slack or during office hours!*