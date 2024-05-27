# 3. Diccionario de listas: 
# Escribe una función que tome un diccionario donde los valores
# son listas y devuelva una lista que contenga todos los elementos de las listas del
# diccionario

def diccionario_lista(diccionario):
    lista_unidos = []
    for elemento in diccionario:
        lista = diccionario[elemento]
        for cosas in lista:
            lista_unidos.append(cosas)
    print(lista_unidos)

diccionario_conlistas = {
    1: ["a", "b", "c", "d"],
    2: [1, 5, 4, 8],
    3: ["cama", "mono", "perro"]
}
diccionario_lista(diccionario_conlistas)