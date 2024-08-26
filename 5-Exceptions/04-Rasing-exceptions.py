#Rising Exceptions
def calculations(age):
    if age <= 0:
        raise ValueError("You can not divided by 0")
    return 50 / age


try:
    print(calculations(-1))
except ValueError as value:
    print(value)
