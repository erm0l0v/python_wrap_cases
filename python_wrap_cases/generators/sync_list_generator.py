from __future__ import unicode_literals
from .base_generator import BaseGenerator


class SyncListGenerator(BaseGenerator):

    def __init__(self, collection):
        self.collection = collection
        self.dependent_generators = []

    def __len__(self):
        return len(self.collection)

    def register_dependency(self, arg_index, key, collection):
        self.dependent_generators.append((arg_index, key, collection))

    def generate_cases(self, arg_index, key, *args, **kwargs):
        sync_generators = self.get_sync_generators(*args, **kwargs)
        size = min(list(map(len, sync_generators)) + [len(self)])
        for generator in sync_generators:
            generator.register_dependency(arg_index, key, self.collection)
        index = self.get_current_index(*args, **kwargs)
        if index is not None:
            return [self.collection[index]]
        else:
            return self.collection[:size]

    def get_sync_generators(self, *args, **kwargs):
        sync_generators = []
        for arg in args:
            if isinstance(arg, self.__class__) and arg is not self:
                sync_generators.append(arg)
        for arg in kwargs.values():
            if isinstance(arg, self.__class__) and arg is not self:
                sync_generators.append(arg)
        return sync_generators

    def get_current_index(self, *args, **kwargs):
        if not self.dependent_generators:
            return None
        arg_index, key, collection = self.dependent_generators[0]
        if arg_index is not None:
            value = args[arg_index]
        else:
            value = kwargs[key]
        return collection.index(value)