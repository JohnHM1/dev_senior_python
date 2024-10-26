#Ejercicio 1
variableUsuario= (input("Digite el primer un numero: "))
numero1 = float(variableUsuario)
variableUsuario=(input("Digite el segundo un numero: "))
numero2 = float(variableUsuario)


isNumeric= variableUsuario.isnumeric()
if not isNumeric:
    print("El numero no es un Digito.")

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2


print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicacion: {multiplicacion}")
print(f"Division: {division}")

#Test GitHub Desktop