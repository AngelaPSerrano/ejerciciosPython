listaLetras = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q",
               "V", "H", "L", "C", "K", "E"]

nif = int(input("Introduzca el NIF: "))

num = nif%23

print("La letra de ese DNI es ", listaLetras[num])

