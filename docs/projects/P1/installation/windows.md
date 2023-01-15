# Installing NodeBB on Windows

## Required Software

### Installing Node.js

- [Download Node.js lts](https://nodejs.org/)
- Execute the installer

Verify installation of Node.js and npm. You should have version lts of Node.js installed, and version 8 of npm installed:

```sh
% node -v
% npm -v // should output "8.11.0" or similar
```

### Installing MongoDB
The following is an abbreviation of the official [MongoDB installation guide for Windows](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/).

Go to the [MongoDB Download Center](https://www.mongodb.com/download-center#production) and download the appropriate setup file for your computer. Then, locate the downloaded `.msi` file and execute it to start the installer. The default installation location is `C:\Program Files\MongoDB\Server\5.0`.

**Add the MongoDB binaries to your PATH:**

- Find the bin directory under your MongoDB installation The default path is `C:\Program Files\MongoDB\Server\5.0\bin`
- Type PATH into the Start Menu search bar
- Open **Edit environment variables for your account**
- Under **User variable for [your username]**, click on `Path`
- Click the **Edit...** button
- Click the **New button** on the right
- Type or paste in the full path to the `bin` directory

**Configure a service for the `mongod` server:**

- Type "cmd" or "Command Prompt" into the Start Menu search bar
- Right-click "Command Prompt" and select "Run as Administrator".
- Create two directories for your database and log files using the `mkdir` command:
    - `% mkdir C:\MongoDB\data\db`
    - `% mkdir C:\MongoDB\logs`
- Create a config file (`C:\MongoDB\mongod.cfg`) with the following contents:

```
systemLog:
    destination: file
    path: C:\MongoDB\logs\mongod.log
storage:
    dbPath: C:\MongoDB\data\db
security:
    authorization: enabled
```

**Install the MongoDB service:**

```sh
mongod.exe --config "C:\MongoDB\mongod.cfg" --install
```

**Verify installation of MongoDB.** You should have version 5.0:

```sh
% mongod --version
db version v5.0
```

**Start the mongod service and verify service status:**

```sh
% net start MongoDB
% sc query "MongoDB" | findstr STATE
```


## Configure MongoDB
General MongoDB administration is done through the MongoDB Shell `mongo`. A default installation of MongoDB listens on port `27017` and is accessible locally. Access the shell:

```sh
% mongo
```

Switch to the built-in admin database:

```mongodb
> use admin
```

Create an administrative user (the is different from the `nodebb` user we'll create later). Replace the placeholder `<Enter a secure password>` with your own selected password. Be sure that the `<` and `>` are also not left behind.

```mongodb
> db.createUser( { user: "admin", pwd: "<Enter a secure password>", roles: [ { role: "root", db: "admin" } ] } )
```

This user is scoped to the admin database to manage MongoDB once authorization has been enabled.

To initially create a database that doesn't exist simply `use` it. Add a new database called `nodebb`:

```mongodb
> use nodebb
```

The database will be created and context switched to `nodebb`. Next create the `nodebb` user with the appropriate privileges:

```mongodb
> db.createUser( { user: "nodebb", pwd: "<Enter a secure password>", roles: [ { role: "readWrite", db: "nodebb" }, { role: "clusterMonitor", db: "admin" } ] } )
```

The `readWrite` permission allows NodeBB to store and retrieve data from the `nodebb` database. The `clusterMonitor` permission provides NodeBB read-only access to query database server statistics which are then exposed in the NodeBB Administrative Control Panel (ACP).

Exit the Mongo Shell:

```mongodb
> quit()
```

Restart MongoDB and verify the administrative user created earlier can connect:

```sh
% net stop MongoDB
% net start MongoDB
% mongo -u admin -p your_password --authenticationDatabase=admin
```

If everything is configured correctly the Mongo Shell will connect. Exit the shell.


## Installing NodeBB

You should have already cloned your NodeBB repository onto your local machine. Enter the directory where you've cloned the repository:

```sh
% cd NodeBB
```

Run the interactive installation command:

```sh
% nodebb setup
```

You will then be presented with a series of setup questions. For each of the questions, you may accept the default answer by pressing ++enter++

When prompted for the `mongodb` username and password, enter `nodebb`, and the password that you configured earlier. Once connectivity to the database is confirmed, the setup will prompt that initial user setup is running. 

The first time you run the `setup` command, you will be asked to configure a forum administrator. When prompted, enter the desired information for the admin account.

Once everything has finished installing, a configuration file `config.json` will be created. This file can be modified if you need to make changes to the above settings, such as the database location or credentials used to access the database.

After the installation, run:

```sh
% nodebb build
% nodebb start
```

You can now visit your forum at [`http://localhost:4567/`](http://localhost:4567/).
