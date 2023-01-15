# Frequently Asked Questions

This section is meant to contain frequently asked questions about the homework. We will continue to update this throughout the period the assignment is released!

## Installation

### I'm running into errors about missing files when running `./nodebb start`!

Be sure you've compiled a build by running the build command `./nodebb build` first, then try running the start command again.

## Analysis Tools

### Running the test suite stops immediately and throws a bunch of errors!

This usually happens if you don't have a test database configured correctly. Scroll up past the errors and copy over the test database configuration into the local `config.json` file.

For redis, you won't have to do any additional setup; for mongodb, you may have to explicitly create another test database. You can reference the installation instructions to get the commands for setting this up. Ask in Slack if you need assistance!

## Other

### How do I reset my NodeBB configurations?

Delete the `config.json` file and re-run the `./nodebb setup` command.

### How do I reset my NodeBB database?

Depending on your database setup, you will need to find the commands to delete all data stored in your database. For redis, this involves using the `redis-cli` to enter the database and using the `FLUSHALL` command.

Once you've cleared your database, delete your `config.json` file and re-run the `./nodebb setup` command. You will need to reconfigure an admin account.
