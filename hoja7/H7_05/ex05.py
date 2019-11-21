class CuentaBanco:
    def __init__(self, num, titular):
        self.setNumero(int(num))
        self.setTitular(str(titular))
        self.bloqueada = False
        self.saldo = 0

    def setSaldo(self, saldo):
        self.saldo = float(saldo)

    def setNumero(self, numero):
        self.numero = numero

    def setTitular(self, titular):
        self.titular = titular
    
    def consultarSaldo(self):
        return self.saldo
    
    def ingresarDinero(self, cantidad):
        if self.bloqueada:
            print("Cuenta bloqueada")
        else:
            self.saldo = self.saldo + cantidad

    def retirarDinero(self, cantidad):
        if self.bloqueada:
            print("Cuenta bloqueada")
        else:
            if (self.saldo - cantidad) >= 0:
                self.saldo = self.saldo - cantidad
            else:
                print("No hay saldo suficiente para realizar la operación")

    def cambioTitular(self, nuevoTitular):
        if self.bloqueada:
            print("Cuenta bloqueada")
        else:
            if nuevoTitular == "":
                print("Nombre no valido")
            else:
                self.titular = nuevoTitular

    def bloquear(self):
        self.bloqueada = True
    
    def desbloquear(self):
        self.bloqueada = False

    def imprimirDatos(self):

        print("Titular: ", self.titular)
        print("Número de cuenta: ", self.numero)
        print("Saldo: ", self.saldo,"€")

