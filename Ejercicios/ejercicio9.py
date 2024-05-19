# Calculadora de Factorial 
# Desarrolla una calculadora que calcule el factorial de un número ingresado por el usuario. 
# El factorial de un número entero positivo n se define como el producto de todos los enteros positivos menores o iguales a n. 
# El programa debe manejar números enteros grandes y mostrar el resultado.

def factorial(numero):
    if numero == 0:
        return 1
    return numero * factorial(numero - 1)

valor_usuario = int(input("Ingrese el número del cual desea saber el factorial: "))
resultado = factorial(valor_usuario)
print(f"El factorial de {valor_usuario} es {resultado}")