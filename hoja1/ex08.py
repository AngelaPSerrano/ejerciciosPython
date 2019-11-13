que = input("¿Cuál es la divisa inicial? ")
cantidad = int(input("Introduzca la cantidad de dinero a convertir (solo enteros) "))

def dolaresAEuros(cantidad):
    cantidadFinal = cantidad *0.9
    return cantidadFinal
def eurosADolares(cantidad):
    cantidadFinal = cantidad *1.11
    return cantidadFinal
    

if que == "dolares" or que == "Dolares":
    print(cantidad, " dolares son ", dolaresAEuros(cantidad), " euros")
elif que == "euros" or que == "Euros":
    print(cantidad, " euros son ", eurosADolares(cantidad), " dolares")

