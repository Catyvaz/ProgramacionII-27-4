# 8. Diccionario de frecuencias: 
# Escribe una función que reciba una lista de palabras y devuelva un diccionario con la frecuencia de cada palabra.

def frecuencias(lista):
    dic_frecuencias = {}
    for elemento in lista:
        elemento = elemento.lower()
        if elemento not in dic_frecuencias:
            dic_frecuencias[elemento] = 1
        else:
            dic_frecuencias[elemento] +=1
    return dic_frecuencias

palabras = ["banana", "pera", "manzana", "pEra", "naranja", "pera", "manzana", "Pera", "Banana", "pera", "Manzana", "pera"]
print(frecuencias(palabras))