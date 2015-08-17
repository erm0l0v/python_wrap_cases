from __future__ import unicode_literals
import unittest
from python_wrap_cases import *
from tests.cases.base_case import BaseCase


@wrap_case
class SimpleAliasExample(unittest.TestCase):

    @wrap_case(1, 2, 3)
    @wrap_case(2, 2, 4)
    def test_sum(self, a, b, result):
        self.assertEqual(a+b, result)


class SimpleAliasExampleTest(BaseCase):

    case_class = SimpleAliasExample
    cases_names = [
        'test_sum_1_2_3',
        'test_sum_2_2_4',
    ]