def menu():

    que = int(input("¿Qué operación desea realizar?\n"
                    " Para pasar de segundos a horas, minutos y segundos pulse 1.\n"
                    " Para pasar de horas minutos y segundos a segundos, pulse 2.\n"
                    " Para salir pulse otro número "))
    if que == 1:
        segundosATodo()
    elif que == 2:
        todoASegundos()

def segundosATodo():
    segundos = int(input("Número de segundos "))

    minutos = int(segundos/60)
    segundos = int(segundos%60)
    horas = int(minutos/60)
    minutos = int(minutos%60)

    print("Horas: ", horas, " minutos: ", minutos, " segundos: ", segundos)
    menu()

def todoASegundos():
    horas = int(input("Número de horas "))
    minutos = int(input("¿Número de minutos "))
    segundos = int(input("Número de segundos "))

    segundosTotales = segundos + (minutos * 60) + ((horas * 60)*60)

    print("Los segundos totales son ", segundosTotales)
    menu()

menu()
