from abc import ABC, abstractmethod
#Interfaces


class ProcesoDePago(ABC):
    
    @abstractmethod
    def pago(self, cantidaDinero: float)-> None:#La mayor caracteristica de una interfaz 
        pass

    @abstractmethod
    def reembolso(self, idTransacion: str)->None:
        pass


class Paypal(ProcesoDePago):

    def pago(self, cantidad: float) -> None:
        print(f"procesando pago de {cantidad} en paypal.")

    def reembolso(self, idTransacion: str) -> None:
        print(f"Reembolsando. Numero de transacion: {idTransacion}")


class Stripe(ProcesoDePago):

    def pago(self, cantidad: float) -> None:
        print(f"procesando pago de {cantidad} en Stripe.")

    def reembolso(self, idTransacion: str) -> None:
        print(f"Reembolsando. Numero de transacion: {idTransacion}")


if __name__ == "__main__":
    procesoPaypal = Paypal()
    procesoStripe = Stripe()

    procesoPaypal.pago(500.0)
    procesoPaypal.reembolso("FDC2134234")

    procesoStripe.pago(400.0)
    procesoStripe.reembolso("C2134234")
