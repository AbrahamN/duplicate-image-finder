from duplicateimagefinder.enums import *
from duplicateimagefinder.output_formats import human, jsono


def outputter_for_format(fmt):
    if fmt is Formats.HUMAN_READABLE:
        return human.HumanFormat()
    if fmt is Formats.JSON:
        return jsono.JsonFormat()
    else: return human.HumanFormat()
