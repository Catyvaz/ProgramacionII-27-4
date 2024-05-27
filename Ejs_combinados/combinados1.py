# 1. Contar palabras en frases: 
# Escribe una función que reciba una lista de frases y
# devuelva un diccionario donde las claves son las palabras y los valores son las
# frecuencias de esas palabras en todas las frases.

def sacar_puntos_comas(lista):
    list(lista)
    if lista[-1] == "." or lista[-1] == ",":
        lista = lista[:-1]
        return lista
    else:
        return lista  

def contar_palabras(lista):
    diccionario = {}
    for i in range(len(lista)):
        lista_simple = lista[i].split()
        for palabra in lista_simple:
            palabra = palabra.lower()
            palabra = sacar_puntos_comas(palabra)
            if palabra not in diccionario:
                diccionario[palabra] = 1
            else:
                diccionario[palabra] += 1
    return diccionario

frases = ("Pablito clavó un clavito", "Tres tristes tigres comen trigo en un trigal", "dos y dos son cuatro, cuatro y dos son seis", "Uno, dos, tres. Cuatro")
print(contar_palabras(frases))
