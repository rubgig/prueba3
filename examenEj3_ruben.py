print('Introduce un numero:')
num = int(input())

if num <= 0:
    print('El numero tiene que ser mayor que 0!')
elif num%2 != 0:
    print('EL numero',num,'es impar')
else:
    print('El numero',num,'es par')