from __future__ import unicode_literals
from unittest import TestCase
from python_wrap_cases import wrap_case, WrapCasesMixin


class GeneratorExample(TestCase, WrapCasesMixin):

    @wrap_case(number__list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_div_1(self, number):
        self.assertEqual(number/1, number)

    @wrap_case(number__list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], result__func=lambda number, result: number + 1)
    def test_add_1(self, number, result):
        self.assertEqual(number + 1, result)