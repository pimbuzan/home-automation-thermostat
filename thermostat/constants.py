from enum import Enum

# this is used to prevent relay rapid switching
# a thermostat with hysteresis will not switch until the temperature has changed
# a little past the set temperature point
MARGIN = 0.5


class Operation(Enum):
    NOOP = 0
    HEAT_ON = 1
    HEAT_OFF = 2


class Conditions(Enum):
    HEAT_OFF = "temperature > threshold + MARGIN"
    HEAT_ON = "temperature < threshold - MARGIN"

