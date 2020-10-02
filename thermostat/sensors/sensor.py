from datetime import datetime
import re

SENSOR_DUMP = '/sys/bus/w1/devices/28-8000002cd6af/w1_slave'
PATTERN = 't='


class TemperatureSensor(object):

    def __init__(self):
        self._last_read_val = None
        self._last_read_time = self._timestamp

    def __str__(self) -> str:
        fmt_timestamp = datetime.fromtimestamp(self._last_read_time)
        ftm_read_val = format(self._last_read_val, '.1f')
        return ("Temperature Sensor:\n"
                "Last read value: {}\n"
                "Last read time: {}".format(ftm_read_val,
                                            fmt_timestamp))

    @property
    def _timestamp(self) -> float:
        return datetime.timestamp(datetime.now())

    def read(self) -> float:
        self._last_read_val = self._read_tmp()
        self._last_read_time = self._timestamp
        return self._last_read_val

    def _read_tmp(self) -> float:
        try:
            with open(SENSOR_DUMP) as f:
                lines = f.read()
                tmp_match = re.search(PATTERN, lines)
                tmp_raw = lines[tmp_match.start()+2:-1]
                return float(tmp_raw) / 1000.0
        except AttributeError:
            raise Exception(
                'Temperature sensor dump location or pattern is invalid: {}'.format(SENSOR_DUMP))
