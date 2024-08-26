class Animal:
    def eat(self):
        print("He can eat")


class Mammal(Animal):
    def walk(self):
        print("He can walk")


class fish(Mammal):
    def swim(self):
        print("He can swim")


garfish = fish()

garfish.eat()
garfish.walk()
garfish.swim()
