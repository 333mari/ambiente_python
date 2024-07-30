# Se crea una variable NOTAS donde se pide al usuario sus notas
notas = input('ingrese sus notas: ')
# Cada nota ingresada se convierte en un punto flotante y las almacena en una lista de llamada NOTAS
notas = [float(notas) for notas in notas.split()]
# calcula el promedio de todas las NOTAS en la lista NOTAS
promedio = sum(notas) / len(notas)
# Calcula el promedio en consola
print('su promedio es: ', promedio)

# split: para separar las notas ingresadas por espacios
# la funcion FLOAT es para convertir las notas a numeros de puntos flotantes
# len: para obtener la cantidad de notas 

