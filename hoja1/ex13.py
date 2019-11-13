menu = int(input("¿Qué conversión desea realizar?\n"
                 "De Celsius a Fahrenheit, pulse 1\n"
                 "De Fahrenheit a Celsius, pulse 2\n"))

def celsiusAFharenheit():
    celsius = float(input("Introduzca los grados Celsius: "))
    fahrenheit = (celsius*9/5)+32
    print(celsius, " grados Celsius son ", fahrenheit, " grados Fahrenheit")

def fahrenheitACelsius():
    fahrenheit = float(input("Introduzca los grados Fahrenheit: "))
    celsius = (fahrenheit - 32)*5/9
    print(fahrenheit, " grados Fahrenheit son ", celsius, " grados Celsius")

if menu == 1:
    celsiusAFharenheit()
elif menu == 2:
    fahrenheitACelsius()
