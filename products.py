class Product:
    """
    Represents a product in the store with a name, price, quantity, and active status.
    """

    def __init__(self, name, price, quantity):
        """
        Initializes a Product instance.

        Args:
            name (str): The name of the product. Must be non-empty.
            price (float): The price of the product. Must be non-negative.
            quantity (int): The quantity of the product available. Must be non-negative.

        Raises:
            Exception: If name is empty or not a string.
            Exception: If price or quantity is negative.
        """
        if not name or not isinstance(name, str):
            raise Exception("Product name must be a non-empty string.")
        if price < 0:
            raise Exception("Product price cannot be negative.")
        if quantity < 0:
            raise Exception("Product quantity cannot be negative.")
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        """
        Returns the current quantity of the product.

        Returns:
            int: The quantity available.
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Sets the quantity of the product. Deactivates product if quantity is zero.

        Args:
            quantity (int): The new quantity to set. Must be non-negative.

        Raises:
            Exception: If quantity is negative.
        """
        if quantity < 0:
            raise Exception("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        """
        Checks if the product is active.

        Returns:
            bool: True if active, False otherwise.
        """
        return self.active

    def activate(self):
        """Activates the product."""
        self.active = True

    def deactivate(self):
        """Deactivates the product."""
        self.active = False

    def show(self):
        """Prints a string representation of the product."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        """
        Purchases a given quantity of the product.

        Args:
            quantity (int): The quantity to buy. Must be positive and <= available quantity.

        Returns:
            float: The total price for the purchase.

        Raises:
            Exception: If product is inactive.
            Exception: If quantity is <= 0 or exceeds available quantity.
        """
        if not self.active:
            raise Exception("Product is inactive, cannot purchase.")
        if quantity <= 0:
            raise Exception("Purchase quantity must be greater than zero.")
        if quantity > self.quantity:
            raise Exception("Not enough product in stock to complete purchase.")
        self.quantity -= quantity
        if self.quantity == 0:
            self.deactivate()
        return self.price * quantity