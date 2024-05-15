#Generador de Contraseñas Aleatorias 
#Escribe un programa en Python que genere una contraseña aleatoria para el usuario. 
#La contraseña debe tener una longitud de al menos 12 caracteres y debe contener una combinación de:
# letras (mayúsculas y minúsculas)
# números
# caracteres especiales. 
# El programa debe mostrar la contraseña generada al usuario.
import random 

def generador(cantidad):
    lista = []
    opciones = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ123456789°¬!$%&/()=?¡¿*+~[]^-.,;:_"
    for i in range(int(cantidad)):
        valor = random.choice(opciones)
        lista.append(valor)
        unido = "".join(lista)
    return unido

while True:
    longitud = input("Ingrese la longitud de su contraseña (recuerde que debe ser mayor de 12): ")
    if longitud.isdigit():
        if (int(longitud) >= 12 and int(longitud) < 30):
            contraseña = generador(longitud)
            print(f"Su contraseña es: {contraseña}")
            break
        elif int(longitud) < 12:
            print("Recuerde que la contraseña debe ser mayor que 12.")
        elif int(longitud) > 30:
            print("El límite de caracteres para la contraseña es de 30")
    else:
        print("Ingrese un valor numérico")