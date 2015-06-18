from __future__ import unicode_literals
from .argumets_collection import ArgumentsCollection


class TestCasesWrapper(object):

    def __init__(self):
        self.cases = []

    def append_case(self, *args, **kwargs):
        arguments_collection = ArgumentsCollection(*args, **kwargs)
        self.cases.append(arguments_collection)