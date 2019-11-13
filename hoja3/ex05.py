import random 

ancho = 3
largo = 3
almacen = [[0 for x in range(ancho)] for y in range(largo)] 

for i in range (3):
        for j in range(3):
            randomNum = random.randint(0,9)
            almacen[i][j]= randomNum
            print(almacen[i][j], end = "")
        print()
    
fila = int(input("Introduce la fila: "))
columna = int(input("Introduce la columna: "))

almacen[fila-1][columna-1] = 0;

for i in range (3):
        for j in range(3):
            print(almacen[i][j], end = "")
        print()

