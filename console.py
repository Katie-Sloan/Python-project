import pdb
from models.product import Product
from models.manufacturer import Manufacturer

import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository

product_repository.delete_all()
manufacturer_repository.delete_all()

manufacturer_1 = Manufacturer("Cadbury's", "PO Box 12, Bournville, Birmingham B30 2LU", True)
manufacturer_repository.save(manufacturer_1)
manufacturer_2 = Manufacturer("Rowntree's", "123, York Avenue, York, Y01 1AB", False)
manufacturer_repository.save(manufacturer_2)

manufacturer_repository.select_all()

product_1 = Product("Dairy Milk", "bar of milk chocolate", 5, 0.2, 1, "chocolate bars", manufacturer_1)
product_repository.save(product_1)
product_2 = Product("Chocolate Buttons", "treatsize chocolate buttons", 3, 0.1, 0.3, "packets", manufacturer_1)
product_repository.save(product_2)
product_3 = Product("Fruit Pastilles", "assorted fruit-flavoured chews", 10, 0.3, 1.2, "packets", manufacturer_2)
product_repository.save(product_3)

product_repository.select_all()

pdb.set_trace()