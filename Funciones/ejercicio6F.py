# Ejercicio 6
# Suma de pares: Escribe una función que tome una lista de números y devuelva la suma de
# los números pares en la lista.

print("\n")
def suma_pares(lista):
    pares = []
    for elemento in lista:
        valor = int(elemento) % 2
        if valor == 0:
            pares.append(elemento)
    return sum(pares)


lista_numeros = list(range(1, 21))
suma = suma_pares(lista_numeros)
print(f"La suma de todos los elementos pares del 1 al 21 es: {suma}")
print("\n")