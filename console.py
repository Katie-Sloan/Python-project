import pdb
from models.product import Product
from models.manufacturer import Manufacturer

import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository

manufacturer_1 = Manufacturer("Cadbury's")
manufacturer_repository.save(manufacturer_1)
manufacturer_2 = Manufacturer("Rowntree's")
manufacturer_repository.save(manufacturer_2)

manufacturer_repository.select_all()

product_1 = Product("Dairy Milk", "bar of milk chocolate", 5, 0.2, 1, manufacturer_1)
product_repository.save(product_1)
product_2 = Product("Chocolate Buttons", "treatsize chocolate buttons", 3, 0.1, 0.3, manufacturer_1)
product_repository.save(product_2)
product_3 = Product("Fruit Pastilles", "assorted fruit-flavoured chews", 10, 0.3, 1.2, manufacturer_2)
product_repository.save(product_3)

product_repository.select_all()

pdb.set_trace()