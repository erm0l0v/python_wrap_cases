from __future__ import unicode_literals
import unittest
from mock import patch, DEFAULT
from python_wrap_cases import *
from tests.cases.base_case import BaseCase


class TestedClass():

    def foo_a(self):
        pass

    def foo_b(self):
        pass

    def tested_method(self):
        return self.foo_a() + self.foo_b()


class DecoratorWithPatchMultiple(unittest.TestCase, WrapCasesMixin):

    @patch.multiple(TestedClass, foo_a=DEFAULT, foo_b=DEFAULT)
    def test_method(self, foo_a, foo_b):
        foo_a.return_value = 2
        foo_b.return_value = 2
        tested_class = TestedClass()
        self.assertEqual(tested_class.tested_method(), 4)

    @wrap_case(foo_a=2, foo_b=2)
    @patch.multiple(TestedClass, foo_a=DEFAULT, foo_b=DEFAULT)
    def test_method_with_test_case(self):
        tested_class = TestedClass()
        self.assertEqual(tested_class.tested_method(), 4)

    @wrap_case(foo_a=2, foo_b=2, result=4)
    @wrap_case(foo_a=3, foo_b=3, result=6)
    @wrap_case(foo_a=4, foo_b=4, result=8)
    @patch.multiple(TestedClass, foo_a=DEFAULT, foo_b=DEFAULT)
    def test_method_with_test_cases(self, result):
        tested_class = TestedClass()
        self.assertEqual(tested_class.tested_method(), result)

    @wrap_case(foo_a=2, result=4)
    @wrap_case(foo_a=4, result=6)
    @wrap_case(foo_a=8, result=10)
    @patch.multiple(TestedClass, foo_a=DEFAULT, foo_b=DEFAULT)
    def test_method_test_case_only_for_one_argument(self, result, foo_b):
        foo_b.return_value = 2
        tested_class = TestedClass()
        self.assertEqual(tested_class.tested_method(), result)


class DecoratorWithPatchMultipleTest(BaseCase):

    case_class = DecoratorWithPatchMultiple
    cases_names = [
        'test_method',
        'test_method_with_test_case_foo_a(2)_foo_b(2)',
        'test_method_with_test_cases_foo_a(2)_foo_b(2)_result(4)',
        'test_method_with_test_cases_foo_a(3)_foo_b(3)_result(6)',
        'test_method_with_test_cases_foo_a(4)_foo_b(4)_result(8)',
        'test_method_test_case_only_for_one_argument_foo_a(2)_result(4)',
        'test_method_test_case_only_for_one_argument_foo_a(4)_result(6)',
        'test_method_test_case_only_for_one_argument_foo_a(8)_result(10)',
    ]
