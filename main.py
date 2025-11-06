import products
import store

def start(store_obj):
    while True:
        print("\nMenu:")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            print("\nProducts available:")
            for product in store_obj.get_all_products():
                product.show()

        elif choice == "2":
            total_qty = store_obj.get_total_quantity()
            print(f"\nTotal amount of items in store: {total_qty}")

        elif choice == "3":
            print("\nEnter your order details.")
            products_to_order = []
            while True:
                name = input("Product name (or type 'done' to finish): ").strip()
                if name.lower() == "done":
                    break
                # find product by name ignoring case and only active ones
                matched_products = [p for p in store_obj.get_all_products() if p.name.lower() == name.lower()]
                if not matched_products:
                    print("Product not found or inactive.")
                    continue
                product = matched_products[0]
                try:
                    qty = int(input(f"Quantity of '{product.name}': "))
                    if qty <= 0:
                        print("Quantity must be positive.")
                        continue
                    products_to_order.append((product, qty))
                except ValueError:
                    print("Please enter a valid integer for quantity.")
                    continue

            if products_to_order:
                try:
                    total_cost = store_obj.order(products_to_order)
                    print(f"Order placed successfully! Total cost: {total_cost}$")
                except Exception as e:
                    print(f"Order failed: {str(e)}")
            else:
                print("No products ordered.")

        elif choice == "4":
            print("Thank you for shopping. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250)
    ]
    best_buy = store.Store(product_list)
    start(best_buy)
