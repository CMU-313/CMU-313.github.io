# Git Commands Reference for NodeBB Project

This reference covers the essential Git commands you'll need for this project. Git can seem intimidating at first, but these commands will handle 95% of your daily workflow.

!!! tip "Golden Rule"
    **Commit early and often** - Git can only help you recover work that's been committed!

## Commands You'll Use 90% of the Time

For daily development, these 10 commands handle most situations:

```bash
git status           # Check what's happening
git checkout -b      # Create new branch
git add .            # Stage changes
git commit -m        # Save changes
git push             # Upload to GitHub
git pull upstream    # Get latest from class repo
git checkout         # Switch branches
git merge            # Combine branches
git log --oneline    # See history
gh pr create         # Make pull request
```

Remember: **When in doubt, check `git status`** - it will tell you what state you're in and often suggest what to do next!

## Setup and Configuration

### Initial Repository Setup
```bash
# Clone your forked repository
git clone https://github.com/<your-username>/NodeBB.git

# Navigate into the project
cd NodeBB

# Set up upstream remote (to sync with class repo)
git remote add upstream https://github.com/CMU-313/NodeBB.git

# Check your remotes
git remote -v
```

**What this does**: Sets up your local copy and connects it to both your fork (origin) and the class repository (upstream).

## Status and Information

### Check What's Happening
```bash
# Check current status (most important command!)
git status

# See commit history
git log --oneline

# See what changed in files
git diff

# See differences between branches
git diff main..feature-branch

# See what files changed since last commit
git diff --name-only
```

**When to use**: Run `git status` frequently to understand what Git sees. Use `git diff` before committing to review your changes.

## Branch Management

### Working with Branches
```bash
# Create and switch to new branch
git checkout -b feature-branch-name

# Switch between branches
git checkout main
git checkout feature-branch-name

# List all branches (* shows current branch)
git branch

# Delete a branch (after merging)
git branch -d feature-branch-name

# Force delete a branch (if not merged)
git branch -D feature-branch-name
```

**Best practices**: 

- Create descriptive branch names: `add-user-profile-editing`, `fix-login-redirect-bug`
- One branch per feature/issue
- Always start from an up-to-date `main` branch

## Saving Changes

### Committing Your Work
```bash
# Add specific files to staging
git add filename.js
git add src/

# Add all changes
git add .

# Commit with message
git commit -m "Add user authentication feature"

# Add and commit in one command (for tracked files)
git commit -am "Fix login bug"

# Check what you're about to commit
git diff --cached
```

**Good commit messages**:
```bash
# Good: Clear and specific
git commit -m "Fix user authentication redirect loop"

# Better: Include context
git commit -m "Fix user authentication redirect loop

- Redirect to profile page after successful login
- Handle edge case for users without profiles  
- Add unit tests for login flow"

# Bad: Vague and unhelpful
git commit -m "fixed stuff"
```

## Syncing with Remotes

### Keeping in Sync
```bash
# Push your branch to GitHub (first time)
git push -u origin feature-branch-name

# Push subsequent changes
git push

# Get latest changes from upstream (class repo)
git fetch upstream
git merge upstream/main

# Or combine fetch and merge
git pull upstream main

# Check if you're up to date with main branch
git status
git log --oneline main..HEAD
```

**Daily workflow**:
```bash
# Start each day by updating main
git checkout main
git pull upstream main
```

## Emergency and Fixing Mistakes

### When Things Go Wrong
```bash
# Undo last commit (keep changes in working directory)
git reset --soft HEAD~1

# Discard changes in working directory
git checkout -- filename.js

# Undo all uncommitted changes
git checkout .

# See what you did recently (lifesaver command!)
git reflog

# Completely start over with a clean branch
git checkout main
git branch -D broken-branch
git checkout -b fresh-start
```

!!! warning "Destructive Commands to Avoid"
    These can permanently delete work - learn these later:
    
    - `git reset --hard` - Permanently deletes changes
    - `git rebase -i` - Interactive rebase (advanced)
    - `git push --force` - Can overwrite others' work

## NodeBB Project Specific

### Useful for Class Workflow
```bash
# Create a branch for each issue/feature
git checkout -b issue-123-add-search-feature

# Before submitting PR, make sure you're current
git checkout main
git pull upstream main
git checkout your-feature-branch
git merge main  # Incorporate latest changes

# See commit history for a specific file
git log --oneline filename.js

# Find which commit introduced a bug
git log --grep="search terms"
```

## GitHub Integration

### Pull Request Commands
```bash
# Create pull request from command line
gh pr create --title "Add feature" --body "Description"

# Create PR with auto-generated title/description
gh pr create

# Check PR status
gh pr status

# View your PRs
gh pr list

# View specific PR
gh pr view 123
```

**Alternative**: You can always create PRs through the GitHub web interface.

## Essential Daily Workflow

### Step-by-Step Process
```bash
# 1. Start new feature
git checkout main
git pull upstream main
git checkout -b new-feature-name

# 2. Work on your code...
# (edit files, test, repeat)

# 3. Save progress frequently
git add .
git commit -m "Descriptive commit message"

# 4. Push for backup/collaboration
git push -u origin new-feature-name

# 5. Continue working...
git add .
git commit -m "Another commit"
git push  # No -u needed after first time

# 6. When ready, create PR
gh pr create --title "Feature name" --body "Description"

# 7. After PR approved and merged
git checkout main
git pull upstream main
git branch -d new-feature-name  # Clean up old branch
```

## Pro Tips and Best Practices

### Habits for Success
```bash
# Before starting work each day
git checkout main
git pull upstream main

# Use descriptive branch names
git checkout -b add-user-profile-editing      # ✅ Good
git checkout -b fix-login-redirect-bug        # ✅ Good
git checkout -b stuff                         # ❌ Bad

# Check status frequently
git status

# Review changes before committing
git diff
git add .
git diff --cached  # See what's staged
git commit -m "Clear description"
```

### Commit Message Guidelines

- **First line**: Brief summary (50 characters or less)
- **Blank line** if adding more detail
- **Body**: Explain what and why, not how
- Use present tense: "Fix bug" not "Fixed bug"

## Troubleshooting Common Issues

### "I Made a Mistake"
```bash
# Scenario: "I committed to main instead of a branch"
git branch new-feature-branch  # Create branch from current commit
git checkout main
git reset --hard HEAD~1        # Move main back one commit
git checkout new-feature-branch

# Scenario: "I want to undo my last commit but keep the changes"
git reset --soft HEAD~1

# Scenario: "I need to see what I did yesterday"
git log --since="yesterday" --author="your-name"

# Scenario: "My branch got messed up"
git checkout main
git branch -D broken-branch
git checkout -b fresh-start
```

### Merge Conflicts
```bash
# When you see "CONFLICT" during merge:
# 1. Edit the conflicted files (look for <<<<<<< markers)
# 2. Remove the conflict markers and choose the correct code
# 3. Add and commit the resolved files
git add conflicted-file.js
git commit -m "Resolve merge conflict"
```

## Additional Resources

### Quick References

- `git --help` - General help
- `git <command> --help` - Help for specific command
- `git status` - Your best friend, use it constantly

### Visual Git Tools

- **VS Code**: Built-in Git integration with visual diff
- **GitKraken**: GUI for complex Git operations
- **GitHub Desktop**: Simple GUI for basic operations

---

*Having trouble with a Git command? Don't hesitate to ask for help on Slack or during office hours. Git can be tricky, but these fundamentals will serve you well throughout your software engineering career.*