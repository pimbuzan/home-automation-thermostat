import time
import atexit

import RPi.GPIO as GPIO

PIN = 12
ON = 'closed'
OFF = 'open'

class Relay:
    
    def __init__(self):
        # setup GPIO pinout
        setup()
        self._state = None

    def open_conn(self):
        # off
        # opens circuit
        if not self.state == OFF:
            self.state = OFF
            GPIO.output(PIN, False)
            print('Relay: opening circuit')
            return
        return
    
    def close_conn(self):
        # on
        # close circuit
        if not self.state == ON:
            self.state = ON
            GPIO.output(PIN, True)
            print('Relay: closing circuit')
            return
        return
    
    
    @property
    def state(self):
        return self._state


    @state.setter
    def state(self, op):
        self._state = op


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN, GPIO.OUT)


def cleanup():
    GPIO.cleanup()


atexit.register(cleanup)
