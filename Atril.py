import Casilla as cas
import random
from random import randint
import Fichas
import PySimpleGUI as sg
import itertools
from pattern import *
from pattern.es import *

def random_letter(lista_letras ):
    lista_nueva= lista_letras.copy() # quiero asegurarme de no agarrar una letra que no exista en la bolsa pero todavia no la quiero borrar del todo
    while True:
        letra= chr(randint(65, 90))
        if letra in (lista_nueva):
            lista_nueva.remove(letra) #no hacer el remove definitivo aca, hacer en el metodo validar
            return letra

class Atril():


    def __init__(self, columnas, tipo_atril = 'Atril_jugador'):
        self.__casilla_seleccionada  = None
        self.set_columnas(columnas)
        self.set_espacio_fichas( [cas.Casilla() for x in range(columnas)])
        for i in range(columnas):
            self.get_espacio_fichas()[i] =(cas.Casilla(tipo_atril, i))  # ES CORRECTO?
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
        '''agrego letras al atril'''
        for i in self.get_espacio_fichas():
            if not i.get_tiene_letra():
                i.set_letra(bolsa.pop(randint(0, len(bolsa)-1)))
                i.set_tiene_letra(True)



    def cambiar_letras(self, lista_letras,window,tablero,checkbox,bolsa,juego):
        ''' cambio las letras del atril por nuevas letras'''
        #self.devolver_fallo(window,tablero) #devuelve las letras que estan en uso  al atril
        for i in range(7):
            if self.get_espacio_fichas()[i].get_tiene_letra() and checkbox[('Checkbox', i)]:
                bolsa.append(self.get_espacio_fichas()[i].get_letra())
                self.get_espacio_fichas()[i].set_letra(bolsa.pop(randint(0, len(bolsa)-1)))
        self.decrement_cambios_atril() #solo hay 3 cambios de atril, decremento en 1
        self.refrescar_atril(window)

        juego.cambiar_turno()


    def refrescar_atril(self, window, atril ='Atril_jugador'):
        '''actualizo el atril del jugador '''
        letras=(self.get_espacio_fichas())
        for i in range(len(letras)):
            window.Element((atril,i)).Update(text=letras[i].get_letra())


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
                window.Element(coor).Update(tablero.get_matriz()[coor[0]][coor[1]].get_premio(), button_color=(('white', tablero.get_matriz()[coor[0]][coor[1]].get_color())))
            # tablero.get_coorUsadas().remove(coor) #NO HACE FALTA PORQUE SE BORRAN CUANDO HACES EL SET.ACTIVO(FALSE)-agus
        for i in range(len(letras)):              #devuelve las letras al atril(falta pulir)... segun agus(yo) esta perfecto, solo faltaba desbloquear el tablero
            if letras[i].get_letra() == ' ':
                if (len(letra_devolver) > 0):
                    letras[i].set_letra(letra_devolver[0])
                    window.Element(('Atril_jugador', i)).Update(letras[i].get_letra())
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

class Atril_PC(Atril):
    def __init__(self, columnas, puntaje=0):
        super().__init__(columnas, 'Atril_PC')
        self._puntaje = 0
    def set_puntaje(self, puntaje):
        self._puntaje= puntaje
    def get_puntaje(self):
        return self._puntaje

    def formar_palabra(self, letras_desordenadas, lista_diccionario, palabras_permitidas= ('NN', 'JJ', 'VB' )):
        seguir = True
        intento = " "
        for i in range(3, len(letras_desordenadas)):
            conteo_let = random.randint(3, 7)
            lista_intentos = list(itertools.permutations(letras_desordenadas, conteo_let))
            for j in lista_intentos[:15]:
                intento = ''.join(j).lower()
                print(intento)
                if intento in lista_diccionario:
                    print("Esta en el diccionario")
                    if parse(intento).split('/')[1] in palabras_permitidas: #puede ser que no toma el parse??
                        print("está en parse")
                        seguir = False
                if not seguir:
                    break
            if not seguir: break
        if (seguir):
            intento = " "
        return intento

    def buscar_espacio(self, tablero, casillas_requeridas):
        for i in range(tablero.get_filas()):
            for j in range(tablero.get_columnas()):
                count = 0
                for k in range(casillas_requeridas):
                    if not tablero.get_matriz()[i][j].get_tiene_letra():
                        count = count + 1
                if count == casillas_requeridas:
                    return (i,j)
        return False

    def orden_coordenadas_atril(self, palabra_armada):
        lista_coordenadas_de_palabra_en_atril = []
        for i in palabra_armada:
            for j in range(len(self.get_espacio_fichas())):
                if self.get_espacio_fichas()[j].get_letra().lower() == i:
                    print("encontró la cordenada", i, self.get_espacio_fichas()[j].get_letra().lower() )
                    lista_coordenadas_de_palabra_en_atril.append(self.get_espacio_fichas()[j].get_id())
                    break
        return lista_coordenadas_de_palabra_en_atril

    def colocar_en_tablero(self,tablero,  lista_coordenadas, coordenada_inicial,ventana):
        coordenadas_tablero = []
        print("entra a colocar en tablero")
        print(lista_coordenadas)
        for i in range(len(lista_coordenadas)):
            letra_a_colocar = self.get_espacio_fichas()[lista_coordenadas[i][1]].get_letra()
            print(letra_a_colocar)
            print(self.get_espacio_fichas()[lista_coordenadas[i][1]].get_id())
            tablero.get_matriz()[coordenada_inicial[0]][coordenada_inicial[1] + i].set_letra(letra_a_colocar)
            tablero.get_matriz()[coordenada_inicial[0]][coordenada_inicial[1] + i].set_definitivo(True)
            tablero.get_matriz()[coordenada_inicial[0]][coordenada_inicial[1] + i].set_tiene_letra(True)
            coordenadas_tablero.append(tablero.get_matriz()[coordenada_inicial[0]][coordenada_inicial[1] + i].get_id())
            ventana.Element((coordenada_inicial[0],coordenada_inicial[1] + i) ).Update(letra_a_colocar, button_color=('white', '#C8C652'))

            self.get_espacio_fichas()[lista_coordenadas[i][1]].set_letra("")
            self.get_espacio_fichas()[lista_coordenadas[i][1]].set_tiene_letra(False)
        return coordenadas_tablero

    def calcular_puntajePC(self, puntajes_letras, botones, tablero):
        total = 0
        aumentos = []
        for pos in botones:
            if (tablero.get_matriz()[pos[0]][pos[1]].get_letra() in puntajes_letras):
                total = total + puntajes_letras[tablero.get_matriz()[pos[0]][pos[1]].get_letra()]
        for pos in botones:
            if (tablero.get_matriz()[pos[0]][pos[1]].get_premio() == "3P"):
                total = total * 3
            elif(tablero.get_matriz()[pos[0]][pos[1]].get_premio() == "3L"):
                total = total + 3
            elif(tablero.get_matriz()[pos[0]][pos[1]].get_premio() == "2P"):
                total = total * 2
            elif(tablero.get_matriz()[pos[0]][pos[1]].get_premio() == "2L"):
                total = total + 2
            elif(tablero.get_matriz()[pos[0]][pos[1]].get_premio() == "2R"):
                total = total - 2
        return total



    def jugar_turno(self,tablero, lista_diccionario,ventana,bolsa, puntajes_letras, palabras_permitidas = ('NN', 'JJ', 'VB' )):
        lista_letras = ""
        for boton in self.listado_botones():
            lista_letras = lista_letras + self.get_espacio_fichas()[boton[1]].get_letra()
        palabra_armada = self.formar_palabra( lista_letras, lista_diccionario, palabras_permitidas)
        if (palabra_armada != " "):
            coordenada_inicial = self.buscar_espacio(tablero, len(palabra_armada))
            print(palabra_armada)
            lista_coordenadas = self.orden_coordenadas_atril(palabra_armada)
            coordenadas_tablero = self.colocar_en_tablero(tablero, lista_coordenadas, coordenada_inicial,ventana)
            self.set_puntaje( self.get_puntaje() + self.calcular_puntajePC(puntajes_letras, coordenadas_tablero, tablero))
            ventana.Element('puntPC').Update(self.get_puntaje())
            self.agregar_letras(bolsa)
            self.refrescar_atril(ventana, 'Atril_PC')
        return False
