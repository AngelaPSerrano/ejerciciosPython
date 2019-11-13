horas = int(input("Número de horas "))
minutos = int(input("¿Número de minutos "))
segundos = int(input("Número de segundos "))

segundosTotales = segundos + (minutos * 60) + ((horas * 60)*60)

print("Los segundos totales son ", segundosTotales)
