# 9. Producto de elementos: 
# Escribe una función que tome una lista de números y devuelva el producto de todos los elementos.

def producto(lista):
    resultado = 1
    for elemento in lista:
        resultado *= elemento
    return resultado

numeros = [1, 5, 4, 2, 8, 6]
numeros2 = [2, 3, 9, 7]

print(producto(numeros))
print(producto(numeros2))
