#Ejercicio 1: Calculadora de Promedio
#Escribe un programa en Python que solicite al usuario que ingrese tres números y luego calcule y muestre el promedio de esos números.

lista_numeros = []
cuantos = 3

for i in range (cuantos):
    numero = int(input("Ingrese {}° número: ".format(i + 1)))
    lista_numeros.append(numero)

suma = sum(lista_numeros)
promedio = suma / len(lista_numeros)

print("El promedio de los numeros {} es: {}".format(lista_numeros, promedio))