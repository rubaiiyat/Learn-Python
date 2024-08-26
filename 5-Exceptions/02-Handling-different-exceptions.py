try:
    age = int(input())
    val = int(input())
    result = age / val
    print("Successful")
except ValueError:
    print("Please Enter the valid input")
except ZeroDivisionError:
    print("Division by zero is not possible")

