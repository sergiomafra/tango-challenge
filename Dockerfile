# Docker image
FROM python:latest

# Exposing port
EXPOSE 5000

# ENV variables
ENV ROOT=/tango-challenge
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# Preparing the container
RUN mkdir $ROOT
COPY . $ROOT
WORKDIR $ROOT
RUN pip install -r requirements.txt --disable-pip-version-check
