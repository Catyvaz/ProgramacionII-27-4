# Ejercicio 5
# Crear una función recursiva que permita calcular el factorial de un número. 
# Realiza un programa principal donde se lea un número validado como entero, el cual es ingresado por
# el usuario y se muestre el resultado del factorial.

def factorial(numero):
    if numero == 0:
        return 1
    return numero * factorial(numero - 1)

numero = input("Ingrese el número del cúal desea conocer el factorial: ")
if numero.isdigit:
    resultado = factorial(int(numero))
    print(f"El factorial de {numero} es {resultado}")
else:
    print("El valor ingresado no corresponde con el tipo de variable aceptado. Debe ser un número entero")