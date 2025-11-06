class Store:
    """
    Represents a store containing multiple Product instances and allows management of them.
    """

    def __init__(self, products=None):
        """
        Initializes the Store with an optional list of products.

        Args:
            products (list of Product, optional): Initial list of products. Defaults to empty list.
        """
        self.products = products if products is not None else []

    def add_product(self, product):
        """
        Adds a product to the store.

        Args:
            product (Product): The product to add.
        """
        self.products.append(product)

    def remove_product(self, product):
        """
        Removes a product from the store if it exists.

        Args:
            product (Product): The product to remove.

        Raises:
            Exception: If product is not found in the store.
        """
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        """
        Calculates the total quantity of all active products in the store.

        Returns:
            int: Total quantity of active products.
        """
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self):
        """
        Retrieves all active products in the store.

        Returns:
            list of Product: List of active products.
        """
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        """
        Buys multiple products as specified in the shopping list.

        Args:
            shopping_list (list of tuples): Each tuple contains a Product and an integer quantity.

        Returns:
            float: The total price of the order.

        Raises:
            Exception: If any product in the list does not belong to the store.
            Exception: Propagates exceptions from Product.buy() if purchase conditions fail.
        """
        total_price = 0
        for product, quantity in shopping_list:
            if product not in self.products:
                raise Exception("Product not in store.")
            total_price += product.buy(quantity)
        return total_price