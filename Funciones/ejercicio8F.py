# # Ejercicio 8
# Palíndromo: Escribe una función que determine si una palabra o frase es un palíndromo (se
# lee igual de adelante hacia atrás que de atrás hacia adelante), ignorando espacios y signos
# de puntuación.

def palidromo(lista):
    lista_original = list(lista)
    lista_vuelta = list(lista)
    lista_vuelta.reverse()

    if lista_original == lista_vuelta:
        return True
    else:
        return False

palabra = input("Ingrese la palabra o frase que desee analizar: ")
if palidromo(palabra):
    print("La palabra o frase es palídromo!")
else:
    print("La palabra o frase NO es polídromo")
