class Shape:
    def __init__(self, num1, num2) -> None:
        self.num1 = num1
        self.num2 = num2


class Triangle(Shape):
    def __init__(self, num1, num2) -> None:
        super().__init__(num1, num2)
        area = 0.5 * num1 * num2
        print("Triangle Area:", area)


class Rectangle(Shape):
    def __init__(self, num1, num2) -> None:
        super().__init__(num1, num2)
        area = num1 * num2
        print("Rectangle Area:", area)


area = Triangle(10, 20)
area = Rectangle(10, 20)
