#importar random para usar randint :V
import random

#de clarando todas las variables necesarias
jugador1 = None
jugador2 = None
dado = None 
bucle = True
again = 1
win1 = 0
win2 = 0

#uso la variable bucle para controlar cuando comienza y termina el while

#preguntar los nombres :D
while bucle:
    jugador1 = input('Dime tu nombre jugador1 :D: ')
    jugador2 = input('Dime tu nombre jugador2 :D: ')
    bucle = input(f'asi que se llaman {jugador1} y {jugador2} correcto? (si-no)')
    if bucle == 'si':
        print('ok comensemos :D')
        bucle = False
    else:
        print('vale, en ese caso escriban sus nombres otra vez :D')

#iniciando el juego 
print('-----------------------------------------------------')

#la neta relleno xD
input(f'ok {jugador1} dime una razon por la que tu tienes que ganar?: ')
input(f'vamos {jugador2}, demuestrame por que tienes que ganar?: ')
print('-----------------------------------------------------')

#volviendo a bucle true para el siguiente while
bucle = True

#bucle de juego para repetirlo cuantas veces prefiera el usuario
while bucle:
    dado = random.randint(1,5)
    dado2 = random.randint(1,5)
    if random.randint(1,100) % 2 == 0:  
        if dado > dado2:
            print(f'OMG {jugador1} gano buena suerte la proxima {jugador2}')
            win1 += 1
        elif dado < dado2:
            print(f'OMG {jugador2} gano buena suerte la proxima {jugador1}')
            win2 += 1
    else:
        if dado2 > dado:
            print(f'{jugador1} que suertudo ganaste')
            win1 += 1
        else:
            print(f'{jugador2} que suertudo que sos ganaste')
            win2 += 1
            
    bucle = input('otra partida? (si-no)')
    if bucle == 'si':
        print('-----------------------------------------------------')
        again += 1
        bucle = True
    else:
        print('entendido')
        print('-----------------------------------------------------')
        bucle = False
print(f'''Resumen de la partida
veces que gano {jugador1} = {win1}
veces que gano {jugador2} = {win2}
total de partidas jugadas = {again}''')
