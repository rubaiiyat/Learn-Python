class Animal:
    def __init__(
        self,
        name,
        food,
    ):
        self.name = name
        self.food = food

    def __str__(self) -> str:
        return f"Name: {self.name}, Food: {self.food}"


print(Animal("Lion", "Meat"))
print(Animal("Elephant", "Grass"))
print(Animal("Panda", "Bamboo"))
print(Animal("Rabbit", "Carrots"))
print(Animal('Rat','Cloth'))
