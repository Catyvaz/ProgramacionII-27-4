#Conversor de Moneda
#Desarrolla un programa en Python que convierta una cantidad de dinero de dólares estadounidenses a euros. 
#El programa debe solicitar al usuario que ingrese la cantidad en dólares y luego mostrar la cantidad equivalente en euros
#, utilizando un tipo de cambio fijo.

dolares = float(input("Ingrese la cantidad de dolares: "))
euros = (dolares * 0.9352)
print("{} Dolares, equivalen a {} Euros".format(dolares, euros))