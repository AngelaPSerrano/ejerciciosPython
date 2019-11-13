num1 = int(input("Indique el número para saber si es factorial "))
divisores = 1
almacen = []

while divisores <= num1:
    if num1 % divisores == 0:
        almacen.append(divisores)
    divisores = divisores + 1
    
print("Los divisores de ", num1, " son ", almacen)
