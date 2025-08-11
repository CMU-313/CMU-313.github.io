FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye
ARG DEBIAN_FRONTEND=noninteractive
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
