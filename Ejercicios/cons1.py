#Escribe un programa que solicite al usuario que ingrese su peso en kilogramos y su altura en metros, luego calcule y muestre su IMC.
#Instrucciones:
#Solicita al usuario que ingrese su peso en kilogramos.
#Solicita al usuario que ingrese su altura en metros.
#Calcula el IMC utilizando la fórmula proporcionada.
#Muestra el resultado al usuario.

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

IMC = peso / (altura * altura)

print("El valor del IMC es: ", IMC)
 