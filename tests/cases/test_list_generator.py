from __future__ import unicode_literals
import unittest
from python_wrap_cases import *


class ListGenerator(unittest.TestCase, WrapCasesMixin):

    @wrap_case(number__list=[0, 1, 2, 3])
    def test_div_1(self, number):
        self.assertEqual(number/1, number)


class ListGeneratorTest(unittest.TestCase):

    def setUp(self):
        self.obj = unittest.TestLoader().loadTestsFromTestCase(ListGenerator)
        self.tests = map(lambda x: x._testMethodName, self.obj._tests)

    def test_methods_count_4(self):
        self.assertEqual(self.obj.countTestCases(), 4)

    def test_has_test_div_1_number_0(self):
        self.assertIn('test_div_1_number(0)', self.tests)

    def test_has_test_div_1_number_1(self):
        self.assertIn('test_div_1_number(1)', self.tests)

    def test_has_test_div_1_number_2(self):
        self.assertIn('test_div_1_number(2)', self.tests)

    def test_has_test_div_1_number_3(self):
        self.assertIn('test_div_1_number(3)', self.tests)


class MultipleListGenerator(unittest.TestCase, WrapCasesMixin):

    @wrap_case(a__list=[1, 2], b__list=[0, 1])
    def test_gte(self, a, b):
        self.assertGreaterEqual(a, b)


class MultipleListGeneratorTest(unittest.TestCase):

    def setUp(self):
        self.obj = unittest.TestLoader().loadTestsFromTestCase(MultipleListGenerator)
        self.tests = map(lambda x: x._testMethodName, self.obj._tests)

    def test_methods_count_4(self):
        self.assertEqual(self.obj.countTestCases(), 4)

    def test_has_test_gte_a_1_b_0(self):
        self.assertIn('test_gte_a(1)_b(0)', self.tests)

    def test_has_test_gte_a_1_b_1(self):
        self.assertIn('test_gte_a(1)_b(1)', self.tests)

    def test_has_test_gte_a_2_b_0(self):
        self.assertIn('test_gte_a(2)_b(0)', self.tests)

    def test_has_test_gte_a_2_b_1(self):
        self.assertIn('test_gte_a(2)_b(1)', self.tests)