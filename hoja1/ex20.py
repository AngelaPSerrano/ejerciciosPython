num1 = int(input("Indique el número para saber si es factorial "))
factoriales = 1
almacen = 2

while factoriales < num1:
    factoriales = factoriales * almacen
    almacen = almacen + 1

if num1 == factoriales:
        print(num1, " es un número factorial")
        
else:
    print(num1, " no es un número factorial")
