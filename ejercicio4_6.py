print('Introduce tu nombre:')
nombre=input()
print('Sexo:')
sexo=input()
if nombre[0] < 'M' and sexo == 'Mujer':
    print('Grupo A')
elif nombre[0] > 'N' and sexo == 'Hombre':
    print('Grupo A')
else:
    print('Grupo B')