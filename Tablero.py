
import Casilla
class Tablero:

        #gettersYsetters
    def set_filas(self, filas):
        self.__filas=filas
    def get_filas(self):
        return self.__filas
    def set_columnas(self, columnas):
        self.__columnas= columnas
    def get_columnas(self):
        return self.__columnas
    def set_matriz(self, matriz):
        self.__matriz= matriz
    def get_matriz(self):
        return self.__matriz
    #def set_matriz_pos(self,fila, columna,dato):
    #    self.__matriz[fila, columna]=dato
    #def get_matriz_pos(self,fila, columna):
        #return self.__matriz #iterable matriz


    def __init__(self, filas, columnas):
        self.set_filas(filas)
        self.set_columnas(columnas)
        self.set_matriz( [[Casilla.Casilla() for x in range(columnas)] for y in range(filas)])
        for i in range(filas):
            for j in range(columnas):
                self.get_matriz()[i][j] = Casilla.Casilla(i,j)

    def imprimir(self):
        ''' imprime el tablero'''
        for i in range(self.get_filas()):
            for j in range(self.get_columnas()):
                print(self.get_matriz()[i][j])

    def listado_botones(self):
        '''   '''
        listado =[]
        for i in range(self.get_filas()):
            for j in range(self.get_columnas()):
                listado.append(self.get_matriz()[i][j].get_id())
        return listado

    def click(self, atril, coordenadas):
    #    if atril.casilla_seleccionada.letra
        if((self.get_matriz()[coordenadas[0]][coordenadas[1]].get_habilitado())==True):
            self.actualizar_letra_tablero(atril, coordenadas)
        update_tablero = self.get_matriz()[coordenadas[0]][coordenadas[1]].get_letra()
        update_atril = atril.get_casilla_seleccionada().get_letra()
        return [update_tablero, update_atril]

    def actualizar_letra_tablero(self, atril, coordenadas):
        self.get_matriz()[coordenadas[0]][coordenadas[1]].set_letra(atril.get_casilla_seleccionada().get_letra())
        self.get_matriz()[coordenadas[0]][coordenadas[1]].set_activo(True)
        self.bloquear_tablero()
        atril.get_casilla_seleccionada().set_letra (' ')


    def bloquear_tablero(self):
        coordenadas_activas = []
        for i in range(self.get_filas()):
            for j in range(self.get_columnas()):
                self.get_matriz()[i][j].set_habilitado( False)
                if self.get_matriz()[i][j].get_activo() == True:
                    coordenadas_activas.append(self.get_matriz()[i][j].get_id())
        if len(coordenadas_activas) == 1:
            try:
                self.get_matriz()[coordenadas_activas[0][0] + 1][coordenadas_activas[0][1] + 0 ].set_habilitado(True)
                self.get_matriz()[coordenadas_activas[0][0] - 1][coordenadas_activas[0][1] + 0].set_habilitado(True)
                self.get_matriz()[coordenadas_activas[0][0] + 0][coordenadas_activas[0][1] + 1].set_habilitado(True)
                self.get_matriz()[coordenadas_activas[0][0] + 0][coordenadas_activas[0][1] - 1].set_habilitado(True)
            except IndexError:
                print("HUBO UN ERROR DE INDEXACION") #Borrar
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
                    self.get_matriz()[coordenada_max[0] ][coordenada_max[1]+ 1].set_habilitado( True)
                    self.get_matriz()[coordenada_min[0] ][coordenada_max[1]- 1].set_habilitado(True)
                except IndexError:
                    print("ERROR?")#borrar
                    pass
            else:
                try:
                    self.get_matriz()[coordenada_max[0]+1][coordenada_max[1]].set_habilitado( True)
                    self.get_matriz()[coordenada_min[0]-1][coordenada_max[1]].set_habilitado( True)
                except IndexError:
                    print('errror')#borrar
                    pass
