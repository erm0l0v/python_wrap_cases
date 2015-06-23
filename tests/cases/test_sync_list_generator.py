from __future__ import unicode_literals
import unittest
from python_wrap_cases import *
from tests.cases.base_case import BaseCase


class SyncListGenerator(unittest.TestCase, WrapCasesMixin):

    @wrap_case(number__sync_list=[0, 1, 2, 3], result__sync_list=[1, 2, 3, 4])
    def test_add_1(self, number, result):
        self.assertEqual(number + 1, result)


class ListGeneratorTest(BaseCase):

    case_class = SyncListGenerator
    cases_names = [
        'test_add_1_number(0)_result(1)',
        'test_add_1_number(1)_result(2)',
        'test_add_1_number(2)_result(3)',
        'test_add_1_number(3)_result(4)',
    ]


class MultipleSyncListGenerator(unittest.TestCase, WrapCasesMixin):

    @wrap_case(a__sync_list=[1, 2, 3, 4, 5, 6], b__sync_list=[1, 2, 3, 4], result__sync_list=[2, 4, 6, 8])
    def test_add(self, a, b, result):
        self.assertTrue(a + b, result)


class MultipleSyncListGeneratorTest(BaseCase):

    case_class = MultipleSyncListGenerator
    cases_names = [
        'test_add_a(1)_b(1)_result(2)',
        'test_add_a(2)_b(2)_result(4)',
        'test_add_a(3)_b(3)_result(6)',
        'test_add_a(4)_b(4)_result(8)',
    ]