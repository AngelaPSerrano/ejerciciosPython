def cerrar():
    f.close()

f = open("H06_01.txt", "w")
f.write("Kogarashi\n")
cerrar()

f = open("H06_01.txt", "a")
f.write("Japonés. El viento frio del norte que anuncia la llegada del invierno agitando las hojas de los árboles.")
cerrar()
