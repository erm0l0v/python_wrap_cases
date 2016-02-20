"""
Module with list generator

This generator may be use for generate list of wrap cases

Example:

.. code:: python

    @wrap_case
    class ListGeneratorTests(unittest.TestCase):

        @wrap_case(number__list=[0, 1, 2, 3])
        def test_div_1(self, number):
            self.assertEqual(number/1, number)

::

This code equal to this  one:

.. code:: python

    @wrap_case
    class ListGeneratorTests(unittest.TestCase):

        @wrap_case(number=0)
        @wrap_case(number=1)
        @wrap_case(number=2)
        @wrap_case(number=3)
        def test_div_1(self, number):
            self.assertEqual(number/1, number)

::

If you use two or more list generator in wrap_case,
library generate all possible combination of arguments from these lists.

.. code:: python

    @wrap_case
    class TestWithTwoListGenerators(unittest.TestCase):

        @wrap_case(a__list=[1, 2], b__list=[0, 1])
        def test_gte(self, a, b):
            self.assertTrue(a >= b)

::

it`s equal to

.. code:: python

    @wrap_case
    class TestWithoutListGenerators(unittest.TestCase):

        @wrap_case(a=1, b=0)
        @wrap_case(a=1, b=1)
        @wrap_case(a=2, b=0)
        @wrap_case(a=2, b=1)
        def test_gte(self, a, b):
            self.assertTrue(a >= b)

::
"""
from __future__ import unicode_literals
from .base_generator import BaseGenerator


class ListGenerator(BaseGenerator):
    """
    Generate tests based on lest of arguments.

    This generator will generate all possible variant of cases
    """

    def __init__(self, collection):
        """
        List generator constructor
        :param collection: list with arguments
        :type collection: list
        """
        self.collection = collection

    def generate_cases(self, arg_index, key, *args, **kwargs):
        return self.collection
