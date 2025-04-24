from config.conexion import conectar
from models.models import Estudiante

class EstidanteController:

    def registrar_estudiante(self, nombre,apellido, edad, carrera):
        conexion = conectar()
        cursor = conexion.cursor()
        sql = "INSERT INTO alumnos (nombre, apellido, telefono, email ) VALUES (%s,%s, %s, %s)"
        cursor.execute(sql, (nombre,apellido, edad, carrera))
        conexion.commit()
        cursor.close()
        conexion.close()
        
    

