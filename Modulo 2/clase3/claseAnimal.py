class Animal:

    def __init__(self):
        pass

    def talk(self):
        pass

class Dog(Animal):
    
    def __init__(self):
        pass

    def talk(self):
        return "Guaof"

class Cat(Animal):

    def __init__(self):
        pass

    def talk(self):
        return "Miauw"

animals = [Dog(),
           Cat()]

for animal in animals:
    print(animal.talk())
