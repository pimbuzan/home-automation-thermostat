from datetime import datetime

SENSOR_DUMP = '/sys/bus/w1/devices/28-8000002cd6af/w1_slave'
PATTERN = 't='

class TemperatureSensor:

    def __init__(self):
        self._last_read_val = None
        self._last_read_time = self._timestamp


    def __str__(self):
        fmt_timestamp = datetime.fromtimestamp(self._last_read_time)
        return ("Temperature Sensor:\n"
               "Last read value: {}\n"
               "Last read time: {}".format(self._last_read_val,
                                           fmt_timestamp))


    @property
    def _timestamp(self):
        return datetime.timestamp(datetime.now())


    def read(self):
        self._last_read_val = self._read_tmp()
        self._last_read_time = self._timestamp
        print(self)
        return self._last_read_val


    def _read_tmp(self):
        try:
            with open(SENSOR_DUMP) as f:
                lines = f.read()
                tmp_match = re.search(PATTERN, lines)
                tmp_raw = lines[tmp_match.start()+2:-1]
                return float(tmp_raw) / 1000.0
        except Exception as e:
            print("Internal error: ", e)
            return None
