class Persona:


    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


    def saludar(self):
        return f"Hola, soy {self.name} y tengo {self.age} años."

