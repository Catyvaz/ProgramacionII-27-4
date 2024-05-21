# Ejercicio 9
# Ordenar lista de cadenas: Escribe una función que tome una lista de cadenas y devuelva una
# lista ordenada alfabéticamente de esas cadenas, ignorando mayúsculas y minúsculas.

def ordenar_cadena(cadena):
    letras = []
    numeros = []
    for elemento in cadena:
        if elemento.isalpha():
            elemento = elemento.lower()
            letras.append(elemento)
        elif elemento.isdigit():
            numeros.append(elemento)
    letras = sorted(letras)
    numeros = sorted(numeros)
    return (letras + numeros)


cadenas = ["Hola", "123", "Mundo", "456", "Python", "789", "Programación", "OpenAI", "987", "Desarrollo"]
ordenado = ordenar_cadena(cadenas)
print(ordenado)