segundos = int(input("Número de segundos "))

minutos = int(segundos/60)
segundos = int(segundos%60)
horas = int(minutos/60)
minutos = int(minutos%60)

print("Horas: ", horas, " minutos: ", minutos, " segundos: ", segundos)
