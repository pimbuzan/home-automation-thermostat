from enum import Enum

# this is used to prevent relay rapid switching
MARGIN = 0.5


class Operation(Enum):
    NOOP = 0
    HEAT_ON = 1
    HEAT_OFF = 2

