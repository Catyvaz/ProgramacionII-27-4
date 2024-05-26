# 4. Elementos mayores que un valor: 
# Escribe una función que tome una lista de números y un valor n, 
# y devuelva una nueva lista con los elementos mayores que n.

def mayor_que(lista, numero):
    lista = sorted(lista)
    lista_mayores = []
    for elemento in lista:
        if elemento > numero:
            lista_mayores = lista[elemento - 1 :]
            break
    return lista_mayores

numero = [10, 5, 4, 8, 7, 6, 3, 9, 2, 1]
nueva = mayor_que(numero, 4)
print(nueva)