registro = []
cursos = ["Java", "Python"]
docentes = []
horarios = []


#Funcion para matricular estudiantes.
def matricularEstudiante():
    nombre = input("Digite el nombre del estudiante: ")

    print("Selecione el curso: ")
    for i, curso in enumerate(cursos):
        print(f"{i+1}: {curso}")
    

    cursoSelecionado = int(input("Ingrese el numero de curso: "))
    if cursoSelecionado > 0 and cursoSelecionado <= len(cursos):
        indiceCurso = cursos[cursoSelecionado-1]
        diccionarioEstudiantes = {"Nombre": nombre, "Curso": curso}
        registro.append(diccionarioEstudiantes)
        print(f"Estudiante: {nombre} matriculado en el Curso: {curso}")
    else:
        print(f"Opcion Invalidad porfavor repitalo. Cursos disponibles: {len(cursos)}")


#Funcion para asignar un docente.
def asignarDocente():
    print("Selecione el curso al que desea asignar un docente: ")
    for i, curso in enumerate(cursos):
        print(f"{i+1}: {curso}")
    

    cursoSelecionado = int(input("Ingrese el numero de curso: "))
    if cursoSelecionado > 0 and cursoSelecionado <= len(cursos):
        curso = cursos[cursoSelecionado-1]
        profesor = input("Ingrese el nombre del docente: ")
        dicionarioProfersores = {"Nombre": profesor, "Curso": curso}
        docentes.append(dicionarioProfersores)
        print(f"Docente: {profesor},  del curso: {curso}")
    else:
        print(f"Opcion Invalidad porfavor repitalo. Cursos disponibles: {len(cursos)}")


#Funcion para asignar Horario a un curso.
def asignarHorario():
    print("Selecione el curso al que desea asignar un Horario: ")
    for i, curso in enumerate(cursos):
        print(f"{i+1}: {curso}")
    

    cursoSelecionado = int(input("Ingrese el numero de curso: "))
    if cursoSelecionado > 0 and cursoSelecionado <= len(cursos):
        curso = cursos[cursoSelecionado-1]
        dias = (input("Ingrese el dia de clase (ejem: Martes y jueves): "))
        hora = (input("Ingrese la hora de la clase: "))
        dicionarioHorario  = {"Curso": curso, "Dias": dias, "Hora": hora}
        horarios.append(dicionarioHorario)
        print(f"Horario asignado al curso {curso}: {dias}, a las {hora} ")
    else:
        print(f"Opcion Invalidad porfavor repitalo. Cursos disponibles: {len(cursos)}")


def mostrarEstudiantes():
    if registro:
        print("Lista de estudiantes: ")
        for estudiante in registro:
            print(f"Estudiante: {estudiante["Nombre"]}, Curso: {estudiante["Curso"]}")
    else:
        print("No hay estudiantes matriculados.")


def mostrarDocentes(): 
    if registro:
        print("Lista de Docentes: ")
        for docente in docentes:
            print(f"Docente : {docentes["Nombre"]}, Curso: {docentes["Curso"]}")  
    else:
        print("No hay estudiantes matriculados.")


def mostrarHorario():
    if registro:
        print("\n Lista de Horario: ")
        for horario in horarios:
            print(f"Curso: {horarios["Curso"]}, Dias: {horarios["Dias"]}, Hora: {horarios["Hora"]}")
    else:
        print("No hay Horarios matriculados.")


while True:
    print("\n Sistema de matricula Devsenior: ")
    print("1. Matricular estudiante.")
    print("2. Matricular Docente a un curso.")
    print("3. registrar Horario a un curso.")
    print("4. Mostrar lista de estudiantes.")
    print("5. Mostrar lista de docentes.")
    print("6. Mostrar lista de horarios.")
    print("7. salir del programa.")

    
    opcion = int(input("Digite una opcion: "))
    if opcion == 1:
        matricularEstudiante()
    elif opcion ==2:
        asignarDocente()
    elif opcion ==3:
        asignarHorario()
    elif opcion ==4:
        mostrarEstudiantes()
    elif opcion ==5:
        mostrarDocentes()
    elif opcion ==6:
        mostrarHorario()
    elif opcion == 7:
        break
    else:
        print("Opcion invalida")

        