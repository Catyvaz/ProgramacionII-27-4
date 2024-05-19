# Ejercicio 7
# Contar letras: Crea una función que tome una cadena como entrada y devuelva un
# diccionario con el recuento de cada letra en la cadena.

def contar_letras(lista):
    letras = {}
    for elemento in lista:
        if elemento.isalpha():
            if elemento not in letras:
                letras[elemento] = 1
            else:
                letras[elemento] += 1
    return dict(sorted(letras.items()))

cadena = input("Ingrese la palabra o frase que desee analizar: ")
cadena = list(cadena)
cadena_letras = contar_letras(cadena)
print(cadena_letras)