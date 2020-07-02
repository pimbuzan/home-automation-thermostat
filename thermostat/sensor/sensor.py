import re
from time import sleep

SENSOR_DUMP = '/sys/bus/w1/devices/28-8000002cd6af/w1_slave'
PATTERN = 't='

def read_tmp():
    try:
        with open(SENSOR_DUMP) as f:
            tmp_raw = f.read()
            tmp_match = re.search(PATTERN, tmp_raw)
            tmp = tmp_raw[tmp_match.start()+2:-1]
    except Exception as e:
        print("Internal error: ", e)
    return tmp


def run():
    while True:
        try:
            tmp = read_tmp()
            print("TTemperature is: ", float(tmp))
            sleep(5)
        except:
            break


if __name__ == "__main__":
    print("Starting temperature gathering")
    run()