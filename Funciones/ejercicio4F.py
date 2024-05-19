# Ejercicio 4
# Crear una subrutina llamada “Login”, que recibe un nombre de usuario y una contraseña y te
# devuelve Verdadero si el nombre de usuario es “usuario1” y la contraseña es “asdasd”.
# Además recibe el número de intentos que se ha intentado hacer login y si no se ha podido
# hacer login incremente este valor, validar con otra función la cantidad de intentos posibles en
# 3 oportunidades.
# Crear un programa principal donde se pida un nombre de usuario y una contraseña y se
# intente hacer login, recuerden solamente tenemos tres oportunidades para intentarlo.

def login(nombre, contraseña):
    if nombre == "usuario1" and contraseña == "asdasd":
        return True
    else:
        return False

def intentos(numero):
    if numero == 3:
        return False
    else:
        numero += 1
        return numero

valor = 1
while True:
    usuario = input("Ingrese nombre de usuario: ")
    contraseña = input("Ingrese contraseña: ")
    if login(usuario, contraseña):
        print("Bienvenido!")
        break
    else:
        print("Usuario o contraseña incorrecta")
        valor = intentos(valor)
        if valor == False:
            print("Demasiados intentos")
            break


