import Casilla
import Fichas
import PySimpleGUI as sg
from pattern.es import *
from pattern.web import Wiktionary


class Tablero:

    def __init__(self, filas=15, columnas=15):

        self.set_filas(filas)
        self.set_columnas(columnas)
        self.set_coorUsadas()
        self.set_coordenadasActivas()
        self.set_matriz([[Casilla.Casilla() for x in range(columnas)] for y in range(filas)])
        for i in range(filas):
            for j in range(columnas):
                self.get_matriz()[i][j] = Casilla.Casilla(i,j)


#------------------------------Comienzo getters y setters-----------------------

    def set_filas(self, filas):
        self.__filas= filas

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

    def set_coorUsadas(self, listCoorUsadas=[]):
        self.__coorUsadas = listCoorUsadas

    def get_coorUsadas(self):
        return self.__coorUsadas

    def set_coordenadasActivas(self, coorAct=[]):
        self.__coordenadas_activas = coorAct

    def get_coordenadasActivas(self):
        return self.__coordenadas_activas

#---------------------comienzo otros metodos-----------------------------------

    def imprimir(self):
        ''' imprime el tablero'''
        for i in range(self.get_filas()):
            for j in range(self.get_columnas()):
                print(self.get_matriz()[i][j])

    def listado_botones(self):
        listado =[]
        for i in range(self.get_filas()):
            for j in range(self.get_columnas()):
                listado.append(self.get_matriz()[i][j].get_id())
        return listado

    def click(self, atril, coordenadas, ventana):
            if atril.get_casilla_seleccionada() is not None:
                if self.get_matriz()[coordenadas[0]][coordenadas[1]].get_habilitado() and not self.get_matriz()[coordenadas[0]][coordenadas[1]].get_definitivo():
                    self.actualizar_letra_tablero(atril, coordenadas)
                    atril.get_casilla_seleccionada().set_letra(' ')
                    atril.get_casilla_seleccionada().set_tiene_letra(False)
                    ventana.Element(atril.get_casilla_seleccionada().get_id()).Update(' ')
                    atril.set_casilla_seleccionada(None)
                    ventana.Element(coordenadas).Update(self.get_matriz()[coordenadas[0]][coordenadas[1]].get_letra(), button_color=('white', '#C8C652'))

    def actualizar_letra_tablero(self, atril, coordenadas):
        self.get_matriz()[coordenadas[0]][coordenadas[1]].set_letra(atril.get_casilla_seleccionada().get_letra())
        self.get_matriz()[coordenadas[0]][coordenadas[1]].set_activo(True)
        self.bloquear_tablero()

    def enlistar_coordenadas_activas(self):
        coordenadas_activas = []
        for i in range(self.get_filas()):
            for j in range(self.get_columnas()):
                self.get_matriz()[i][j].set_habilitado(False)
                if self.get_matriz()[i][j].get_activo():
                    coordenadas_activas.append(self.get_matriz()[i][j].get_id())
        return coordenadas_activas

    def bloquear_tablero(self):
        coordenadas_activas = self.enlistar_coordenadas_activas()
        adyacente_arriba = (0, -1)
        adyacente_abajo = (0, +1)
        adyacente_izquierda = (-1, 0)
        adyacente_derecha = (+1, 0)

        adyacentes_todas = (adyacente_arriba, adyacente_abajo, adyacente_izquierda, adyacente_derecha)

        if len(coordenadas_activas) == 1:
            for i in adyacentes_todas:
                try:
                    fila_a_desbloquear = coordenadas_activas[0][0]+i[1]
                    columna_a_desbloquear =coordenadas_activas[0][1]+i[0]
                    if fila_a_desbloquear >= 0 and columna_a_desbloquear >= 0:
                        self.get_matriz()[fila_a_desbloquear][columna_a_desbloquear].set_habilitado(True)
                except IndexError:
                    print("Casilla a desbloquear fuera de rango, se ignora")  # Borrar
                    pass

        if len(coordenadas_activas) > 1:
            coordenada_max = max(coordenadas_activas)
            coordenada_min = min(coordenadas_activas)
            horizontal = False
            if coordenada_max[0] != coordenada_min[0]:
                horizontal = True
            if horizontal:
                coordenada_adyacente_izquierda = (coordenada_min[0]-1, coordenada_min[1])
                coordenada_adyacente_derecha = (coordenada_max[0]+1, coordenada_max[1])
                coordenadas_a_desbloquear = [coordenada_adyacente_izquierda, coordenada_adyacente_derecha]
            else:
                coordenada_adyacente_arriba = (coordenada_min[0], coordenada_min[1]-1)
                coordenada_adyacente_abajo = (coordenada_max[0], coordenada_max[1]+1)
                coordenadas_a_desbloquear = [coordenada_adyacente_arriba, coordenada_adyacente_abajo]

            for i in coordenadas_a_desbloquear:
                try:
                    self.get_matriz()[i[0]][i[1]].set_habilitado(True)
                except IndexError:
                    print("Casilla a desbloquear fuera de rango, se ignora")  # borrar
                    pass

    def calcular_puntaje(self, lista):
        dic_puntos = Fichas.crear_diccionario_de_puntos()
        total = 0
        for coor in lista:
            if self.get_matriz()[coor[0]][coor[1]].get_letra() in dic_puntos.keys():
                total = total + dic_puntos[self.get_matriz()[coor[0]][coor[1]].get_letra()]
        return total

    def desactivar_coordenadas_activas(self, lista_coordenadas_activas):
        for coor in lista_coordenadas_activas:
            self.get_matriz()[coor[0]][coor[1]].set_activo(False)

    def set_palabra_definitiva(self, lista_coors): #ver si se usa
        for coor in lista_coors:
            #eliminar_letra(lista_letras) hay que hacerlo!!
            self.get_matriz()[coor[0]][coor[1]].set_definitivo(True)

    def validar_pal(self):
        lista_coordenadas_activas = self.enlistar_coordenadas_activas()
        puntaje = self.calcular_puntaje(lista_coordenadas_activas)
        w = Wiktionary(language="es")
        palabra_separada = []
        for coor in lista_coordenadas_activas:
            palabra_separada.append(self.get_matriz()[coor[0]][coor[1]].get_letra())
        palabra = ''.join(palabra_separada)
        analisis = parse(palabra.lower()).split('/')
        if analisis[1] == "JJ" or analisis[1] == "VB":
            self.set_palabra_definitiva(lista_coordenadas_activas)           # la palabra es definitiva
            return (True, puntaje)
        elif (analisis[1] == "NN"):
            article=w.search(palabra.lower())
            if article is not None:
                self.set_palabra_definitiva(lista_coordenadas_activas)
                # la palabra es definitiva
                self.desactivar_coordenadas_activas(lista_coordenadas_activas)
                return (True, puntaje)
            else:

                return (False, 0)
        else:
            return (False, 0)

    def desbloquear_tablero(self):
        '''desbloquea el tablero menos los botones activos'''  #ver botones definitivos
        for i in range(self.get_filas()):
            for j in range(self.get_columnas()):
                if self.get_matriz()[i][j].get_activo():
                    self.get_matriz()[i][j].set_definitivo(True)
                self.get_matriz()[i][j].set_activo(False)
                self.get_matriz()[i][j].set_habilitado(True)

    def validar_palabra(self, palabra, diccionario, palabras_permitidas):
        palabra_valida = False
        print(palabra in diccionario)
        if palabra in diccionario:
            if parse(palabra).split('/')[1] in palabras_permitidas:
                palabra_valida = True
        return palabra_valida

    def click_validar(self, atril, tablero, window, diccionario, puntaje, bolsa,palabras_permitidas=('NN', 'JJ', 'VB')):
        coordenadas_activas = tablero.enlistar_coordenadas_activas()
        palabra_en_lista = []
        for coordenada in coordenadas_activas:
            palabra_en_lista.append(self.get_matriz()[coordenada[0]][coordenada[1]].get_letra())

        palabra = ''.join(palabra_en_lista).lower()

        palabra_valida = self.validar_palabra(palabra, diccionario, palabras_permitidas)
        print(palabra_valida)
        if palabra_valida:
            puntaje = puntaje + self.calcular_puntaje(coordenadas_activas)
            atril.agregar_letras(bolsa)
            atril.refrescar_atril(window)
            tablero.desbloquear_tablero()
            window.Element('punt').Update(puntaje)
            return puntaje
        else:
            atril.devolver_fallo(window, tablero)
            tablero.desbloquear_tablero()
            return puntaje






#______________________________________________________agregado nuevo


    def modificar_premios(self,lista, tipo,clave, color):
        for valor in lista:
            try:
                self.get_matriz()[valor[0]][valor[1]].set_premio(tipo) # si es palabra x2, letrax2, letrax3
                self.get_matriz()[valor[0]][valor[1]].set_color(color)
            except :
                continue #por si me equivoque agregando tuplas

    def devolver_lista(self,lista):
        #for tupla in lista:
        #    try:
        #        lista.append(tupla[1],tupla[0])
        #    except:
        #        continue
        #print(lista)            #me volo la cabeza, no funciona
        return lista

    def modificaciones_principiante(self):
        self.set_columnas(15)
        self.set_filas(15)
        lista_3p=[(1,1),(1,4),(1,3),(1,12),(1,15),(2,2),(2,14)]# me equivoque, empece desde 1 en vez de 0, despues lo modifico
        lista_3p= self.devolver_lista(lista_3p)  # la idea era hacer un espejo pero no me estaría funcionando el devolver lista
        self.modificar_premios(lista_3p,'3P','3P','#33FF71') #verde
        lista_2p=[(2,5),(2,11),(3,3),(3,6),(3,10),(3,13),(4,4),(4,12,)]
        lista_2p= self.devolver_lista(lista_2p)
        self.modificar_premios(lista_2p,'2P','2P','#FFC133') #naranja
        lista_3L=[(4,7),(4,9),(5,5),(5,11),(6,6),(6,10),(7,8),(8,7),(8,9)]
        lista_3L=self.devolver_lista(lista_3L)
        self.modificar_premios(lista_3L,'3L','3L','#334CFF') #azul
        lista_2L=[(5,8),(7,7),(7,9)]
        lista_2L= self.devolver_lista(lista_2L)
        self.modificar_premios(lista_2L,'2L','2L','#33D4FF')#celeste
        
   # def modificaciones_principiante(self):
       # self.set_columnas(15)
       # self.set_filas(15)
       # lista_3p = []
       # lista_2p = []
       # lista_3l = []
       # lista_2l = []
       # for i in range(0, 15, 2):
       #     tupla = (i, i)
       #     tupla2 = (((self.get_columnas()-1)-i), ((self.get_filas()-1)-i))
       #     lista_3p.append(tupla)
       #     lista_3p.append(tupla2)
       # self.modificar_premios(lista_3p,'3P','3P','#33FF71') #verde
       # for i in range(1, 14, 2):
       #     if (i == 7):
       #         continue
       #     tupla = (i, i)
       #     tupla2 = (((self.get_columnas()-1)-i), ((self.get_filas()-1)-i))
       #     lista_2l.append(tupla)
       #     lista_2l.append(tupla2)
       # self.modificar_premios(lista_2l,'2L','2L','#33D4FF') #naranja
       # for i in range(0, 15, 2):
       #     tupla = ((i, (self.get_columnas()-1)-i))
       #     tupla2 = (((self.get_filas()-1)-i), i)
       #     lista_3l.append(tupla)
       #     lista_3l.append(tupla2)
       # self.modificar_premios(lista_3l,'3L','3L','#334CFF') #azul
       # for i in range(1, 14, 2):
       #     if (i == 7):
       #         continue
       #     tupla = ((i, (self.get_columnas()-1)-i))
       #     tupla2 = (((self.get_filas()-1)-i), i)
       #     lista_2p.append(tupla)
       #     lista_2p.append(tupla2)
       # self.modificar_premios(lista_2p,'2P','2P','#FFC133')#celeste    

    def modificaciones_intermedio(self):

        #COMPLETAR
        pass

    def modificaciones_experto(self):

        #COMPLETAR agus

        pass
    def modificaciones_usuario(self):
        #terminarrrrr

        pass
    def crear_tablero(self, nivel='principiante'):

        if nivel== 'principiante':
            self.modificaciones_principiante()
        elif nivel== 'intermedio':
            self.modificaciones_intermedio()
        elif nivel=="experto":
            self.modificaciones_experto()
        else:
            self.modificaciones_usuario()
        for x in range( self.get_filas()):
            for y in range(self.get_columnas()):
                try:
                    self.get_matriz()[x][y].set_color ('white', '#C8C652')
                    self.get_matriz()[x][y].set_premio(' ')
                except:
                    continue
        filas= self.get_filas()
        columnas= self.get_columnas()
        letter_tablero = { 'size' : (2,1), 'pad' : (0,0)} # ACA PODEMOS MODIFICAR EL TAMAN
        layout = [[sg.Button(key = (i, j),button_text= self.get_matriz()[i][j].get_premio(),button_color=('white',self.get_matriz()[i][j].get_color()),  **letter_tablero) for i in range(filas)] for j in range(columnas)]

        return layout









        pass
