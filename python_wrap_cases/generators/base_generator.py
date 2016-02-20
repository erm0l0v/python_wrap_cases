"""
Module with base generator
"""
from __future__ import unicode_literals
import collections
from six import string_types


class BaseGenerator(object):
    """
    Base class for all generators
    """

    dependent = False

    def generate_cases(self, arg_index, key, *args, **kwargs):
        """
        Generate test case. This method must be implement in all generators
        :param arg_index: index of current element position
            in argument in wrap_case. Use it to parse arg
        :type arg_index: int
        :param key: key word of current argument.
            Use it to parse kwargs
        :param args: all wrap_case arguments
        :type args: list
        :param kwargs: all named arguments in wrap_case
        :type kwargs: dict
        :return: List of new argument that should be used instead of this one
        :rtype: list
        """
        pass

    @staticmethod
    def is_iter(obj):
        """
        Check is object are iterable
        :param obj: some object
        :type obj: any
        :return: is object are iterable
        :rtype: bool
        """
        return (isinstance(obj, collections.Iterable) and
                not isinstance(obj, string_types))
