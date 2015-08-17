from __future__ import unicode_literals
from functools import wraps
from mock import MagicMock


class TestCaseMeta(type):

    def __new__(mcs, name, bases, attributes):
        return super(TestCaseMeta, mcs).__new__(mcs, name, bases, mcs.replace_methods(attributes))

    @classmethod
    def replace_methods(mcs, attributes):
        new_args = dict()
        for arg_key in attributes:
            if not hasattr(attributes[arg_key], 'test_cases_wrapper'):
                new_args[arg_key] = attributes[arg_key]
            else:
                new_args.update(mcs.get_cases(arg_key, attributes[arg_key]))
        return new_args

    @classmethod
    def get_cases(mcs, function_name, function):
        case_methods = dict()
        wrapper = getattr(function, 'test_cases_wrapper')
        cases = wrapper.cases
        for case in cases:
            new_name, new_function = mcs.get_case(function_name, case, function)
            case_methods[new_name] = new_function
        return case_methods

    @classmethod
    def get_case(mcs, function_name, case, function):
        @wraps(function)
        def wrap_function(self, *args, **kwargs):
            arg_wrapper = ArgumentWrapper(case.args, case.kwargs)
            new_argument_list, new_argument_dict = arg_wrapper.wrap_function(function)
            new_argument_list = new_argument_list + args
            new_argument_dict.update(kwargs)
            return function(self, *new_argument_list, **new_argument_dict)
        return '{0}_{1}'.format(function_name, str(case)), wrap_function


class ArgumentWrapper(object):

    def __init__(self, arguments_list, arguments_dict):
        self.__arguments_list = arguments_list
        self.__arguments_dict = arguments_dict

    def wrap_function(self, function):
        if 'patchings' not in function.__dict__:
            return self.__arguments_list, self.__arguments_dict
        new_argument_list_index = 0
        removed_argument_dict = set()
        patchings = function.__dict__.get('patchings')
        removed_argument_dict, new_argument_list_index = self.__wrap_patchings(patchings, removed_argument_dict, new_argument_list_index)
        new_argument_list = self.__arguments_list[new_argument_list_index:]
        new_argument_dict = dict()
        for arg_key in self.__arguments_dict:
            if arg_key not in removed_argument_dict:
                new_argument_dict[arg_key] = self.__arguments_dict[arg_key]
        return new_argument_list, new_argument_dict

    def __wrap_patchings(self, patchings, removed_argument_dict, new_argument_list_index):
        for patch in patchings:
            if patch.attribute_name and patch.attribute_name in self.__arguments_dict:
                patch.new = MagicMock()
                patch.new.return_value = self.__arguments_dict.get(patch.attribute_name)
                removed_argument_dict.add(patch.attribute_name)
            elif len(self.__arguments_list) > new_argument_list_index:
                patch.new = MagicMock()
                patch.new.return_value = self.__arguments_list[new_argument_list_index]
                new_argument_list_index += 1
            if patch.additional_patchers:
                removed_argument_dict, new_argument_list_index = self.__wrap_patchings(patch.additional_patchers,
                                                                                       removed_argument_dict,
                                                                                       new_argument_list_index)
        return removed_argument_dict, new_argument_list_index