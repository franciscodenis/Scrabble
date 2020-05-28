import Casilla as cas #podemos cambiarlo si queda feo hacer un from casilla import *
import random
from random import randint
import Fichas
import PySimpleGUI as sg

def random_letter(lista_letras ):
    lista_nueva= lista_letras.copy() # quiero asegurarme de no agarrar una letra que no exista en la bolsa pero todavia no la quiero borrar del todo
    while True:
        letra= chr(randint(65, 90))
        if letra in (lista_letras):
            lista_nueva.remove(letra) #no hacer el remove definitivo aca, hacer en el metodo validar
            return letra

class Atril:


    __casilla_seleccionada = cas.Casilla()

    #----------- getters y setters-------------------------
    def set_cambios_atril(self, cantidad):
        self.__cambios_atril= cantidad
    def get_cambios_atril(self):
        return self.__cambios_atril
    def decrement_cambios_atril(self):
        self.set_cambios_atril(self.get_cambios_atril()-1)

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
        self.set_cambios_atril(3)

    def agregar_letras(self,lista_letras):
        '''Agrega letras a un atril vacio, o hace cambio de letras '''
        for i in self.get_espacio_fichas():
            i.set_letra( random_letter(lista_letras))
        self.decrement_cambios_atril()

    def refrescar_atril(self, window):
        letras=(self.get_espacio_fichas())
        for i in range(len(letras)):
            window[(-1,i)].update(text=letras[i].get_letra())


    def llenar_atril(self, lista_letras):
        for i in self.get_espacio_fichas():
            if i.get_letra()== "" or i.get_letra()==' ': # tengo que llenar
                i.set_letra(random_letter.get_espacio_fichas())




    #DEJAR PARA COMPARAR
    #def agregar_letras(self):
    #    '''Agrega letras a un atril vacio'''
    #    list_letras = Fichas.crear_bolsa_de_fichas() #lo modifique porque quiero que sirva para cuando  no hay  letras y para cuando quiero renovarlas

    #    for i in self.get_espacio_fichas():
    #        letra = random.choice(list_letras)
    #        if (letra.upper() in list_letras):
    #            i.set_letra(letra)
    #            list_letras.pop(list_letras.index(letra))
    #        else:
    #            letra = random.choice(list_letras)
    #            i.set_letra(letra)
    #    print(len(list_letras))

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
