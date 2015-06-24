===============================
Python wrap cases
===============================

.. image:: https://img.shields.io/travis/erm0l0v/python_wrap_cases.svg
        :target: https://travis-ci.org/erm0l0v/python_wrap_cases

.. image:: https://img.shields.io/pypi/v/python_wrap_cases.svg
        :target: https://pypi.python.org/pypi/python_wrap_cases


Simple library for generate test cases.

What is this?
-------------

This library helps to generate tests with parameters.

Let's write some tests for this function:

.. code:: python

    import re

    def clear_start_end_dash(string):
        return re.sub(r'^[\s\-]*-|-[\s\-]*$', '', string)
        
::

We may write something like this:

.. code:: python

    from unittest import TestCase
    
    
    class ClearStartEndDashTest(TestCase):

        def test_remove_first_dash(self):
            result = clear_start_end_dash('-my string')
            self.assertEqual(result, 'my string')

        def test_remove_all_first_dashes(self):
            result = clear_start_end_dash('-  -- --my string')
            self.assertEqual(result, 'my string')

        def test_remove_last_dash(self):
            result = clear_start_end_dash('my string-')
            self.assertEqual(result, 'my string')

        def test_remove_all_last_dashes(self):
            result = clear_start_end_dash('my string-- -- -- - ')
            self.assertEqual(result, 'my string')

        def test_keep_dash_at_center(self):
            result = clear_start_end_dash('my-string')
            self.assertEqual(result, 'my-string')

::

It's good, but we spent a lot of time to write those absolutely the same test functions.

So let's decrease the number of duplicate functions:

.. code:: python

    from unittest import TestCase
    
    
    class ClearStartEndDashDryTest(TestCase):

        def test_remove_dash(self):
            cases = (
                ('-my string', 'my string'),
                ('-  -- --my string', 'my string'),
                ('my string-', 'my string'),
                ('my string-- -- -- - ', 'my string'),
                ('my-string', 'my-string')
            )
            for string, expected_result in cases:
                result = clear_start_end_dash(string)
                self.assertEqual(result, expected_result)

::

This code has a few problems:

* Ease to write but difficult to read.
* We can't use test fixture (`setUp`, `tearDown`) with each case.
* If one case failed, the other cases won't run.
* If test `test_remove_dash` fails, it won't help us find out what happened.

Look how easy we may solve this problem using this library:

.. code:: python

    from unittest import TestCase
    from python_wrap_cases import *
    
    
    class ClearStartEndDashWrapTest(TestCase, WrapCasesMixin):

        @wrap_case('-my string', 'my string')
        @wrap_case('-  -- --my string', 'my string')
        @wrap_case('my string-', 'my string')
        @wrap_case('my string-- -- -- - ', 'my string')
        @wrap_case('my-string', 'my-string')
        def test_remove_dash(self, string, expected_result):
            result = clear_start_end_dash(string)
            self.assertEqual(result, expected_result)

::

This code generates 5 tests, that works like a simple test functions.

Console output:

.. code::

    test_remove_dash_u'-  -- --my string'_u'my string' (tests.example.test_simple_test.ClearStartEndDashWrapTest) ... ok
    test_remove_dash_u'-my string'_u'my string' (tests.example.test_simple_test.ClearStartEndDashWrapTest) ... ok
    test_remove_dash_u'my string-'_u'my string' (tests.example.test_simple_test.ClearStartEndDashWrapTest) ... ok
    test_remove_dash_u'my string-- -- -- - '_u'my string' (tests.example.test_simple_test.ClearStartEndDashWrapTest) ... ok
    test_remove_dash_u'my-string'_u'my-string' (tests.example.test_simple_test.ClearStartEndDashWrapTest) ... ok

::

* Free software: BSD license
* Documentation: https://python_wrap_cases.readthedocs.org.
