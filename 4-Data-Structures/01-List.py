letters = ["A", "B", "C"]

for letter in letters:
    print(letter, end=" ")

matrix = [[1, 2, 3], [1, 2, 3]]

for m in matrix:
    print(m)


combined = letters + matrix
print(combined)

zeros = [0] * 5
combined = zeros + matrix
print(combined)

numbers = list(range(5))
print(numbers)
char = list("Hello World")
print(len(char))

nums = list((10, 20, 30, 40, 50))
print(nums[0] + nums[3])

n = [1, 2, 3, 4, 5]
print(n[0] + n[3])
