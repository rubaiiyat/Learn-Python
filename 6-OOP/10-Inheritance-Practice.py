class Shape:

    def __init__(self, w, l) -> None:
        self.w = w
        self.l = l


class Triangle(Shape):
    def __init__(self) -> None:
        area = 0.5 * self.w * self.l
        print("Area:", area)


class Rectangle(Shape):
    def __init__(self) -> None:
        area = self.w * self.l
        print("Area:", area)


a = Triangle(10, 20)
b = Rectangle(10, 20)
