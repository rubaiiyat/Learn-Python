from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def eat(self):
        print("He eat food")

    @abstractmethod
    def move(self):
        print("He can move")


class Monkey(Animal):
    def __init__(self, name) -> None:
        self.name = name
        print(f"Hello this is {self.name}")

    def eat(self):
        print("I can eat banana")

    def move(self):
        print("Also I can move on branches")


monkey = Monkey("Layka")
monkey.eat()
monkey.move()
