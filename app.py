from flask import Flask, render_template
from controllers.products_controller import products_blueprint
from controllers.manufacturers_controller import manufacturers_blueprint
from repositories import product_repository, manufacturer_repository 

app = Flask(__name__)

app.register_blueprint(products_blueprint)
app.register_blueprint(manufacturers_blueprint)

@app.route('/')
def home():
    products = product_repository.select_all()
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)