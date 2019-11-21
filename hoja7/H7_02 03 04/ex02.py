class Televisor:

    def __init__(self, marcaInicial, modeloInicial, anioInicial):
        self.setMarca(marcaInicial)
        self.setModelo(modeloInicial)
        self.setAnio(anioInicial)
        self.encendida = False
        self.panoramica #Dan problemas porque no se como inicalizar por defecto :D
        self.stereo
        pass

    def setMarca(self, marca):
        self.marca = str(marca)

    def getMarca(self):
        return self.marca

    def setModelo(self, modelo):
        self.modelo = str(modelo)
    def getModelo(self):
        return self.modelo

    def setAnio(self, anio):
        if anio >= 1950 and anio <=2200:
            self.anio = anio
        else:
            self.anio = 2000
    def getAnio(self):
        return self.anio

    def setPanoramica(self, panoramica):
        self.panoramica = bool(panoramica)
    def getPanoramica(self):
        return self.panoramica

    def setStereo(self, stereo):
        self.stereo = bool(stereo)
    def getStereo(self):
        return self.stereo

    def setVolumen(self, volumen):
        if self.encendida == False:
            print("Está apagada")
        else:
            if volumen >= 0 and volumen <=100:
                self.volumen = int(volumen)
                print("Volumen: ", self.volumen)
            else:
                print("Volumen no valido")

    def getVolumen(self):
        return self.volumen

    def setCanal (self, canal):
        if self.encendida == False:
            print("Está apagada")
        else:
            if canal >= 0 and canal <= 99:
                self.canal = canal
                print("Canal: ", self.canal)
            else:
                print("Canal no valido")

    def encender(self):
        if self.encendida == True:
            print("Ya está encendida")
        else:
            self.encendida = True
            print("Has encendido la television")

    def apagar(self):
        if self.encendida == False:
            print("Ya está apagada")
        else:
            self.encendida = False
            print("Has apagado la television")
        
    def seleccionarCanal(self, nuevoCanal):
        if self.encendida == False:
            print("Está apagada")
        else:
            if self.encendida:
                self.setCanal(nuevoCanal)
            else:
                print("Televisor apagado")
        
    def obtenerCanal(self):
        if self.encendida == False:
            print("Está apagada")
        else:
            if self.encendida:
                return self.canal
            else:
                return "Televisor apagado"
    
    def subirCanal(self):
        if self.encendida == False:
            print("Está apagada")
        else:
            if self.encendida:
                self.setCanal(self.canal+1)
            else:
                return "Televisor apagado"

    def bajarCanal(self):
        if self.encendida == False:
            print("Está apagada")
        else:
            if self.encendida:
                self.setCanal(self.canal-1)
            else:
                return "Televisor apagado"
    
    def cambiarVolumen(self, nuevoVolumen):
        if self.encendida == False:
            print("Está apagada")
        else:
            if self.encendida:
                self.setVolumen(nuevoVolumen)
            else:
                return "Televisor apagado"

    def imprimirCaracteristicas(self):
        print("Marca: ", self.marca)
        print("Modelo: ", self.modelo)
        print("Año: ", self.anio)
        print("Panorámica: ", self.panoramica)
        print("Stereo: ", self.stereo)

        
    