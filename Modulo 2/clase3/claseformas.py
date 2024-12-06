from abc import ABC, abstractmethod
#Clases Abstractas
class Form(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Circle(Form):

    def __init__(self, radial):
        self.radial = radial
        
    def area(self):
        return f"El areal del circulo es: {3.1416 * self.radial**2}"
    
    def perimetro(self):
        return f"El perimetro de un circulo : {2 * 3.14 * self.radial}"
    
class Rectangulo(Form):

    def __init__(self, base, altura):
        self.altura = altura
        self.base = base

    def area(self):
        return f"El areal del rectangulo es: {self.base * self.altura}"
    
    def perimetro(self):
        return f"El perimetro de un rectangulo : {2*(self.base +self.altura)}"
    

formas = [
    Circle(2),
    Rectangulo(3,2)
]

print("Area de las formas: \n")
for forma in formas:
    print(forma.area())

print("Perimetro de las formas: \n")
for forma in formas:
    print(forma.perimetro())
