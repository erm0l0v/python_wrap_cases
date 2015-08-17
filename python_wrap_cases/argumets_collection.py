from __future__ import unicode_literals


class ArgumentsCollection(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    @staticmethod
    def argument_to_str(arg):
        try:
            return str(arg)
        except UnicodeError:
            return repr(arg)

    def __str__(self):
        arguments = list(map(repr, self.args))
        keys = sorted(self.kwargs.keys())
        arguments = arguments + ['{0}({1})'.format(str(key), self.argument_to_str(self.kwargs[key])) for key in keys]
        return '_'.join(arguments)