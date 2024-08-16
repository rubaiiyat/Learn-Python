letters = ["a", "b", "c", "d"]
print(letters)

letters.append("e")
print(letters)

letters.insert(0, "-")
print(letters)

letters.remove("c")
print(letters)

letters.pop()
print(letters)


del letters[0:2]
print(letters)


letters.clear()
print(letters)
