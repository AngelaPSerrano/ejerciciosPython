anyo = int(input("Dí un año y te diré si es bisiesto: "))

if (anyo%4==0 and anyo%100!=0) or anyo%400==0:
    print(anyo, " sí es un año bisiesto")
else:
    print(anyo, " no es un año bisiesto")
