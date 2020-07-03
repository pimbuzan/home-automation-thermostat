from controller import Controller

import sys
import multiprocessing
import time

from redis import Redis


from flask import Flask, request

ctl = Controller()
r = Redis()

app = Flask(__name__)

def task_run_controller_loop():
    while True:
        try:
            temp = r.get('temp')
            ctl.threshold = temp
            time.sleep(1)
            ctl.handle_threshold_update()
        except Exception as e:
            print(e)


@app.route('/start')
def start_thermostat():
    print('starting this whole thing up')
    p2 = multiprocessing.Process(target=task_run_controller_loop)
    p2.daemon = True
    p2.start()
    return "The controller started in the background"

    

@app.route('/config/<float:temp>', methods=["POST"])
def config(temp):
    r.set('temp', temp)
    return "Thermostat temperature set to: {}".format(temp)

