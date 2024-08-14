# Have two type of fucntion
# 1. Perform a task
# 2. Return type function


# Perform a task
def greet(name):
    print(f"Hi {name}")


greet("John")


def greeting(name):
    return name


message = greeting("Bob")
print(message)
