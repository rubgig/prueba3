print('Introduce edad:')
edad = int(input())
if edad < 4 :
    print('Entrada gratis')
elif edad >= 4 and edad <= 18:
    print('ENtrada 5€')
else:
    print('ENtrada 10€')