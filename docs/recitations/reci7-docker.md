
# Recitation 7:  Microservices and Docker

## Prerequisites

You should have downloaded Docker. If you haven't follow the installation instructions [here](https://docs.docker.com/get-docker/)
 
## Setup Instructions (10 min): 

Fork [this repo](https://github.com/CMU-313/s23-docker-recitation) and clone it.
Also start the docker engine.
 
## Overview

During this recitation, students will create a simple FastAPI app, containerize it and deploy it.
 
## Context

Sadly, you still are unsure when your recitation time is AND who your TAs are. There exist a microservice that tells you which TA's are responsible for each section.

Try it out using this link: [https://whos-my-ta.fly.dev/section_id/a](https://whos-my-ta.fly.dev/section_id/a)

All you have to do is create another service that return the time of the recitation as well.

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

1. Implement the `section_info` endpoint according to specifications. You can edit `app/main.py` to do so.
2. Test it by running the app locally.
To install necessary files:
```terminal
pip install -r requirement.txt
```

To run the app locally:
```terminal
uvicorn app.main:app --host 0.0.0.0 --port 8080
```
Change the port number if you need to.

3. Implement `./Dockerfile`. You can use the slides and [this link](https://docs.docker.com/engine/reference/builder/) as resources.
4. Create the docker image using the command below, and check the image has been created.
```terminal
docker build -t YOUR_IMAGE_NAME  .
```
5. Implement `./docker-compose.yml`. You can use the slides for reference.
6. Create a container using the docker image using the command below.
```terminal
docker-compose up -d 
```
7. Check the your container is running correctly by locally invoking the endpoint.
You can try [http://localhost:8080/section_id/a](http://localhost:8080/section_id/a).
Change the port number (8080) according to your `docker-compose.yml`.
 
## Bonus

Try deploying your container using instructions from [here](https://fly.io/docs/languages-and-frameworks/dockerfile/).
