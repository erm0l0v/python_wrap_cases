from __future__ import unicode_literals
from .base_generator import BaseGenerator


class CustomGenerator(BaseGenerator):

    def __init__(self, func):
        self.func = func

    dependent = True

    def generate_cases(self, *args, **kwargs):
        result = self.func(*args, **kwargs)
        if not (isinstance(result, list) or isinstance(result, tuple)):
            result = [result]
        return result