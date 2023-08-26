# Resources & Documentation
Below are some common resources to assist you with your completion of this project. If you get stuck, start by consulting the following materials; if you have any additional questions, the course staff will be available to answer questions via Slack and Office Hours.

### Git & GitHub Documentation
Documentation for working with Git and GitHub:

- [Git Documentation](https://git-scm.com/docs/gittutorial)
- [Git Flow](https://datasift.github.io/gitflow/IntroducingGitFlow.html)
- [GitHub Basics](https://guides.github.com/activities/hello-world/)
- [GitHub's Flow](https://guides.github.com/introduction/flow/)
- [GitHub Cross-Referencing](https://docs.github.com/en/github/writing-on-github/working-with-advanced-formatting/autolinked-references-and-urls#issues-and-pull-requests)

We also have a [simple Git-based exercise](/projects/P1/github) that you are highly recommeneded to complete before proceeding with this project.

### TypeScript Documentation

The repository README contains links to different documentation material that you may find helpful in your development process. Particularly, you will want to focus on the documentation relating to JavaScript/TypeScript:

- [TypeScript for New Programmers](https://www.typescriptlang.org/docs/handbook/typescript-from-scratch.html)
- [TypeScript for JavaScript Programmers](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html)
- [JavaScript to TypeScript Translation](https://www.typescriptlang.org/docs/handbook/migrating-from-javascript.html#moving-to-typescript-files)

You will also find some sample translated TypeScript files within the repository. You can use these as guidance for your translation process:

- [`src/social.ts`](https://github.com/CMU-313/NodeBB/blob/main/src/social.ts)
- [`src/controllers/composer.ts`](https://github.com/CMU-313/NodeBB/blob/main/src/controllers/composer.ts)

### Additional TypeScript Background
This section provides more context on how TypeScript is used for this project and when it is appropriate to suppress ESLint warnings in your translated TypeScript files.

As native JavaScript does not have any typing, by default, all functions/values/classes/modules that are not typed will be automatically given the `any` type by TypeScript. Under default settings, this allows any valid JavaScript code to be run as TypeScript.

Using the `any` type, however, will defeat the purpose of the various type-checking features TypeScript provides. As such, we’ve set our linter to **check for strict typing** and **disallow the use of the `any` type**. For the most part, this should check that you explicitly type everything within your files and ensure that you are able to make the most out of TypeScript.

A limitation of this strictness is that there will be errors thrown when using non-translated JavaScript imports, which TypeScript will assume to have type `any`. As an example from one of our sample translated files [`src/social.ts`](https://github.com/CMU-313/NodeBB/blob/main/src/social.ts):

```TypeScript title="src/social.ts"
// A module import from a non-translated JavaScript file database/index.js
import db from './database';
…
const activated = await db.getSetMembers('social:posts.activated');
```

Running the linter will give the following errors:
```sh
error  Unsafe member access .getSetMembers on an `any` value 
@typescript-eslint/no-unsafe-member-access

error  Unsafe call of an `any` typed value
@typescript-eslint/no-unsafe-call

error  Unsafe assignment of an `any` value
@typescript-eslint/no-unsafe-assignment
```

Let’s take a look at each error:

- **``@typescript-eslint/no-unsafe-member-access``** - we don’t know the typing of our imported module `db`, so it is treated as `any`. However, we don’t know if something of type `any` has a function called `getSetMembers`, hence this is an unsafe member access
- **``@typescript-eslint/no-unsafe-call``** - we don’t know the typing of the function `db.getSetMembers`, and so it is treated as `any`. We can not call a function of type `any`, so `db.getSetMembers('social:posts.activated')` is an unsafe call
- **``@typescript-eslint/no-unsafe-assignment``** - we don’t know the return type of `db.getSetMembers`, and so it is treated as `any`. We can not assign something of type `any` to our variable `activated`

The first two errors are dependent on us knowing the typing of `db` and `db.getSetMembers`. However, because we haven’t translated the `database/index.js` file yet, we don’t have access to their typing information. In this case, it is okay to suppress the ESLint errors as they only arise from a lack of translation. We can do this by adding the following comments:

```TypeScript
// The next line calls a function in a module that has not been updated to TS yet
// eslint-disable-next-line @typescript-eslint/no-unsafe-member-access, @typescript-eslint/no-unsafe-call
const activated = await db.getSetMembers('social:posts.activated');
```

For the last error, even though we don’t have typing information provided by the `db` module, we still want to make sure future uses of the `activated` variable get properly typechecked. Checking the rest of the file reveals that `activated` should be a `string[]` type; we can also manually cross-reference the `db.getSetMembers` function to check that this is the correct typing. Hence, it’s okay to cast the return value of this function call to `string[]`, and our full solution looks like this:

```TypeScript
// The next line calls a function in a module that has not been updated to TS yet
// eslint-disable-next-line @typescript-eslint/no-unsafe-member-access, @typescript-eslint/no-unsafe-call
const activated: string[] = await db.getSetMembers('social:posts.activated') as string[];
```

### Installing Typing Packages

In some cases, if your file imports an `npm` package (such as `lodash`, `nconf`, etc), you will need to install the typings for the package. To do this, run:

```sh
% npm install @types/[packagename] --save-dev
```

You should then see the `@types/[packagename]` added to your `package.json` file. 

!!! note "GitHub Actions Packages"
	To make sure your GitHub Actions also install the correct packages, you should copy the `package.json` file to `install/package.json`.
