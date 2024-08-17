numbers = [10, 40, 2, 60, 20, 40, 5, 60, 60, 7, 2, 5, 2, 6]

""" for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            temp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = temp

for i in range(len(numbers)):
    print(numbers[i], end=" ") """

numbers.sort(reverse=True)
for number in numbers:
    print(number, end=" ")
