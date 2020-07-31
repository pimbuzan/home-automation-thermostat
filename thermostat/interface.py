import multiprocessing
import time

from redis import Redis
from flask import Flask, jsonify


db = Redis()
app = Flask(__name__)


@app.route('/config/read/', methods=["GET"])
def read_tmp():
    message = "Thermostat temperature is set to: {}".format(db.get('temp'))
    return jsonify({'message': message})


@app.route('/config/<float:temp>/', methods=["POST"])
def config(temp):
    db.set('temp', temp)
    message = "Thermostat temperature set to: {}".format(temp)
    return jsonify({'message': message})


if __name__ == "__main__":
    app.run(host='0.0.0.0')
