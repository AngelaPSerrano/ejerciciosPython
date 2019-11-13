lista = input("Introduzca 20 números, separados por comas")

lista = lista.split(",")
total = 0

for i in range(len(lista)):
    total = total + int(lista[i])
    
total = total/20
print("La media es", total)
