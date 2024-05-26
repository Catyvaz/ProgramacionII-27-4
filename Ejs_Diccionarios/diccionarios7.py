# 7. Sumar valores: 
# Escribe una función que reciba un diccionario con valores numéricos y devuelva la suma de todos los valores.

def sumar_valores(diccionario):
    lista = []
    for elemento in diccionario:
        lista.append(diccionario[elemento])
    return sum(lista)

varios = {1: 10, 2: 20, 3: 30, 4: 5}
print(sumar_valores(varios))