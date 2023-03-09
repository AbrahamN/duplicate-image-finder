from types import *
from typing import List
import sys

from duplicateimagefinder.output_formats.base import BaseFormatter, OutputRecord


class HumanFormat(BaseFormatter):
    def output(self, data):
        assert type(data) == list, "data is not a list"

        if not len(data):
            print("No results.")
            return

        # List the images that are similar to each other
        for similar in data:
            assert type(similar).__name__ == OutputRecord.__name__, "record is not instance of OutputRecord"
            sys.stdout.old_write("%s is %d%% similar to %s\n" % (
                similar.image1, similar.similarity_pct, similar.image2
            ))
            sys.stdout.flush()
