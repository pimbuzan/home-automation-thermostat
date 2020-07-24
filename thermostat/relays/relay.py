import atexit

PIN = 12
ON = 'closed'
OFF = 'open'


class Relay(object):

    def __init__(self, gpio):
        # setup GPIO pinout
        self._gpio = self.setup(gpio)
        self._state = None

    def open_conn(self):
        # off
        # opens circuit
        if not self.state == OFF:
            self.state = OFF
            self._gpio.output(PIN, False)
            print('Relay: opening circuit')
            return
        return

    def close_conn(self):
        # on
        # close circuit
        if not self.state == ON:
            self.state = ON
            self._gpio.output(PIN, True)
            print('Relay: closing circuit')
            return
        return

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, op_state):
        self._state = op_state

    @staticmethod
    def setup(gpio):
        gpio.setmode(gpio.BOARD)
        gpio.setup(PIN, gpio.OUT)
        return gpio


def cleanup():
    try:
        import RPi.GPIO as GPIO
        GPIO.cleanup()
    except RuntimeError:
        # This module can only be run on a Raspberry Pi
        pass


atexit.register(cleanup)
