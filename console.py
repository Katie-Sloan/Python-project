import pdb
from models.product import Product
from models.manufacturer import Manufacturer

import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository

manufacturer_1 = Manufacturer("Cadbury's")
manufacturer_repository.save(manufacturer_1)
manufacturer_2 = Manufacturer("Rowntree's")
manufacturer_repository.save(manufacturer_2)

product_1 = Product("Dairy Milk")
product_repository.save(product_1)
product_2 = Product("Fruit Pastilles")
product_repository.save(product_2)

pdb.set_trace()