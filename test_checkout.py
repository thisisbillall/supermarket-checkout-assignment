# tests for main checkout logic

import unittest
from checkout import SupermarketCheckout

class TestSupermarketCheckout(unittest.TestCase):
    def setUp(self):
        self.checkout = SupermarketCheckout()

    def test_empty_cart(self):
        self.assertEqual(self.checkout.calculate_total(""), 0)

    def test_single_items(self):
        self.assertEqual(self.checkout.calculate_total("A"), 50)
        self.assertEqual(self.checkout.calculate_total("B"), 30)

    def test_multiple_items(self):
        self.assertEqual(self.checkout.calculate_total("AB"), 80)
        self.assertEqual(self.checkout.calculate_total("CDBA"), 115)

    def test_other_cases(self):
        self.assertEqual(self.checkout.calculate_total("AAABB"), 175)
        self.assertEqual(self.checkout.calculate_total("AAABBD"), 190)
        self.assertEqual(self.checkout.calculate_total("DABABA"), 190)

if __name__ == "__main__":
    unittest.main()
