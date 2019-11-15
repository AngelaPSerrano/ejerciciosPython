import random

global dineroGanado

#Genera resultados del sorteo y archiva en .txt
def generarSorteo():
    f = open("sorteo.txt", "w")
    f.write(generarNumero() + " 15000\n")
    f.write(generarNumero() + " 5000\n")
    f.write(generarNumero() + " 2500\n")
    for i in range(2):
        f.write(generarNumero() + " 1000\n")
    for i in range(8):
        f.write(generarNumero() + " 250\n")
    for i in range(1531):
        f.write(generarNumero() + " 5\n")
    f.close()
    
#Genera un número aleatorio
def generarNumero():
    numeros = [0 for i in range(5)]
    for i in range(5):
        numeros[i] = str(random.randint(0,9))
    
    return "".join(numeros)

#Lee el archivo de sorteo y lo mete en un array bidimensional
def leerSorteo():
    f = open("sorteo.txt", "r")
    documento = f.readlines()
    listaPremios = [0 for i in range(len(documento))]
    for i in range(0,len(documento)):
        listaPremios[i] = documento[i].split()
    f.close()
    return listaPremios

#Lee el archivo de participaciones y lo mete un array bidimensional
def leerParticipacion():
    f = open("participacion.txt", "r")
    documento = f.readlines()
    listaParticipacion = [0 for i in range(len(documento))]
    for i in range(0,len(documento)):
        listaParticipacion[i] = documento[i].split()
    f.close()
    return listaParticipacion

#Compara los dos arrays y devuelve si hay ganador
def verSiPremio():
    listaParticipacion = leerParticipacion()
    listaPremios = leerSorteo()
    dineroGanado = 0
    for i in range(len(listaPremios)):
        for j in range (len(listaParticipacion)):
            if listaPremios[i][0] == listaParticipacion[j][0]:
                dineroGanado = dineroGanado + (int(listaPremios[i][1]) * int(listaParticipacion[j][1]))
                print("¡Ha ganado un premio! ", motivoPremio(int(listaPremios[i][1])), ", gana ", (int(listaPremios[i][1]) * int(listaParticipacion[j][1])), "€ con el numero ", listaPremios[i][0] )  
    if dineroGanado == 0:
        print("No ha ganado ningun premio.")
    elif dineroGanado > 0:
        print("Ha ganado un total de ", dineroGanado, "€")
    print("Dinero Invertido: ", dineroInvertido(listaParticipacion), "€")

#Suma del dinero invertido
def dineroInvertido(listaParticipacion):
    dineroInvertido = 0
    for i in range(len(listaParticipacion)):
        dineroInvertido = dineroInvertido + int(listaParticipacion[i][1])
    return dineroInvertido

#Devuelve el motivo del premio
def motivoPremio(motivo):
    if motivo == 15000:
        return "Primer Premio"
    elif motivo == 5000:
        return "Segundo Premio"
    elif motivo == 1000:
        return "Tercer Premio"
    elif motivo == 250:
        return "Cuarto Premio"
    elif motivo == 5:
        return "Quinto Premio"
            
def main():
    generarSorteo()
    verSiPremio()

main()
