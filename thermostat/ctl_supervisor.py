import logging
import time

from redis import Redis
import RPi.GPIO as GPIO

from controller import Controller
from relays.relay import Relay
from sensors import TemperatureSensor

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
    level=logging.DEBUG
)

ctl = Controller(TemperatureSensor(), Relay(GPIO))
db = Redis()


def task_run_controller_loop():
    while True:
        temp = db.get('temp')
        logging.debug(
            'Controller temp threshold={}'.format(temp)
        )
        logging.debug(
            'Sensor temp reading={}'.format(ctl.temperature)
        )
        ctl.threshold = temp
        ctl.monitor()
        time.sleep(1)


if __name__ == '__main__':
    logging.info('Starting Thermostat Controller')
    task_run_controller_loop()
