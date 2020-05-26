import Casilla as cas #podemos cambiarlo si queda feo hacer un from casilla import *
from random import randint
def random_letter():
    return chr(randint(65, 90))

class Atril:


    __casilla_seleccionada = cas.Casilla()

    #----------- getters y setters-------------------------
    def set_espacio_fichas(self, arreglo):
        self.__espacio_fichas= arreglo
    def get_espacio_fichas(self):
        return self.__espacio_fichas


    def set_casilla_seleccionada(self, casilla):
        self.__casilla_seleccionada = casilla
    def get_casilla_seleccionada(self):
        return self.__casilla_seleccionada
    def set_columnas(self,columnas):
        self.__columnas= columnas
    def get_columnas(self):
        return self.__columnas

    def __init__(self, columnas):
        self.set_columnas(columnas)
        self.set_espacio_fichas( [cas.Casilla() for x in range(columnas)])
        for i in range(columnas):
            self.get_espacio_fichas()[i] =(cas.Casilla(-1, i)) #ES CORRECTO?


    def agregar_letras(self):
        '''Agrega letras a un atril vacio'''
        for i in self.get_espacio_fichas():
            i.set_letra( random_letter())

    def listado_botones(self):
        ''' retorna una lista con las teclas del atril'''
        listado =[]
        for i in range(self.get_columnas()):
            listado.append(self.get_espacio_fichas()[i].get_id())
        return listado

    def click(self, casilla, coordenadas):

        self.set_casilla_seleccionada(self.get_espacio_fichas()[coordenadas[1]])
        refresh = self.get_casilla_seleccionada().get_letra()
        return refresh
