from simulacion import Simulacion

simulacion = Simulacion()

numeroPiezas = int(input("¿Con cuantas piezas vamos a jugar? "))
while numeroPiezas >7 or numeroPiezas <3:
    print("Número no valido. Solo de 3 a 7.")
    numeroPiezas = int(input("¿Con cuantas piezas vamos a jugar? "))
    
simulacion.setNumeroPiezas(numeroPiezas)
simulacion.vistaInicial()


