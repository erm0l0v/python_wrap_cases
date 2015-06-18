from __future__ import unicode_literals
from functools import wraps
from .list_generator import ListGenerator
from .func_generator import FuncGenerator


generators_dict = dict(
    list=ListGenerator,
    func=FuncGenerator
)


def add_generators(*args, **kwargs):
    new_kwargs = dict()
    for key in kwargs:
        if '__' in key:
            generator_name = key.split('__')[1]
            new_key = key.split('__')[0]
            if generator_name in generators_dict:
                new_kwargs[new_key] = generators_dict[generator_name](kwargs[key])
            else:
                new_kwargs[key] = kwargs[key]
        else:
            new_kwargs[key] = kwargs[key]
    return args, new_kwargs


def find_generators(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        new_args, new_kwargs = add_generators(*args, **kwargs)
        return func(*new_args, **new_kwargs)
    return wrapper