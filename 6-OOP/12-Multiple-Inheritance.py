class Flyer:
    def fly(self):
        print("This is Flyer class")


class Swimmer:
    def swim(self):
        print("This is Swimmer class")


class Walker(Flyer, Swimmer):
    def walk(self):
        print("This is Walker class")


obj = Walker()
obj.fly()
obj.swim()
obj.walk()
