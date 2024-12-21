class Vehiculo:

     def __init__(self, marca, modelo):
          self.marca = marca 
          self.modelo = modelo
     
     def descripicon(self):
          return f"El vehiculo es de marca {self.marca} y modelo {self.modelo}"
     


class Auto(Vehiculo):
     
    def __init__(self, marca, modelo, puertas) :
          super().__init__(marca, modelo)
          self.puertas = puertas 

    def descripicon(self):
         return f"El vehiculo tiene {self.puertas} puertas."
    

if __name__ == "__main__":
     
     chevrolet = Auto("chevrolet",2022,4)
     print(chevrolet.descripicon())