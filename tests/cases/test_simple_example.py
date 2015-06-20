from __future__ import unicode_literals
import unittest
from python_wrap_cases import *


class SimpleExample(unittest.TestCase, WrapCasesMixin):

    @wrap_case(1, 2, 3)
    @wrap_case(2, 2, 4)
    def test_sum(self, a, b, result):
        self.assertEqual(a+b, result)


class SimpleExampleTest(unittest.TestCase):

    def setUp(self):
        self.obj = unittest.TestLoader().loadTestsFromTestCase(SimpleExample)
        self.tests = map(lambda x: x._testMethodName, self.obj._tests)

    def test_methods_count_2(self):
        self.assertEqual(self.obj.countTestCases(), 2)

    def test_has_test_sum_1_2_3(self):
        self.assertIn('test_sum_1_2_3', self.tests)

    def test_has_test_sum_2_2_4(self):
        self.assertIn('test_sum_2_2_4', self.tests)