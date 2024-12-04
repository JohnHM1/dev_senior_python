from os import name


class Animal:

    def __init__(self, name):
        self.name = name

    def talk(self):
        return "Tu animal habla de alguna forma."

    def __str__(self):
        return f"El nombre del animal es: {self.name}"

class Perro(Animal):
    
    def __init__(self, name, race):
        super().__init__(name)#Como traer al diablo digo un atributo de la clase que heredamos.
        self.race = race


    def talk(self):#Polimorfismo. El uso del mismo nombre del metodo en otra clase xd
        return "Guao guao"

    def __str__(self):
        return f"El perro tiene nombre y es {self.name}. Es de raza {self.race}"


animalUno = Animal("wiskey")
print(animalUno.talk())
print(animalUno.__str__())


perroUno = Perro("Tequila", "capuchino")
print(perroUno.talk())
print(perroUno.__str__())
