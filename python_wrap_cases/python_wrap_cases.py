from .decorators import TestCaseDecorator
from .metaclasses import TestCaseMeta
from pip._vendor import six


__all__ = ['WrapCasesMixin', 'wrap_case']


@six.add_metaclass(TestCaseMeta)
class WrapCasesMixin(object):
    pass


wrap_case = TestCaseDecorator