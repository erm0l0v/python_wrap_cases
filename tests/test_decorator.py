from __future__ import unicode_literals
from unittest import TestCase
from python_wrap_cases import *
from python_wrap_cases.case_wrapper import TestCasesWrapper


@wrap_case()
def function():
    """This is function"""
    pass


@wrap_case()
@wrap_case()
def function_witch_two_test_case():
    """This is function_witch_two_test_case"""
    pass


class TestFunction(TestCase):

    def test_set_wrapper(self):
        wrapper = getattr(function, 'test_cases_wrapper')
        self.assertTrue(isinstance(wrapper, TestCasesWrapper))

    def test_keep_doc(self):
        doc = function.__doc__
        self.assertEqual(doc, 'This is function')

    def test_cases_count_1(self):
        wrapper = getattr(function, 'test_cases_wrapper')
        self.assertEqual(len(wrapper.cases), 1)


class TestFunctionWitchTwoTestCase(TestCase):

    def test_set_wrapper(self):
        wrapper = getattr(function_witch_two_test_case, 'test_cases_wrapper')
        self.assertTrue(isinstance(wrapper, TestCasesWrapper))

    def test_keep_doc(self):
        doc = function_witch_two_test_case.__doc__
        self.assertEqual(doc, 'This is function_witch_two_test_case')

    def test_cases_count_2(self):
        wrapper = getattr(function_witch_two_test_case, 'test_cases_wrapper')
        self.assertEqual(len(wrapper.cases), 2)
