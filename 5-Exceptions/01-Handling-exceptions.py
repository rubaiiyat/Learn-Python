try:
    age = int(input())
    if age >= 18:
        print("You are eligible to create an account")
    else:
        print("You are not eligible to create an account")
except ValueError:
    print("Please enter the valid number")

