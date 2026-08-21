---
title: "Development Container Setup"
nav_order: 70
---

# Development Container Installation Instructions

For this class, you should be using a VSCode Development container to run OpenCode. **Please take the time to carefully read through these instructions!**


First, follow the instructions for installing Docker on your respective operating system [here](https://code.visualstudio.com/docs/devcontainers/containers#_installation).


Then, follow along with the tutorial for [installing docker and development containers for VScode](https://code.visualstudio.com/docs/devcontainers/tutorial).

Once you have set up Docker and devcontainer extensions properly, you should be able to run the example in the tutorial smoothly .



After that, clone the repo from your fork of the class repository:

```console
> git clone git@github.com:<your-username>/opencode.git

Cloning into 'opencode'...

remote: Enumerating objects: ..., done.

remote: Counting objects: 100% (.../...), done.

remote: Compressing objects: 100% (.../...), done.

Receiving objects: 100% (.../...), done.

Resolving deltas: 100% (.../...), done.
```

Next, open the directory you just created with vscode. You can do this in the UI, but if you have launching from the command line enabled ([https://code.visualstudio.com/docs/setup/mac](https://code.visualstudio.com/docs/setup/mac)) then you can use the command: 

```
code .
```

This should open vscode as such: 

![VSCode](../../assets/project/installed.png)

If you followed the tutorial correctly, you will see a blue square in the bottom left corner:

![Install Extension](../../assets/project/menu.png)




Click on that, and it will open this menu:

![DevContainer Menu](../../assets/project/reopenInContainer.png)





From there, choose “Reopen in Container”

It will take a little while for that to run, then it should restart VSCode and you will see this in the bottom left:



![Running Devcontainer](../../assets/project/runningDevContainer.png)


Now go to the menu, and select 

Terminal -> New Terminal

![Running Devcontainer](../../assets/project/terminal.png)


Now you will see an integrated terminal window.  You should be able to check the node version and npm version also:

![Running Devcontainer](../../assets/project/nodeVersion.png)


