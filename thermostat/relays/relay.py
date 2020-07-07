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
        print('Relay: doing nothing')
        return
    
    def close_conn(self):
        # on
        # close circuit
        if not self.state == ON:
            self.state = ON
            GPIO.output(PIN, True)
            print('Relay: closing circuit')
            return
        print('Relay: doing nothing')
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

def play():
    sleep_time = 1.0
    loop_count = 0
    while True:
        try:
            if loop_count % 5 == 0 and sleep_time > 0.3:
                sleep_time -= 0.2
                print(sleep_time)
            print('Loop no: ', loop_count)
            GPIO.output(PIN, True)
            time.sleep(sleep_time)
            GPIO.output(PIN, False)
            time.sleep(sleep_time)
            loop_count += 1
        except (KeyboardInterrupt, Exception) as e:
            print(e)
            GPIO.cleanup()
            break


if __name__ == "__main__":
    print('RUN')
    setup()
    play()

atexit.register(cleanup)
