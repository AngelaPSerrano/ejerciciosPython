import random
from random import randint

contador = 0

for i in range(10):
    num1=randint(1,10)
    num2=randint(1,10)
    print(num1, "x", num2," = ")
    respuesta = int(input())
    if num1*num2 == respuesta:
        print("¡Es correcto!")
        contador = contador + 1
    else:
        print("¡Error!")

print("Has conseguido ", contador, " respuesta correctas de 10")
