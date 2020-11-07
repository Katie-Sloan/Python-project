from db.run_sql import run_sql

from models.product import Product
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

def save(product):
    sql = "INSERT INTO products (name, description, stock_quantity, buying_cost, selling_price, manufacturer_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [product.name, product.description, product.stock_quantity, product.buying_cost, product.selling_price, product.manufacturer_id]
    results = run_sql(sql, values)
    id = results [0]['id']
    product.id = id
    return product

 