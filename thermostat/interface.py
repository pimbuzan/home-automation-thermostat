import multiprocessing
import time

from redis import Redis
from flask import Flask, jsonify


db = Redis()
app = Flask(__name__)


@app.route('/sensor/read/', methods=['GET'])
def read_sensor():
    message = 'Thermostat sensor reads: {} C'.format(db.get('sensor_temp'))
    return jsonify({'message': message})


@app.route('/config/read/', methods=['GET'])
def read_config():
    message = 'Thermostat temperature is set to: {} C'.format(db.get('temp'))
    return jsonify({'message': message})


@app.route('/config/<float:temp>/', methods=['POST'])
def config(temp):
    db.set('temp', temp)
    message = 'Thermostat temperature set to: {} C'.format(temp)
    return jsonify({'message': message})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
