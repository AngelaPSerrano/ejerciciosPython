import random

class Loteria:

    global premio
    global reintegro
    global numeroPremio

    def __init__(self):
        self.premio = 50000
        self.reintegro = 5

    def getPremio(self):
        return self.premio
    
    def getReintegro(self):
        return self.reintegro

    def generaGanador(self):
        self.listaGanador = [0 for i in range(0,5)] 
        for i in range(0,5):
            self.listaGanador[i] = random.randint(0,9)
        return self.listaGanador
