class Bombilla:
    global count 
    global encendida

    def __init__(self):
        self.setCount(0)
        self.setEncendida(False)

    def setCount(self, count):
        self.count = count
    
    def setEncendida(self, encendida):
        self.encendida = encendida
        
    def encender(self):
        if self.fundida() == False:
            if self.encendida == False:
                    print("La bombilla se ha encendido")
                    self.count = self.count +1
                    self.setEncendida(True)
            else: 
                print("La bombilla ya estaba encendida")

    def apagar(self):
        if self.fundida() == False:
            if self.encendida == True:
                    print("La bombilla se ha apagado")
                    self.setEncendida(False)
            else:
                print("La bombilla ya estaba apagada")

    def fundida(self):
        if self.count >= 1000:
            print("La bombilla está fundida")
            return True
        else:
            return False

class PruebaBombilla:
    bombilla = Bombilla()
    #Encendemos y apagamos mil veces
    for i in range(1000): 
        bombilla.encender()
        bombilla.apagar() 

    #Y otra vez más, aunque debería estar fundida ya
    bombilla.encender()
    bombilla.apagar()
