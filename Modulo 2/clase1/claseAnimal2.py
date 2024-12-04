class Animal2:
    

    contadorAnimales = 0 #Variable de una clase


    def __init__(self, name, age):
      self.name = name
      self.age = age
      Animal2.contadorAnimales += 1 # Se usa como contador pues cada vez que se inicialice su suma aumentara.


    @classmethod                #Decorador para definir un llamado a la clase en simisma y extrar informacion inerente.
    def totalAnimal(cls):
      return f"Tengo {cls.contadorAnimales} animalitos."

