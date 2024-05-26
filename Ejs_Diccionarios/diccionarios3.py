# 3. Merge de diccionarios: 
# Crea una función que tome dos diccionarios y devuelva uno
# nuevo que combine ambos (en caso de conflicto, usa los valores del segundo
# diccionario).

def mergear(diccionario, diccionario2):
    nuevo = {}
    for elemento, info in diccionario.items():
        nuevo[elemento] = info
    for elemento, info in diccionario2.items():
        nuevo [elemento] = info
    return nuevo

conjunto = {"a": 1, "b": 5, "c": 8}
conjunto2 = {"f": 3, "h": 4, "b": 2}

print(mergear(conjunto, conjunto2))