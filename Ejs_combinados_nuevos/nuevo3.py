# Inventario de productos : 
# Escribe una función que recibe un diccionario donde las claves son los nombres de los productos 
# y los valores son listas de precios históricos de esos productos. La función debe devolver un nuevo diccionario donde las 
# claves son los nombres de los productos y los valores son el precio promedio de cada producto.

def inventario(diccionario):
    prom_inventario = {}
    for producto, precios in diccionario.items():
        valor = diccionario[producto]
        promedio = sum(valor)/ len(valor)
        prom_inventario[producto] = promedio
    return prom_inventario

precios_productos = {
    "Martillo": [5, 8.5, 14.6, 20],
    "Destornillador": [6, 15, 19, 22],
    "Lapiz": [6, 7, 8, 10, 12],
    "Hojas": [5, 4, 6, 8]
}
print(inventario(precios_productos))