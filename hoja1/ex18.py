num1 = int(input("Indique el número para saber si es triangular "))
triangulares = 1
almacen = 2

while triangulares < num1:
    triangulares = triangulares + almacen
    almacen = almacen + 1

if num1 == triangulares:
        print(num1, " es un número triangular")
        
else:
    print(num1, " no es un número triangular")

