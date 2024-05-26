# 5. Eliminar duplicados: 
# Crea una función que tome una lista y devuelva una nueva lista sin elementos duplicados.

def lista_simple(lista):
    lista_uno_solo = []
    for elemento in lista:
        if elemento not in lista_uno_solo:
            lista_uno_solo.append(elemento)
    return lista_uno_solo

numeros = [1, 5, 1, 4, 8, 8, 4]
letras = ["s", "a", "s", "y", "t", "a"]
palabras = ["banana", "pera", "manzana", "pera"]
print(lista_simple(numeros))
print(lista_simple(letras))
print(lista_simple(palabras))