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
                        matrizVista[fila-1][columna-1]= "! "
                        print("¡Le diste!")
        
                else:
                        matrizVista[fila-1][columna-1]= "x " 
                # Imprime la matriz actual
                for x in range (0,num):
                       for j in range(0,num):
                           print(matrizVista[x][j], end = "")
                           if matrizVista[x][j] ==  "! ":
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
                        matrizJugador[fila-1][columna-1]= "! "
                        print("¡Te dieron!")
        
                else:
                        matrizJugador[fila-1][columna-1]= "x "
                
                # Imprime la matriz actual y suma al contador.
                for x in range (0,num):
                        for j in range(0,num):
                           print(matrizJugador[x][j], end = "")
                           if matrizJugador[x][j] == "! ":
                                contadorMuertes = contadorMuertes + 1
                        print()
                # Comprueba si ya se han destruido todos los barcos
                if contadorMuertes >= 7:
                        print("¡Has perdido!")
                        sys.exit()
                print("Te quedan ", int(7- contadorMuertes), " barcos")
                continua()

def continua():
    continua = int(input("¿Desea guardar partida(1) o cargar partida(2)? Si desea continuar, pulse cualquier otro numero "))
    if continua == 1:
        guardarPartida(matrizVista, matrizOculta, matrizJugador)
    elif continua == 2:
        recuperarPartida()
    else:
        jugadorAtaca()
        
def menu():

        menu = int(input("¿Desea empezar una partida nueva(1) o una guardada(2)? "))
        if menu == 1:
            inicio()
        elif menu == 2:
            recuperarPartida()
    
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
                        
        print("Tablero del jugador: ")
        for i in range (0,num):
                for j in range(0,num):
                    print(matrizJugador[i][j], end = "")
                print()
                
        jugadorAtaca()

def guardarPartida(matrizVista, matrizOculta, matrizJugador):
    f = open("saved.txt","w")
    f.write(str(matrizVista))
    f.write("\n")
    f.write(str(matrizOculta))
    f.write("\n")
    f.write(str(matrizJugador))
    f.close()
    print("*Partida guardada*")
    jugadorAtaca()

def recuperarPartida():
        f = open("saved.txt","r")
        lineas = f.readlines()
        tablero1 = []
        tablero2 = []
        tablero3 = []
        tablero1 = [[" " for x in range(num)] for y in range(num)]
        linea1 = list(lineas[0])
        y = 0
        x = 0
        for j in range(len(linea1)):
                if (linea1[j] == "~" or linea1[j] == "!" or linea1[j] == "x") and linea1[j+1] == " " :
                        tablero1[x][y] = linea1[j] + linea1[j+1]
                        y = y+1
                if y == num:
                        x = x+1
                        y = 0
                if x == num:
                        break

        tablero2 = [[0 for x in range(num)] for y in range(num)]
        linea2 = list(lineas[1])
        y = 0
        x = 0
        for j in range(len(linea2)):
                if linea2[j] == 0 or linea2[j] == 0 or linea2[j] == 0:
                        tablero2[x][y] = int(linea2[j])
                        y = y+1
                if y == num:
                        x = x+1
                        y = 0
                if x == num:
                        break
                        
        tablero3 = [[" " for x in range(num)] for y in range(num)]
        linea3 = list(lineas[2])
        y = 0
        x = 0
        for j in range(len(linea3)):
                if (linea3[j] == "~" or linea3[j] == "!" or linea3[j] == "x" or linea3[j] == "B")and linea1[j+1] == " " :
                        tablero3[x][y] = linea3[j] + linea3[j+1]
                        y = y+1
                if y == num:
                        x = x+1
                        y = 0
                if x == num:
                        break
                      
        matrizVista = tablero1
        matrizOculta = tablero2
        matrizJugador = tablero3
        f.close()
        print("*Partida Recuperada*")

        print("Tablero del ordenador:")
        for x in range (0,num):
            for j in range(0,num):
                print(matrizVista[x][j], end = "")
                if matrizVista[x][j] ==  "!":
                    contadorVictorias = contadorVictorias + 1
            print()
        print("Tablero del jugador:")
        for x in range (0,num):
            for j in range(0,num):
                print(matrizJugador[x][j], end = "")
                if matrizJugador[x][j] == "!":
                    contadorMuertes = contadorMuertes + 1
            print()
        
        jugadorAtaca()

def inicializar():
        global num
        global matrizOculta
        global matrizVista
        global matrizJugador
        num = 5
        matrizOculta = [[0 for x in range(num)] for y in range(num)]
        matrizVista = [["  " for x in range(num)] for y in range(num)]
        matrizJugador = [["  " for x in range(num)] for y in range(num)]
        
        
#Programa:
inicializar()
menu()

