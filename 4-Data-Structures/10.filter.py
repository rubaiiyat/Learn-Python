items = [
    {"name": "Rice", "price": 60, "quantity": 5},
    {"name": "Sugar", "price": 70, "quantity": 3},
    {"name": "Lentils", "price": 110, "quantity": 2},
    {"name": "Cooking Oil", "price": 150, "quantity": 2},
    {"name": "Flour", "price": 50, "quantity": 5},
    {"name": "Salt", "price": 30, "quantity": 1},
    {"name": "Soap", "price": 25, "quantity": 5},
    {"name": "Shampoo", "price": 200, "quantity": 1},
    {"name": "Toothpaste", "price": 90, "quantity": 1},
    {"name": "Tea", "price": 120, "quantity": 0.5},
]

prices = list(filter(lambda item: item["price"] > 100, items))

print("\n", prices)
