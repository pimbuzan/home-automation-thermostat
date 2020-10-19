"""
This module is used to format the temperature retrieved from redis
to a human readable value, limiting floats to one decimal point
"""


def convert_to_human_readable(temperature: str):
    return "{:.1f}".format(float(temperature))
