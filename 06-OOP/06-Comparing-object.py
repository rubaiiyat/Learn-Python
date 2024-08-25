class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __eq__(self, value: object) -> bool:
        return value == self.name and value == self.id


rahim = (1, 2)
karim = (1, 2)

print(rahim < karim)
