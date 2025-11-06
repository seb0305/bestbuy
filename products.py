class Product:
    def __init__(self, name, price, quantity):
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
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise Exception("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
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