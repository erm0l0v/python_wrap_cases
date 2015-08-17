from __future__ import unicode_literals
import collections


class BaseGenerator(object):

    dependent = False

    def generate_cases(self, arg_index, key, *args, **kwargs):
        pass

    @staticmethod
    def is_iter(obj):
        return (isinstance(obj, collections.Iterable) and
                not isinstance(obj, basestring))