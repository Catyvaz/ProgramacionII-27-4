#Ejercicio 2
# Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el
# valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el
# máximo y el mínimo, utilizando la función anterior.

def calcularMaxMin(lista):
    for i in range (len(lista)):
        if lista[i].isdigit:
            if i == 0:
                maximo = int(lista[i])
                minimo = int(lista[i])
            elif int(lista[i]) > maximo:
                maximo = int(lista[i])
            elif int(lista[i]) < minimo:
                minimo = int(lista[i])
        else:
            return 0
            break
    return maximo, minimo

numeros = input("Ingrese los números a evaluar")
valores = calcularMaxMin(numeros)
print(valores)