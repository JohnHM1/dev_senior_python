import pdb
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Empleado(ABC):
    nombre: str
    salario: float

    @abstractmethod
    def calcularSalario(self) -> float:
        pass

@dataclass
class Manager(Empleado):
    def calcularSalario(self):
        return self.salario + 5000

@dataclass
class Developer(Empleado):
    def calcularSalario(self):
        return self.salario + 2000
    

def calcularSalarioTotal(empleado: Empleado) -> float:
    """_summary_

    Args:
        empleado (Empleado): _description_
        n = Avance de linea en linea por  el codigo
        s = Salta de funcion en funcion(metodos)
        c = Continua la ejecucion del codigo hasta la siguiente pausa
        p = Imprime el valor de la variable
        l = Muestra el codigo fuente   
        b = Agrega un punto de interrupcion
        cl = Limpia los puntos de interrupcion
        q = Salir del debugger

    Returns:
        float: _description_
    """
    pdb.set_trace() # Punto de interrupción
    return empleado.calcularSalario()

if __name__ == '__main__':
    manager = Manager('Juan', 10000)
    developer = Developer('Pedro', 8000)

    print(calcularSalarioTotal(manager))
    print(calcularSalarioTotal(developer))
    
