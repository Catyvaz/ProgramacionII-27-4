#Escribe un programa que solicite al usuario que ingrese una temperatura en grados Celsius y luego muestre la temperatura equivalente en grados Fahrenheit.
#Instrucciones:
#Solicita al usuario que ingrese una temperatura en grados Celsius.
#Convierte la temperatura ingresada a grados Fahrenheit utilizando la fórmula proporcionada.
#Muestra el resultado al usuario.

celsius = float(input("Ingrese temperatura en grados Celsius: "))

def Convercion_F(valor):
    fahren = (valor * (9/5)) + 32
    return fahren

print("El valor de {} Celsius a Fahrenheit es: {} ".format(celsius, Convercion_F(celsius)))
