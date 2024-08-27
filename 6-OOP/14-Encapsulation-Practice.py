class Bank:
    def __init__(self, name, balance) -> None:
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        return amount

    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
            return amount
        else:
            return f"Your Withdraw request is {amount}\nYou have not enough money"

    def getBalance(self):
        return self.__balance


john = Bank("John", 1000)
print(f"Name: {john.name}, Amount: {john.getBalance()}")


print(f"You Have Deposit {john.deposit(500)}")
print(f"Name: {john.name}, Amount: {john.getBalance()}")

print(f"{john.withdraw(2000)}")

print(f"Your Current Balance is: {john.getBalance()}")
