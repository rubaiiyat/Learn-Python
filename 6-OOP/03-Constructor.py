class Student:
    name = ""
    roll = ""
    gpa = ""

    def __init__(self, name, roll, gpa) -> None:
        self.name = name
        self.roll = roll
        self.gpa = gpa

    def displayValue(self):
        print(f"Name: {self.name}, Roll: {self.roll} GPA: {self.gpa}")


abir = Student("Abir", 43, 3.0)
abir.displayValue()

rubaiyat = Student("Rubaiyat", 44, 3.0)
rubaiyat.displayValue()

rahim=Student('Rahim',45,3.10)
rahim.displayValue()

