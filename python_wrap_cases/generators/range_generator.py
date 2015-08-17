from __future__ import unicode_literals
from .base_generator import BaseGenerator


class RangeGenerator(BaseGenerator):

    def __init__(self, args):
        if not (isinstance(args, list) or isinstance(args, tuple)):
            self.range_args = (args, )
        else:
            self.range_args = args

    def generate_cases(self, arg_index, key, *args, **kwargs):
        return range(*self.range_args)