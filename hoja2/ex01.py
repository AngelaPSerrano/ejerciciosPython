largo = 0
izqdcha = 2.5
while largo < 15:
    num = int(input("Dí un numero: "))

    if num%2==0:
        largo = largo+1
        print("¡Ha dado un paso al frente!")
    elif num < 0:
        print("¡El pirata se ha quedado dormido!")
        break
    elif num%2!=0 and (num-1)%4==0:
        izqdcha = izqdcha + 1
        print("¡Ha dado un paso a la derecha!")
        if izqdcha > 5 :
            print("¡El pirata cayó por el costado derecho de la tabla y se ahogó!")
            break
    else:
        izqdcha = izqdcha - 1
        print("¡Ha dado un paso a la izquierda!")
        if izqdcha < 0:
            print("¡El pirata cayó por el costado izquierdo de la tabla y se ahogó!")
            break

if largo == 15:
    print("¡El pirata llegó sano y salvo al barco")
