class Simulacion:

    global numeroPiezas
    global torreO
    global torreA
    global torreD
    global punteroO
    global punteroA
    global punteroD

    def __init__(self):
        self.punteroA = 0
        self.punteroD = 0

    def setNumeroPiezas(self, numeroPiezas):
        self.numeroPiezas = numeroPiezas
        self.punteroA = numeroPiezas-1
    
    def vistaInicial(self):
        self.torreO = ["" for i in range(0,self.numeroPiezas)]
        self.torreA = ["" for i in range(0,self.numeroPiezas)]
        self.torreD = ["" for i in range(0,self.numeroPiezas)]

        for i in range (0, self.numeroPiezas):
            self.torreO[i] = " "*(self.numeroPiezas-i-1) + "*"*(2*i+1) + " "*(self.numeroPiezas-i-1)
            self.self.torreA[i] = " "*self.numeroPiezas
            self.torreD[i] = " "*self.numeroPiezas
            print(self.torreO[i], " ", self.torreA[i], " ", self.torreD[i])
            
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
        print("D", end= "")

    def moverPieza(self, origen, destino):
        if origen == "O":
            storage = torreO[punteroO]
        elif origen == "A":
            storage = torreA[punteroA]
        elif origen == "D":
            storage = torreD[punteroD]
        if destino == "O":
            torreO[punteroO] = storage
        elif destino == "A":
            torreA[punteroA] = storage
        elif destino == "D":
            torreD[punteroD] = storage
