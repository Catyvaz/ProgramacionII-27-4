#Validación de Contraseña
#Escribe un programa en Python que valide una contraseña ingresada por el usuario. La contraseña debe cumplir con los siguientes requisitos:
# - Debe tener al menos 8 caracteres de longitud.
# - Debe contener al menos una letra mayúscula, una letra minúscula, un número y un carácter especial (por ejemplo, !, @, #, $, %, etc.). 
# - El programa debe informar al usuario si la contraseña es válida o no.

contraseña = input("Ingrese su contraseña. \n*Recuerde que debe contener, al menos; \n - Una mayúscula.\n - Una minuscula.\n - Un número.\n - Un caracter especial (!, @, #, $, %, etc)* \nContraseña:")

def mayuscula(lista):
    estado = False
    for i in range(len(lista)):
        value = lista[i]
        if lista[i].isupper():
            estado = True
            break
    return estado

def minuscula(lista):
    estado = False
    for i in range(len(lista)):
        value = lista[i]
        if lista[i].islower():
            estado = True
            break
    return estado

def numeros(lista):
    estado = False
    for i in range(len(lista)):
        value = lista[i]
        if lista[i].isdigit():
            estado = True
            break
    return estado

def caracter(lista):
    estado = False
    for i in range(len(lista)):
        value = lista[i]
        if not(lista[i].isalpha() or lista[i].isdigit()):
            estado = True
            break
    return estado

if len(contraseña) > 7:
    value = mayuscula(contraseña) and minuscula(contraseña) and numeros(contraseña) and caracter(contraseña)
    if value:
        print("Su contraseña es válida")
    else:
        print("Contraseña no válida")