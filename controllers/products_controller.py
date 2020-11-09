from flask import Flask, Blueprint, render_template, request, redirect
from repositories import product_repository, manufacturer_repository
from models.product import Product
from models.manufacturer import Manufacturer

products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products", methods=["GET"])
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", products=products)

@products_blueprint.route("/products/add", methods=["GET"])
def add_product():
    manufacturers = manufacturer_repository.select_all()
    return render_template("products/add.html", manufacturers = manufacturers)

@products_blueprint.route("/products", methods=["POST"])
def create_product():
    name = request.form["name"]
    description = request.form["description"]
    stock_quantity = request.form["stock_quantity"]
    buying_cost = request.form["buying_cost"]
    selling_price = request.form["selling_price"]
    manufacturer_id = request.form["manufacturer_id"]

    manufacturer = manufacturer_repository.select(manufacturer_id)
    product = Product(name, description, stock_quantity, buying_cost, selling_price, manufacturer)
    product_repository.save(product)
    return redirect('/products')

@products_blueprint.route("/products/<id>", methods=["GET"])
def show_product(id):
    product = product_repository.select(id)
    return render_template("products/show.html", product = product)

@products_blueprint.route("/products/<id>/edit", methods=["GET"])
def edit_product(id):
    product = product_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template("products/edit.html", product = product, manufacturers = manufacturers)

@products_blueprint.route("/products/<id>", methods=["POST"])
def update_product(id):
    name = request.form["name"]
    description = request.form["description"]
    stock_quantity = request.form["stock_quantity"]
    buying_cost = request.form["buying_cost"]
    selling_price = request.form["selling_price"]
    manufacturer_id = request.form["manufacturer_id"]

    manufacturer = manufacturer_repository.select(manufacturer_id)
    product = Product(name, description, stock_quantity, buying_cost, selling_price, manufacturer_id)
    product_repository.save(product)
    return redirect('/products')

@products_blueprint.route("/products/<id>/delete", methods=["POST"])
def delete_product(id):
    product_repository.delete(id)
    return redirect('/products')



