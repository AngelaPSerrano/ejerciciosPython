def menu():
    que = int(input("¿Cuál es la divisa inicial?\n Para Dolares pulse 1\n Para Euros pulse 2\n"))
    cantidad = int(input("Introduzca la cantidad de dinero a convertir (solo enteros)"))
    if que == 1:
        dolaresAEuros(cantidad)
    elif que == 2:
        eurosADolares(cantidad)

def dolaresAEuros(cantidad):
    cantidadFinal = cantidad *0.9
    print(cantidad, " dolares son ", cantidadFinal, " euros")
    menu()
def eurosADolares(cantidad):
    cantidadFinal = cantidad *1.11
    print(cantidad, " euros son ", cantidadFinal, " dolares")
    menu()
    
menu()
