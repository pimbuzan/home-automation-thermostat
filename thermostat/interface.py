import multiprocessing
import time

from redis import Redis
from flask import Flask, jsonify
import RPi.GPIO as GPIO

from controller import Controller
from relays.relay import Relay
from sensors import TemperatureSensor

ctl = Controller(TemperatureSensor(), Relay(GPIO))
db = Redis()
app = Flask(__name__)


def task_run_controller_loop():
    while True:
        temp = db.get('temp')
        ctl.threshold = temp
        time.sleep(1)
        ctl.monitor()


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
    loop = multiprocessing.Process(target=task_run_controller_loop)
    loop.start()
    app.run(host='0.0.0.0')
