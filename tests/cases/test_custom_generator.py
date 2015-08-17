from __future__ import unicode_literals
import unittest
from python_wrap_cases import wrap_case
from tests.cases.base_case import BaseCase


@wrap_case
class CustomGenerators(unittest.TestCase):

    @wrap_case(number__list=[0, 1, 2, 3], result__custom=lambda number, result: number + 1)
    def test_add_1(self, number, result):
        self.assertEqual(number + 1, result)

    @wrap_case(number__range=(1, 4,), smaller_number__custom=lambda number, smaller_number: iter(range(number)))
    def test_less_then(self, number, smaller_number):
        self.assertTrue(number > smaller_number)


class CustomGeneratorsTest(BaseCase):

    case_class = CustomGenerators
    cases_names = [
        'test_add_1_number(0)_result(1)',
        'test_add_1_number(1)_result(2)',
        'test_add_1_number(2)_result(3)',
        'test_add_1_number(3)_result(4)',
        'test_less_then_number(1)_smaller_number(0)',
        'test_less_then_number(2)_smaller_number(0)',
        'test_less_then_number(2)_smaller_number(1)',
        'test_less_then_number(3)_smaller_number(0)',
        'test_less_then_number(3)_smaller_number(1)',
        'test_less_then_number(3)_smaller_number(2)',
    ]
