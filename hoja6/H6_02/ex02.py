
def abrirFichero(documento):
    return open(documento, "r")

def datosPorLinea(documento):
    f = abrirFichero(documento)

    listaLineas = f.readlines()
    for i in range (len(listaLineas)):
        suma = 0
        palabrasLinea = listaLineas[i].split(" ")
        print("Línea ", (i+1), ":")
        print("Número de caracteres: ", len(listaLineas[i]))
        print("Número de palabras: ", len(palabrasLinea))
        for j in range (len(palabrasLinea)):
            suma = suma + len(palabrasLinea[j])
        print("El tamaño medio por palabra es: ",int(suma/len(palabrasLinea)))
        #sacar ultima letra y comprobar si más palabras así
        primeraPalabra = list(palabrasLinea[0])
        ultimaLetra = primeraPalabra[len(primeraPalabra)-1]
        cuentaLetras = 0
        for j in range(1, len(palabrasLinea)):
            palabra = list(palabrasLinea[j])
            if palabra[len(palabra)-1] == ultimaLetra:
                cuentaLetras = cuentaLetras +1
        print("Ultima letra de la primera palabra es '", ultimaLetra, "' y hay ", cuentaLetras, "que terminan igual.\n")

    f.close()

def datosPorArchivo(documento):
    f = abrirFichero(documento)
    
    textoArchivo = f.read()
    print(f.read())
    print("En el archivo completo: ")
    suma = 0
    palabrasArchivo = textoArchivo.split()
    lineasArchivo = textoArchivo.split("\n")
    
    caracteresArchivo = 0
    for i in range(len(palabrasArchivo)):
        caracteresArchivo = caracteresArchivo + len(list(palabrasArchivo[i]))
    print("Número de caracteres: ", caracteresArchivo)
    print("Número de palabras: ", len(palabrasArchivo))
    print("Número de lineas: ", len(lineasArchivo))
    
    for i in range(len(palabrasArchivo)):
            suma = suma + len(palabrasArchivo[i])
    print("El tamaño medio por palabra es: ",int(suma/len(palabrasArchivo)))

    lineaMasLarga = 0

    numeroPalabrasCoinciden = 0
    lineaCoinciden = 0
    for i in range(len(lineasArchivo)):
        palabrasLinea = lineasArchivo[i].split()
        if lineaMasLarga < len(palabrasLinea):
                lineaMasLarga = i
                
        # aprovechamos el bucle        
        primeraPalabra = list(palabrasLinea[0])
        ultimaLetra = primeraPalabra[len(primeraPalabra)-1]
        cuentaLetras = 0
        
        for j in range(len(palabrasLinea)):
            palabra = palabrasLinea[j]
            if palabra[len(palabra)-1] == ultimaLetra:
                cuentaLetras = cuentaLetras + 1

        if cuentaLetras >= numeroPalabrasCoinciden:
            lineaCoinciden = i+1
            numeroPalabrasCoinciden = cuentaLetras
                
    palabrasEnMasLarga = lineasArchivo[lineaMasLarga].split()
    print("La línea con más palabras es la línea ", lineaMasLarga+1, " que contiene ", len(palabrasEnMasLarga) , " palabras.")
    print("La línea con más palabras que terminan igual es la ", lineaCoinciden, " con ", numeroPalabrasCoinciden, " palabras que terminan igual.")
    
    f.close()

documento = input("¿Que archivo desea inspeccionar? ")

datosPorLinea(documento)
datosPorArchivo(documento)

