edad = int(input("¿Cuál es su edad? "))
fecha = input("¿Qué fecha es hoy? En formato DD/MM/AAAA ")
siONo = input("¿Has cumplido años ya este año? ")
fecha = fecha.split("/")

def anyoMenosEdad(fecha, edad):
    anyoNacimiento = int(fecha[2]) - edad
    return anyoNacimiento


if siONo == "si" or siONo == "Si":
    anyoNacimiento = anyoMenosEdad(fecha, edad)
else:
    anyoNacimiento = anyoMenosEdad(fecha, edad) + 1


print("Naciste el año ", anyoNacimiento)

