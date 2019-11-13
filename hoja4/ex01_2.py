#Version con barcos de varios tamanyos


import random
import sys 

# Jugador contra maquina
def jugadorAtaca():
        contadorVictorias = 0
        
        while contadorVictorias < 7:
                fila = 0
                columna = 0
                while fila > num or fila <= 0:
                        fila = int(input("Introduce la fila a atacar: "))
                while columna > num or columna <= 0:
                        columna = int(input("Introduce la columna a atacar: "))
                #if matrizVista[fila-1][columna-1] != "~ ":
                #        print("Estas coordenadas ya han sido bombardeadas")
                        
                print("¡Bombardeas en las coordenadas ", fila, "x", columna, "!")
                # Comprueba si hay un barco en la posición en oculto y lo pone en vista
                if matrizOculta[fila-1][columna-1] == 1:
                        matrizVista[fila-1][columna-1]= "?"
                        print("¡Le diste!")
        
                else:
                        matrizVista[fila-1][columna-1]= "x " 
                # Imprime la matriz actual
                for x in range (0,num):
                       for j in range(0,num):
                           print(matrizVista[x][j], end = "")
                           if matrizVista[x][j] ==  "?":
                                contadorVictorias = contadorVictorias + 1
                       print()
                if contadorVictorias >= 7:
                        print("¡Has ganado!")
                        sys.exit()
                print("Le quedan ", int(7- contadorVictorias), " barcos")
                maquinaAtaca()
               
        
        


# Maquina contra jugador


def maquinaAtaca():
        contadorMuertes = 0
        
        while contadorMuertes < 7:
                fila = random.randint(1,num)
                columna = random.randint(1,num)
        
                print("¡Te bombardean en las coordenadas ", fila, "x", columna, "!")

                # Comprueba si hay un barco en la posición en oculto y lo pone en vista
                if matrizJugador[fila-1][columna-1] == "B " or matrizJugador[fila-1][columna-1]== "?":
                        matrizJugador[fila-1][columna-1]= "?"
                        print("¡Te dieron!")
        
                else:
                        matrizJugador[fila-1][columna-1]= "x "
                
                # Imprime la matriz actual y suma al contador.
                for x in range (0,num):
                        for j in range(0,num):
                           print(matrizJugador[x][j], end = "")
                           if matrizJugador[x][j] == "?":
                                contadorMuertes = contadorMuertes + 1
                        print()
                # Comprueba si ya se han destruido todos los barcos
                if contadorMuertes >= 7:
                        print("¡Has perdido!")
                        sys.exit()
                print("Te quedan ", int(7- contadorMuertes), " barcos")
                jugadorAtaca()
        

def inicio():

        #Genera las matrices vista y oculta e imprime la primera
        print("Tablero del ordenador: ")
        for i in range (0,num):
                for j in range(0,num):
                    matrizOculta[i][j]= 0
                    matrizVista[i][j]= "~ "
                    print(matrizVista[i][j], end = "")
                print()
        
        #Genera los puntos donde están los barcos
        
        for i in range (0, 2):
                colocable = 0
                while colocable == 0:
                        horizontalVertical = random.randint(0,1)
                        if horizontalVertical == 0:
                                randomCol = random.randint(0, num-2)
                                randomFil = random.randint(0, num-1)
                
                                if matrizOculta[randomFil][randomCol] == 0 and matrizOculta[randomFil][randomCol+1] == 0:
                                        colocable = 1
                                        matrizOculta[randomFil][randomCol] = 1
                                        matrizOculta[randomFil][randomCol+1] = 1
 
                                else:
                                        colocable = 0
                        elif horizontalVertical == 1:
                                randomCol = random.randint(0, num-1)
                                randomFil = random.randint(0, num-2)
                                if matrizOculta[randomFil][randomCol] == 0 and matrizOculta[randomFil+1][randomCol] == 0:
                                        colocable = 1
                                        matrizOculta[randomFil][randomCol] = 1
                                        matrizOculta[randomFil+1][randomCol] = 1
                                                
                                else:
                                        colocable = 0
        # Barco de 3
        colocable = 0
        while colocable == 0:
                horizontalVertical = random.randint(0,1)
                
                if horizontalVertical == 0:
                        randomCol = random.randint(0, num-3)
                        randomFil = random.randint(0, num-1)
                        if matrizOculta[randomFil][randomCol] == 0 and matrizOculta[randomFil][randomCol+1] == 0 and matrizOculta[randomFil][randomCol+2] == 0 :
                                colocable = 1
                                matrizOculta[randomFil][randomCol] = 1
                                matrizOculta[randomFil][randomCol+1] = 1
                                matrizOculta[randomFil][randomCol+2] = 1
 
                        else:
                                colocable = 0
                elif horizontalVertical == 1:
                        randomCol = random.randint(0, num-1)
                        randomFil = random.randint(0, num-3)
                        if matrizOculta[randomFil][randomCol] == 0 and matrizOculta[randomFil+1][randomCol] == 0 and matrizOculta[randomFil+2][randomCol] == 0 :
                                colocable = 1
                                matrizOculta[randomFil][randomCol] = 1
                                matrizOculta[randomFil+1][randomCol] = 1
                                matrizOculta[randomFil+2][randomCol] = 1
                                                
                        else:
                                colocable = 0



        #Introduce los puntos donde están los barcos del jugador
        for i in range (0,num):
                for j in range(0,num):
                    matrizJugador[i][j]= "~ "
                    
                
        #Nuevo codigo
        
        for i in range(0,2):
                colocable = False
                print("Barco de dos casillas número ", i+1)
                verticalHorizontal = int(input("¿Posición vertical(1) u horizontal(2)? "))
        
                if verticalHorizontal == 2:
                        while colocable == False:
                                fil = int(input("Indique la fila de la esquina superior del barco: "))
                                col = int(input("Indique la columna de la esquina superior del barco: "))
                                if col > num:
                                        print("El barco se sale de las dimensiones")
                                elif matrizJugador[fil-1][col-1] == "B " or matrizJugador[fil-1][col] == "B ":
                                        print("Ya hay un barco ocupando esos huecos")
                                else:
                                        colocable = True
                                        if matrizJugador[fil-1][col-1] == "~ ":
                                                matrizJugador[fil-1][col-1] = "B "
                                        if matrizJugador[fil-1][col] == "~ ":
                                                matrizJugador[fil-1][col] = "B "
                elif verticalHorizontal == 1:
                        while colocable == False:
                                fil = int(input("Indique la fila de la esquina izquierda del barco: "))
                                col = int(input("Indique la columna de la esquina izquierda del barco: "))
                                if fil > num:
                                        print("El barco se sale de las dimensiones")
                                elif matrizJugador[fil-1][col-1] == "B " or matrizJugador[fil][col-1] == "B ":
                                        print("Ya hay un barco ocupando esos huecos")
                                else:
                                        colocable = True
                                        if matrizJugador[fil-1][col-1] == "~ ":
                                                matrizJugador[fil-1][col-1] = "B "
                                        if matrizJugador[fil][col-1] == "~ ":
                                                matrizJugador[fil][col-1] = "B "
                else:
                        print("Valor no valido")
                        sys.exit()
                for i in range (0,num):
                        for j in range(0,num):
                            print(matrizJugador[i][j], end = "")
                        print()
                        
        print("Barco de 3 casillas")
        verticalHorizontal = int(input("¿Posición vertical(1) u horizontal(2)? "))
        colocable = False
        if verticalHorizontal == 2:
                
                while colocable == False:
                        fil = int(input("Indique la fila de la esquina superior del barco: "))
                        col = int(input("Indique la columna de la esquina superior del barco: "))
                
                        if col+1 >= num:
                                print("El barco se sale de las dimensiones")
                        elif matrizJugador[fil-1][col-1] == "B " or matrizJugador[fil-1][col] == "B " or matrizJugador[fil-1][col+1] == "B ":
                               print("Ya hay un barco ocupando esos huecos")
                        else:
                                colocable = True
                                if matrizJugador[fil-1][col-1] == "~ ":
                                        matrizJugador[fil-1][col-1] = "B "
                                if matrizJugador[fil-1][col] == "~ ":
                                        matrizJugador[fil-1][col] = "B "
                                if matrizJugador[fil-1][col+1] == "~ ":
                                        matrizJugador[fil-1][col+1] = "B "
        elif verticalHorizontal == 1:
                while colocable == False:
                        fil = int(input("Indique la fila de la esquina izquierda del barco: "))
                        col= int(input("Indique la columna de la esquina izquierda del barco: "))
                        if fil+1 > num:
                                print("El barco se sale de las dimensiones")
                        elif matrizJugador[fil-1][col-1] == "B " or matrizJugador[fil][col-1] == "B " or matrizJugador[fil+1][col-1] == "B ":
                               print("Ya hay un barco ocupando esos huecos")
                        else:
                                colocable = True
                                if matrizJugador[fil-1][col-1] == "~ ":
                                        matrizJugador[fil-1][col-1] = "B "
                                if matrizJugador[fil][col-1] == "~ ":
                                        matrizJugador[fil][col-1] = "B "
                                if matrizJugador[fil+1][col-1] == "~ ":
                                        matrizJugador[fil+1][col-1] = "B "
        else:
                print("Valor no valido")
                sys.exit()

        #Fin nuevo codigo
                        
        print("Tablero del jugador: ")
        for i in range (0,num):
                for j in range(0,num):
                    print(matrizJugador[i][j], end = "")
                print()
                
        jugadorAtaca()

        
#Programa:
num = 5
matrizOculta = [[0 for x in range(num)] for y in range(num)]
matrizVista = [[0 for x in range(num)] for y in range(num)]
matrizJugador = [[0 for x in range(num)] for y in range(num)]
inicio()
