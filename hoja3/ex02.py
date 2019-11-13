def militarAComun():
    lista = []
    AMPM = "AM"

    while len(lista) != 4:
        numMilitar = input("Introduzca el número a convertir en formato HHMM : ")
        lista = list(numMilitar)

        if len(lista) != 4:
            print("Debe introducir un número con 4 números.")

    horas = int(lista[0]) * 10 + int(lista[1])
    minutos = int(lista[2]) * 10 + int(lista[3])
    if horas > 12:
        horas = horas - 12
        AMPM = "PM"
    print(horas, ":", minutos, " ", AMPM)
        
def comunAMilitar():
    lista = []

    while len(lista) != 3:
        numMilitar = input("Introduzca el número a convertir en formato HH:MM AM : ")
        import re
        lista = re.split(" |:", numMilitar)

        if len(lista) != 3:
            print("Debe introducir un número con 4 números seguido AM/PM")
 
    hora = int(lista[0])
    minutos = int(lista[1])
    if lista[2] == "PM":
        hora = hora + 12
    horaMilitarFinal = (hora*100)+minutos
    print(horaMilitarFinal)
        

menu = int(input("1) Pasar de hora militar a formato común \n2) Pasar de formato común a hora militar\n"))

if menu == 1:
    militarAComun()
elif menu == 2:
    comunAMilitar()
