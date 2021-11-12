from flask import Flask
from flask_restful import Api

from resources.appointment import AppointmentAPI, AppointmentListAPI


app = Flask(__name__)
api = Api(app)

api.add_resource(AppointmentAPI, '/appointment')
api.add_resource(AppointmentListAPI, '/appointments/<int:id>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
