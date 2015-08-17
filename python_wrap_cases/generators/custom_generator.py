from __future__ import unicode_literals
from .base_generator import BaseGenerator


class CustomGenerator(BaseGenerator):

    def __init__(self, func):
        self.func = func

    dependent = True

    def generate_cases(self, arg_index, key, *args, **kwargs):
        result = self.func(*args, **kwargs)
        if not self.is_iter(result):
            result = [result]
        return result