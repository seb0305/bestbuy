class Store:
    def __init__(self, products=None):
        self.products = products if products is not None else []

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self):
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        total_price = 0
        for product, quantity in shopping_list:
            if product not in self.products:
                raise Exception("Product not in store.")
            total_price += product.buy(quantity)
        return total_price


if __name__ == "__main__":
    import products  # Make sure products.py is in the same directory

    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    products_active = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(products_active[0], 1), (products_active[1], 2)]))
