class Animal:
    def make_sound(self):
        print("Animal can do sound")


class cat(Animal):
    def __init__(self) -> None:
        super().__init__()

    def make_sound(self):
        print("Meow, Mew")


class dog(Animal):
    def __init__(self) -> None:
        super().__init__()

    def make_sound(self):
        print("Woof, Bark")


class cow(Animal):
    def __init__(self) -> None:
        super().__init__()

    def make_sound(self):
        print("Moo")


class Lion(Animal):
    def __init__(self) -> None:
        super().__init__()

    def make_sound(self):
        print("Roar")


ronaldo = cat()
messi = dog()
neymar = cow()
benjama = Lion()

animals = [ronaldo, messi, neymar, benjama]

for animal in animals:
    animal.make_sound()
