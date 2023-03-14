# Deploying NodeBB to Fly.io

This document will provide instructions to deploy NodeBB on Fly.io. We recommend following this tutorial with a clean install of NodeBB to ensure it works. Once you successfully deploy, you can add your changes. 

The steps are as follows:

## Install Fly.io command line tools

First, you should install and log into Fly.io’s command line utility. Follow these guides!

- [https://fly.io/docs/hands-on/install-flyctl/](https://fly.io/docs/hands-on/install-flyctl/)
- [https://fly.io/docs/getting-started/log-in-to-fly/](https://fly.io/docs/getting-started/log-in-to-fly/)

## Edit database connection file

In `src/database/redis/connection.js`. Add

```JS
family: 6,
```

to whenever a new Redis object is created. ~ lines 20, 28, 37. i.e.

```JS hl_lines="4"
new Redis({
    sentinels: options.sentinels,
    ...options.options,
    family: 6,
});
```

The Redis database that Fly.io creates connects via IPv6, so we must change our connection config to account for this. 

### Initial Launch

1. In your NodeBB directory, run `flyctl launch`
2. For the following prompts, answer as follows:
    - **Name** -> Anything reasonable you’d like for your app name
    - **Region** -> Ashburn, Virginia (or any reasonable US ones)
    - **Setup a Postgres DB?** -> No
    - **Setup a Redis DB?** -> Yes
        - Choose the free 100MB data plan
        - It’ll output something along these lines
        ```console
        Your Upstash Redis database nodebb-redis is ready.
        Apps in the personal org can connect to at
        redis://default:a2b2e64367fa4b7c8a14f8f8d558f3dc@fly-nodebb-redis.upstash.io
        ```
        - Keep this URL handy!
    - **Create a .dockerignore?** -> No
    - **Deploy now?** -> No
        - We still need to update some config files
3. Run `fly ips allocate-v6`
4. Edit `fly.toml`
    - Change internal_port to 4567. This is the port that NodeBB uses as default.
    - Add the following under `[[services]]`:
```yaml
[[services.ports]]
handlers = ["tls", "http"]
port = 4567
```
1. Run `flyctl deploy`
    - This will build the image.
    - Click the monitoring link, which will open your app’s dashboard on Fly.io

## Remote Setup

1. On the monitoring page, click Overview on the left navbar, and click the purple hostname link. You should now see the NodeBB installer page
2. Enter admin username, email, and password, as usual
3. For database type, select Redis
4. Populate database form. Remember that URL from the initial launch?
    - Host IP or address: the `fly-XXXX-redis.upstash.io` part of the link above
    - Host port: 6379
    - Password: the string between the `:` and `@` of the link
        - Example URL: redis://default:==a2b2e64367fa4b7c8a14f8f8d558f3dc==@^^fly-nodebb-redis.upstash.io^^
        - The underlined text is your host, and highlighted text is your password.
5. Click **Install NodeBB**
6. Monitor deployment back on Fly.io page
7. It will run, and eventually attempt to build the TypeScript files. **Here, it will fail. This is okay!** The free Fly.io instances don’t have enough memory to fully build NodeBB. To get around this, we’ll build NodeBB locally and deploy the compiled files. The steps we’ve completed thus far just served to set up our database correctly.

## Local Setup

1. Run `./nodebb setup` and set it up like usual. No need to run `./nodebb start`
2. The above command will build NodeBB and generate a `config.json` file. We’ll need to edit this so that it matches the `config.json` of our deployed app. 
3. Edit `config.json`
    a. Run `flyctl ssh console` to SSH into your app.
    b. Run `cd usr/src/app`
    c. Run `cat config.json`
    d. Copy the output from the console into your local `config.json` file
4. Next, we’ll update the Dockerfile (which are the instructions Fly.io uses to deploy your app)
    a. Open the `Dockerfile` file in your local NodeBB directory
    b. Update line 25 as follows. We remove the build command from the deployment instructions. This way, we use the build artifacts from our local build.
```Dockerfile
-CMD test -n "${SETUP}" && ./nodebb setup || node ./nodebb build; node ./nodebb start
+CMD test -n "${SETUP}" && ./nodebb setup || node ./nodebb start
```

## Deploy
1. Run `flyctl deploy`
2. Click the monitoring link, which will open your app’s dashboard on Fly.io. Wait until the log output shows that NodeBB was initialized. Click the overview again and open your app!

Congratulations, you have now successfully deployed NodeBB!

Be sure to share the application link with your teammates to ensure they can also access the application and test that all your added features from Project 2 have been successfully applied.
