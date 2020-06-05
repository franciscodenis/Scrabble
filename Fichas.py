def crear_bolsa_de_fichas ():
    bolsa_de_fichas = []

    for i in range(11):
        bolsa_de_fichas.append("A")
        bolsa_de_fichas.append("E")

    for i in range(8):
        bolsa_de_fichas.append("O")

    for i in range(7):
        bolsa_de_fichas.append("S")

    for i in range(6):
        bolsa_de_fichas.append("I")
        bolsa_de_fichas.append("U")

    for i in range(5):
        bolsa_de_fichas.append("N")

    for i in range(4):
        bolsa_de_fichas.append("L")
        bolsa_de_fichas.append("R")
        bolsa_de_fichas.append("T")
        bolsa_de_fichas.append("C")
        bolsa_de_fichas.append("D")

    for i in range(3):
        bolsa_de_fichas.append("M")
        bolsa_de_fichas.append("B")

    for i in range(2):
        bolsa_de_fichas.append("G")
        bolsa_de_fichas.append("P")
        bolsa_de_fichas.append("V")
        bolsa_de_fichas.append("F")
        bolsa_de_fichas.append("H")
        bolsa_de_fichas.append("V")

    bolsa_de_fichas.append("Y")
    bolsa_de_fichas.append("Ñ")
    bolsa_de_fichas.append("Q")
    bolsa_de_fichas.append("W")
    bolsa_de_fichas.append("X")
    bolsa_de_fichas.append("Z")

    return bolsa_de_fichas

def crear_diccionario_de_puntos():

    diccionario_de_puntos = dict()

    for letra in ["A", "E", "O", "S", "I", "U", 'N', 'L', 'R', 'T']:
        diccionario_de_puntos[letra] = 1

    for letra in ['C', 'D', 'G']:
        diccionario_de_puntos[letra] = 2

    for letra in ['M', 'B', 'P']:
        diccionario_de_puntos[letra] = 3

    for letra in ['F', 'H', 'V', 'Y']:
        diccionario_de_puntos[letra] = 4

    for letra in ['K',  'Ñ', 'Q', 'W', 'X']:
        diccionario_de_puntos[letra] = 6

    diccionario_de_puntos["Z"] = 10

    return diccionario_de_puntos

def crear_diccionario():
    lista_diccionario = []
    with open('diccionarios/diccionario.txt', 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            lista_diccionario.append(line)
    return lista_diccionario


#Checkeando como hacer cambios en git
