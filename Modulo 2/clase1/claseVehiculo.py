class Vehiculo:

    def __init__(self, tipo):
      self.tipo = tipo


    def descripcion(self):
       return f"Este vehiculo es de tipo {self.tipo}"


class Motocicleta(Vehiculo):
   

    def __init__(self, tipo, marca):
        super().__init__(tipo)
        self.marca = marca
    
      