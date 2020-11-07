from flask import Flask, Blueprint, render_template, request, redirect
from repositories import product_repository, manufacturer_repository
from models.product import Product

products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products", methods=["GET"])
def products():
    products = product_repository.select_all()
    return render_template("products/index.html", products=products)