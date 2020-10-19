from typing import Dict

from utils import temperature_formatter as formatter

from redis import Redis
from flask import Flask, jsonify, request

db = Redis()
app = Flask(__name__)


@app.route('/sensor/read/', methods=['GET'])
def read_sensor() -> Dict[str, str]:
    message = 'The thermostat sensor reads: {} degrees celsius'.format(
        formatter(db.get('sensor_temp').decode()))
    return jsonify({'message': message})


@app.route('/config/read/', methods=['GET'])
def read_config() -> Dict[str, str]:
    message = 'The thermostat temperature is set to: {} degrees celsius'.format(
        formatter(db.get('temp').decode()))
    return jsonify({'message': message})


@app.route('/config/', methods=['POST'])
def config() -> Dict[str, str]:
    temp = request.json.get('temperature')
    db.set('temp', temp)
    message = 'Thermostat temperature set to: {} degrees celsius'.format(temp)
    return jsonify({'message': message})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
