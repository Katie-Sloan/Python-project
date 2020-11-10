class Product:

    def __init__(self, name, description, stock_quantity, buying_cost, selling_price, category, manufacturer, id = None):
        self.name = name
        self.description = description
        self.stock_quantity = stock_quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.category = category
        self.manufacturer = manufacturer
        self.id = id

    def calculate_profit(self, product):
        profit = None
        profit = self.selling_price - self.buying_cost
        return round(profit, 2)

    def calculate_markup(self, product):
        markup = None
        markup = self.calculate_profit(product)
        return round((markup / self.buying_cost * 100))

    

    


