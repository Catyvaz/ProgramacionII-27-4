#Validación de Contraseña
#Escribe un programa en Python que valide una contraseña ingresada por el usuario. La contraseña debe cumplir con los siguientes requisitos:
# - Debe tener al menos 8 caracteres de longitud.
# - Debe contener al menos una letra mayúscula, una letra minúscula, un número y un carácter especial (por ejemplo, !, @, #, $, %, etc.). 
# - El programa debe informar al usuario si la contraseña es válida o no.

contraseña = input("Ingrese su contraseña. \n*Recuerde que debe contener, al menos; \n - Una mayúscula.\n - Una minuscula.\n - Un número.\n - Un caracter especial (!, @, #, $, %, etc)* \nContraseña:")

def contiene_(lista):
    esta = False
    for i in range(len(lista)):
        value = lista[i]
        if value

#if len(contraseña > 7)