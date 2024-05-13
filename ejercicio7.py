#Juego de Adivinar el Número
# Desarrolla un juego en el que el programa selecciona aleatoriamente un número entre 1 y 100 y el jugador debe adivinarlo. 
# El programa debe proporcionar pistas al jugador si el número ingresado es demasiado alto o demasiado bajo. 
# El juego debe continuar hasta que el jugador adivine correctamente el número.
import random

numero = random.randint(1,100)

while True:
    respuesta = input("Que número será?: ")
    if respuesta.isdigit():
        respuesta = int(respuesta)
        if respuesta < numero:
            print("El número es más grande.")
        elif respuesta > numero:
            print("El número es más chico")
        elif respuesta == numero:
            print(f"¡Adivinaste el número!, era el {numero}")
            break
    else:
        print("Coloque un valor numérico")