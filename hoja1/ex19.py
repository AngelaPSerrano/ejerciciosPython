num1 = int(input("Indique el número para conocer ese número de triangulares "))
triangulares = 1
almacen = 2

for i in range(num1):
    triangulares = triangulares + almacen
    almacen = almacen + 1
    print(triangulares)
