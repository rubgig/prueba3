print('Pizza vegetariana o no vegetariana:')
pizza=input()
if pizza == 'vegetariana':
    print('Ingredientes vegetarianos: Pimiento, Tofu')
    print('Elige uno:')
    ingrediente=input()
else:
    print('Ingredientes no vegetarianos: Pepperoni, Jamon, Salmon')
    print('Elige uno:')
    ingrediente=input()
print('Pizza:',pizza,'Ingredientes: Mozzarella, Tomate,',ingrediente)