nota = int(input('Proporciona la nota del alumno: '))

calificacion = None

if 9 <= nota <= 10:
    calificacion = 'A'
elif 8 <= nota < 9:
    calificacion = 'B'
elif 7 <= nota < 8:
    calificacion = 'C'
elif 6 <= nota < 7:
    calificacion = 'D'
elif 0 <= nota < 6:
    calificacion = 'F'

if calificacion != None:
    print(f'la nota del estudiante es {nota}, en ese caso su calificacion es {calificacion}')
else:
    print('pusiste un valor invalido las notas van del 0-10, intentelo nuevamente')

