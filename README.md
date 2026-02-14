# BestBuy Store CLI
**Interactive Command-Line Store Management with Product Inventory & Shopping Cart**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)

## 🎯 Features

| Feature | Description |
|---------|-------------|
| **Product Catalog** | Add/view/remove products with name, price, quantity & active status  |
| **Inventory Tracking** | Auto-deactivate products when quantity reaches 0  |
| **Interactive CLI Menu** | List products, show total stock, place orders via fuzzy name search  |
| **Shopping Cart Orders** | Build basket (name → qty), process buy → deduct stock & calculate total  |
| **Input Validation** | Strict checks: non-empty names, positive prices/qty, available stock  |
| **Preloaded Demo** | Ships with MacBook Air, Bose Earbuds, Google Pixel 7  |

## 🏗️ Tech Stack

**Core:** Pure Python 3 OOP (no external deps)  
**Models:** `products.py` (Product class with buy/activate logic)   
**Business Logic:** `store.py` (Store class with order processing)   
**CLI:** `main.py` (menu-driven interface with fuzzy search) 

## 🚀 Quick Start

```bash
# Clone & run (no deps needed!)
git clone https://github.com/seb0305/BestBuy-Store-CLI.git
cd BestBuy-Store-CLI

# Start interactive store
python main.py
```

## 🎮 How to Use
1. Welcome Menu

```text
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
```
2. Option 1: List Products

    Shows each: MacBook Air M2 - Price: 1450, Quantity: 100

3. Option 2: Total Inventory

   Displays: X amount of items in store (sum of all active quantities).

4. Option 3: Place Order

    - Enter product name/type (case-insensitive, partial match): macbook → MacBook Air M2

    - Enter quantity (positive integer).

    - Repeat or done to finish basket.

    - Processes order → Deducts stock → Shows total cost (e.g. Order placed successfully! Total cost: 2900.0).

5. Edge Cases

    - Product inactive/out-of-stock → "Product not found or inactive." or "Not enough product in stock."

    - Invalid qty → "Quantity must be positive." / "Please enter a valid integer."

6. Quit
4 → "Thank you for shopping. Goodbye!"


## 📝 Development
```bash
# Run in debug mode
python main.py

# Test core functions
python -c "from store import Store; from products import Product; s=Store(); s.add_product(Product('Test',10,5)); print(s.order([(s.products,2)]))"

# Lint
pip install black; black *.py
```
## 🙌 Contributing
- Fork & clone

- Add new product types (clothing/food).

- Improve fuzzy search (multiple matches → select menu).

- Add requirements.txt for future deps.

- Test full order flow → Submit PR


## 📄 License
MIT - Free for educational use!
