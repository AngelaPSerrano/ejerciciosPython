def arabeARomano (stringArabes):
    suma = ""
    stringArabes = list(stringArabes)
    stringFinal = []
    if len(stringArabes) > 4:
        print("El número no puede ser mayor a 4000")
    else:
        if len(stringArabes)== 4:
            stringFinal = transformarMillares(stringArabes[0]),transformarCentenas(stringArabes[1]), transformarDecenas(stringArabes[2]), transformarUnidades(stringArabes[3])
        elif len(stringArabes)== 3:
            stringFinal = transformarCentenas(stringArabes[0]),transformarDecenas(stringArabes[1]), transformarUnidades(stringArabes[2])
        elif len(stringArabes)== 2:
            stringFinal = transformarDecenas(stringArabes[0]), transformarUnidades(stringArabes[1])
        else:
            stringFinal = transformarUnidades(stringArabes[0])
    resultado = "".join(stringFinal)
    print(resultado)

def transformarUnidades(num):
    num = int(num)
    if num == 1:
        return "I"
    elif num == 2:
        return "II"
    elif num == 3:
        return "III"
    elif num == 4:
        return "IV"
    elif num == 5:
        return "V"
    elif num == 6:
        return "VI"
    elif num == 7:
        return "VII"
    elif num == 8:
        return "VIII"
    elif num == 9:
        return "IX"
    else:
        return ""
    
def transformarDecenas(num):
    num = int(num)
    if num == 1:
        return "X"
    elif num == 2:
        return "XX"
    elif num == 3:
        return "XXX"
    elif num == 4:
        return "XL"
    elif num == 5:
        return "L"
    elif num == 6:
        return "LX"
    elif num == 7:
        return "LXX"
    elif num == 8:
        return "LXXX"
    elif num == 9:
        return "XC"
    else:
        return ""

def transformarCentenas(num):
    num = int(num)
    if num == 1:
        return "C"
    elif num == 2:
        return "CC"
    elif num == 3:
        return "CCC"
    elif num == 4:
        return "CD"
    elif num == 5:
        return "D"
    elif num == 6:
        return "DC"
    elif num == 7:
        return "DCC"
    elif num == 8:
        return "DCCC"
    elif num == 9:
        return "CM"
    else:
        return ""
    
def transformarMillares(num):
    num = int(num)
    if num == 1:
        return "M"
    elif num == 2:
        return "MM"
    elif num == 3:
        return "MMM"

def romanoAArabe(stringRomanos):
    suma = 0
    stringRomanos = list(stringRomanos)
    
    i = 0
    while i <= len(stringRomanos)-1:
        if stringRomanos[i] == "I":
            if len(stringRomanos)-1 != i:
                if stringRomanos[i+1] == "V":
                    suma = suma + 4
                    i = i + 1
                elif stringRomanos[i+1] == "X":
                    suma = suma +9
                    i = i + 1
                else:
                    suma = suma + 1
            else:
                suma = suma + 1
                
        elif stringRomanos[i] == "V":
            suma = suma + 5
           
        elif stringRomanos[i] == "X":
            if len(stringRomanos)-1 != i:
                if stringRomanos[i+1] == "L":
                    suma = suma + 40
                    i = i + 1
                elif stringRomanos[i+1] == "C":
                    suma = suma + 90
                    i = i + 1
                else:
                    suma = suma + 10
            else:
                suma = suma + 10
               
        elif stringRomanos[i] == "L":
            suma = suma + 50
        elif stringRomanos[i] == "C":
            if len(stringRomanos)-1 != i:
                if stringRomanos[i+1] == "D":
                    suma = suma + 400
                    i = i + 1
                elif stringRomanos[i] == "M":
                    suma = suma + 900
                    i = i + 1
                else:
                    suma = suma + 100
            else:
                suma = suma + 100
    
        elif stringRomanos[i] == "D":
            suma = suma + 500

        elif stringRomanos[i] == "M" :
            suma = suma + 1000
        i = i +1
            
    print("Resultado: ", suma)

#fin de defs

eleccion = int(input("Introduzca 1 para convertir de números árabes a romanos\n"
                     "Introduzca 2 para convertir de números romanos a árabes\n"))

if eleccion == 1 or eleccion == 2:
    num = input("Introduzca el valor a convertir \n")
    if eleccion == 1:
        arabeARomano(num)
    elif eleccion == 2:
        romanoAArabe(num)
  
