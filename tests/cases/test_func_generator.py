from __future__ import unicode_literals
import unittest
from python_wrap_cases import wrap_case
from tests.cases.base_case import BaseCase


@wrap_case
class FuncGenerator(unittest.TestCase):

    @wrap_case(string__func=lambda: 'Hello World{0}'.format('!'*3))
    def test_simple_func(self, string):
        self.assertEqual(string, 'Hello World!!!')

    @wrap_case(number__func=lambda: iter(range(4)))
    def test_func_range(self, number):
        self.assertEqual(number/1, number)


class FuncGeneratorTest(BaseCase):

    case_class = FuncGenerator
    cases_names = (
        'test_simple_func_string(Hello World!!!)',
        'test_func_range_number(0)',
        'test_func_range_number(1)',
        'test_func_range_number(2)',
        'test_func_range_number(3)',
    )