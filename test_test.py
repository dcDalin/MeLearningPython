import unittest
from test import valid_month, name_of_month

class TestMonth(unittest.TestCase):

    def test_invalid_month(self):
        self.assertFalse(valid_month(20))
        self.assertFalse(valid_month(0))
        self.assertFalse(valid_month(-1))
        self.assertFalse(valid_month(2.3))
    def test_valid_month(self):
        self.assertTrue(valid_month(2))

    def test_name_of_month(self):
        result = name_of_month(12)
        self.assertEqual(result, 'December')