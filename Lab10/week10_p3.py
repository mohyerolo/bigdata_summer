class Animal:
    def __init__(self, name):
        self.name = name
    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def talk(self):
        return "Woof! Woof!"

class Cat(Animal):
    def talk(self):
        return "Meow!"

animals = [Cat('Missy'), Cat('Mr.Mistoffelees'), Dog('Lassie')]
for animal in animals:
    print(animal.name + ': ' + animal.talk())