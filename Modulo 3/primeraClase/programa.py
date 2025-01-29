#App de divisiones



#Single Except
def divisionPorCero(num1, num2):
    try:
        resultado =  num1 / num2
        print(resultado)
    except ZeroDivisionError as e: 
        print("La division no se puede realizar.")
        return None
    

#Multiple Except
def divisionSegura():
    try:
        numerador = int(input("Ingrese porfavor el numero del numerador: ")) 
        denominador = int(input("Ingrese el numero del denominador: "))
        resultado = numerador / denominador
        print(f"El resultado entre el numerador {numerador} y el denominador {denominador} es : {resultado}")
    except (ZeroDivisionError,ValueError) as e:
        print(f"Error {e}")


# Manejo de excepciones especificas  Exception( No es recomendable pues puede esconder errores)
def abrirArchivo():
    try:
        with open("datos.txt","r") as archivo:
            contenido = archivo.read()
            numero = int(contenido.strip())
            print(numero)
    except Exception as e:
        print(f"Se produjo un error {e}")


#Uso de Else y Finally
def divisionCompleta():
    try:
        numero = int(input("Ingrese un numero: "))
        resultado =  10 / numero
    except ValueError as e:
        print(f"Error {e}")
    except ZeroDivisionError as e:
        print(f"Error {e}")
    else:
        print(f"El resultado de la division es: {resultado}")
    finally:
        print("Operacion completada")

#App para pedidos
#Validar que el codigo del producto sea alpha numerico
#Validar que la cantidad sea mayor a 0
def procesarPedidos():
    try:
        codigoProducto = input("Ingrese el codigo del producto: ")
        cantidad = int(input("Ingrese cantidad del producto: "))
        if not codigoProducto.isalnum():
            raise ValueError("Codigo del producto debe ser alpha numerico")
        if  cantidad <= 0:
            raise ValueError("La cantidad del producto debe de ser mayor a 0")
    except ValueError as e:
        print(f"Error al procesar el pedido: {e}")
    else:
        precioUnidad = 50
        total = precioUnidad*cantidad
        print(f"Total a pagar: {total}")
    finally:
        print("Operacion Finalizada...")
    

#Excepciones Personalizadas
class ErrorProductoNoDisponible(Exception):
    def __init__(self, message= "El producto no esta disponible"):
        self.message = message





if __name__ == "__main__":
    #divisionPorCero(2,0)
    #divisionSegura()
    #abrirArchivo()
    #divisionCompleta()
    procesarPedidos()
