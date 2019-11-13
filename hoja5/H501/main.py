from random import randint
from tablero import Tablero


tablero = Tablero()
matrizOculta = tablero.getMatrizOculta()
matrizVista = tablero.getMatrizVista()


def menu():
    
    maquinaOHumano = int(input("¿Contra quién desea jugar?\n1) Maquina\n2) Humano\n"))

    if maquinaOHumano == 1:
        dinamicaVSMaquina()
    elif maquinaOHumano == 2:
        dinamicaVSJugador()
        

def maquinaColoca():

    if tablero.compruebaSiGana() == False:
        
        fil = randint(0,2)
        col = randint(0,2)
        while tablero.comprobadorLibres(fil,col) == False:
            fil = randint(0,2)
            col = randint(0,2)
        
        matrizOculta[fil][col] = 2
        print("Movimiento de la máquina:")
        tablero.dibujarEnVista(fil,col)

def jugadorColoca(num):

    if tablero.compruebaSiGana() == False:
        fil = int(input("Introduce la fila "))
        col = int(input("Introduce la columna "))

        while tablero.comprobadorLibres(fil-1,col-1) == False:
            print("Espacio no libre.")
            fil = int(input("Introduce la fila "))
            col = int(input("Introduce la columna "))
    
        print("Movimiento del jugador " + str(num) + ":")
        matrizOculta[fil-1][col-1] = num
        tablero.dibujarEnVista(fil-1,col-1)

def dinamicaVSMaquina():

    while tablero.compruebaSiGana() == False:
        jugadorColoca(1)
        maquinaColoca()
        
    ganador = tablero.getGanador()
    if ganador == 1:
        print("¡Has ganado!")
    elif ganador == 2:
        print("¡Has perdido!")
    elif ganador == 0:
        print("¡Empate!")

def dinamicaVSJugador():

    while tablero.compruebaSiGana() == False:
        jugadorColoca(1)
        jugadorColoca(2)
        
    ganador = tablero.getGanador()
    if ganador == 1:
        print("¡Ha ganado en jugador 1!")
    elif ganador == 2:
        print("¡Ha ganado el jugador 2!")
    elif ganador == 0:
        print("¡Empate!")

menu()
