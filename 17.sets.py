numbers = [2, 3, 4, 5, 4, 6, 7, 2]
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 4, 6, 7, 2}
set3 = set(numbers)


print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
print(set2 - set1)
print(set1 ^ set2)
