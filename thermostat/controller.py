from enum import Enum

# this is used to prevent relay rapid switching
MARGIN = 0.5


class Operation(Enum):
    NOOP = 0
    HEAT_ON = 1
    HEAT_OFF = 2


class Controller(object):
    """
    This object should operate the Relay and the Temp Sensor
    Read / Set the threshold value
    Open / Close the relay based on the threshold temperature
    """

    def __init__(self, tmp_sensor, relay):
        self._tmp_sensor = tmp_sensor
        self._relay = relay
        self._threshold = None
        self._last_op = None

    @property
    def threshold(self):
        return self._threshold

    @threshold.setter
    def threshold(self, value):
        self._threshold = float(value)

    @property
    def temperature(self):
        return self._tmp_sensor.read()

    def monitor(self):
        # Check if the threshold is above the current read temperature
        # Case current read temperature < threshold:
        # - start heating
        # Case current read temperature > threshold:
        # - stop heating
        if not self.threshold:
            raise Exception("Set a Threshold value first")
        if not self.temperature:
            # wait for sensor valid reading
            self._operation_handler(Operation.NOOP)
        elif self.temperature > self.threshold + MARGIN:
            self._operation_handler(Operation.HEAT_OFF)
        elif self.temperature < self.threshold - MARGIN:
            self._operation_handler(Operation.HEAT_ON)
        else:
            self._operation_handler(Operation.NOOP)

    def _operation_handler(self, operation):
        """Accepts an operation object and runs an action mapped to that operation"""
        operations = {
            0: self._action_noop,
            1: self._action_start_heat,
            2: self._action_stop_heat,
        }
        action = operations.get(operation.value, self._action_noop)
        if self._last_op != operation.value:
            self._last_op = operation.value
            print('Running operation: %s' % operation.name)
        action()

    def _action_start_heat(self):
        self._relay.close_conn()

    def _action_stop_heat(self):
        self._relay.open_conn()

    def _action_noop(self):
        pass
