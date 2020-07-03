from datetime import datetime

from sensors.script import read_tmp

class TemperatureSensor:

    def __init__(self, timeout=5):
        self._last_read_val = None
        self._last_read_time = self._timestamp
        self._timeout = timeout


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
        if self._last_read_time + self._timeout < self._timestamp:
            self._last_read_val = read_tmp()
            self._last_read_time = self._timestamp 
        return self._last_read_val
    

