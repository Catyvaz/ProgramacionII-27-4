# 9. Actualizar diccionario: 
# Escribe una función que tome un diccionario y una lista de tuplas (clave, valor) y actualice el diccionario con esas tuplas.

def actualizar(diccionario, lista):
    diccionario[lista[0]] = lista[1]
    return diccionario

tupla = ("z", 45)
tupla2 = (8, "si")
varios = {
    "a": 1,
    6: "xs",
    8: "po",
    "m": 45
}
print(varios)
print(actualizar(varios, tupla))
print(actualizar(varios, tupla2))