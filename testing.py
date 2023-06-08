import unittest

import main

class TestCashMethods(unittest.TestCase):
    def test_cash_to_string(self):
        self.assertEqual(main.cash_to_string(1234), "$12.34")
        self.assertEqual(main.cash_to_string(0), "$0.00")
        self.assertEqual(main.cash_to_string(1), "$0.01")
        self.assertEqual(main.cash_to_string(123456), "$1234.56")

    def test_discount(self):
        self.assertEqual(main.discount(100, 50), 50)
        self.assertEqual(main.discount(100, 51), 51)
        self.assertEqual(main.discount(300, 30), 90)
