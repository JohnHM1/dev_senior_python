
import logging
from dataclasses import dataclass, field


# logging.basicConfig(
#     level=logging.DEBUG,
#     format="%(asctime)s - %(levelname)s -%(message)s"
# )

# logging.debug("Este mensaje es de DEBUG")
# logging.info("Este mensaje es de info")
# logging.warning("Este mensaje es de warning")
# logging.error("Este mensaje es de error")
# logging.critical("Este mensaje es de critical")


#App que permite llevar seguimiento de compras y fallos en el proceso de tipo transacion
#esta app registrara la cantidad de productos comprados, con confirmacion de compra y errores en estas transaciones.
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s -%(message)s",
    filename='registro.log',
    filemode='a'
)

@dataclass
class Producto:
    nombre: str
    precio: int
    cantidad: int

    
    def comprar(self, cantidad):
        if cantidad > self.cantidad:
            logging.error(f'No hay suficiente cantidad de producto {self.nombre}. El estock disponible es: {self.cantidad}')
            raise ValueError(f'No hay suficiente cantidad de producto {self.nombre}. El estock disponible es: {self.cantidad}')
        else:
            self.cantidad -= cantidad
            logging.info(f'La compra fue exitosa. El estock disponible es {self.cantidad}')
            return self.precio * cantidad

@dataclass
class Tienda:

    productos: list[Producto] = field(default_factory=list)

    def agregarProducto(self, producto: Producto):
        self.productos.append(producto)
        logging.debug(f'Producto {producto.nombre} fue agregado. El precio es {producto.precio}. Cantidad disponible en stock {producto.cantidad}')

    def comprarProducto(self, nombre: str, cantidad: int):
        producto = next((p for p in self.productos if p.nombre == nombre), None)

        if producto is True:
            try:
                total =  producto.comprar(cantidad)
                logging.info(f'Compra exitosa. El total a pagar es {total}')
                return total
            except ValueError as e:
                logging.error(f'Error en la compra. {e}')
            else:
                logging.warning(f'Producto {nombre} no encontrado')
                raise ValueError(f'Producto {nombre} no encontrado')




if __name__ == '__main__':
    tienda = Tienda()
    invetario = Producto(nombre ='Camisa',precio = 100, cantidad =  10)
    tienda.agregarProducto(invetario)
    tienda.comprarProducto('Camisa', 5)