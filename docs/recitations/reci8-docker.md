# Recitation 8: Microservices and Docker

## Prerequisites

You should have downloaded Docker. If you haven't follow the installation instructions [here](https://docs.docker.com/get-docker/)

## Setup Instructions (10 min):

Fork [this repo](https://github.com/CMU-313/f25-docker-recitation) and clone it.

Open the folder in VSCode.  Then you should "reopen in continer" similar to NodeBB, but this container is setup for python.

Also start the docker engine.

## Overview

During this recitation, students will create a simple FastAPI app, containerize it and deploy it.

## Context

Sadly, you still are unsure when your recitation time is AND who your TAs are. There exist a microservice that tells you which TA's are responsible for each section.

Try it out using this link: [http://17313-teachers2.s3d.cmu.edu:8080/section_info/a](http://17313-teachers2.s3d.cmu.edu:8080/section_info/a)

All you have to do is build a new service that builds on top of this microservice by including the time of the recitation as well.

The endpoint has to return a JSON object in the following form:

```json
{
  "section": "section_name",
  "start_time": "HH:MM",
  "end_time": "HH:MM",
  "ta": ["taName1", "taName2"]
}
```

## Activity

1. Implement the `section_info` endpoint according to the specifications. You can edit `app/main.py` to do so.
2. Test it by running the app locally.
   To install necessary files:

   ```terminal
   pip install -r requirements.txt
   ```

3. To run the app locally use the following command:

   ```terminal
   uvicorn app.main:app --host 0.0.0.0 --port 8080
   ```

4. Implement `./Dockerfile`. You can use the slides and [this link](https://docs.docker.com/engine/reference/builder/) as resources.
5. Create the docker image using the command below, and check that the image has been created.

   ```terminal
   docker build -t YOUR_IMAGE_NAME  .
   ```

6. Try running your image (it should work similarly to when you run the app locally.
   ```terminal
   docker run --rm -p 8080:8080 YOUR_IMAGE_NAME
   ```

7. Implement `./docker-compose.yml`. You can use the slides for reference.
8. Create a container using the docker image using the command below.

   ```terminal
   docker compose up -d --build
   ```

10. Check that your container is running correctly by locally invoking the endpoint.
   You can try [http://localhost:8080/section_info/a](http://localhost:8080/section_info/a).
    You should receive a JSON response with the section name, and TA names. Your job is to implement the start time and end time for all the recitations.

## Bonus

Try deploying your container by running it in codespaces

## Submission: 
Make sure to [Submit on Gradescope](https://www.gradescope.com/courses/1086939/assignments/7049021/submissions) after this recitation. Everyone should submit individually.
