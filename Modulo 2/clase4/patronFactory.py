from abc import ABC, abstractmethod

#Clase abstracta
class Clases(ABC):
    @abstractmethod
    def operacion(self):
        pass

class ClaseA(Clases):
    def operacion(self):
        return "_Clase A xd "
    
class ClaseB(Clases):
    def operacion(self):
        return "Clase B xd "
    
class FactoryOfClass:

    @staticmethod
    def creacionDeObjeto(claseDeObjeto):
        if claseDeObjeto == "A":
            return ClaseA()
        elif claseDeObjeto == "B":
            return ClaseB()
        else:
            raise ValueError(f"esa clase {claseDeObjeto} no existe")

objeto1 = FactoryOfClass.creacionDeObjeto("A")
objeto2 = FactoryOfClass.creacionDeObjeto("C")

print(objeto1.operacion())
print(objeto2.operacion())