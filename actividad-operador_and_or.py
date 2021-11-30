print("-----Bienvenido al algoritmo para determinar en que rango de edad estas :D-----")
edad = int(input("ingresa tu edad: "))
menor = edad >= 1 and edad < 18
veintes = edad >= 20 and edad < 30 
treintas = edad >= 30 and edad < 40
adulto = edad >= 40 and edad < 100
viejo = edad >= 100 and edad < 120
if menor or veintes or treintas or adulto or viejo:
    if veintes: 
        print("estas entre los 20 a 29 años eres veinteañer@")
    elif treintas:
        print("estas entre los 30 a 39 años eres treinteañer@")
    elif menor: 
        print("eres menor de edad :D")
    elif adulto:
        print("eres un adulto :D")
    elif viejo:
        print("que lindo que sigues vivo :d")

else:
    print("fuera de rango")
