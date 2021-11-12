from flask_restful import Resource, reqparse

from datetime import datetime


data = {}


class AppointmentAPI(Resource):
    '''
    Endpoint responsable for appointment creation with validation.

    Endpoint URL: <base_url>/appointment

    Required fields for incoming data:
        user_id (int): The id of the user
        date_and_time (str): The date and the time for the appointment in ISO
                             format.

    Example of JSON raw data:
    {
        "user_id": 1,
        "date_and_time": "2021-11-12T14:00"
    }
    '''

    def _validate_date_and_time(self, date_and_time):
        try:
            date_and_time_obj = datetime.strptime(
                                date_and_time,
                                '%Y-%m-%dT%H:%M')
        except ValueError as ve:
            return {'message': f'Invalid date and time: {ve}'}, 400
        except Exception as e:
            return {'message': f'Something went wrong: {e}'}, 400

        minutes = date_and_time_obj.minute
        if minutes not in [0, 30]:
            return {
                'message': (f'Invalid minutes: {minutes}. You can only request'
                            ' an appointment on the hour or half-hour.')
                }

        return date_and_time_obj

    def post(self):
        reqparser = reqparse.RequestParser()
        reqparser.add_argument(
            'user_id',
            type=int,
            location='json',
            required=True)
        reqparser.add_argument(
            'date_and_time',
            type=str,
            location='json',
            required=True)
        args = reqparser.parse_args()

        user_id = args.user_id
        date_and_time = self._validate_date_and_time(args.date_and_time)
        if type(date_and_time) is not datetime:
            return date_and_time
        else:
            date = date_and_time.strftime('%Y-%m-%d')
            time = date_and_time.strftime('%H:%M')

        if user_id in data.keys():
            if date in data[user_id]:
                return {'message': 'This date is already taken.'}, 400
            else:
                data[user_id][date] = time
        else:
            data[user_id] = {date: time}

        return {'message': 'Appointment scheduled successfully!'}, 201


class AppointmentListAPI(Resource):
    '''
    Endpoint responsable for retrieving all user's appointment.

    Endpoint URL: /appointment/<user_id>

    params:
        user_id (int): The id of the user
    '''

    def get(self, id):
        if id in data.keys():
            appointments = []
            for key in data[id]:
                appointments.append(f'{key}T{data[id][key]}')
            return {'appointments_list': sorted(appointments)}
        return {'message': 'User does not exist.'}
