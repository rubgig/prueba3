print('Inntroduce tu edad:')
edad=int(input())
print('Ingresos mensuales:')
ingresos=int(input())
if edad >= 16 and ingresos > 1000 :
    print('Tiene que tributar')
else:
    print('No tiene que tributar')