letters = ["a", "b", "c", "d", "e"]

for n in range(len(letters)):
    print(f"({n}, {letters[n]})")

print("")
n = 0
while n < len(letters):
    print(letters[n], end=" ")
    n += 1

for i, l in enumerate(letters):
    print((i, l))
