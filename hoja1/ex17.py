num1 = int(input("Indique el número a multiplicar "))
num2 = int(input("Indique cuantas veces lo quiere multiplicar "))
lista = []

for i in range(1,num2):
    lista.append(num1 * i)
print(lista)
