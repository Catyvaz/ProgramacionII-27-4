# Adivinador de números
# Crea un juego que le pida al usuario que piense un número entre 1 y 100. 
# Luego, el programa debe intentar adivinar ese número utilizando la estrategia de búsqueda binaria. 
# En cada intento, el programa debe preguntar al usuario si el número a adivinar es mayor, menor o igual al número propuesto por el programa. 
# El juego debe terminar cuando el programa adivine el número correcto.

def medio(lista):
    valor_medio = len(lista) // 2
    return valor_medio

def mayor(lista):
    lista_mayor = lista[(medio(lista)):]
    return lista_mayor

def menor(lista):
    lista_menor = lista[:(medio(lista))]
    return lista_menor

print("********************************")
print("*Jueguemos a adivinar el número*")
print("********************************")
lista = list(range(1,101))
while True:
    num = medio(lista)
    print("El número es: ", lista[num - 1])
    valor = int(input("El número que pensaste es; \n Mayor : 1. \n Menor : 2. \n Igual : 3. \n: "))
    if valor == 1:
        lista = mayor(lista)
    elif valor == 2:
        lista = menor(lista)
    elif valor == 3:
        print("Adivine el valor!")
        break
    else:
        print("Comando no válido")