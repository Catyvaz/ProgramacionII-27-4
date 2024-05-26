# 1. Contar letras: 
# Escribe una función que reciba una cadena y devuelva un diccionario con la frecuencia de cada letra en la cadena.

def contar_letras(lista):
    contador = {}
    lista = lista.lower()
    for elemento in lista:
        if elemento.isalpha():
            if elemento not in contador:
                contador[elemento] = 1
            else:
                contador[elemento] += 1
    return contador

cadena = "Hola, mundo. Esto es python. Hola"
print(contar_letras(cadena))