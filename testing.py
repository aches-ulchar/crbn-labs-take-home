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

class TestDiscountMethods(unittest.TestCase):
    def setUp(self):
        self.available_items = [
                {"item_id": "shirt_1", "price": 8},
                {"item_id": "shirt_2", "price": 8},
                {"item_id": "shirt_3", "price": 8},
                {"item_id": "shirt_4", "price": 8},
                {"item_id": "shirt_5", "price": 8},
                ]

    def test_get_total_discount(self):
        self.shopping_cart = ["shirt_1",
                              "shirt_1",
                              "shirt_2",
                              "shirt_2",
                              "shirt_3",
                              "shirt_3",
                              "shirt_4",
                              "shirt_5"]

        self.assertEqual(main.get_total_discount(self.shopping_cart, self.available_items), 1040)
