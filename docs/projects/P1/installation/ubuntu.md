# Installing on Ubuntu

## Required Software

### Installing Node.js

Node.js is available from the NodeSource Ubuntu binary distributions repository.

```sh
% curl -sL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
% sudo apt-get install -y nodejs
```

Verify installation of Node.js and npm. You should have version lts of Node.js installed, and version 8 of npm installed:

```sh
node -v
npm -v // should output "8.11.0" or similar
```

### Installing MongoDB

The following is an abbreviation of the official [MongoDB installation guide for Ubuntu](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/).

```sh
% wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -
% echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list
% sudo apt-get update
% sudo apt-get install -y mongodb-org
```

**Verify installation of MongoDB.** You should have version 5.0:

```sh
mongod --version
db version v5.0
```

**Start the mongod service and verify service status:**

```sh
sudo systemctl start mongod
sudo systemctl status mongod
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
% sudo systemctl restart mongod
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
% ./nodebb setup
```

You will then be presented with a series of setup questions. For each of the questions, you may accept the default answer by pressing ++enter++

When prompted for the `mongodb` username and password, enter `nodebb`, and the password that you configured earlier. Once connectivity to the database is confirmed, the setup will prompt that initial user setup is running. 

The first time you run the `setup` command, you will be asked to configure a forum administrator. When prompted, enter the desired information for the admin account.

Once everything has finished installing, a configuration file `config.json` will be created. This file can be modified if you need to make changes to the above settings, such as the database location or credentials used to access the database.

After the installation, run:

```sh
% ./nodebb build
% ./nodebb start
```

You can now visit your forum at [`http://localhost:4567/`](http://localhost:4567/).
