from __future__ import unicode_literals
import unittest
from python_wrap_cases import wrap_case
from tests.cases.base_case import BaseCase


@wrap_case
class ListGenerator(unittest.TestCase):

    @wrap_case(number__list=[0, 1, 2, 3])
    def test_div_1(self, number):
        self.assertEqual(number/1, number)


class ListGeneratorTest(BaseCase):

    case_class = ListGenerator
    cases_names = [
        'test_div_1_number(0)',
        'test_div_1_number(1)',
        'test_div_1_number(2)',
        'test_div_1_number(3)',
    ]


@wrap_case
class MultipleListGenerator(unittest.TestCase):

    @wrap_case(a__list=[1, 2], b__list=[0, 1])
    def test_gte(self, a, b):
        self.assertTrue(a >= b)


class MultipleListGeneratorTest(BaseCase):

    case_class = MultipleListGenerator
    cases_names = [
        'test_gte_a(1)_b(0)',
        'test_gte_a(1)_b(1)',
        'test_gte_a(2)_b(0)',
        'test_gte_a(2)_b(1)',
    ]
