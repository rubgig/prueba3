helados = {'Chocolate':'1,99€','Nata':'2,49€','Vainilla':'2,49€','Fresa':'2,49€'}
print('Que helado desea?')
helado=input()
if helado.title() in helados:
    print(helado,helados[helado.title()])
else:
    print('El helado de:',helado,'no esta disponible')