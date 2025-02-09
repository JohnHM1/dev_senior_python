import logging
from dataclasses import dataclass
import re

logging.basicConfig(level=logging.DEBUG)

@dataclass
class Vendedor:
    nombre: str
    ventasTotales : float


    def calculoComision(self)-> float:
        if self.ventasTotales > 10000:
            comision = self.ventasTotales * 0.1
            logging.debug(f'Comision: {comision}')
            return comision
        else:
            comision =  self.ventasTotales * 0.05
            logging.debug(f'Comision: {comision}')
            return comision
        
if __name__ == '__main__':
    vendedor = Vendedor('Juan', 15000)
    vendedor.calculoComision()
    vendedor = Vendedor('Pedro', 5000)
    vendedor.calculoComision()
