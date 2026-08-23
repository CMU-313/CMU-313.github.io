---
title: "FAQ"
nav_order: 60
---

# Frequently Asked Questions

This section is meant to contain frequently asked questions about the homework. We will continue to update this throughout the period the assignment is released!

## Installation and Running the Instance

### `bun install` fails or errors out on some packages!

Make sure you're running **Bun 1.3 or later** inside your dev container (`bun --version`). If the version checks out and you're still seeing errors, try deleting `node_modules` and re-running `bun install` from the repo root.

### `bun dev` doesn't start, or exits immediately!

Confirm you ran `bun install` first from the repo root, and that you're running the command **inside your dev container**, not on your host machine. If it still won't start, copy the full terminal output and ask on Slack or during office hours, including your Bun version and OS.

!!! warning "TBD: opencode migration"
    NodeBB ran as a localhost web server on a fixed port (4567), so port conflicts were a common FAQ. opencode's TUI doesn't run as a traditional localhost server in the same way, so it's unclear whether a port-conflict-style question belongs here. Leaving this open until confirmed.

## Analysis Tools

### I can't run `bun test` or `bun lint` because of missing dependencies.

Run `bun install` from the repo root first to make sure all dependencies are present, then retry.

### `bun test` behaves strangely or throws a lot of errors when I run it from the repo root.

opencode's test suite isn't meant to be run all at once — run it **package by package**, from inside the specific package directory you're working in (see [Project 1A](1_checkpoint.md)). Running it from the repo root may produce misleading results.

### My coverage report is empty or mostly red.

Make sure you ran the coverage command from inside the correct package directory:

```bash
bun test --coverage --coverage-reporter=lcov --coverage-dir=./coverage
```

Then open `coverage/index.html` in a browser. If it's still mostly red, double-check that the tests actually ran and passed first — a failed or incomplete test run will also produce an incomplete coverage report.

## Reset

If you run into a broken local state, the safest first step is deleting `node_modules` and re-running `bun install`. This section will be filled in once we confirm whether opencode needs anything more specific reset.
