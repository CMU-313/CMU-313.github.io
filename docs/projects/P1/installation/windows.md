# Installing NodeBB on Windows

17-313 will only be supporting development using Windows Subsystem Linux 2 (WSL2) on Windows (Ubuntu variant). To support the use of WSL2, it is **highly recommended** that you develop using [VSCode](https://code.visualstudio.com/download). 

To learn more, refer to Microsoft's official [WSL Documentation](https://learn.microsoft.com/en-us/windows/wsl/about).

## Installing WSL2 on Windows

Follow the instructions on the official Microsoft [Getting Started Guide](https://learn.microsoft.com/en-us/windows/wsl/setup/environment#get-started) and complete all the steps up to (and including) the [**Use Visual Studio Code**](https://learn.microsoft.com/en-us/windows/wsl/setup/environment#use-visual-studio-code) section.

By the end of these instructions, you should:

- [ ] Have Ubuntu WSL2 installed
- [ ] Have a root Linux username and password set up
- [ ] Have updated and upgraded your packages
- [ ] Be able to open Ubuntu WSL2 in Windows Terminal
- [ ] Understand that you should [**store your project files on the same operating system as the tools you plan to use**](https://learn.microsoft.com/en-us/windows/wsl/filesystems#file-storage-and-performance-across-file-systems). For example, in order to successfully run NodeBB in Ubuntu, you should run `git clone` in your Ubuntu file system, open the cloned directory in Ubuntu, and edit the code files in Ubuntu
- [ ] Be able to open a directory in Ubuntu in VSCode

!!! note
    In all future projects of this course, we will expect you to develop using WSL2. Thus, it is **very important** that you set up WSL2 correctly. Please come to office hours or ask on Slack if you need any assistance with the installation.

## Installing NodeBB
If you do not already have Git installed, follow the [**Git Installation on Linux**](https://github.com/git-guides/install-git#install-git-on-linux) for Ubuntu.

Then, follow the [Ubuntu](/projects/P1/installation/ubuntu) instructions to install required tools and NodeBB itself on WSL2. 
