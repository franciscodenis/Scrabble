from random import randint

def random_letter():
    return chr(randint(65, 90))

class Casilla:
    def __init__(self, fila=-1, columna =-1, multiplicador=1):
        self.ID = (fila, columna)
        self.activo = False # Indica si la casilla está en juego, completandose la palabra.
        self.habilitado = True # Indica si el espacio puede ser usado o no.
        self.definitivo = False # Evita la modificación de la casilla definitivamente
        self.letra = '' # Letra almacenada temporal o definitivamente en la casilla.
        self.multiplicador_de_puntos= multiplicador # Multiplica los puntos de la letra al ocupar la casilla.
        self.imagen_fondo = '' #String de la dirección de la imagen de fondo.

class Tablero:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = [[Casilla() for x in range(columnas)] for y in range(filas)]
        for i in range(filas):
            for j in range(columnas):
                self.matriz[i][j] = Casilla(i,j)

    def imprimir(self):
        for i in range(self.filas):
            for j in range(self.columnas):
                print(self.matriz[i][j])

    def listado_botones(self):
        listado =[]
        for i in range(self.filas):
            for j in range(self.columnas):
                listado.append(self.matriz[i][j].ID)
        return listado

    def click(self, atril, coordenadas):
    #    if atril.casilla_seleccionada.letra
        if self.matriz[coordenadas[0]][coordenadas[1]].habilitado == True:
            self.actualizar_letra_tablero(atril, coordenadas)

        update_tablero = self.matriz[coordenadas[0]][coordenadas[1]].letra
        update_atril = atril.casilla_seleccionada.letra
        return [update_tablero, update_atril]

    def actualizar_letra_tablero(self, atril, coordenadas):
        self.matriz[coordenadas[0]][coordenadas[1]].letra = atril.casilla_seleccionada.letra
        self.matriz[coordenadas[0]][coordenadas[1]].activo = True
        self.bloquear_tablero()
        atril.casilla_seleccionada.letra = ' '


    def bloquear_tablero(self):
        coordenadas_activas = []
        for i in range(self.filas):
            for j in range(self.columnas):
                self.matriz[i][j].habilitado = False
                if self.matriz[i][j].activo == True:
                    coordenadas_activas.append(self.matriz[i][j].ID)
        if len(coordenadas_activas) == 1:
            try:
                self.matriz[coordenadas_activas[0][0] + 1][coordenadas_activas[0][1] + 0 ].habilitado = True
                self.matriz[coordenadas_activas[0][0] - 1][coordenadas_activas[0][1] + 0].habilitado = True
                self.matriz[coordenadas_activas[0][0] + 0][coordenadas_activas[0][1] + 1].habilitado = True
                self.matriz[coordenadas_activas[0][0] + 0][coordenadas_activas[0][1] - 1].habilitado = True
            except IndexError:
                pass

        if (len(coordenadas_activas) > 1):
            coordenada_max = max(coordenadas_activas)
            coordenada_min = min(coordenadas_activas)
            print(coordenada_max)
            print(coordenada_min)
            horizontal = False
            if coordenada_max[0] == coordenada_min[0]:
                horizontal = True
            if horizontal:
                try:
                    self.matriz[coordenada_max[0] ][coordenada_max[1]+ 1].habilitado = True
                    self.matriz[coordenada_min[0] ][coordenada_max[1]- 1].habilitado = True
                except IndexError:
                    pass
            else:
                try:
                    self.matriz[coordenada_max[0]+1][coordenada_max[1]].habilitado = True
                    self.matriz[coordenada_min[0]-1][coordenada_max[1]].habilitado = True
                except IndexError:
                    pass

class Atril:
    casilla_seleccionada = Casilla()


    def __init__(self, columnas):
        self.columnas = columnas
        self.espacio_fichas = [Casilla() for x in range(columnas)]
        for i in range(columnas):
            self.espacio_fichas[i] = Casilla(-1, i)

    def agregar_letras(self):
        for i in self.espacio_fichas:
            i.letra = random_letter()

    def listado_botones(self):
        listado =[]
        for i in range(self.columnas):
            listado.append(self.espacio_fichas[i].ID)
        return listado

    def click(self, casilla, coordenadas):
        self.casilla_seleccionada = self.espacio_fichas[coordenadas[1]]
        refresh = self.casilla_seleccionada.letra
        return refresh





