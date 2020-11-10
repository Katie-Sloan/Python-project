from db.run_sql import run_sql

from models.manufacturer import Manufacturer
from models.product import Product
import repositories.product_repository as product_repository

def save(manufacturer):
    sql = "INSERT into manufacturers (name, deactivated) VALUES (%s, %s) RETURNING *"
    values = [manufacturer.name,  manufacturer.deactivated]
    results = run_sql(sql, values)
    id = results[0]['id']
    manufacturer.id = id
    return manufacturer

def select_all():
    manufacturers = []

    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)

    for row in results:
        manufacturer = Manufacturer(row['name'], row['deactivated'], row['id'])
        manufacturers.append(manufacturer)
    return manufacturers

def select(id):
    manufacturer = None
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = Manufacturer(result['name'], result['deactivated'], result['id'])
    return manufacturer

def delete_all():
    sql = "DELETE  FROM manufacturers"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM manufacturers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(manufacturer):
    sql = "UPDATE manufacturers SET (name, deactivated) = (%s, %s) WHERE id = %s"
    values = [manufacturer.name, manufacturer.deactivated, manufacturer.id]
    run_sql(sql, values)

def products(manufacturer):
    products = []

    sql = "SELECT * FROM products WHERE manufacturer_id = %s"
    values = [manufacturer.id]
    results = run_sql(sql, values)

    for row in results:
        product = Product(row['name'], row['description'], row['stock_quantity'], row['buying_cost'], row['selling_price'], row['category'], row['manufacturer_id'], row['id'])
        products.append(product)
    return products

