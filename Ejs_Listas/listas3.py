# 3. Promedio de una lista: 
# Crea una función que calcule el promedio de los números en una lista dada.

def calc_promedio(lista):
    total = sum(lista)
    promedio = total / len(lista)
    return promedio

numeros = [10, 5, 3, 4, 1]
print(calc_promedio(numeros))