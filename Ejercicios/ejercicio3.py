#Área de un Triángulo
#Escribe un programa en Python que solicite al usuario que ingrese la base y la altura de un triángulo,
#.y luego calcule y muestre el área del triángulo.

base = float(input("Ingrese el tamaño de la base: "))
altura = float(input("Ingrese el tamaño de la altura: "))

areaT = (base * altura)/2

print("El area del triangulo de base {} y altura {} es: {}".format(base, altura, areaT))