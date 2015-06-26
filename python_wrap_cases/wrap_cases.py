from python_wrap_cases.decorators import TestCaseDecorator
from python_wrap_cases.metaclasses import TestCaseMeta
from pip._vendor import six


__all__ = ['WrapCasesMixin', 'wrap_case']


@six.add_metaclass(TestCaseMeta)
class WrapCasesMixin(object):
    pass


wrap_case = TestCaseDecorator