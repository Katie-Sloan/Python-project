from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

manufacturers_blueprint = Blueprint("manufacturers", __name__)

@manufacturers_blueprint.route("/manufacturers", methods=["GET"])
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template("manufacturers/index.html", manufacturers = manufacturers)

@manufacturers_blueprint.route("/manufacturers/<id>", methods=["GET"])
def show(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template("manufacturers/show.html", manufacturer=manufacturer)

@manufacturers_blueprint.route("/manufacturers/add", methods=["GET"])
def add_manufacturer():
    products = product_repository.select_all()
    return render_template("products/index.html", products = products)

@manufacturers_blueprint.route("/manufacturers", methods=["POST"])
def create_manufacturer():
    name = request.form["name"]

    manufacturer = Manufacturer(name)
    manufacturer_repository.save(manufacturer)
    return redirect(/manufacturers)

@manufacturers_blueprint.route("/manufacturers/<id>/edit", methods=["GET"])
def edit_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template("manufacturers.edit.html",  manufacturer = manufacturer)

@manufacturers_blueprint.route("/manufacturers/<id>", methods=["POST"])
def update_manufacturer():
    name = request.form["name"]

    manufacturer = Manufacturer(name)
    manufacturer_repository.save(manufacturer)
    return redirect(/manufacturers)

@manufacturers_blueprint.route("/manufacturers/<id>/delete", methods=["POST"])
def delete_manufacturer(id):
    manufacturer_repository.delete(id)
    return redirect('/manufacturers')

