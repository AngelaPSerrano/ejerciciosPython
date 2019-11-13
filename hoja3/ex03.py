num = int(input("Escribe el número de números que tendrá la lista  "))
lista = []

for i in range(0, num):
    numAIntroducir = int(input("Introduce el número: "))
    lista.append(numAIntroducir)
    
print(lista)
