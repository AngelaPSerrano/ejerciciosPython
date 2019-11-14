def abrir(direccion):
    return open(direccion, "r")

def encontrarPalabra(direccion, palabra):
    f = abrir(direccion)
    texto = f.read()

    letrasPalabra = list(palabra)
    letrasTexto = list(texto.lower())
    puntero = 0
    contador = 0
    encontrada = False

    for i in range(len(letrasTexto)):
        if letrasTexto[i] == letrasPalabra[puntero]:
            contador = contador +1
            puntero = puntero+1
        if contador == len(letrasPalabra):
            encontrada = True
            charSalida = i+1
            break
    if encontrada:
        print("¡Palabra encontrada! Hemos terminado en el caracter ", charSalida, " del documento.")
    else:
        print("¡Palabra no encontrada!")

    f.close()

direccion = input("Indique el nombre del documento: ")
palabra = input("Indique la palabra a encontrar: ")
encontrarPalabra(direccion, palabra)
