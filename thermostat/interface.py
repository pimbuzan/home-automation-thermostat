import multiprocessing
import time

from redis import Redis
from flask import Flask

from controller import Controller

ctl = Controller()
db = Redis()
app = Flask(__name__)


def task_run_controller_loop():
    while True:
        try:
            temp = db.get('temp')
            ctl.threshold = temp
            time.sleep(1)
            ctl.observe()
        except Exception as e:
            print(e)


@app.route('/config/<float:temp>', methods=["POST"])
def config(temp):
    db.set('temp', temp)
    return "Thermostat temperature set to: {}".format(temp)


if __name__ == "__main__":
    loop = multiprocessing.Process(target=task_run_controller_loop)
    loop.start()
    app.run(host='0.0.0.0')
