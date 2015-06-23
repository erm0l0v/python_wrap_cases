from __future__ import unicode_literals
import unittest
from python_wrap_cases import *
from tests.cases.base_case import BaseCase


class CustomGenerator(unittest.TestCase, WrapCasesMixin):

    @wrap_case(number__list=[0, 1, 2, 3], result__custom=lambda number, result: number + 1)
    def test_add_1(self, number, result):
        self.assertEqual(number + 1, result)


class CustomGeneratorTest(BaseCase):

    case_class = CustomGenerator
    cases_names = [
        'test_add_1_number(0)_result(1)',
        'test_add_1_number(1)_result(2)',
        'test_add_1_number(2)_result(3)',
        'test_add_1_number(3)_result(4)',
    ]
