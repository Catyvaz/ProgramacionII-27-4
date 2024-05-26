# 2. Máximo y mínimo: 
# Escribe una función que reciba una lista de números y devuelva el valor máximo y el mínimo de la lista.

def max_min(lista):
    print("El máximo es: ", max(lista))
    print("El mínimo es: ", min(lista))

numeros = [10 , 5, 8, 3, 4, 1]
max_min(numeros)