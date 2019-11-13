num = 1
contador =0

while contador < 4:
    num = num + 1
    divisor = 1
    sumaDivisores = 0

    while divisor < num:
        if num % divisor == 0:
            sumaDivisores = sumaDivisores + divisor
        divisor = divisor + 1

    if sumaDivisores == num:
        print(num)
        contador = contador+1   
