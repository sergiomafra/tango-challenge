from flask_restful import Resource


class Appointment(Resource):
    '''
    Endpoint description goes here
    '''

    def get(self):
        return {'status': 'ok'}