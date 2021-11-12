# Docker image
FROM python:3.9-bullseye

# ENV variables
ENV ROOT=/tango-challenge
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# Preparing the container
RUN mkdir $ROOT
WORKDIR $ROOT
COPY ./requirements.txt .
RUN pip install -r requirements.txt --disable-pip-version-check

# Running the app
ENTRYPOINT ["python"]
CMD ["api/app.py"]