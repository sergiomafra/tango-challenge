from flask import Flask
from flask_restful import Api

from api.resources.appointment import Appointment


app = Flask(__name__)
api = Api(app)


api.add_resource(Appointment, '/appointment') #, '/appointment/<user:id>')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
