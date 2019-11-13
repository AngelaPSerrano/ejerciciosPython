class Tablero:

    global matrizOculta, matrizVista
    matrizOculta = [[0 for i in range(0,3)] for j in range(0,3)]
    matrizVista = [[" " for i in range(0,3)] for j in range(0,3)]
    global ganador
    
    def __init__(self):
        pass
        

    def getMatrizOculta(self):
        return matrizOculta
    
    def getMatrizVista(self):
        return matrizVista

    def getGanador(self):
        return ganador

    def dibujarEnVista(self,i,j):

        if matrizOculta[i][j] == 1:
                matrizVista[i][j] = "x"
        elif matrizOculta[i][j] == 2:
                matrizVista[i][j] = "o"
        
        for i in range(len(matrizVista)):
            for j in range(len(matrizVista)):
                print("|", matrizVista[i][j], "|", end="")
            print()

    def comprobadorLibres(self,i,j):

        if matrizOculta[i][j] == 0:
            return True
        else:
            return False


    def compruebaSiGana(self):
        
        if (matrizOculta[0][0] == 1 and matrizOculta[1][0] == 1 and matrizOculta[2][0] == 1) or (matrizOculta[0][1] == 1 and matrizOculta[1][1] == 1 and matrizOculta[2][1] == 1)or (matrizOculta[0][2] == 1 and matrizOculta[1][2] == 1 and matrizOculta[2][2] == 1)or (matrizOculta[0][0] == 1 and matrizOculta[0][1] == 1 and matrizOculta[2][2] == 1)or (matrizOculta[1][0] == 1 and matrizOculta[1][1] == 1 and matrizOculta[1][2] == 1)or (matrizOculta[2][0] == 1 and matrizOculta[2][1] == 1 and matrizOculta[2][2] == 1)or (matrizOculta[0][0] == 1 and matrizOculta[1][1] == 1 and matrizOculta[2][2] == 1)or (matrizOculta[0][2] == 1 and matrizOculta[1][1] == 1 and matrizOculta[2][0] == 1):
            ganador = 1
            return True

        elif (matrizOculta[0][0] == 2 and matrizOculta[1][0] == 2 and matrizOculta[2][0] == 2) or (matrizOculta[0][1] == 2 and matrizOculta[1][1] == 2 and matrizOculta[2][1] == 2)or (matrizOculta[0][2] == 2 and matrizOculta[1][2] == 2 and matrizOculta[2][2] == 2)or (matrizOculta[0][0] == 2 and matrizOculta[0][1] == 2 and matrizOculta[2][2] == 2)or (matrizOculta[1][0] == 2 and matrizOculta[1][1] == 2 and matrizOculta[1][2] == 2)or (matrizOculta[2][0] == 2 and matrizOculta[2][1] == 2 and matrizOculta[2][2] == 2)or (matrizOculta[0][0] == 2 and matrizOculta[1][1] == 2 and matrizOculta[2][2] == 2)or (matrizOculta[0][2] == 2 and matrizOculta[1][1] == 2 and matrizOculta[2][0] == 2):
            ganador = 2
            return True
        
        elif self.compruebaEmpate() == True:
            ganador = 0
            return True
        
        else:
            return False

    def compruebaEmpate(self):
        contadorOcupadas = 0
        
        for i in range(len(matrizOculta)):
            for j in range(len(matrizOculta)):
                if matrizOculta[i][j] != 0:
                    contadorOcupadas = contadorOcupadas + 1

        if contadorOcupadas == 9:
            return True
        else:
            return False

