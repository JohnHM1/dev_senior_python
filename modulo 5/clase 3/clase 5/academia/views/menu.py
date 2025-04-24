from controllers.estudiantes import EstidanteController

def menu():
    print("Bienvenido al sistema de gestión de estudiantes")
    print("1. Registrar estudiante")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        nombre = input("Ingrese el nombre del estudiante: ")
        apellido = input("Ingrese el apellido del estudiante: ")
        telefono = input("Ingrese el teléfono del estudiante: ")
        email = input("Ingrese el email del estudiante: ")
        
        controller = EstidanteController()
        controller.registrar_estudiante(nombre,apellido, telefono, email)
        print("Estudiante registrado con éxito.")
    print("2. Listar estudiantes")
    print("3. Buscar estudiante")
