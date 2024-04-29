#Ejercicio 1: Calculadora de Promedio
#Escribe un programa en Python que solicite al usuario que ingrese tres números y luego calcule y muestre el promedio de esos números.

lista_numeros = []
cuantos = input("Cuantos numeros desea ingresar?: ")

if cuantos.isdigit():
    for i in range (len(cuantos)):
        numero = int(input("Ingrese {}° número: ".format(i + 1)))
        if numero.isdigit():
            lista_numeros.append(numero)
        else:
            print("Se ingresaron valores no numericos")

suma = sum(lista_numeros)
promedio = suma / len(lista_numeros)

print("El promedio de los numeros {} es: {}".format(lista_numeros, promedio))