---
kind: recitation
title: Recitation 9 - CI/CD with Vercel
date: 2026-11-02
reveal_date: 2026-10-30
---

# Recitation 9: CI/CD with Vercel

Today you'll put a game on the internet, change it safely, and stop a broken change from going live. You'll fork the classic 2048 game, deploy it with [Vercel](https://vercel.com), redesign it with AI, and add a test that GitHub runs on every pull request.

- **Part 1 (~10 min):** deploy your game to a live URL.
- **Part 2 (~15 min):** redesign it on a branch, and preview the change before it goes live.
- **Part 3 (~15 min):** add CI, so that a broken change can't reach your live site.

[Recitation slides](https://docs.google.com/presentation/d/17-1NlG1I62hdImh0x78K7kOe4Np8x2G5UI1Ee-i8E7w/edit?usp=sharing)

After the recitation, remember to complete the [Gradescope assignment](https://www.gradescope.com/courses/1356702/assignments/8417892) to receive credit!

## How the pieces fit

```text
  git push
    │
    ▼
  GitHub ──┬──▶ CI (Part 3): GitHub Actions runs your tests
           │      → ✅ or ❌ on the pull request
           │
           └──▶ CD (Parts 1–2): Vercel builds and deploys
                  → master branch:  production URL
                  → other branches: preview URL
```

| Term | Meaning |
|---|---|
| Continuous integration (CI) | Automatically testing every change, so problems surface before the change merges. |
| Continuous deployment (CD) | Automatically deploying every change that lands on the main branch to the live site. |
| Production deployment | The live site everyone sees, built from `master`. |
| Preview deployment | A separate copy of the site, built from another branch or a pull request, with its own URL. Production is untouched. |
| Status check | A pass/fail result, such as a test run or a Vercel build, that GitHub shows on a pull request. |
| Ruleset | A repository setting that blocks merging into `master` unless the required checks pass. |

## Before recitation: setup (5 min)

1. Check that you can sign in to GitHub and that `git --version` works in your terminal.
2. Go to [vercel.com/signup](https://vercel.com/signup).
3. Choose the **Hobby** plan, enter your name, and click **Continue**.
4. Click **Continue with GitHub** and authorize Vercel.
5. Have an AI coding assistant ready.

**Check:** you land on your Vercel dashboard.

## Part 1: Deploy your game (~10 min)

### Step 1: Fork the repository

1. Open [github.com/gabrielecirulli/2048](https://github.com/gabrielecirulli/2048).
2. Click **Fork** (top right).
3. Leave every setting as it is, including **Copy the `master` branch only**.
4. Click **Create fork**.

**Check:** the page now shows `<your-username>/2048`, with "forked from gabrielecirulli/2048" underneath.

> **Welcome to the real world.** Until now, your course repos have been cozy sandboxes where only your TAs could see your mistakes. Today you're forking the real 2048, starred by more than 13,000 people. Open your pull request against the original project by accident, and its author gets a surprise redesign proposal while the whole internet watches. It's completely harmless, and you can close it with one click, but Step 5 shows you how to keep your masterpiece to yourself. (One of your TAs did exactly this while testing this recitation. [The pull request](https://github.com/gabrielecirulli/2048/pull/645) is still there for all to see.)

### Step 2: Deploy on Vercel

1. Go to [vercel.com/new](https://vercel.com/new).
2. Under **Import Git Repository**, find `2048` and click **Import**.
    - *Don't see it?* Click **Adjust GitHub App Permissions** (or **Install**), choose **Only select repositories**, select `2048`, and click **Save**. You'll come back to this page.
3. In **Project Name**, type `2048-<andrewid>` (for example, `2048-smtiwari`). This becomes your URL.
4. Leave everything else as it is. **Framework Preset** should say **Other**.
5. Click **Deploy** and wait about a minute.
6. When the **Congratulations!** page appears, click the screenshot of your game to open it.

**Check:** your game loads at `https://2048-<andrewid>.vercel.app`, and the tiles move when you press the arrow keys.

> **What just happened?** Vercel now watches your fork. Every time you push to `master`, it redeploys this site by itself. That is **continuous deployment**.

## Part 2: Preview a change (~15 min)

### Step 3: Clone your fork and create a branch

1. On your fork's GitHub page, click the green **Code** button and copy the HTTPS URL.
2. In your terminal, run:

    ```bash
    git clone <the URL you copied>
    cd 2048
    git switch -c restyle
    ```

**Check:** `git branch --show-current` prints `restyle`.

> **Why a branch?** When you push any branch other than `master`, Vercel builds a **preview deployment**: a separate copy of the site with its own URL. Your production site stays as it is.

### Step 4: Make the game your own with AI

This is the fun part. Use an AI assistant to redesign the game however you like: the colors, fonts, background, tiles, title text, or a whole new theme. Get as creative as you want and have fun with it.

For example, Shrey, one of your TAs, is a big *Tron: Legacy* fan and gave the game a *Tron: Legacy* look.

1. Open the `2048` folder in your AI assistant.
2. Describe the look you want.
3. Open `index.html` in your browser (double-click it, or run `open index.html` on macOS) to see the result.
4. Keep asking for changes and refreshing the page until you love it.

**Check:** your new design shows up in the browser, and the game still plays.

### Step 5: Push your branch and open a pull request

1. In your terminal, inside the `2048` folder, run:

    ```bash
    git add -A
    git commit -m "My new theme"
    git push -u origin restyle
    ```

2. Open your fork's page on GitHub and click **Compare & pull request** in the yellow banner.
    - *No banner?* Click the **Pull requests** tab, then **New pull request**.
3. **Important:** GitHub points your pull request at the *original* project by default. Click the **base repository** dropdown and choose `<your-username>/2048`, unless you want 13,000 stargazers reviewing your redesign.
4. Check that the top of the page now reads **base: master ← compare: restyle**.
5. Give the pull request a title, such as the name of your theme.
6. Click **Create pull request**.
7. Wait up to a minute for the **vercel** bot to comment on your pull request.
8. In the bot's comment, under **Actions**, click **Preview**.
9. In another tab, open your production URL (`2048-<andrewid>.vercel.app`).

**Check:** the preview shows your new design, while production still shows the original game.

> **Why previews?** When you pushed `restyle`, Vercel built a preview deployment of your branch with its own URL. A preview lets teammates and reviewers try a change before it reaches real users. Production only changes when the change is merged.

### Step 6: Merge and watch production update

1. At the bottom of your pull request, click **Merge pull request**, then **Confirm merge**.
2. In Vercel, open your project and click the **Deployments** tab.
3. Watch the newest deployment, labeled **Production**, until it says **Ready**.
4. Refresh your production URL. If it still looks unchanged, hard-refresh with **Cmd+Shift+R** (macOS) or **Ctrl+Shift+R** (Windows).

**Check:** your production site now shows your new design.

> **What just happened?** Merging put your change on `master`, and Vercel deployed `master` to production with no extra steps. That's the full loop of continuous deployment: branch, preview, review, merge, production.

## Part 3: Protect production with CI (~15 min)

So far, anything merged into `master` goes straight to production, even if it breaks the game. In this part, you add a test that GitHub runs on every pull request. Then you break the game on purpose and watch GitHub refuse to merge it.

### Step 7: Add CI to your repository

1. **Finish Step 6 first.** Your restyle pull request must be merged before you add CI.
2. In your terminal, inside the `2048` folder, update `master`:

    ```bash
    git switch master
    git pull
    ```

3. Create a file named `.github/workflows/ci.yml` with this content. It tells GitHub to run your test on every pull request and on every push to `master`.

    ```yaml
    name: CI

    on:
      push:
        branches: [master]
      pull_request:

    jobs:
      test:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v7
          - uses: actions/setup-node@v7
            with:
              node-version: 22
          - run: node --test test/game.test.js
    ```

4. Create a file named `test/game.test.js` with this content. It checks one rule of the game: two 2s merge into a 4.

    ```js
    // Checks one rule of 2048 against the real game code in js/.
    const test = require("node:test");
    const assert = require("node:assert");
    const fs = require("node:fs");
    const vm = require("node:vm");

    // Load the game's logic. These three files never touch the browser.
    const game = vm.createContext({});
    for (const file of ["tile.js", "grid.js", "game_manager.js"]) {
      vm.runInContext(fs.readFileSync("js/" + file, "utf8"), game);
    }

    // A do-nothing stand-in for the keyboard, the screen, and storage.
    function Fake() {}
    for (const method of ["on", "actuate", "getGameState", "setGameState",
                          "clearGameState", "getBestScore", "setBestScore"]) {
      Fake.prototype[method] = function () {};
    }

    test("two 2s merge into a 4", () => {
      const manager = new game.GameManager(4, Fake, Fake, Fake);
      manager.grid = new game.Grid(4); // start from an empty board
      manager.grid.insertTile(new game.Tile({ x: 0, y: 0 }, 2));
      manager.grid.insertTile(new game.Tile({ x: 1, y: 0 }, 2));

      manager.move(3); // 3 means "left"

      assert.strictEqual(manager.grid.cells[0][0].value, 4);
    });
    ```

5. Run the test on your machine:

    ```bash
    node --test test/game.test.js
    ```

    You should see output like this. The times will differ.

    ```text
    ✔ two 2s merge into a 4 (1.687ms)
    ℹ tests 1
    ℹ suites 0
    ℹ pass 1
    ℹ fail 0
    ℹ cancelled 0
    ℹ skipped 0
    ℹ todo 0
    ℹ duration_ms 56.487084
    ```

6. Commit and push to `master`:

    ```bash
    git add .github test
    git commit -m "Add CI"
    git push
    ```

7. On GitHub, click your fork's **Actions** tab.
    - *Asked to enable workflows?* Click the button, then trigger a run with `git commit --allow-empty -m "Run CI"` and `git push`.

**Check:** the test passes on your machine (`pass 1`), and the **Actions** tab shows a **CI** run with a green check mark.

> **What is CI?** Continuous integration means every change is tested automatically, so problems show up before the change reaches `master`. From now on, GitHub runs your test on every pull request.

### Step 8: Require CI to pass before merging

1. In your fork, click **Settings**.
2. In the left sidebar, click **Rules**, then **Rulesets**.
3. Click **New ruleset**, then **New branch ruleset**.
4. For **Ruleset Name**, type `protect-master`.
5. Set **Enforcement status** to **Active**.
6. Under **Target branches**, click **Add target**, then **Include default branch**.
7. Under **Branch rules**, check **Require a pull request before merging**. Leave **Required approvals** at 0.
8. Check **Require status checks to pass**.
9. In the **Required status checks** box, click **Add checks**, type `test` in the search box, and click **test** in the list.
10. Leave the **Bypass list** empty, and click **Create**.

**Check:** `protect-master` appears in your list of rulesets as **Active**.

> **Why a rule?** CI only reports results. The rule makes GitHub enforce them: nothing reaches `master`, and so nothing reaches production, unless `test` passes.

### Step 9: Break the game on a branch

1. Create a branch:

    ```bash
    git switch -c break-it
    ```

2. Open `js/game_manager.js` and find this line (around line 157):

    ```js
    var merged = new Tile(positions.next, tile.value * 2);
    ```

3. Change `* 2` to `* 3`, so that two 2s now merge into a 6.
4. Run the test again:

    ```bash
    node --test test/game.test.js
    ```

    This time it fails. The key line is `6 !== 4`: the test expected a 4 and got a 6.

    ```text
    ✖ two 2s merge into a 4 (1.8265ms)
    ℹ tests 1
    ℹ suites 0
    ℹ pass 0
    ℹ fail 1
    ℹ cancelled 0
    ℹ skipped 0
    ℹ todo 0
    ℹ duration_ms 49.815125

    ✖ failing tests:

    test at test/game.test.js:20:2
    ✖ two 2s merge into a 4 (1.8265ms)
      AssertionError [ERR_ASSERTION]: Expected values to be strictly equal:

      6 !== 4

          at TestContext.<anonymous> (.../2048/test/game.test.js:28:11)
          at Test.runInAsyncScope (node:async_hooks:214:14)
          at Test.run (node:internal/test_runner/test:1047:25)
          at Test.start (node:internal/test_runner/test:944:17)
          at startSubtestAfterBootstrap (node:internal/test_runner/harness:297:17) {
        generatedMessage: true,
        code: 'ERR_ASSERTION',
        actual: 6,
        expected: 4,
        operator: 'strictEqual'
      }
    ```

5. Commit and push anyway:

    ```bash
    git commit -am "Bigger merges"
    git push -u origin break-it
    ```

6. Open a pull request as in Step 5. Click **Compare & pull request**, set the **base repository** to `<your-username>/2048`, and click **Create pull request**.

**Check:** the **test** check on your pull request shows a red ✗, and GitHub blocks the merge.

### Step 10: See what CI caught

1. Open the preview from the **vercel** bot's comment and merge two 2s. You get a 6.
2. Back on the pull request, click **Details** next to the failing **test** check.
3. Find the failed test, `two 2s merge into a 4`. It expected 4 and got 6.

> **Discuss:** Vercel still deployed a preview of the broken game. What kept it out of production?

> **What just happened?** CI caught the broken rule before the merge, and your ruleset turned that red ✗ into a blocked merge. Production stays on the last good version.

*Finished early?*

- Fix the line, push, watch **test** turn green, and merge.
- Break the game a different way: delete the line `self.score += merged.value;` so that merges stop adding to your score. Does CI catch it? Why not?
