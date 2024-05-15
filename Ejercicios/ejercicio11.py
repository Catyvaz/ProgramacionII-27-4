# Adivinador de números
# Crea un juego que le pida al usuario que piense un número entre 1 y 100. 
# Luego, el programa debe intentar adivinar ese número utilizando la estrategia de búsqueda binaria. 
# En cada intento, el programa debe preguntar al usuario si el número a adivinar es mayor, menor o igual al número propuesto por el programa. 
# El juego debe terminar cuando el programa adivine el número correcto.

def mayor_menor(numero):
    
    nuevo = []
    if numero == 1:
        nuevo.append()

    return medio



while True:
    valor = int(input("El número es; Mayor : 1, Menor : 2, Igual : 3."))
    if valor == 1:
        # buscar mayor
    elif valor == 2:
        # buscar menor
    elif valor == 3:
        print("Adivine el valor!")
    else:
        print("Comando no válido")