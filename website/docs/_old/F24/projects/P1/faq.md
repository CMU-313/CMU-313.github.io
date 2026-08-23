# Frequently Asked Questions

This section is meant to contain frequently asked questions about the homework. We will continue to update this throughout the period the assignment is released!

## Installation and Running the Instance

### I'm running into errors about missing files when running `./nodebb start`!

Try re-building some of the assets by running `./nodebb build` first, then try running the start command again.

### I can't start a NodeBB instance and I get an error message saying that port 4567 is already in use.

Maybe you have another NodeBB instance already running. Try stopping it via `./nodebb stop`. Otherwise, try using a differnt port.

## Analysis Tools

### I can't run the `test` or `lint` commands because I have missing dependencies.

Run `npm install` after `./nodebb setup` to make sure you have all the dependencies needed for running tests.

### Running the test suite stops immediately and throws a bunch of errors!

This usually happens if you don't have a test database configured correctly. Scroll up past the errors and copy over the test database configuration into the local `config.json` file under the `"test_database"` field. For redis: if you are using database `0` for running the local instance, you can use database `1` for testing so that the test data remains separate.

## Reset

### How do I reset my NodeBB configurations?

Delete the `config.json` file and re-run the `./nodebb setup` command.

### How do I reset my NodeBB database?

Depending on your database setup, you will need to find the commands to delete all data stored in your database. For redis, this involves using the `redis-cli` to enter the database and using the `FLUSHALL` command.

Once you've cleared your database, delete your `config.json` file and re-run the `./nodebb setup` command. You will need to reconfigure an admin account.
