from simulacion import Simulacion

simulacion = Simulacion()

def comprobarValores(valor):
    if valor == "O" or valor == "A" or valor == "D":
        return True
    else:
        return False

numeroPiezas = int(input("¿Con cuantas piezas vamos a jugar? "))
while numeroPiezas >7 or numeroPiezas <3:
    print("Número no valido. Solo de 3 a 7.")
    numeroPiezas = int(input("¿Con cuantas piezas vamos a jugar? "))
    
simulacion.setNumeroPiezas(numeroPiezas)
simulacion.vistaInicial()

while simulacion.juegoFinalizado() == False:
    origen = (input("¿De qué torre cogemos la pieza? ¿O, A, D? ")).upper()
    while comprobarValores(origen) == False:
        print("Introduzca un valor válido")
        origen = input("¿De qué torre cogemos la pieza? ¿O, A, D? ").upper()
        
    destino = input("¿En qué torre la dejamos? ").upper()
    while comprobarValores(destino) == False:
        print("Introduzca un valor válido")
        destino = input("¿En qué torre la dejamos? ").upper()
        
    simulacion.moverPieza(origen,destino)
    simulacion.mostrarTorres()
    
print("¡LO CONSEGUISTE!")
