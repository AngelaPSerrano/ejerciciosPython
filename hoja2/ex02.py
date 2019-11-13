import random
from random import randint

aSet = 0
bSet = 0

setTenis = int(input("¿Cuántos set van a jugar? "))
               
for i in range(setTenis):
    juego = 0
    aPuntos = 0
    bPuntos = 0
    setGanado = False
    i = i + 1
    
    while setGanado == False:
        juego = juego + 1
        quienMarca = randint(0, 1)
    
        if quienMarca == 0:
            aPuntos = aPuntos + 1
            print("A ha ganado el juego")
        
        elif quienMarca == 1:
            bPuntos = bPuntos + 1
            print("B ha ganado el juego")

        print("PUNTOS\nA: ", aPuntos, " B: ", bPuntos)
        
        if aPuntos == 7 or (aPuntos == 6 and bPuntos <= 4):
            aSet = aSet + 1
            print("A ganó el Set")
            setGanado = True

        if bPuntos == 7 or (bPuntos == 6 and aPuntos <= 4):
            bSet = bSet + 1
            print("B ha ganado el set")
            setGanado = True
            
    print("SETS:\nA: ", aSet," B: ", bSet)
    
    if aSet >= int((setTenis/2) + 1):
        print("A Gana la partida")
        break
    
    if bSet >= int((setTenis/2) + 1):
        print("B Gana la partida")
        break
    
