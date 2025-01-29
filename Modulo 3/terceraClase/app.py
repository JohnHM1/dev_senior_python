# Uso de breakPoints simples 
from dataclasses import dataclass


@dataclass
class Empleado:
    nombre: str
    ventas: int
    
    def calcular_comision(self):
        if self.ventas <= 0:
            return 0
        elif self.ventas <= 100:
            return self.ventas * 0.05
        elif self.ventas <= 200:
            return self.ventas * 0.1
        else:
            return self.ventas * 0.15
        
empleados = [
    Empleado('Juan', 50),
    Empleado('Pedro', 150),
    Empleado('Maria', 250)
]

for empleado in empleados:
    comision = empleado.calcular_comision()
    print(f'Empleado: {empleado.nombre}: Comision {comision} Bs.')

# BreakPoint conditionales 
# 1. Click derecho en el numero de linea
# 2. Seleccionar Add BreakPoint
# 3. Click derecho en el BreakPoint
# 4. Seleccionar Edit BreakPoint
# 5. Ingresar la condicion de parada
# 6. Click en OK

