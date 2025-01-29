#Implementar un sistema monitoreo para facturacion c/ manejo de excepciones por consola y archivo de logs

import logging
from dataclasses import dataclass
from math import log

logging.basicConfig(
    level=logging.DEBUG,
    filename='app2.log',
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s'
    )

# Crear un nuevo handler para gestionar mensajes de auditoria por .log y por consola
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.DEBUG)
consoleHandler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logging.getLogger().addHandler(consoleHandler)

@dataclass
class Factura:
    cliente: str
    cantidad : int
    precioUnitario: float

    def procesar(self):
        try:
            logging.info(f'Procesando factura para {self.cliente}')

            if self.cantidad <= 0:
                raise ValueError('Cantidad no puede ser negativo o menor a 0')
            if self.precioUnitario <= 0:
                raise ValueError('Precio unitario no puede ser negativo o 0')

            total = self.cantidad * self.precioUnitario
            logging.info(f'Total: {total}')
        except ValueError as ve:
            logging.error(f'Error al procesar factura {ve}')
        except Exception as e:
            logging.critical(f'Error inesperado {e}')
        finally:
            logging.info('Proceso finalizado')


if __name__ == '__main__':
    f = Factura('Juan', 10, 100)
    f.procesar()

    f2 = Factura('Pedro', 0, 100)
    f2.procesar()

    f3 = Factura('Carlos', 10, 0)
    f3.procesar()

    f4 = Factura('Maria', -10, 100)
    f4.procesar()

    f5 = Factura('Ana', 10, -100)
    f5.procesar()

    f6 = Factura('Lucia', 10, 200)
    f6.procesar()