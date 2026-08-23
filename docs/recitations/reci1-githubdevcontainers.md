---
title: Recitation 1 - GitHub, Dev Containers, and Typescript
---

# Recitation 1: GitHub, Dev Containers, and Typescript - DUE Monday August 24th, 11:59pm

!!! warning "Long Recitation"
    Because this is the first recitation and you are still familiarizing yourself with the development environment you will use this semester, you may find it a bit overwhelming. For this reason, you have until the end of the day to complete it. By completing this recitation, you are essentially getting started with P1.

!!! note "Before You Begin"
    The instructions below are designed to work for most students. However, your operating system or configuration may differ from what we expect, and some commands may not work as described. Do not panic—ask a member of the course staff for help. The purpose of this recitation is to identify and resolve any initial setup problems now so that you do not have to worry about them later in the course.

## Overview

After this recitation, students should be able to set up their development environment, create and clone a GitHub repository, run a TypeScript program, and use a Docker-based development container through Visual Studio Code. These skills will prepare students to work on P1 and other development projects throughout the course.

## Prerequisites

- [x] You have a [GitHub](https://github.com/) account


## Activity 1: Create Your Own GitHub Repository

Create a new GitHub repository using the following settings:

| Setting | Value |
|---|---|
| **Repository name** | `{ANDREW-ID}-17313-reci1` |
| **Visibility** | Public |
| **README** | On |

Then click **Create repository**.

> **Important:** Your repository must remain **public** because you will submit a link to it.


## Activity 2: Install the Required Software

!!! warning "Already Set?"
    If you already have Visual Studio Code and Git installed, you can skip this step.

### Visual Studio Code

Install **Visual Studio Code**:

[Download Visual Studio Code](https://code.visualstudio.com/download?_exp_download=d53503e735)

### Git

Install Git:

[Install Git](https://git-scm.com/install/)

If Visual Studio Code was already open when you installed Git, **restart Visual Studio Code**.

Verify that Git is installed by opening a terminal and running:

```bash
git --version
```

You should see the installed Git version.

### GitHub CLI

Install the **GitHub CLI**. You will use it to authenticate your GitHub account.

[Install GitHub CLI](https://cli.github.com/)

If Visual Studio Code was already open when you installed GitHub CLI, **restart Visual Studio Code**.


## Activity 3: Authenticate GitHub

!!! warning "Already Set?"
    You may already have an authenticated GitHub session if you have used Git in the past. If so, skip this step.

In the VS Code terminal, run:

```bash
gh auth login
```

Follow the prompts and select:

```text
? Where do you use GitHub?
> GitHub.com

? What is your preferred protocol for Git operations on this host?
> HTTPS

? Authenticate Git with your GitHub credentials?
> Yes

? How would you like to authenticate GitHub CLI?
> Login with a web browser
```

Complete the authentication process in your web browser.


## Activity 4: Clone Your Repository

First, navigate to the folder where you want your local repository to live.

You can use the VS Code terminal to navigate to the desired directory:

```bash
cd <path-to-your-folder>
```

On your GitHub repository page, click the green **`<> Code`** button.

Select **HTTPS** and copy your repository URL.

Then clone the repository:

```bash
git clone <repo-URL>
```

For example:

```bash
git clone https://github.com/<your-username>/<your-repository>.git
```


## Activity 5: Open Your Repository in VS Code

Open the repository folder in Visual Studio Code:

**File → Open Folder**

Select the folder that was created when you cloned your repository.

Then open a new terminal:

**Terminal → New Terminal**

You should now be working inside your repository.


## Activity 6: Set Up a Dev Container

Dev Containers allow you to develop inside a consistent, containerized environment. We will discuss containers in more detail later in the course. For now, you should know that Dev Containers simplify the installation and configuration of the development tools required for a project.

In this recitation, we will work with TypeScript, so the Dev Container will provide Node.js and the other tools needed to develop and run the project.

You will need:

1. Docker Desktop
2. The VS Code Dev Containers extension

### Install the Dev Containers Extension

Install the **Dev Containers** extension for Visual Studio Code:

[VS Code Dev Containers Tutorial](https://code.visualstudio.com/docs/devcontainers/tutorial)

### Start Docker Desktop

Open **Docker Desktop** and make sure the Docker engine is running.

Verify Docker from the VS Code terminal:

```bash
docker version
```

You should see information for both the:

- **Client**
- **Server**

If you only see the client or receive an error, make sure Docker Desktop is running before continuing.

---

## Activity 7: Create the Dev Container Configuration

Inside your repository, create a directory named:

```text
.devcontainer
```

!!! note
    Note the . (dot) in front of the directory name

Your repository should now look like:

```text
{ANDREW-ID}-17313-reci1/
├── .devcontainer/
└── README.md
```

Inside `.devcontainer`, create a file named:

```text
devcontainer.json
```

Add the following configuration:

```json
{
  "name": "TypeScript Recitation",
  "image": "node:24-slim"
}
```

Your final structure should be:

```text
{ANDREW-ID}-17313-reci1/
├── .devcontainer/
    └── devcontainer.json
└── README.md
```


## Activity 8: Reopen the Repository in the Dev Container

Open the VS Code Command Palette:

**Ctrl + Shift + P**

Search for:

```text
Reopen in Container
```

and select:

**Dev Containers: Reopen in Container**

VS Code will now reopen your repository inside the Docker container.

> **Note:** The first time you do this, VS Code may take a few moments to download the Node.js image and configure the container.

---

## Activity 9: Test Node.js Inside the Container

Once the container has started, open a new terminal:

**Terminal → New Terminal**

You should now be inside the container.

Run this command:

```bash
node -v
```

Verify that the Node.js installation runs successfully.

```bash
v24.19.0
```

!!! note "What Did You Accomplish?"
    You now have Node.js installed and running inside a container without modifying your local machine's configuration. Everyone who uses this Dev Container will have the same development environment—including the exact same version of Node.js. This is particularly useful when working in a team because it ensures that everyone uses the same development tools and avoids compatibility issues caused by differences in local configurations.

## Activity 10: Translate a simple code into TypeScript

This semester, you will be working on the open-source project opencode. Like
most modern web codebases, opencode is written in TypeScript. Most students
start this course without ever having used TypeScript, because of that, becoming
familiar with TypeScript is a learning goal for this class. Picking up a new
language quickly from documentation, rather than waiting for it to be taught to
you, is itself a skill this course (and most software jobs) will ask of you
repeatedly, so before you dive into the codebase, you should spend some time
learning TypeScript on your own.

We recommend using the official TypeScript Handbook (or any other resource you
find helpful, there are many YouTube videos) and online resources of your
choosing, study (at least) the following core topics:

- Basic types & type annotations (string, number, arrays, functions)
- Unions, literals, and narrowing
- Object shapes: interfaces and type aliases
- Tooling, config, and ecosystem (tsconfig.json, flags, frameworks)

For now, you will spend a few minutes learning the very basics to translate this code. You can collaborate with other students in this activity and/or ask a CA for help.


Inside your repository, create a new file named:

```text
greet_students.ts
```

Your repository should now contain:

```text
{ANDREW-ID}-17313-reci1/
├── .devcontainer/
├── greet_students.ts
└── README.md
```

Open the file `greet_students.ts` and write the TypeScript code that is equivalent ot the following Python code:


```python
def greet_students(names: list[str], min_length: int) -> None:
 for name in names:
    if len(name) >= min_length:
        print(f"Hello, {name}! Your name is long enough.")
    else: print(f"Hello, {name}!")

students = ["Alice", "Bob", "Charlie", "David"]
greet_students(students, 5)
```

Run your TypeScript program:

```bash
node greet_students.ts
```

Verify that your program runs successfully.


## Activity 11: Commit and Push Your Work

Before submitting, make sure your repository contains all required files.

Your repository should look similar to:

```text
{ANDREW-ID}-17313-reci1/
├── .devcontainer/
│   └── devcontainer.json
├── greet_students.ts
└── README.md
```

Check the status of your repository:

```bash
git status
```

You will notice that Git detects all of your new files (`.devcontainer/` and `greet_students.ts`) as untracked, except `README.md`, which has been in the repository since it was created back in Activity 1.
Add your changes:

```bash
git add .devcontainer greet_students.ts
```

Commit your changes:

```bash
git commit -m "recitation 01 for {ANDREW-ID}"
```

Push your commit to GitHub:

```bash
git push origin main
```

Refresh your GitHub repository page and verify that your files are visible.

## Final Repository Structure

Your repository should look like:

```text
{ANDREW-ID}-17313-reci1/
├── .devcontainer/
│   └── devcontainer.json
├── greet_students.ts
└── README.md
```


## Submission

Submit the **link to your GitHub repository**.

Before submitting, verify that:

- [ ] The repository name is `{ANDREW-ID}-17313-reci1`.
- [ ] The repository is **public**.
- [ ] `greet_students.ts` is present.
- [ ] `.devcontainer/devcontainer.json` is present.
- [ ] Your code runs successfully inside the Dev Container.
- [ ] Your latest changes have been committed.
- [ ] Your latest commit has been pushed to GitHub.
- [ ] The repository link you submit is accessible without signing in.


**Submission:** Submit the URL to your public GitHub repository on [Gradescope](https://gradescope.com/courses/1360202/assignments/8461221/)!
