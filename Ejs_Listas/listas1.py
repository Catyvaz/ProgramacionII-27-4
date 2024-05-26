# 1. Suma de elementos: 
# Escribe una función que tome una lista de números y devuelva la suma de todos los elementos en la lista.

def sumar_elementos(lista):
    resultado = 0
    for elemento in lista:
        num = isinstance(elemento, (int, float))
        if num:
            resultado += elemento
    return resultado


numeros = [1, 2, 7, 5]
con_coma = [2.5 , 3.2, 8, 1.4]
mezcla = [1, "s", 8, "m"]
nums_palabras = ["8", "perro", "2", "1"]
print(sumar_elementos(numeros))
print(sumar_elementos(con_coma))
print(sumar_elementos(mezcla))

print(sum(numeros))  