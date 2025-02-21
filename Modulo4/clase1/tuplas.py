from typing import Tuple # Importamos la clase Tuple de typing para el uso de tuplas en el código que se está creando. Ademas por seguridad

#app para registro de empleados 

def getInfoEmploy(employ: Tuple[int,str,str]) -> Tuple:
    idEmploy, nameEmploy, rolEmploy = employ # Descomposición de tupla
    print(f"ID: {idEmploy}, Nombre: {nameEmploy}, Rol: {rolEmploy}")
    return employ # Retornamos la tupla con los datos del empleado

def salaryAnalysis(salaries: Tuple[int,...]) -> None:
    print(f'salarios en la tupla: {salaries}')
    print(f'Numero de salarios: {len(salaries)}')
    print(f'El salario mas alto es: {max(salaries)}')
    print(f'El salario mas bajo es: {min(salaries)}')
    print(f'La suma de todos los salarios es: {sum(salaries)}')
    print(f'Los salarios registrados de forma ordenada son: {sorted(salaries)}')
    
    findSalary = 5000
    print(f'El salario de {findSalary} se encuentra {salaries.count(findSalary)} veces en la tupla.')

    if findSalary in salaries:
        print(f'El salario {findSalary} se encuentra en la tupla en la posicion {salaries.index(findSalary)+1}.')

def main():
    employ1 = (1, 'Juan', 'Gerente')
    employ2 = (2, 'Pedro', 'Programador')
    employ3 = (3, 'Maria', 'Diseñadora')
    
    print(getInfoEmploy(employ1))  

    salaries = (1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000)
    salaryAnalysis(salaries)

if __name__ == "__main__":
    main()
