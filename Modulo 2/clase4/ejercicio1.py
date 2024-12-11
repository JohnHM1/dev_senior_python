#Singeltom y Factory
import threading
from abc import ABC, abstractmethod

#Patron Singeltom
class SistemaFacturacion:

    _instancia = None 
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):

        with cls._lock:
            if not cls._instancia:
                cls._instancia = super(SistemaFacturacion, cls).__new__(cls)
                cls._instancia._inicializacionHistorico()
            return cls._instancia
    
    def _inicializacionHistorico(self):

        self.historial = []
        print("Sistema de facturacion Inicializada")

    def registrarOperacion(self, operacion):

        self.historial.append(operacion)
        print("Sistema de facturacion Inicializada xdddd")

#Crear patron Factory
#Clase Abstracta 

class ProcesoDeNegocio(ABC):

    @abstractmethod
    def ejecutar(self):
        pass 



class ProcesarPedido(ProcesoDeNegocio):

    def ejecutar(self):
        return "Procesando Pedido"
    



class ProcesarFactura(ProcesoDeNegocio):

    def ejecutar(self):
        return "Procesando Pedido"




   
    
class FabricaDeNegocio:

    @staticmethod
    def crearProceso(tipoProceso):

        if tipoProceso == "Pedido":
            return ProcesarPedido()
        elif tipoProceso == "Factura":
            return ProcesarFactura()
        else:
            raise ValueError(f"El proceso {tipoProceso} no existe")

if __name__ == "__main__":

    sistemaDeVentas = SistemaFacturacion()

    proceso1 = FabricaDeNegocio.crearProceso("Pedido")
    proceso2 = FabricaDeNegocio.crearProceso("Factura")

    resultadoPedido = proceso1.ejecutar()
    sistemaDeVentas.registrarOperacion(resultadoPedido)
    
    resultadoFactura = proceso2.ejecutar()
    sistemaDeVentas.registrarOperacion(resultadoFactura)


    print("Historico ")
    for operacion in sistemaDeVentas.historial:
        print(f"Transacion {operacion}")