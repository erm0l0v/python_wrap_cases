========
Usage
========

To use Python wrap cases in a project

.. code:: python

    from unittest import TestCase
    from python_wrap_cases import wrap_case

    @wrap_case
    class SomeTest(TestCase):
    
        @wrap_case('value1_a', 'value2_a')
        @wrap_case('value1_b', 'value2_b')
        def test_with_params(self, param1, param2)
            # ...
        
::

Just add decorators @wrap_case to test function with parameters that you wanna add to test method.


Usage with mock
---------------

By default wrap_case detects the mock arguments and changes a return_value.

.. code:: python

    import unittest
    from python_wrap_cases import wrap_case
    from mock import patch
    
    
    class TestedClass():

        def foo_a(self):
            pass

        def foo_b(self):
            pass

        def tested_method(self):
            return self.foo_a() + self.foo_b()
    
    @wrap_case
    class TestsWithMock(unittest.TestCase):
    
        @wrap_case(2, 2, 4)
        @wrap_case(3, 3, 6)
        @wrap_case(4, 4, 8)
        @patch.object(TestedClass, 'foo_b')
        @patch.object(TestedClass, 'foo_a')
        def test_with_patch_object(self, return_value):
            tested_class = TestedClass()
            self.assertEqual(tested_class.tested_method(), return_value)
        
        @wrap_case(foo_a=2, result=4)
        @wrap_case(foo_a=4, result=6)
        @wrap_case(foo_a=8, result=10)
        @patch.multiple(TestedClass, foo_a=DEFAULT, foo_b=DEFAULT)
        def test_with_patch_multiple(self, result, foo_b):
            foo_b.return_value = 2
            tested_class = TestedClass()
            self.assertEqual(tested_class.tested_method(), result)

::

ListGenerator
-------------

List generator helps to generate cases based on list of arguments.

.. code:: python

    import unittest
    from python_wrap_cases import wrap_case
    
    
    @wrap_case
    class ListGeneratorTests(unittest.TestCase):

        @wrap_case(number__list=[0, 1, 2, 3])
        def test_div_1(self, number):
            self.assertEqual(number/1, number)

::

This code will work like this one:

List generator helps to generate cases based on list of arguments.

.. code:: python

    import unittest
    from python_wrap_cases import wrap_case
    
    
    @wrap_case
    class TestsWithoutListGenerator(unittest.TestCase):

        @wrap_case(number=0)
        @wrap_case(number=1)
        @wrap_case(number=2)
        @wrap_case(number=3)
        def test_div_1(self, number):
            self.assertEqual(number/1, number)

::

If you use two or more list generator in wrap_case, library will generate all possible combination of arguments from these lists.

.. code:: python

    import unittest
    from python_wrap_cases import wrap_case
    
    
    @wrap_case
    class TestWithTwoListGenerators(unittest.TestCase):

        @wrap_case(a__list=[1, 2], b__list=[0, 1])
        def test_gte(self, a, b):
            self.assertTrue(a >= b)

::

it's equal to:

.. code:: python

    import unittest
    from python_wrap_cases import wrap_case
    
    
    @wrap_case
    class TestWithoutListGenerators(unittest.TestCase):

        @wrap_case(a=1, b=0)
        @wrap_case(a=1, b=1)
        @wrap_case(a=2, b=0)
        @wrap_case(a=2, b=1)
        def test_gte(self, a, b):
            self.assertTrue(a >= b)

::


SyncListGenerator
-----------------

The same as ListGenerator but instead of generate all possible argument combination it generate cases successively.

.. code:: python

    import unittest
    from python_wrap_cases import wrap_case
    
    
    @wrap_case
    class TestWithSyncListGenerator(unittest.TestCase):

        @wrap_case(number__sync_list=[0, 1, 2, 3], result__sync_list=[1, 2, 3, 4])
        def test_add_1(self, number, result):
            self.assertEqual(number + 1, result)

::

it's equal to:

.. code:: python

    import unittest
    from python_wrap_cases import wrap_case
    
    
    @wrap_case
    class TestWithoutSyncListGenerator(unittest.TestCase):

        @wrap_case(number=0, result=1)
        @wrap_case(number=1, result=2)
        @wrap_case(number=2, result=3)
        @wrap_case(number=3, result=4)
        def test_add_1(self, number, result):
            self.assertEqual(number + 1, result)

::

CustomGenerator
---------------

If you need more flexible generator you may use CustomGenerator

.. code:: python

    import unittest
    from python_wrap_cases import wrap_case
    
    
    @wrap_case
    class CustomGenerators(unittest.TestCase):

        @wrap_case(number__list=[0, 1, 2, 3], result__custom=lambda number, result: number + 1)
        def test_add_1(self, number, result):
            self.assertEqual(number + 1, result)

::

FuncGenerator
-------------

Simple as a CustomGenerator but without arguments.


.. code:: python

    import unittest
    from python_wrap_cases import wrap_case
    
    
    @wrap_case
    class FuncGenerator(unittest.TestCase):

        @wrap_case(string__func=lambda: 'Hello World{0}'.format('!'*3))
        def test_simple_func(self, string):
            self.assertEqual(string, 'Hello World!!!')

::

RangeGenerator
--------------

Generate range of numbers

.. code:: python

    import unittest
    from python_wrap_cases import wrap_case
    
    
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

::
