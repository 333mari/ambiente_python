# 1. Escribe las líneas que faltan en el código para que se escriba del 1 al 12.
a = 0
while a < 12:
    a = a + 1
    print(a)

# 2. Modifica el código anterior para que se cree un contador infinito.
a = 0
while True:  # Bucle infinito
    a = a + 1
    print(a)
    if a == 12:  # Reinicia el contador al llegar a 12
        a = 0

# 3. Escribe la línea de código que falta de forma que el programa pregunte por el nombre, hasta que se escriba Carlos.    
    # Preguntar por el nombre
    nombre = input('¿Cuál es tu nombre? ')
    if nombre.lower() == 'carlos':  # No sensible a mayúsculas/minúsculas
        print('¡Hola, Carlos!')
        break  # Sale del bucle infinito
    else:
        print('Nombre incorrecto, intenta de nuevo.')
