# Installing NodeBB on Windows

17-313 will only be supporting Windows Subsystem Linux 2 (WSL2), Ubuntu variant, on Windows. It's highly recommended that you develop using VSCode as well. Refer to Microsoft's official documentation on what is [WSL](https://learn.microsoft.com/en-us/windows/wsl/about).

## Installing WSL2 on Windows

Follow the instructions on the official [Get Started Guide](https://learn.microsoft.com/en-us/windows/wsl/setup/environment#get-started), and ensure you complete all the steps until (and including) **Use Visual Studio Code**.

By the end of the instructions you should:

- [ ] Have Ubuntu WSL2 installed
- [ ] Have a root Linux username and password setup
- [ ] Have updated and upgraded your packages
- [ ] Be able to open Ubuntu WSL2 in Windows Terminal
- [ ] Understand that you should **store your project files on the same operating system as the tools you plan to use.** You should for example, be doing `git clone` in your Ubuntu file system, open the directory in Ubuntu, and edit the code in Ubuntu.
- [ ] Be able to open a directory in Ubuntu in VSCode

In all future projects of this course, you should develop using WSL2. It is thus very important that you setup WSL2 correctly; come to office hours if you need any assistance with the installation.

## Installing NodeBB

Follow the [Ubuntu](ubuntu.md) instructions to install NodeBB.