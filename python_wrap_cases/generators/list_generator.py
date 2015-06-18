from __future__ import unicode_literals
from .base_generator import BaseGenerator


class ListGenerator(BaseGenerator):

    def __init__(self, collection):
        self.collection = collection

    def generate_cases(self, *args, **kwargs):
        return self.collection