class Student:
    name = ""
    roll = ""
    cls = ""
    gpa = ""

    def setValue(self, name, roll, cls, gpa):
        self.name = name
        self.roll = roll
        self.cls = cls
        self.gpa = gpa

    def displayValue(self):
        print(
            f"(Name: {self.name}, Roll: {self.roll}, Class: {self.cls}, GPA: {self.gpa})"
        )


abir = Student()
abir.setValue("Rubaiyat", 44, "CSE17", 3.00)
abir.displayValue()

Rubaiyat = Student()
Rubaiyat.setValue("Rubaiyat", 44, "CSE17", 3.00)
Rubaiyat.displayValue()

Rahim = Student()
Rahim.setValue("Rahim", 45, "CSE17", 3.00)
Rahim.displayValue()
