x, y = 10, 20

x, y = y, x
print(x, y)

a, b = 10, 20

temp = a
a = b
b = temp

print(a, b)


a = 10
b = 20

a = a * b
b = int(a / b)
a = int(a / b)
print(a, b)
