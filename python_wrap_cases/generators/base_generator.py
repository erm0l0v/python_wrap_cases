from __future__ import unicode_literals


class BaseGenerator(object):

    dependent = False

    def generate_cases(self, *args, **kwargs):
        pass