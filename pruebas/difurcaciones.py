# # 1. Completa el código siguiente para que "Buenos dias" siempre y cuando se introduzca el nombre Ana.
# nombre = input('introduce tu nombre: ')
# if nombre == 'ana':
#     print('¡Buenos días!')

# 2. Completa el código siguiente para que diga "Coge un pastel" siempre y cuando se introduzca "pastel".
# De lo contrario, haz que le ofrezca una galleta

# Solicita al usuario que introduzca su comida favorita
comida = input('¿Cuál es tu comida favorita?: ')

# Verifica si la comida introducida es "pastel"
if comida.lower() == 'pastel':  # .lower() asegura que la comparación no sea sensible a mayúsculas
    print('Coge un pastel')
else:
    print('Coge una galleta')
