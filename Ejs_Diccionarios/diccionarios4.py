#4. Filtrar diccionario: 
#Escribe una función que reciba un diccionario y una lista de claves,
# y devuelva un nuevo diccionario solo con las claves especificadas.

def filtrar(diccionario, lista):
    resultado = {}
    for elemento, valor in diccionario.items():
        if elemento in lista:
            resultado[elemento] = valor
    return resultado

claves = [2, 5, 4, 7]
varios = {1: "d", 2: "h", 3: "i", 4: "o", 5: "l", 6: "s", 7: "a"}
print(filtrar(varios, claves))