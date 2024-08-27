class Student:
    def __init__(self, name, id, password) -> None:
        self.name = name
        self._id = id
        self.__passowrd = password


John = Student("John", 43, 1234)
print(John.name)
print(John._id)
print(John.__passowrd)
