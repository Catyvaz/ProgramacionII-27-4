# 8. Concatenar listas:
# Escribe una función que reciba dos listas y devuelva una nueva lista que sea la concatenación de ambas.

def concat_listas(lista1 , lista2):
    lista_concat = lista1 + lista2
    return lista_concat

letras = ["s", "a", "y", "t", "w"]
palabras = ["banana", "pera", "manzana", "mandarina"]

numeros = [1, 5, 4, 2, 8, 6]
numeros2 = [2, 3, 9, 7]

print(concat_listas(letras, palabras))
print(concat_listas(numeros, numeros2))
print(concat_listas(numeros, letras))