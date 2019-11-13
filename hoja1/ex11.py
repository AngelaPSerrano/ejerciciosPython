num1 = int(input("Introduzca un número: "))
num2 = int(input("Introduzca otro número: "))
num3 = int(input("Introduzca un tercer número: "))

while num1>num2 or num2>num3 or num1>num3:
    if num1>num2:
        numAlmacen = num1
        num1 = num2
        num2 = numAlmacen
    if num2>num3:
        numAlmacen = num2
        num2 = num3
        num3 = numAlmacen
    if num1>num3:
        numAlmacen = num1
        num1 = num3
        num3 = numAlmacen

print("Ordenados son ", num1, ", ", num2, " y ",num3)
