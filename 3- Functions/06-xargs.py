def increase(*numbers):
    total = 1
    for number in numbers:
        total = number * total
        print(total)


increase(1, 2, 3, 4, 5)
