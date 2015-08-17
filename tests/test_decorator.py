from __future__ import unicode_literals
import unittest
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


class TestCaseWithDoc(unittest.TestCase, WrapCasesMixin):

    @wrap_case(1)
    def test_function_with_doc(self, data):
        """Some doc"""
        self.assertEqual(data, data)


class TestFunction(unittest.TestCase):

    def test_set_wrapper(self):
        wrapper = getattr(function, 'test_cases_wrapper')
        self.assertTrue(isinstance(wrapper, TestCasesWrapper))

    def test_keep_doc(self):
        doc = function.__doc__
        self.assertEqual(doc, 'This is function')

    def test_cases_count_1(self):
        wrapper = getattr(function, 'test_cases_wrapper')
        self.assertEqual(len(wrapper.cases), 1)


class TestFunctionWitchTwoTestCase(unittest.TestCase):

    def test_set_wrapper(self):
        wrapper = getattr(function_witch_two_test_case, 'test_cases_wrapper')
        self.assertTrue(isinstance(wrapper, TestCasesWrapper))

    def test_keep_doc(self):
        doc = function_witch_two_test_case.__doc__
        self.assertEqual(doc, 'This is function_witch_two_test_case')

    def test_cases_count_2(self):
        wrapper = getattr(function_witch_two_test_case, 'test_cases_wrapper')
        self.assertEqual(len(wrapper.cases), 2)


class TestCaseDoc(unittest.TestCase):

    def test_doc_in_case(self):
        instance = unittest.TestLoader().loadTestsFromTestCase(TestCaseWithDoc)
        func = instance._tests[0]
        self.assertEqual(func._testMethodDoc, 'Some doc')
