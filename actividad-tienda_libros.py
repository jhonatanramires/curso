print("-----Bienvenido al algoritmo de la tienda de libros :D-----")
print("Proporciona los siguientes datos sobre el libro")
nombre = input("Proporciona el nombre del libro: ")
ID = int(input("Proporciona el ID del libro: "))
Precio = float(input("Proporciona el Precio del libro: "))
envio = (input("Indica si el envio es gratuito (True/False): "))
if envio == "True":
    envio = True
elif envio == "False":
    envio = False
print(f'''
    nombre: {nombre}
    ID: {ID}
    Precio: {envio}
    envio: {envio}
''')
#if envio == True:
#    print("el envio es gratuito :D")
#else:
#    print("el envio no es gratuito :C")

