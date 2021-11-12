# tango-challenge
This repository contains the code for Tango's challenge which is an Appointment API.

## Installation
To run the API locally, first clone the repo to our machine:

    $ git clone https://github.com/sergiomafra/tango-challenge.git

Now move inside the folder and run the command to build and run it:

    $ cd tango-challenge
    $ docker-compose up --build

NOTE: you should have installed Docker and Docker Compos in order to this commands to successfully run.

The API can be reached through the url `http://localhost:5001`.

## Usage
There are two endpoints in this API that can be hit through `curl` or importing the `openapi.yml` file into Swagger or Postman.

### Create new appointment
The endpoint for new appointment creation is:

    /appointment

It should be hit with POST method passing a JSON body with the `user_id` key corresponding to user identification and `date_and_time` key with the corresponding date and time of the appointment in ISO format.

#### Example:

    {
        "user_id": 1,
        "date_and_time": "2021-11-11T14:00"
    }

There is no need to specify the seconds or miliseconds. Appointments can only be made on the hour or half-hour.

### Retrieve appointments for a specific user
In order to retrieve all appointments for one user, the endpoint is:

    /appointment/<user_id>

A list in JSON format with all user appointments will be returned if there is any.

    {
        "appointments_list": [
            "2021-12-11T18:00",
            "2021-12-17T14:00",
            "2021-12-21T09:00"
        ]
    }

All appointments are in ISO format and ordered.