# 1. Notas de estudiantes : 
# Escribe una función que recibe un diccionario donde las claves son nombres de estudiantes
# y los valores son listas de sus calificaciones. La función debe devolver un nuevo diccionario con las mismas claves 
# pero donde los valores son la calificación promedio de cada estudiante.

def prom_notas(diccionario):
    alumno_promedio = {}
    for alumno, notas in diccionario.items():
        valor = diccionario[alumno]
        promedio = sum(valor)/(len(valor))
        alumno_promedio[alumno] = promedio
    return alumno_promedio

notas_alumnos = {
    "Amanda": [7, 8, 10, 9],
    "Carla": [10, 9, 7, 5],
    "Marcos": [9, 8, 7, 6],
    "Pedro": [5, 4, 6, 8]
}
print(prom_notas(notas_alumnos))