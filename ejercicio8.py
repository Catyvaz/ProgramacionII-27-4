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
    opciones = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ123456789°¬!$%&/()=?¡¿'*+~[]^-.,;:_"
    for i in range(len(cantidad)):
        valor = random.choice(opciones)
        lista.append(valor)
    return lista

while True:
    longitud = input("Ingrese la longitud de su contraseña (recuerde que debe ser mayor de 12): ")
    if longitud.isdigit():
        if (int(longitud) >= 12):
            contraseña = generador (int(longitud))
            print(f"Su contraseña es: {contraseña}")
            break
        else:
            print("Recuerde que la contraseña debe ser mayor que 12.")
    else:
        print("Ingrese un valor numérico")