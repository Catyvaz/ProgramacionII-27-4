# Ejercicio 3
# Diseñar una función que calcule el área y el perímetro de una circunferencia. 
# Utiliza dicha función en un programa principal que lea el radio de una circunferencia y muestre su área y perímetro.
import math

def calcular_area_perimetro(radio):
    radio = float(radio)
    area = math.pi * (radio ** 2)
    perimetro = 2 * math.pi * radio

    return area, perimetro

valor_radio = input("Ingrese el valor del radio: ")
area_perimetro = calcular_area_perimetro(valor_radio)
print(f"El valor del area y perimetro de {valor_radio} es : {area_perimetro}")