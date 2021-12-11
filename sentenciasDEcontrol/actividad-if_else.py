print('-----Bienvenido a un algoritmo de conversion de numero a texto :D-----')
numero = int(input("Proporciona un valor entre uno y tres: "))
numeroTexto = ''

if numero == 1:
    numeroTexto = 'Número Uno'
elif numero == 2:
    numeroTexto = 'número Dos'
elif numero == 3:
    numeroTexto = 'número Tres'
else:
    numeroTexto = 'valor fuera de rango'

print(f'Número proporcionado: {numeroTexto}')

