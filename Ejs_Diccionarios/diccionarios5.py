# 5. Diccionario de cuadrados: 
# Escribe una función que reciba un número n y devuelva un
# diccionario con los números de 1 a n como claves y sus cuadrados como valores.

def cuadrado(numero):
    diccionario = {}
    for i in range(1,(numero + 1)):
        valor = i*i
        diccionario[i] = valor
    return diccionario

num = int(input("valor: "))
resultado = cuadrado(num)
print(resultado)