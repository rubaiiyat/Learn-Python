class Triangle:
    def __init__(self, base, height) -> None:
        self.base = base
        self.height = height

    def Calculate_Area(self):
        area = 0.5 * self.base * self.height
        print(f"Area: {area}")


t1 = Triangle(10, 20)
t1.Calculate_Area()

t2 = Triangle(20, 30)
t2.Calculate_Area()
