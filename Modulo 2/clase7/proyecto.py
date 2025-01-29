from abc import ABC, abstractmethod
from datetime import datetime


class Persona(ABC):

    def __init__(self, nombre,contacto,direccion):
        self.nombre = nombre
        self.contacto = contacto
        self.direccion = direccion

    @abstractmethod
    def mostrar_informacion(self):
        pass


class Mascota(ABC):

    def __init__(self, nombre, especie, raza, edad):
        self.nombre = nombre
        self.especie = especie
        self.raza = raza 
        self.edad = edad
        self.historialCitas = []
    
    @abstractmethod
    def agregarCitaAlHistorial(self, detallesServicio):
        pass


class Cita(ABC):

    def __init__(self, fecha, hora,servicio, veterinario):
        self.fecha = fecha
        self.hora = hora
        self.servicio = servicio
        self.veterinario = veterinario

    @abstractmethod
    def actualizar(self, **kwargs):
        pass


#Definicion de las subclases
class Cliente(Persona):

    def __init__(self, nombre, contacto, direccion):
        super().__init__(nombre, contacto, direccion)
        self.mascotas = []
    
    def agregarMascota(self, mascota):
        self.mascotas.append(mascota)

    def mostrar_informacion(self):
        return f"Cliente: {self.nombre}, Contacto: {self.contacto}, Direccion: {self.direccion}"


class RegistroMascota(Mascota):

    def agregarCitaAlHistorial(self, detallesServicio):
        self.historialCitas.append(detallesServicio)

    def obtenerHistorial(self):
        return self.historialCitas
    

class CitaMascota(Cita):

    def actualizar(self, **kwargs):
        for clave, valor in kwargs.items():
            if hasattr(self, clave):
                setattr(self, clave, valor)


class SistemaVeterinario():

    def __init__(self):
        self.clientes = []

    def registrarClientes(self):

        try:
            nombre = input("Ingrese el nombre del cliente: ").strip()
            contacto = input("Ingrese el contacto del cliente: ").strip()
            direccion = input("Ingrese la direccion del cliente: ").strip()
        
            if not nombre or not contacto or not direccion:
                raise ValueError("Todos Los campos son obligatorios")
            
            cliente = Cliente(nombre, contacto, direccion)
            self.clientes.append(cliente)
            print("Cliente registrado")

        except  ValueError as e:
            print(f"Error: {e}")

    
    def registrarMascota(self):

        try:
            nombreCliente = input("Ingrese el nombre del cliente al que asociar la mascota.").strip()
            cliente = next((c for c in self.clientes if c.nombre == nombreCliente),None)

            if not cliente:
                raise ValueError("Cliente no encontrado")
            
            nombreMascota = input("Ingrese el nombre de la mascota: ").strip()
            especie = input("Ingrese la especie de la mascota: ").strip()
            raza =  input("Ingrese la raza de la mascota: ").strip()
            edad = int(input("Ingrese la edad de la mascota: ").strip())
            
            if not nombreMascota or not especie or not raza or edad <=0:
                raise ValueError("Detalles de la mascota invalidos")
            
            mascota = RegistroMascota(nombreMascota,especie,raza,edad)
            cliente.agregarMascota(mascota)
            print("Mascota registrada con exito")


        except ValueError as e:
            print(f"Error: {e}")

class ProgramarCita():
    pass



