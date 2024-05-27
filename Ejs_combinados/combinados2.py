# 2. Agrupar por longitud: 
# Escribe una función que reciba una lista de palabras y devuelva
# un diccionario donde las claves son las longitudes de las palabras y los valores son
# listas de palabras con esa longitud.

def longitud(lista):
    diccionario = {}
    for elemento in lista:
        n_letras = len(list(elemento))
        if n_letras not in diccionario:
            diccionario[n_letras] = [elemento] #en la clave yo creo un valor tipo lista, y dentro de esta lista voy agregando los nuevos valores con el . append
        else:
            diccionario[n_letras].append(elemento)
    return diccionario

palabras = ("elefante", "elefante", "perro", "computadora", "uno", "programacion", "dos", "bicicleta", "arquitectura", "biblioteca", "astronauta")
print(longitud(palabras))
