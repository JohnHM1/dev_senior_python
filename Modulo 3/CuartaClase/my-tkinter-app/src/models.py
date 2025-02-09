class Cliente:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.mascotas = []

    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)

class Mascota:
    def __init__(self, id, nombre, tipo):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo
        self.historial = []

    def agregar_historial(self, servicio):
        self.historial.append(servicio)

    def mostrar_historial(self):
        for servicio in self.historial:
            print(servicio)