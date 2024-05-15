# Ejercicio 1
# Crea un función “ConvertirEspaciado”, que reciba como parámetro un texto y devuelve una
# cadena con un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” devolverá “H o l a , t ú “. 
# Crea un programa principal donde se use dicha función luego del ingreso del usuario.

def ConvertirEspaciado(lista):
    nueva = []
    contador = 0
    for i in range (len(lista)):
        if lista[i] == " ":
            nueva.append(lista[i])
        else:
            nueva.append(lista[i] + " ")
    return "".join(nueva)

oracion = input("Ingrese su oración: ")
convercion = ConvertirEspaciado(oracion)
print(convercion)

