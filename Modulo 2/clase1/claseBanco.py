class Banco:

    tasaInteres = 0.03

    def __init__(self, name):
        self.name = name
    

    @classmethod
    def cambiarTasa(cls, nuevaTasa):
        cls.tasaInteres = nuevaTasa


    
    def descripcion(self):
        return f"El banco {self.name} cuenta con una tasa de interes de {tasaInteres}" 


    @staticmethod
    def convercionDLLEUR(dolares):
        return dolares * 0.85

