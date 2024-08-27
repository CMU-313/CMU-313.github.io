# Installing on Ubuntu

## Required Software

### Installing Node.js

Node.js is available from the NodeSource Ubuntu binary distributions repository. Start by adding this repository to the apt index:

```console
% curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/master/install.sh | bash
```

Then, update the apt packages and install nodejs:
```console
% sudo apt-get update
% sudo apt-get install -y nodejs
```

Verify installation of Node.js and npm by checking their installed versions.

```console
% node -v     # ideally v18.x or v20.x
% npm -v      # ideally 9.x or above
```

### Installing Redis

The original NodeBB installation guide suggests the use of MongoDB database, but for simplicity and consistency across the installation guides, we will be using Redis as our database.

Here is an abbreviated version of the installation instructions provided by [Redis](https://redis.io/docs/getting-started/installation/install-redis-on-linux/):

```console
% sudo apt-get update
% sudo apt-get install redis
```

Start the redis server:

```console
% redis-server
```

## Installing NodeBB

You should have already forked the [class-specific repository](https://github.com/CMU-313/NodeBB). Clone your forked repository onto your local machine.

!!! warning "Windows WSL2 Warning"
    For Windows WSL2 users, you should [**store your project files on the same operating system as the tools you plan to use**](https://learn.microsoft.com/en-us/windows/wsl/filesystems#file-storage-and-performance-across-file-systems). When it comes to cloning the NodeBB repository, it means that you should clone it in:
    
    - the Linux file system root directory: `\\wsl$\Ubuntu\home\<user name>\`
    - **NOT** the Windows file system root directory: `/mnt/c/Users/<user name>/$` or `C:\Users\<user name>\`

    You can use `% cd ~` to access the Linux home directory, then clone the repository there.

Enter the directory where you have cloned the repository:

```console
% cd NodeBB
```

Run the interactive installation command:

```console
% ./nodebb setup
```

You will then be presented with a series of setup questions. 

For each of the questions — **except for "Which database to use (mongo)"**, which you should answer with "redis" — you may accept the default answer by pressing ++enter++

```console
URL used to access this NodeBB (http://127.0.0.1:4567) 
Please enter a NodeBB secret (ee18b7c3-1d23-41c9-800f-78d74acc0861) 
Would you like to submit anonymous plugin usage to nbbpm? (yes) 
Which database to use (mongo) redis

Now configuring redis database:
Host IP or address of your Redis instance (127.0.0.1) 
Host port of your Redis instance (6379) 
Password of your Redis database 
Which database to use (0..n) (0) 
```

The first time you run the `setup` command, you will also be asked to configure a forum administrator. When prompted, enter the desired information for the admin account.

Once everything has finished installing, a configuration file `config.json` will be created. This file can be modified if you need to make changes to the above settings, such as the database location or credentials used to access the database.

After the installation, start the NodeBB server:

```console
% ./nodebb start
```

You can now visit your forum at [`http://localhost:4567/`](http://localhost:4567/).
