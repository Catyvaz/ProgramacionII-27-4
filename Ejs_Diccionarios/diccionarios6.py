# 6. Intercambiar valores: 
# Crea una función que tome un diccionario y dos claves, e
# intercambie los valores de esas dos claves en el diccionario.

def intercambio(diccionario, clave, clave2):
    valor = diccionario[clave]
    valor2 = diccionario[clave2]
    diccionario[clave] = valor2
    diccionario[clave2] = valor 
    return diccionario

varios = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e", 6: "f", 7: "g"}
numero1 = 3
numero2 = 6
print(intercambio(varios, numero1, numero2))