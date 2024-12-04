


class Persona:

    def __init__(self, name, age):
        self.name = name
        self._age = age # la edad sera un atributo protegido . _protegted
        self.__accountBank = 12345 # Dato privado. __privade

    def showInfo(self):
        return f"Nombre: {self.name} Edad: {self._age}"

    def __infoAccount(self):# el metodo showAccount es privado. __privade
        return f"Cuenta Bancaria: {self.__accountBank}"

    def printInfo(self):
        return self.__infoAccount()
    

juan = Persona("juan",23)
print(juan._age)
print(juan.name)
print(juan.showInfo())
print(juan.printInfo())


