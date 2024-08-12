n = 1
while n <= 10:

    if n % 2 == 0:
        print(n)

    n += 1


command = ""

while command.lower() != "quit":
    command = input()

    print("Echo: ", command)
