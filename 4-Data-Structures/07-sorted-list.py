numbers = [10, 40, 2, 60, 20, 40, 5, 60, 60, 7, 2, 5, 2, 6]

""" for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp

for i in range(len(numbers)):
    print(numbers[i], end=" ") """

""" numbers.sort(reverse=True)
for number in numbers:
    print(number, end=" ") """


products = [
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

for i in range(len(products)):
    for j in range(i + 1, len(products)):
        if products[i]["price"] < products[j]["price"]:
            temp = products[i]
            products[i] = products[j]
            products[j] = temp

for i in range(len(products)):
    print(products[i])
