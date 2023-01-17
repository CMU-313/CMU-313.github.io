# Installing NodeBB on MacOS

## Required Software

First, install the following programs:

-   <http://nodejs.org/>
-   <http://brew.sh/>

### Installing Redis

Install redis with homebrew:

```console
% brew install redis
```

Start the redis server:

```console
% redis-server
```

## Installing NodeBB

You should have already forked the [class-specific repository](https://github.com/CMU-313/NodeBB). Clone your forked repository into your local machine.

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

After the installation, build the files:

```console
% ./nodebb build
```

And start the NodeBB server:

```console
% ./nodebb start
```

You can now visit your forum at [`http://localhost:4567/`](http://localhost:4567/).
