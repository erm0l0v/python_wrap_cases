from __future__ import unicode_literals
from functools import wraps
from unittest import TestCase
from .case_wrapper import TestCasesWrapper
from .metaclasses import TestCaseMeta
import six


class TestCaseDecorator(object):

    def __new__(cls, *args, **kwargs):
        if args and type(args[0]) == type and issubclass(args[0], TestCase):
            return six.add_metaclass(TestCaseMeta)(args[0])
        return super(TestCaseDecorator, cls).__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        self.__args = args
        self.__kwargs = kwargs

    def __call__(self, method):
        @wraps(method)
        def wrap_function(*args, **kwargs):
            return method(*args, **kwargs)
        wrapper_name = 'test_cases_wrapper'
        if hasattr(method, wrapper_name):
            case_wrapper = getattr(method, wrapper_name)
            setattr(wrap_function, wrapper_name, case_wrapper)
        else:
            case_wrapper = TestCasesWrapper()
            setattr(wrap_function, wrapper_name, case_wrapper)
        case_wrapper.append_case(*self.__args, **self.__kwargs)
        return wrap_function