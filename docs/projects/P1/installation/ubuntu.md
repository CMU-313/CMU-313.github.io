# Installing on Ubuntu

## Required Software

### Installing Node.js

Node.js is available from the NodeSource Ubuntu binary distributions repository.

```sh
curl -sL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
```
```sh
sudo apt-get install -y nodejs
```

Verify installation of Node.js and npm. You should have version LTS of Node.js installed, and version 8 of npm installed:

```sh
node -v
npm -v // should output "8.11.0" or similar
```

### Installing Redis
The original NodeBB installation guide suggests the use of MongoDB database, but we have found more success with using Redis as the database.

Here's an abbreviated version of the instructions provided by [Redis](https://redis.io/docs/getting-started/installation/install-redis-on-linux/):

Add Redis repository to the apt index:

```sh
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
```

```sh
echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
```

Update and install:

```sh
sudo apt-get update
sudo apt-get install redis
```

Start the redis server:

```sh
redis-server
```

## Installing NodeBB

You should have already cloned your NodeBB repository onto your local machine. Enter the directory where you've cloned the repository:

```sh
cd NodeBB
```

Run the interactive installation command:

```sh
./nodebb setup
```

For each of the questions — **except for "Which database to use (mongo)"**, which you should answer with "redis" — you may accept the default answer by pressing ++enter++

```
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

The first time you run the `setup` command, you will be asked to configure a forum administrator. When prompted, enter the desired information for the admin account.

Once everything has finished installing, a configuration file `config.json` will be created. This file can be modified if you need to make changes to the above settings, such as the database location or credentials used to access the database.

After the installation, build the executable:

```sh
./nodebb build
```

Then start the nodebb server:

```sh
./nodebb start
```

You can now visit your forum at [`http://localhost:4567/`](http://localhost:4567/).
