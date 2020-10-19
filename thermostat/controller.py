from constants import Operation, MARGIN

from relays import Relay
from sensors import TemperatureSensor
from utils.decorators import log_new_operation


class Controller:
    """
    Purpose:
        This object should operate the Relay and the Temp Sensor
        Read / Set the threshold value
        Open / Close the relay based on the threshold temperature
    """

    def __init__(self, temp_sensor: TemperatureSensor, relay: Relay):
        self._temp_sensor = temp_sensor
        self._relay = relay
        self._threshold = None
        self._last_op = None

    @property
    def last_operation(self):
        return self._last_op

    @last_operation.setter
    def last_operation(self, last_op):
        self._last_op = last_op

    @property
    def threshold(self):
        return self._threshold

    @threshold.setter
    def threshold(self, value: float) -> None:
        self._threshold = float(value)

    @property
    def temperature(self) -> float:
        return self._temp_sensor.read()

    def monitor(self):
        """
        Purpose:
            This method checks the threshold value and the current temperature
            reading from the sensor and calls the next operation

        Raises Exception if the threshold value is not set
        """
        if not self.threshold:
            raise Exception("Set a Threshold value first")
        if not self.temperature:
            # wait for sensor valid reading
            self._operation_handler(Operation.NOOP)
        self._next_operation(self.temperature)

    def _next_operation(self, temperature):
        """
        Purpose:
            This method checks if the temperature is higher or lower than the threshold value
            and determines what is the next operation handler
        """
        if temperature > self.threshold + MARGIN:
            self._operation_handler(Operation.HEAT_OFF)
        elif temperature < self.threshold - MARGIN:
            self._operation_handler(Operation.HEAT_ON)
        else:
            self._operation_handler(Operation.NOOP)

    @log_new_operation
    def _operation_handler(self, operation: Operation):
        """Accepts an operation object and runs an action mapped to that operation"""
        actions = {
            0: self._action_noop,
            1: self._action_start_heat,
            2: self._action_stop_heat,
        }
        action = actions.get(operation.value, self._action_noop)
        action()

    def _action_start_heat(self):
        self._relay.close_conn()

    def _action_stop_heat(self):
        self._relay.open_conn()

    def _action_noop(self):
        pass
