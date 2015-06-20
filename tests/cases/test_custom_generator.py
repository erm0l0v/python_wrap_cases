from __future__ import unicode_literals
import unittest
from python_wrap_cases import *


class CustomGenerator(unittest.TestCase, WrapCasesMixin):

    @wrap_case(number__list=[0, 1, 2, 3], result__custom=lambda number, result: number + 1)
    def test_add_1(self, number, result):
        self.assertEqual(number + 1, result)


class CustomGeneratorTest(unittest.TestCase):

    def setUp(self):
        self.obj = unittest.TestLoader().loadTestsFromTestCase(CustomGenerator)
        self.tests = map(lambda x: x._testMethodName, self.obj._tests)

    def test_methods_count_4(self):
        self.assertEqual(self.obj.countTestCases(), 4)

    def test_has_test_add_1_number_0_result_1(self):
        self.assertIn('test_add_1_number(0)_result(1)', self.tests)

    def test_has_test_add_1_number_1_result_2(self):
        self.assertIn('test_add_1_number(1)_result(2)', self.tests)

    def test_has_test_add_1_number_2_result_3(self):
        self.assertIn('test_add_1_number(2)_result(3)', self.tests)

    def test_has_test_add_1_number_3_result_4(self):
        self.assertIn('test_add_1_number(3)_result(4)', self.tests)