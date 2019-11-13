# Version barcos de un tamanyo
import random
import sys 

# Jugador contra maquina
def jugadorAtaca():
        contadorVictorias = 0
        
        while contadorVictorias < 3:
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
                if contadorVictorias >= 3:
                        print("¡Has ganado!")
                        sys.exit()
                print("Le quedan ", int(3- contadorVictorias), " barcos")
                maquinaAtaca()
               
        
        


# Maquina contra jugador


def maquinaAtaca():
        contadorMuertes = 0
        
        while contadorMuertes < 3:
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
                if contadorMuertes >= 3:
                        print("¡Has perdido!")
                        sys.exit()
                print("Te quedan ", int(3- contadorMuertes), " barcos")
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
        
        for i in range (0, 3):
                valido = 0
                while valido == 0:
                        randomCol = random.randint(0, num-1)
                        randomFil = random.randint(0, num-1)
                        if matrizOculta[randomFil][randomCol] == 0:
                                valido = 1
                                matrizOculta[randomFil][randomCol] = 1
                        else:
                                valido = 0


        #Introduce los puntos donde están los barcos del jugador
        for i in range (0,num):
                for j in range(0,num):
                    matrizJugador[i][j]= "~ "
                    
                
        for i in range (0, 3):
                textoFila = "Introduce la fila de tu barco número "+str(i+1)+": "
                textoColumna = "Introduce la columna de tu barco número "+str(i+1)+": "
                fil = int(input(textoFila))
                col = int(input(textoColumna))
                if matrizJugador[fil-1][col-1] == "~ ":
                        matrizJugador[fil-1][col-1] = "B "
                        
        print("Tablero del jugador: ")
        for i in range (0,num):
                for j in range(0,num):
                    print(matrizJugador[i][j], end = "")
                print()
                
        jugadorAtaca()

        
#Programa:
num = int(input("¿Medidas del tablero?  "))
matrizOculta = [[0 for x in range(num)] for y in range(num)]
matrizVista = [[0 for x in range(num)] for y in range(num)]
matrizJugador = [[0 for x in range(num)] for y in range(num)]
inicio()
