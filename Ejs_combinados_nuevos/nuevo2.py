# Palabras por letra inicial : 
# Escribe una función que tome una lista de palabras y devuelva un diccionario donde las 
# claves son las letras iniciales de las palabras y los valores son listas de palabras que comienzan con esa letra.

def dic_letras(lista):
    lista = sorted(lista)
    diccionario_letras = {}
    for palabra in lista:
        letras_palabra = list(palabra)
        valor = letras_palabra[0]
        if valor not in diccionario_letras:
            diccionario_letras[valor] = [palabra]
        else:
            diccionario_letras[valor].append(palabra)
    return diccionario_letras

palabras = ("perro", "alma", "constelación", "palo", "elefante", "auto", "zorro")
print(dic_letras(palabras))