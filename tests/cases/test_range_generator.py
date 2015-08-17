from __future__ import unicode_literals
import unittest
from python_wrap_cases import wrap_case
from tests.cases.base_case import BaseCase


@wrap_case
class RangeGenerator(unittest.TestCase):

    @wrap_case(number__range=4)
    def test_range_4_div_1(self, number):
        self.assertEqual(number/1, number)

    @wrap_case(number__range=(1, 4, ))
    def test_range_1_4_div_1(self, number):
        self.assertEqual(number/1, number)

    @wrap_case(number__range=(1, 4, 2, ))
    def test_range_1_4_2_div_1(self, number):
        self.assertEqual(number/1, number)


class RangeGeneratorTest(BaseCase):

    case_class = RangeGenerator
    cases_names = [
        'test_range_4_div_1_number(0)',
        'test_range_4_div_1_number(1)',
        'test_range_4_div_1_number(2)',
        'test_range_4_div_1_number(3)',
        'test_range_1_4_div_1_number(1)',
        'test_range_1_4_div_1_number(2)',
        'test_range_1_4_div_1_number(3)',
        'test_range_1_4_2_div_1_number(1)',
        'test_range_1_4_2_div_1_number(3)',
    ]