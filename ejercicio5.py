#Conversor de Temperatura (Actualización)
# Mejora el programa de conversión de temperatura que escribiste anteriormente
# para que permita al usuario elegir entre convertir de grados Celsius a grados Fahrenheit o viceversa.

print("Seleccione que tipo de conversion desea.\n", "Escriba 1 si desea pasar de Fahrenheit a Celsius.\n", "Escriba 2 si desea pasar de Celsius a Fahrenheit.\n")
eleccion = (input("Escriba su selección: "))

if eleccion == "1":
    temperatura = float(input("Coloque la temperatura en Fahrenheit: "))
    resultado = (temperatura - 32)/1.8
    print("El resultado de la conversion es: {}".format(resultado))
elif eleccion == "2":
    temperatura = float(input("Coloque la temperatura en Celsius: "))
    resultado = (temperatura * 1.8) + 32
    print("El resultado de la conversion es: {}".format(resultado))
else:
    print("No se ingreso comando valido")