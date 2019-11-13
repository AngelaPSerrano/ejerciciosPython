class Simulacion:

    global numeroPiezas
    global torreO
    global torreA
    global torreD
    global punteroO
    global punteroA
    global punteroD

    def __init__(self):
        self.punteroO = -1

    def setNumeroPiezas(self, numeroPiezas):
        self.numeroPiezas = numeroPiezas
        self.punteroA = numeroPiezas-1
        self.punteroD = numeroPiezas-1
    
    def vistaInicial(self):
        self.torreO = ["" for i in range(0,self.numeroPiezas)]
        self.torreA = ["" for i in range(0,self.numeroPiezas)]
        self.torreD = ["" for i in range(0,self.numeroPiezas)]
        
        for i in range (0, self.numeroPiezas):
            self.torreO[i] = " " *(self.numeroPiezas-i-1) + "*"*(2*i+1) + " "*(self.numeroPiezas-i-1)
            self.torreA[i] = " " * (self.numeroPiezas*2)
            self.torreD[i] = " " * (self.numeroPiezas*2)
            print(self.torreO[i], " ", self.torreA[i], " ", self.torreD[i])
            
        self.imprimirBase()


    def mostrarTorres(self):
        for i in range (0, self.numeroPiezas):
            print(self.torreO[i], self.torreA[i], self.torreD[i])
            
        self.imprimirBase()
        
    def imprimirBase(self):
        for i  in range (0,2):
            print(("="*(self.numeroPiezas*2-1)), end= " ")
        print("="*(self.numeroPiezas*2-1))
        print(" "*(self.numeroPiezas-1), end= "")
        print("O",end= "")
        print(" "*((self.numeroPiezas-1)*2+1), end= "")
        print("A", end= "")
        print(" "*((self.numeroPiezas-1)*2+1), end= "")
        print("D")

    def moverPieza(self, origen, destino):

        if self.comprobarPieza(origen, destino):
            if origen == "O":
                self.punteroO = self.punteroO+1
                self.storage = self.torreO[self.punteroO]
                self.torreO[self.punteroO] = " "*(self.numeroPiezas*2-1)
            elif origen == "A":
                self.punteroA = self.punteroA+1
                self.storage = self.torreA[self.punteroA]
                self.torreA[self.punteroA] = " "*(self.numeroPiezas*2-1)
            elif origen == "D":
                self.punteroD = self.punteroD+1
                self.storage = self.torreD[self.punteroD]
                self.torreD[self.punteroD] = " "*(self.numeroPiezas*2-1)
            if destino == "O":
                self.torreO[self.punteroO] = self.storage
                self.punteroO = self.punteroO-1
            elif destino == "A":
                self.torreA[self.punteroA] = self.storage
                self.punteroA = self.punteroA-1
            elif destino == "D":
                self.torreD[self.punteroD] = self.storage
                self.punteroD = self.punteroD-1
        else:
            print("La pieza inferior es menor a la superior, por lo que no se puede colocar ahí.")

    def comprobarPieza(self, origen, destino):
        print(self.punteroO+1)
        if origen == "O":
            self.piezaSuperior = self.torreO[self.punteroO+1]
        elif origen == "A":
            self.piezaSuperior = self.torreA[self.punteroA+1]
        elif origen == "D":
            self.piezaSuperior = self.torreD[self.punteroD+1]
        try:
            if destino == "O":
                 self.piezaInferior = self.torreO[self.punteroO+1]
            elif destino == "A":
                self.piezaInferior = self.torreA[self.punteroA+1]
            elif destino == "D":
                self.piezaInferior = self.torreD[self.punteroD+1]
        except:
            self.piezaInferior = " "

        if (self.piezaSuperior.count("*") > self.piezaInferior.count("*")) and self.piezaInferior.count("*") > 0:
            return False
        else:
            return True
                                        
    def juegoFinalizado(self):
        if self.punteroD == -1:
            return True
        else:
            return False

