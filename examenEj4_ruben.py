ingresos = []
reintegros = []
opcion = ''
saldo = 0
while opcion != '3':
    print('Que desea hacer?')
    print('1-Ingreso')
    print('2-Reintegro')
    print('3-Salir')
    opcion = input()
    if opcion == '1':
        print('Introduce cantidad:')
        cant=int(input())
        ingresos.append(cant)
        saldo = saldo + cant
        print('Saldo:',saldo)
    elif opcion == '2':
        print('Introduce la cantidad')
        cantReing=int(input())
        if cantReing > saldo:
            print('No hay saldo suficiente!')
        else:
            reintegros.append(-cantReing)
            saldo = saldo - cantReing
            print('Saldo:',saldo)
    
print(ingresos)
print(reintegros)