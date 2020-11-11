import unittest

from models.product import Product
from models.manufacturer import Manufacturer

class TestProduct(unittest.TestCase):

    def setUp(self):
        self.manufacturer_1 = Manufacturer("Cadbury's", "PO Box 12, Bournville, Birmingham B30 2LU", True)
        self.product1 = Product("Dairy Milk", "bar of milk chocolate", 5, 0.2, 1, "chocolate bars", self.manufacturer_1) 

    def test_product_has_name(self):
        self.assertEqual("Dairy Milk", self.product1.name)

    def test_product_has_description(self):
        self.assertEqual("bar of milk chocolate", self.product1.description)

    def test_product_has_stock_quantity(self):
        self.assertEqual(5, self.product1.stock_quantity)

    def test_product_has_buying_cost(self):
        self.assertEqual(0.2, self.product1.buying_cost)

    def test_product_has_selling_price(self):
        self.assertEqual(1, self.product1.selling_price)

    def test_product_has_category(self):
        self.assertEqual("chocolate bars", self.product1.category)

    def test_product_has_manufacturer(self):
        self.assertEqual(self.manufacturer_1, self.product1.manufacturer)

    def test_can_calculate_profit(self):
        self.assertEqual(0.8, self.product1.calculate_profit(self.product1))

    def test_can_calculate_markup(self):
        self.assertEqual(400, self.product1.calculate_markup(self.product1))