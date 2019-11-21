class Coche:
    def __init__(self, matricula, maxLitrosDeposito, consumoMedio, velocidadMax):
        self.matricula = str(matricula)
        self.maxLitrosDeposito = self.setMaxLitrosDeposito(float(maxLitrosDeposito))
        self.velocidadMax = self.setVelocidadMax(float(velocidadMax))
        self.consumoMedio = float(consumoMedio) #por km/h
        self.maxLitrosReserva = (self.maxLitrosDeposito/100)*15

        self.motorArrancado = False
        self.estaEnReserva = True
        self.numLitrosActual = 0.0
        self.velocidadActual = 0.0
        self.kilometraje = 0.0
    
    def setVelocidadMax(self, velocidadMax):
        if velocidadMax < 0:
            return 180.0
        else:
            return velocidadMax
    
    def setMaxLitrosDeposito(self, maxLitrosDeposito):
        if maxLitrosDeposito < 0:
            return 50
        else:
            return maxLitrosDeposito

    def setConsumoMedio(self, consumoMedio):
        if consumoMedio < 0:
            return 7.5
        else:
            return consumoMedio

    def arrancarMotor(self):
        if self.motorArrancado == False:
            if self.numLitrosActual > 0:
                self.motorArrancado = True
                print("El coche con matricula ", self.matricula, " ha arrancado.")
                if self.estaEnReserva:
                    print("El coche con matricula ", self.matricula, " esta en reserva de combustible.")
            else:
                print("El coche con matricula ", self.matricula, " no ha posido arrancar porque no le queda gasolina.")
        else: 
            print("El coche con matricula ", self.matricula, " ya estaba arrancado.")

    def pararMotor(self):
        if self.motorArrancado == True:
            self.motorArrancado = False
            print("El coche con matricula ", self.matricula, " ha parado.")
        else:
            print("El coche con matricula ", self.matricula, " ya estaba parado.")

    def repostar(self, litros):
        if self.numLitrosActual + litros > self.maxLitrosDeposito:
            self.numLitrosActual = self.maxLitrosDeposito
            print("El coche con matricula ", self.matricula, " ha rebosado su deposito.")
        else:
            if litros > 0:
                self.numLitrosActual = self.numLitrosActual + litros

        print("El coche con matricula ", self.matricula, " tiene ", self.numLitrosActual, " litros de gasolina.")

    def fijarVelocidad(self, velocidad):
        if self.motorArrancado == True:
            if self.velocidadMax < velocidad:
                self.velocidadActual = self.velocidadMax
            elif velocidad < 0:
                self.velocidadActual = 0
            else: 
                self.velocidadActual = velocidad

            print("El coche con matricula ", self.matricula, " conduce a ", self.velocidadActual)
        else:
            print("El coche con matricula ", self.matricula, " esta parado.")

    def recorrerDistancia(self, kilometros):
        if self.motorArrancado == False:
            print("El coche con matricula ", self.matricula, " esta parado.")
        elif self.velocidadActual == 0:
            print("El coche con matricula ", self.matricula, " conduce a 0km/h.")
        else:
            if kilometros <= 0:
                print("El coche con matricula ", self.matricula, " no puede recorrer esos kilometros.")
            else: 
                if self.numLitrosActual > (kilometros*(self.consumoMedio*(1+(self.velocidadActual-100)/100)))/100:
                    print("El coche con matricula ", self.matricula, " ha recorrido ", kilometros ,"km.")
                    self.numLitrosActual = self.numLitrosActual - (kilometros*self.consumoMedio*(1+(self.velocidadActual-100)/100))/100
                    if self.numLitrosActual <= self.maxLitrosReserva:
                        print("El coche con matricula ", self.matricula, " esta en reserva de combustible.")
                else: 
                    distanciaReal = 100 * self.numLitrosActual/((kilometros*self.consumoMedio*(1+(self.velocidadActual-100)/100))/100)
                    print("El coche con matricula ", self.matricula, " ha recorrido ", distanciaReal ,"km.")
                    print("El coche con matricula ", self.matricula, " se ha quedado sin gasolina.")
                    self.pararMotor()

