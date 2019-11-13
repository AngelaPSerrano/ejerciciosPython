num1 = int(input("Introduzca un número: "))
num2 = int(input("Introduzca otro número: "))

if num1>num2:
    numAlmacen = num1
    num1 = num2
    num2 = numAlmacen

print("Ordenados son ", num1, " y ", num2)
