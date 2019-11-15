import random
import sys

def posValida(i,j):

        if i >= 0 and j >= 0 and i < num and j < num:
                
                if tableroVisible[i][j] == 0 or tableroVisible[i][j] == 1 or tableroVisible[i][j] == 2:

                        return True
                else:
                        return False
        else:
                return False
        
def generaAleatorio():
        
        for i in range (0, num):
                for j in range(0,num):
                        rndm = random.randint(0, 1)
                        tableroVisible[i][j] = rndm
        printTablero()
        menu()

def generaBlanco():
        
        for i in range (0,num):
                for j in range(0,num):
                    tableroVisible[i][j]= 0
        printTablero()
        menu()
        
def compruebaBicho(i,j):

        contadorBichos = 0
        for x in range (i-1,i+2):
                if posValida(x,j-1):
                        if tableroVisible[x][j-1] == 1:
                                contadorBichos = contadorBichos + 1
        if posValida(i,j-1):
                if tableroVisible[i][j-1] == 1:
                        contadorBichos = contadorBichos + 1
        if posValida(i,j+1):
                if tableroVisible[i][j+1] == 1:
                        contadorBichos = contadorBichos + 1
        for x in range (i-1,i+2):
                if posValida(x,j+1):
                        if tableroVisible[x][j+1] == 1:
                                contadorBichos = contadorBichos + 1
                                
        #Y ahora actúa:
        if contadorBichos <=1 or contadorBichos >= 4:
                muereBicho(i,j)
        elif contadorBichos == 3:
                naceBicho(i,j)

def muereBicho(i,j):
        if tableroVisible[i][j] == 1:
                tableroOculto[i][j] = 0
       

def naceBicho(i,j):
        if tableroVisible[i][j] == 0:
                tableroOculto[i][j] = 1
        

def menu():

        select = int(input("¿Qué desea hacer a continuación?\n"
                           "1) Generar nuevo tablero aleatorio\n"
                           "2) Generar nuevo tablero en blanco\n"
                           "3) Nuevo bicho en coordenadas a indicar\n"
                           "4) Borrar bicho en coordenadas a indicar\n"
                           "5) Simular determinado número de generaciones\n"
                           "6) Guardar partida\n"
                           "7) Recuperar partida\n"
                           "8) Salir\n"))
        if select == 1:
                datosTablero()
                generaAleatorio()
        elif select == 2:
                datosTablero()
                generaBlanco()
        elif select == 3:
                col = int(input("¿En qué fila? "))
                fil = int(input("¿En qué columna? "))
                
                if posValida(fil-1, col-1):
                        naceBicho(fil-1, col-1)
                        printTablero()
                        menu()
                else:
                        print("Posición no existente")
                        menu()
        elif select == 4:
                fil = int(input("¿En qué fila? "))
                col = int(input("¿En qué columna? "))
                
                if posValida(fil-1, col-1):
                        muereBicho(fil-1, col-1)
                        printTablero()
                        menu()
                else:
                        print("Posición no existente")
                        menu()
        elif select == 5:
                veces = int(input("¿Cuantas generaciones quieres mostrar? "))
                for i in range(0, veces):
                        for i in range(0, num):
                                for j in range(0, num):
                                        compruebaBicho(i,j)
                        print("\n", "Gen ", i+1)
                        printTablero()
                        
                menu()
        elif select == 6:
                guardarPartida(num, tableroVisible, tableroOculto)
                print("Partida guardada.")
                menu()
        elif select == 7:
                recuperarPartida()
                print("Partida recuperada.")
                printTablero()
                menu()
        elif select == 8:
                sys.exit()


def printTablero():
        for i in range(0, num):
                for j in range(0, num):
                        tableroVisible[i][j] = tableroOculto[i][j]
                        print(tableroVisible[i][j],end= "")
                print()
        print(num, tableroVisible)
        
def datosTablero():
        global num
        global tableroVisible
        global tableroOculto

        num = int(input("¿Tamaño del tablero? "))
        while num > 20:
                print("Tamaño máximo 20")
                num = int(input("¿Tamaño del tablero? "))
                
        tableroVisible = [[0 for x in range(num)] for y in range(num)]
        tableroOculto = tableroVisible
        tableroOculto = tableroVisible
        
def guardarPartida(num, tableroVisible, tableroOculto):
    f = open("saved.txt","w")
    f.write(str(num))
    f.write("\n")
    f.write(str(tableroVisible))
    f.write("\n")
    f.write(str(tableroOculto))
    f.close()

def recuperarPartida():
        f = open("saved.txt","r")
        lineas = f.readlines()
        print(len(lineas))
        numero = int(lineas[0])
        tablero1 = []
        tablero2 = []
        tablero1 = [[0 for x in range(numero)] for y in range(numero)]
        linea1 = list(lineas[1])
        for j in range(len(linea1)):
                y = 0
                x = 0
                if linea1[j] == "1" or linea1[j] == "0":
                        tablero1[x][y] = int(linea1[j])
                        y = y+1
                if y == numero:
                        x = x+1
                        
        tablero2 = [[0 for x in range(numero)] for y in range(numero)]
        linea2 = list(lineas[2])
        for j in range(len(linea2)):
                y = 0
                x = 0
                if linea2[j] == "1" or linea2[j] == "0":
                        tablero2[x][y] = int(linea2[j])
                        y = y+1
                if y == numero:
                        x = x+1
        num = numero
        tableroVisible = tablero1
        tableroOculto = tablero2
        print(num, tableroOculto)
        f.close()

select = int(input("¿Qué desea hacer a continuación?\n"
                   "1) Generar nuevo tablero aleatorio\n"
                   "2) Generar nuevo tablero en blanco\n"))

datosTablero()

if select == 1:
        generaAleatorio()
elif select == 2:
        generaBlanco()

