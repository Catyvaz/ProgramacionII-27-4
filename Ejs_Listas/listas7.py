# 7. Invertir lista: 
# Escribe una función que tome una lista y devuelva una nueva lista con los elementos en orden inverso.

def reverso(lista):
    lista.reverse()
    return lista

numeros = [1, 5, 4, 2, 8, 6]
letras = ["s", "a", "y", "t", "w"]
palabras = ["banana", "pera", "manzana", "mandarina"]

print(reverso(numeros))
print(reverso(letras))
print(reverso(palabras))