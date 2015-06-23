from __future__ import unicode_literals


class ArgumentsCollection(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        arguments = list(map(repr, self.args))
        keys = sorted(self.kwargs.keys())
        arguments = arguments + ['{0}({1})'.format(str(key), repr(self.kwargs[key])) for key in keys]
        return '_'.join(arguments)