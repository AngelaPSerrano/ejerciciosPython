import random

class Jugador:
    global dineroGastado
    global dineroGanado
    global numeroJugado
    global numeroVeces
    global semanas
    
    def __init__(self):
        self.dineroGastado = 0
        self.dineroGanado = 0

    def setNumeroJugado(self, numeroJugado):
        self.numeroJugado = list(str(numeroJugado))
        self.numeroJugado = [int(i) for i in self.numeroJugado] 

    def setNumeroVeces(self, numeroVeces):
        self.numeroVeces = numeroVeces

    def setSemanas(self,semanas):
        self.semanas = semanas

    def getSemanas(self):
        return self.semanas

    def setNumeroFijo(self,numeroFijo):
        self.numeroFijo = numeroFijo

    def definirCondiciones(self):
        print("El premio de cada sorteo son 5000€.\nEl precio del boleto son 5€.\nHay dos sorteos por semana.")
        num = int(input("¿Cuantas apuestas va a hacer por sorteo? "))
        self.setNumeroVeces(num)

        num = int(input("¿Desea jugar con un número fijo(1) o dinámico(2)"))
        if num == 1:
            self.setNumeroFijo(True)
            num = int(input("Introduzca el número de 5 cifras a jugar: "))
            while num < 10000 or num > 99999:
                print("Número no valido")
                num = int(input("Introduzca el número de 5 cifras a jugar: "))
            self.setNumeroJugado(num)

        else:
            self.setNumeroFijo(False)

        
        self.semanas = int(input("¿Cuantas semanas jugamos? "))


    def compraBoleto(self):
        self.dineroGastado = self.dineroGastado + (5*self.numeroVeces)
        if self.numeroFijo == False:
            self.numeroJugado = [random.randint(0,9) for i in range(0,5)]

    def ganaPremio(self, premio, repeticion, listaGanador, reintegro):
 
        numeroscoincidentes = 0
        
        for i in range(0,5):
            if listaGanador[i] == self.numeroJugado[i]:
                numeroscoincidentes = numeroscoincidentes + 1
        if numeroscoincidentes == 5:
            print("¡Ha ganado el premio del sorteo numero ", repeticion, "!")
            self.dineroGanado = self.dineroGanado + (premio * self.numeroVeces)
        elif listaGanador[4] == self.numeroJugado[4]:
            print("¡Ha ganado el reintegro del sorteo numero ", repeticion, "!")
            self.dineroGanado = self.dineroGanado + (reintegro * self.numeroVeces)

    def resultado(self):
        print("\nResultados tras jugar ", self.semanas, " semana/s:")
        print("Ha invertido ", self.dineroGastado)
        print("Ha ganado ", self.dineroGanado)
        print("El saldo final es ", (self.dineroGanado-self.dineroGastado))
