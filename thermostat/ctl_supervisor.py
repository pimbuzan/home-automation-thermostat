import logging
import time

from redis import Redis
import RPi.GPIO as GPIO
from controller import Controller
from relays import Relay
from sensors import TemperatureSensor
from utils import temperature_formatter as formatter

logging.basicConfig(
    format='%(asctime)s %(levelname)s %(message)s',
    level=logging.DEBUG
)

ctl = Controller(TemperatureSensor(), Relay(GPIO))
db = Redis()


def task_run_controller_loop():
    while True:
        temp = db.get('temp').decode()
        logging.debug(
            'Controller temp threshold={}'.format(formatter(temp))
        )
        sensor_tmp = ctl.temperature
        db.set('sensor_temp', sensor_tmp)
        logging.debug(
            'Sensor temp reading={}'.format(formatter(sensor_tmp))
        )
        ctl.threshold = temp
        ctl.monitor()
        time.sleep(1)


if __name__ == '__main__':
    logging.info('Starting Thermostat Controller')
    task_run_controller_loop()
