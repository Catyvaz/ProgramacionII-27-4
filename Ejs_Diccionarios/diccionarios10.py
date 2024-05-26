# 10.Valores únicos: 
# Escribe una función que reciba un diccionario y devuelva una lista de valores únicos en el diccionario.

def valores_unicos(diccionario):
    lista = []
    for elemento, valor in diccionario.items():
        if valor not in lista:
            lista.append(valor)

    return lista

diccionario = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 4, "f": 2}
print(valores_unicos(diccionario))
