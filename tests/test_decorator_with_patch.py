from __future__ import unicode_literals
from unittest import TestCase
from mock import patch, MagicMock, DEFAULT
from python_wrap_cases import wrap_case, WrapCasesMixin


class TestedClass():

    def foo_a(self):
        pass

    def foo_b(self):
        pass

    def tested_method(self):
        return self.foo_a() + self.foo_b()


class DecoratorWithPatchObjectTestCase(TestCase, WrapCasesMixin):

    @patch.object(TestedClass, 'foo_b')
    @patch.object(TestedClass, 'foo_a')
    def test_method(self, foo_a_mock=MagicMock, foo_b_mock=MagicMock):
        foo_a_mock.return_value = 2
        foo_b_mock.return_value = 2
        tested_class = TestedClass()
        self.assertEqual(tested_class.tested_method(), 4)

    @wrap_case(2, 2)
    @patch.object(TestedClass, 'foo_b')
    @patch.object(TestedClass, 'foo_a')
    def test_method_with_test_case(self):
        tested_class = TestedClass()
        self.assertEqual(tested_class.tested_method(), 4)

    @wrap_case(2, 2, 4)
    @wrap_case(3, 3, 6)
    @wrap_case(4, 4, 8)
    @patch.object(TestedClass, 'foo_b')
    @patch.object(TestedClass, 'foo_a')
    def test_method_with_test_cases(self, return_value):
        tested_class = TestedClass()
        self.assertEqual(tested_class.tested_method(), return_value)


class DecoratorWithPatchMultipleTestCases(TestCase, WrapCasesMixin):

    @patch.multiple(TestedClass, foo_a=DEFAULT, foo_b=DEFAULT)
    def test_method(self, foo_a, foo_b):
        foo_a.return_value = 2
        foo_b.return_value = 2
        tested_class = TestedClass()
        self.assertEqual(tested_class.tested_method(), 4)

    @wrap_case(foo_a=2, foo_b=2)
    @patch.multiple(TestedClass, foo_a=DEFAULT, foo_b=DEFAULT)
    def test_method_with_test_cases(self):
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