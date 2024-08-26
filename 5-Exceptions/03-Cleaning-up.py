try:

    file = open("app.py")
    age = int(input())
    val = int(input())
    result = age / val
    print("Successful")
except ValueError:
    print("Please Enter the valid input")
except ZeroDivisionError:
    print("Division by zero is not possible")

finally:
    file.close()


#This code is Wrong Code. In here have lots of error
#This is just a dummy code.
#Thanks
