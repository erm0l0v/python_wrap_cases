from __future__ import unicode_literals
import unittest


class BaseCase(unittest.TestCase):

    case_class = None
    cases_names = []

    def setUp(self):
        cls = self.case_class or self.__class__
        self.obj = unittest.TestLoader().loadTestsFromTestCase(cls)
        self.tests = list(map(lambda x: x._testMethodName, self.obj._tests))
        self.expected_names = list(set(self.cases_names))

    def test_methods_count(self):
        if self.case_class:
            self.assertEqual(self.obj.countTestCases(), len(self.expected_names))

    def test_contains_case_name(self):
        if self.case_class:
            for name in self.expected_names:
                self.assertTrue(name in self.tests)