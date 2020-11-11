import unittest

from models.manufacturer import Manufacturer
from models.product import Product

class TestManufacturer(unittest.TestCase):

    def setUp(self):
        self.manufacturer1 = Manufacturer("Cadbury's", "PO Box 12, Bournville, Birmingham B30 2LU", True)
        self.manufacturer2 = Manufacturer("Rowntree's", "123, York Avenue, York, Y01 1AB", False)

    def test_manufacturer_has_name(self):
        self.assertEqual("Cadbury's", self.manufacturer1.name)

    def test_manufacturer_has_address(self):
        self.assertEqual("PO Box 12, Bournville, Birmingham B30 2LU", self.manufacturer1.address)

    def test_manufacturer_is_deactivated__True(self):
        self.assertEqual(True, self.manufacturer1.deactivated)

    def test_manufacturer_is_deactivated__False(self):
        self.assertEqual(False, self.manufacturer2.deactivated)

    
    