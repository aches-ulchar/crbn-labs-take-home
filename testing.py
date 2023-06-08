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
        self.assertEqual(main.discount(1000, 0), 0)

    def test_sum_items_price(self):
        self.available_items = {
                "shirt_1": {"item_name": "Shirt 1", "price": 800},
                "shirt_2": {"item_name": "Shirt 2", "price": 800},
                "shirt_3": {"item_name": "Shirt 3", "price": 800},
                "shirt_4": {"item_name": "Shirt 4", "price": 800},
                "shirt_5": {"item_name": "Shirt 5", "price": 800},
                }

        self.shopping_cart = ["shirt_1",
                              "shirt_1",
                              "shirt_2",
                              "shirt_2",
                              "shirt_3",
                              "shirt_3",
                              "shirt_4",
                              "shirt_5"]

        self.assertEqual(main.sum_items_price(self.shopping_cart, self.available_items), 6400)

        self.shopping_cart = []

        self.assertEqual(main.sum_items_price(self.shopping_cart, self.available_items), 0)

class TestListMethods(unittest.TestCase):
    def setUp(self):
        self.test_list_a = ["a", "b", "c", "d", "e"]
        self.test_list_b = ["a", "b", "c", "a", "b", "c", "d", "e"]
        self.test_list_c = ["a", "b", "c", "a", "b", "a", "b", "c", "a", "b", "c", "d", "e"]
        self.test_list_d = []
        self.test_list_e = ["a", "b", "c"]

    def test_count_unique_values(self):
        self.assertEqual(main.count_unique_values(self.test_list_a), 5)
        self.assertEqual(main.count_unique_values(self.test_list_b), 5)
        self.assertEqual(main.count_unique_values(self.test_list_c), 5)
        self.assertEqual(main.count_unique_values(self.test_list_d), 0)
        self.assertEqual(main.count_unique_values(self.test_list_e), 3)

    def test_get_unique_values(self):
        for x in range(0, 5):
            self.assertEqual(main.count_unique_values(main.get_unique_values(x, self.test_list_a)), x)
            self.assertEqual(main.count_unique_values(main.get_unique_values(x, self.test_list_b)), x)
            self.assertEqual(main.count_unique_values(main.get_unique_values(x, self.test_list_c)), x)

    def test_remove_unique_values(self):
        self.test_list_copy = self.test_list_a.copy()
        main.remove_unique_values(0, self.test_list_a)
        self.assertEqual(self.test_list_copy, self.test_list_a)
        main.remove_unique_values(5, self.test_list_a)
        self.assertEqual(self.test_list_a, [])


class TestDiscountMethods(unittest.TestCase):
    def setUp(self):
        self.available_items = {
                "shirt_1": {"item_name": "Shirt 1", "price": 800},
                "shirt_2": {"item_name": "Shirt 2", "price": 800},
                "shirt_3": {"item_name": "Shirt 3", "price": 800},
                "shirt_4": {"item_name": "Shirt 4", "price": 800},
                "shirt_5": {"item_name": "Shirt 5", "price": 800},
                }

    def test_get_total_discount_basic(self):
        self.shopping_cart = ["shirt_1",
                              "shirt_1",
                              "shirt_2",
                              "shirt_2",
                              "shirt_3",
                              "shirt_3",
                              "shirt_4",
                              "shirt_5"]

        self.assertEqual(main.get_total_discount(self.shopping_cart, self.available_items), 1040)

    def test_get_total_discount_edge(self):
        self.shopping_cart = []

        self.assertEqual(main.get_total_discount(self.shopping_cart, self.available_items), 0)

        for x in range(0, 30):
            self.shopping_cart.append("shirt_1")

        self.assertEqual(main.get_total_discount(self.shopping_cart, self.available_items), 0)
