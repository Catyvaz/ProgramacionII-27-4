# 6. Contar elementos: 
# Escribe una función que reciba una lista y un valor, y devuelva cuántas veces aparece ese valor en la lista.

def contar(lista, valor):
    cantidad = 0
    for elemento in lista:
        if elemento == valor:
            cantidad += 1
    return cantidad

numeros = [1, 5, 1, 4, 8, 8, 4, 5, 4, 2, 4, 8, 6]
letras = ["s", "a", "s", "y", "t", "a", "s", "t", "w", "a", "a"]
palabras = ["banana", "pera", "manzana", "pera", "pera", "manzana", "pera"]
print(contar(numeros, 4))
print(contar(letras, "s"))
print(contar(palabras, "manzana"))