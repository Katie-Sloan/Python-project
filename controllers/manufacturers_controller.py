from flask import Flask, Blueprint, render_template, request, redirect
from repositories import manufacturer_repository, product_repository
from models.manufacturer import Manufacturer
from models.product import Product

manufacturers_blueprint = Blueprint("manufacturers", __name__)

@manufacturers_blueprint.route("/manufacturers", methods=["GET"])
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template("manufacturers/index.html", manufacturers=manufacturers)

@manufacturers_blueprint.route("/manufacturers/<id>", methods=["GET"])
def show(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template("manufacturers/show.html", manufacturer=manufacturer)

@manufacturers_blueprint.route("/manufacturers/add", methods=["GET"])
def add_manufacturer():
    return render_template("manufacturers/add.html")

@manufacturers_blueprint.route("/manufacturers", methods=["POST"])
def create_manufacturer():
    name = request.form["name"]
    address = request.form["address"]
    deactivated = request.form["deactivated"]

    manufacturer = Manufacturer(name, address, deactivated)
    manufacturer_repository.save(manufacturer)
    return redirect("/manufacturers")

@manufacturers_blueprint.route("/manufacturers/<id>/edit", methods=["GET"])
def edit_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template("manufacturers/edit.html",  manufacturer = manufacturer)

@manufacturers_blueprint.route("/manufacturers/<id>", methods=["POST"])
def update_manufacturer(id):
    name = request.form["name"]
    address = request.form["address"]
    deactivated = request.form["deactivated"]

    manufacturer = Manufacturer(name, address, deactivated, id)
    manufacturer_repository.update(manufacturer)
    return redirect("/manufacturers")

@manufacturers_blueprint.route("/manufacturers/<id>/delete", methods=["POST"])
def delete_manufacturer(id):
    manufacturer_repository.delete(id)
    return redirect('/manufacturers')

