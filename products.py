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



if __name__ == "__main__":
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))            # Should output 12500.0
    print(mac.buy(100))            # Should output 145000.0
    print(mac.is_active())         # Should output False (quantity is now 0, auto-deactivated)

    bose.show()                    # Bose QuietComfort Earbuds, Price: 250, Quantity: 450
    mac.show()                     # MacBook Air M2, Price: 1450, Quantity: 0

    bose.set_quantity(1000)
    bose.show()                    # Bose QuietComfort Earbuds, Price: 250, Quantity: 1000
