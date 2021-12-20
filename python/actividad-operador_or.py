print("-----Bienvenido al algoritmo para determinar si puede asistir al juego :D-----")

vacaciones = input("estas de vacaciones? (si-no): ")

if vacaciones == "si":
    vacaciones = True
else:
    vacaciones = False 

#print(vacaciones)

diaDescanso = input("estas en un dia de descanso? (si-no): ")

if diaDescanso == "si":
    diaDescanso = True 
else:
    diaDescanso = False 

#print(diaDescanso)

if vacaciones or diaDescanso:
    print("puedes ir ya que tienes tiempo :D")
else:
    print("no puedes ir, tienes cosas por hacer :C")

