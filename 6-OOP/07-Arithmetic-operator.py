class Student:
    def __init__(self, name, id) -> None:
        self.name = name
        self.id = id

    def __add__(self, other):
        return Student(other.name + self.name, other.id + self.id)

    def __str__(self) -> str:
        return f"Name: {self.name}, ID: {self.id}"


john = Student("John", 1)
Swift = Student("Swift", 2)

print(john + Swift)
