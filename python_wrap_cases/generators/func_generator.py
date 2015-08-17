from __future__ import unicode_literals
from .base_generator import BaseGenerator


class FuncGenerator(BaseGenerator):

    def __init__(self, func):
        self.func = func

    def generate_cases(self, arg_index, key, *args, **kwargs):
        result = self.func()
        if not (isinstance(result, list) or isinstance(result, tuple)):
            result = [result]
        return result