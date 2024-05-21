#Ejercicio 2
# Crea una función “calcularMaxMin” que recibe una lista con valores numéricos y devuelve el
# valor máximo y el mínimo. Crea un programa que pida números por teclado y muestre el
# máximo y el mínimo, utilizando la función anterior.

def calcularMaxMin(lista):
    for i in range (len(lista)):
        if lista[i].isdigit:
            if i == 0:
                maximo = int(lista[i])
                minimo = int(lista[i])
            elif int(lista[i]) > maximo:
                maximo = int(lista[i])
            elif int(lista[i]) < minimo:
                minimo = int(lista[i])
        resultado = [maximo, minimo]
    return resultado

def calcular_max_min(lista):
    lista = sorted(lista)
    maximo = lista[0]
    valor = (len(lista) - 1)
    minimo = lista[valor]
    return [maximo, minimo]

numeros = []
contador = 0
while True:
    print("Para terminar de ingresar numeros, escriba FIN")
    numero = input(f"Ingrese número {contador}: ")
    if numero.isdigit():
        numeros.append(numero)
    elif numero.isalpha():
        if numero.upper() == "FIN":
            break
        else:
            print("Comando no entendido")
    contador = contador + 1

valores = calcularMaxMin(numeros)
valores_2 = calcular_max_min(numeros)
print(valores)
print(valores_2)