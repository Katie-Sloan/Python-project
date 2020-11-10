def get_unique_categories_from_products(products):
    categories_list = [product.category for product in products]
    
    
    
    return list(set(categories_list))