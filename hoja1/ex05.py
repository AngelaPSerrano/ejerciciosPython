edad = int(input("¿Cuál es su edad? "))
fecha = input("¿Qué fecha es hoy? En formato DD/MM/AAAA ")
fechaNacimiento = input("¿Día y mes de tu nacimiento? En formato DD/MM ")

fecha = fecha.split("/")
fechaNacimiento = fechaNacimiento.split("/")


def anyoMenosEdad(fecha, edad):
    anyoNacimiento = int(fecha[2]) - edad
    return anyoNacimiento


if fechaNacimiento[1] > fecha[1]:
    if fechaNacimiento[0] > fecha[0]:
        anyoNacimiento = anyoMenosEdad(fecha, edad) +1
else:
    anyoNacimiento = anyoMenosEdad(fecha, edad)


print("Naciste el año ", anyoNacimiento)
