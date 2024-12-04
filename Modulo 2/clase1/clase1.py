from claseAnimal import Animal
from clasePersona import Persona
from claseAnimal2 import Animal2
from claseMatematica import Matematica
from claseVehiculo import Motocicleta
from claseBanco import Banco

# john = Persona("John",23)
# print(john.saludar())


# pumaNegro = Animal("Puma Negro",2)
# print(pumaNegro.saludar()


# perroBlanco = Animal2("Mono", 5)
# gatoBravo = Animal2("Peluche", 8)
# print(gatoBravo.totalAnimal())


# print(Matematica.suma(1,2))
# print(Matematica.resta(1,2))


# ducattiMotocicle =  Motocicleta("Motocicleta", "Ducatti")
# print(ducattiMotocicle.descripcion())


bbvaBanco = Banco("BBVA")
Banco.cambiarTasa(0.004)
print(bbvaBanco.descripcion())