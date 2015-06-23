from __future__ import unicode_literals


class BaseGenerator(object):

    dependent = False

    def generate_cases(self, arg_index, key, *args, **kwargs):
        pass