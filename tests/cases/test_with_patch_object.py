from __future__ import unicode_literals
import unittest
from mock import patch, MagicMock
from python_wrap_cases import *


class TestedClass():

    def foo_a(self):
        pass

    def foo_b(self):
        pass

    def tested_method(self):
        return self.foo_a() + self.foo_b()


class DecoratorWithPatchObject(unittest.TestCase, WrapCasesMixin):

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


class DecoratorWithPatchObjectTest(unittest.TestCase):

    def setUp(self):
        self.obj = unittest.TestLoader().loadTestsFromTestCase(DecoratorWithPatchObject)
        self.tests = map(lambda x: x._testMethodName, self.obj._tests)

    def test_methods_count_5(self):
        self.assertEqual(self.obj.countTestCases(), 5)

    def test_has_test_method(self):
        self.assertIn('test_method', self.tests)

    def test_has_test_method_with_test_case_2_2(self):
        self.assertIn('test_method_with_test_case_2_2', self.tests)

    def test_has_test_method_with_test_cases_2_2_4(self):
        self.assertIn('test_method_with_test_cases_2_2_4', self.tests)

    def test_has_test_method_with_test_cases_3_3_6(self):
        self.assertIn('test_method_with_test_cases_3_3_6', self.tests)

    def test_has_test_method_with_test_cases_4_4_8(self):
        self.assertIn('test_method_with_test_cases_4_4_8', self.tests)