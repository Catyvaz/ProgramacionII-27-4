# 10.Encontrar índice: 
# Escribe una función que reciba una lista y un valor, 
# y devuelva el índice de la primera aparición de ese valor en la lista, o -1 si el valor no está presente.

def encontrar(lista, valor):
    if valor in lista:
        posicion = lista.index(valor)
    else:
        posicion = -1
    return posicion  

numeros = [1, 5, 4, 2, 8, 6]
letras = ["s", "a", "y", "t", "w"]
palabras = ["banana", "pera", "manzana", "mandarina", "banana"]

print(encontrar(numeros, 8))
print(encontrar(letras, "a"))
print(encontrar(letras, "z"))
print(encontrar(palabras, "banana"))