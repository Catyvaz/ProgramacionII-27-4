# Juego del Ahorcado 
# Juego de Ahorcado: Crea un juego de ahorcado donde el jugador debe adivinar una palabra oculta antes de que se agoten los intentos. 
# Puedes hacerlo con una lista predefinida de palabras.
import random

def letra_en_la_palabra(palabra, letra):
    palabra_nueva = []
    for elemento in palabra:
        if elemento != letra:
            palabra_nueva.append(elemento)
    return palabra_nueva

def letra_incorrecta(numero):
    if numero == 1:
        print("  (.,.)   ")
    elif numero == 2:
        print("  (.,.)   ")
        print("   /      ")
    elif numero == 3:
        print("  (.,.)   ")
        print("   / \\   ")
    elif numero == 4:
        print("  (.,.)   ")
        print("   /|\\   ")
    elif numero == 5:
        print("  (.,.)   ")
        print("   /|\\   ")
        print("   /      ")
    elif numero == 6:
        print("  (.,.)   ")
        print("   /|\\   ")
        print("   / \\   ")
    elif numero == 7:
        print("  (-,-)/  ")
        print("   ---/   ")
        print("   /|\\   ")
        print("   / \\   ")

def letra_acertada(lista, lista2, letra):
    for i in range(len(lista)):
        if lista[i] == letra:
            lista2[i] = letra
    return lista2

def lista_de_guiones(lista):
    lista_guiones = ["_"] * len(lista)
    return lista_guiones 

print("**********************")
print("* JUEGO DEL AHORCADO *")
print("**********************")

lista_palabras = ["elefante", "computadora", "programacion", "bicicleta", "arquitectura", "biblioteca", "astronauta", "matematicas", "volcan", "dinosaurio", "fotografia", "galaxia", "electricidad", "helicoptero"]
palabra_para_adivinar = list(random.choice(lista_palabras))
correcta = list(palabra_para_adivinar)
conteo_intentos = 0
lista_guiones = lista_de_guiones(palabra_para_adivinar)
letras_correctas = []
letras_incorrectas = []

print(f"Tu palabra tiene {len(palabra_para_adivinar)} letras. \nBuena suerte!")
while True:
    print(lista_guiones)
    print("Letras correctas usadas: ", letras_correctas)
    print("Letras incorrectas usadas: ", letras_incorrectas)
    letra = (input("Cúal letra?: ")).lower()
    if letra not in letras_correctas and letra not in letras_incorrectas:
        if letra.isalpha() and len(letra) == 1:
            if letra in palabra_para_adivinar:
                lista_guiones = letra_acertada(correcta, lista_guiones, letra)
                palabra_para_adivinar = letra_en_la_palabra(palabra_para_adivinar, letra)
                letras_correctas.append(letra)

                if len(palabra_para_adivinar) == 0:
                    print("CORRECTO")
                    print("Adivinaste la palabra, era: ", "".join(correcta))
                    break
            else:
                conteo_intentos += 1
                print(" ")
                imprime = letra_incorrecta(conteo_intentos)
                print(" ")
                letras_incorrectas.append(letra)
                if conteo_intentos == 7:
                    print("Perdiste, la palabra era ", "".join(correcta))
                    break
        else:
            print("Ingrese una letra.")
    else:
        print("Letra ya ingresada")

