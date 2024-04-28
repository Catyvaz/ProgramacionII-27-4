#Contador de Palabras
#Desarrolla un programa en Python que solicite al usuario que ingrese una frase y luego cuente
# y muestre el número de palabras en esa frase.

maximo = 100
cont = 0
booleano = 0

frase = input("Ingrese su frase: ".format(maximo))

def hay_num(lista):
    value = 0
    for i in range(len(lista)):
        if not lista[i].isdigit:
            value = value =+ 0
        else:
            value = value =+ 1
    if value == (len(lista) + 1):
        return True
    else:
        return False

listaF = frase.split()
for i in range(len(listaF)):
    palabra = listaF[i]
    booleano = hay_num(palabra)
    if booleano == True:
        cont += 1

print(cont)