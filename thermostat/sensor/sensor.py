import re
from time import sleep

SENSOR_DUMP = '/sys/bus/w1/devices/28-8000002cd6af/w1_slave'
PATTERN = 't='

def read_tmp():
    try:
        with open(SENSOR_DUMP) as f:
            lines = f.read()
            tmp_match = re.search(PATTERN, lines)
            tmp_raw = lines[tmp_match.start()+2:-1]
    except Exception as e:
        print("Internal error: ", e)
    tmp_str = '.'.join((tmp_raw[:2], tmp_raw[-2]))
    return '{:.1f}'.format(tmp_str)


def run():
    while True:
        try:
            tmp = read_tmp()
            print("Temperature is: ", tmp)
            sleep(5)
        except:
            break


if __name__ == "__main__":
    print("Starting temperature gathering")
    run()