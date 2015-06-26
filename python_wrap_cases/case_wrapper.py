from __future__ import unicode_literals
from python_wrap_cases.argumets_collection import ArgumentsCollection
from python_wrap_cases.generators.base_generator import BaseGenerator
from python_wrap_cases.generators.generatorst_factory import find_generators


def find_contain_generator(*args, **kwargs):
    result = None
    for arg in args:
        if isinstance(arg, BaseGenerator):
            return args.index(arg), None, arg
    for key in kwargs:
        if isinstance(kwargs[key], BaseGenerator):
            if not result and kwargs[key].dependent:
                result = None, key, kwargs[key]
            else:
                return None, key, kwargs[key]
    if result:
        return result
    return None, None, None


def generate_params(arg_index, key, generator, *args, **kwargs):
    args_collection = list()
    included_args = generator.generate_cases(arg_index, key, *args, **kwargs)
    for included_arg in included_args:
        new_args = [a for a in args]
        new_kwargs = kwargs.copy()
        if key:
            new_kwargs[key] = included_arg
        else:
            new_args[arg_index] = included_arg
        args_collection.append((new_args, new_kwargs))
    return args_collection


class TestCasesWrapper(object):

    def __init__(self):
        self.cases = []

    @find_generators
    def append_case(self, *args, **kwargs):
        arg_index, key, generator = find_contain_generator(*args, **kwargs)
        if generator:
            args_collection = generate_params(arg_index, key, generator, *args, **kwargs)
            for new_args, new_kwargs in args_collection:
                self.append_case(*new_args, **new_kwargs)
        else:
            arguments_collection = ArgumentsCollection(*args, **kwargs)
            self.cases.append(arguments_collection)