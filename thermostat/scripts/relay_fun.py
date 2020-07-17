import time
import RPi.GPIO as GPIO

PIN = 12


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN, GPIO.OUT)


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
