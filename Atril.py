import Casilla as cas #podemos cambiarlo si queda feo hacer un from casilla import *
import random
from random import randint
import Fichas
import PySimpleGUI as sg

def random_letter(lista_letras ):
    lista_nueva= lista_letras.copy() # quiero asegurarme de no agarrar una letra que no exista en la bolsa pero todavia no la quiero borrar del todo
    while True:
        letra= chr(randint(65, 90))
        if letra in (lista_nueva):
            lista_nueva.remove(letra) #no hacer el remove definitivo aca, hacer en el metodo validar
            return letra

class Atril():


    def __init__(self, columnas):
        self.__casilla_seleccionada  = None
        self.set_columnas(columnas)
        self.set_espacio_fichas( [cas.Casilla() for x in range(columnas)])
        for i in range(columnas):
            self.get_espacio_fichas()[i] =(cas.Casilla(-1, i))  # ES CORRECTO?
        self.set_cambios_atril(3) # Cantidad de cambios está dada por la cantidad de fichas para cambiar en la bolsa
        self.set_esta_vacio(True)


    #----------- getters y setters-------------------------
    # cambios_atril
    def set_cambios_atril(self, cantidad):
        self.__cambios_atril= cantidad
    def get_cambios_atril(self):
        return self.__cambios_atril
    def decrement_cambios_atril(self):
        self.set_cambios_atril(self.get_cambios_atril()-1)

    #__espacio_fichas
    def set_espacio_fichas(self, arreglo):
        self.__espacio_fichas= arreglo
    def get_espacio_fichas(self):
        return self.__espacio_fichas

    #__casilla_seleccionada
    def set_casilla_seleccionada(self, casilla):
        self.__casilla_seleccionada = casilla
    def get_casilla_seleccionada(self):
        return self.__casilla_seleccionada

    #__columnas
    def set_columnas(self,columnas):
        self.__columnas= columnas
    def get_columnas(self):
        return self.__columnas

    #__esta_vacio
    def set_esta_vacio(self,validez):
        self.__esta_vacio= validez
    def esta_vacio(self):
        return self.__esta_vacio

#_____________________________________________Comienzo de  otros metodos ____________

    def agregar_letras(self, bolsa):
        for i in self.get_espacio_fichas():
            if not i.get_tiene_letra():
                i.set_letra(bolsa.pop(randint(0, len(bolsa)-1)))
                i.set_tiene_letra(True)



    def cambiar_letras(self, lista_letras,window,tablero,checkbox,bolsa):
        ''' cambio las letras del atril por nuevas letras'''
        for i in range(7):
            if self.get_espacio_fichas()[i].get_tiene_letra() and checkbox[('Checkbox', i)]:
                bolsa.append(self.get_espacio_fichas()[i].get_letra())
                self.get_espacio_fichas()[i].set_letra(bolsa.pop(randint(0, len(bolsa)-1)))
        self.refrescar_atril(window)


    def refrescar_atril(self, window):
        letras=(self.get_espacio_fichas())
        for i in range(len(letras)):
            window.Element((-1,i)).Update(text=letras[i].get_letra())


    def llenar_atril(self, lista_letras):

        for i in self.get_espacio_fichas():
            if i.get_letra()== "" or i.get_letra()==' ': # tengo que llenars
                i.set_letra(random_letter(lista_letras))

    def devolver_fallo(self, window, tablero): #no hace falta mandar la lista de coordenadas si te mandas el tablero -agus
        '''Este metodo devuelve las letras al atril'''
        letra_devolver = []
        letras = self.get_espacio_fichas()
        for coor in tablero.enlistar_coordenadas_activas(): #actualiza los botones usados en el tablero y se guarda las letras para devolver al atril
            if (tablero.get_matriz()[coor[0]][coor[1]].get_definitivo() == False): #ahora solo devuelve las letras que no son definitivas
                letra_devolver.append(tablero.get_matriz()[coor[0]][coor[1]].get_letra())
                tablero.get_matriz()[coor[0]][coor[1]].set_letra(' ')
                tablero.get_matriz()[coor[0]][coor[1]].set_activo(False)
                window.Element(coor).Update(tablero.get_matriz()[coor[0]][coor[1]].get_letra(), button_color=(('white', 'white')))
            # tablero.get_coorUsadas().remove(coor) #NO HACE FALTA PORQUE SE BORRAN CUANDO HACES EL SET.ACTIVO(FALSE)-agus
        for i in range(len(letras)):              #devuelve las letras al atril(falta pulir)... segun agus(yo) esta perfecto, solo faltaba desbloquear el tablero
            if letras[i].get_letra() == ' ':
                if (len(letra_devolver) > 0):
                    letras[i].set_letra(letra_devolver[0])
                    window.Element((-1, i)).Update(letras[i].get_letra())
                    letra_devolver.pop(0)
        tablero.desbloquear_tablero()


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
