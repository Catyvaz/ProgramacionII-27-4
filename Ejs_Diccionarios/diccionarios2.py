# 2. Diccionario inverso: 
# Escribe una función que tome un diccionario y devuelva uno nuevo que invierta las claves y los valores.

def volteo(diccionario):
    nuevo_diccionario = {}
    for clave, valores in diccionario.items():
        nuevo_diccionario[valores] = clave
    return nuevo_diccionario

nombres_edades = {
    "maria" : 25,
    "juan" : 30,
    "carlos" : 44,
    "romina" : 18
}

print(volteo(nombres_edades))
