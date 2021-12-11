print('-----Bienvenido al algoritmo que determina la estacion del año :D-----')
mes = int(input('En que mes del año estamos, es que perdi mi calendario :c (1-12): '))
estacion = 'nada' 

if mes == 12 or mes == 1 or mes == 2:
    estacion = 'Invierno'
elif mes == 3 or mes == 4 or mes == 5:
    estacion = 'Primavera'
elif mes == 6 or mes == 7 or mes == 8:
    estacion = 'Verano'
elif mes == 9 or mes == 10 or mes == 11:
    estacion = 'Otoño'
    print(estacion)

if estacion == 'nada' or mes >= 13 or mes <= 0:
    print(f'Oye bro no es por molestarte pero {mes} no es un mes del año los meses van del 1 al 12 no se si sabias :/')
else:
    print(f'O asi que estamos a el mes {mes}, eso quiere decir que estamos en {estacion}')
