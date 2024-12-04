class Empleado:

    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
        self.__salaryMin = 1300000
        
    def showInfo(self):
        return f"Nombre: {self.name} Salario: {self._salary}"

    def getSalary(self):
        return self._salary

    def setSalary(self, newSalary):
        if newSalary < self.__salaryMin:
            return f"El salario no puede ser menor al salario minimo."
        self._salary = newSalary
        return f"El nuevo saliro es: {self._salary}"
    

empleadoUno = Empleado("Juan",1500000)
print(empleadoUno.showInfo())
print(empleadoUno.getSalary())
print(empleadoUno.setSalary(1200000))
print(empleadoUno.setSalary(1400000))

