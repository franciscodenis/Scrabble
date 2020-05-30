from pattern.es import *
from pattern.web import Wiktionary
import Casilla
import Fichas
import PySimpleGUI as sg
class Tablero:

    def __init__(self, filas=15, columnas=15):
        coordenadas = []
        coordenadas_activas = []
        self.set_filas(filas)
        self.set_columnas(columnas)
        self.set_coorUsadas()
        self.set_coordenadasActivas()
        self.set_matriz( [[Casilla.Casilla() for x in range(columnas)] for y in range(filas)])
        for i in range(filas):
            for j in range(columnas):
                self.get_matriz()[i][j] = Casilla.Casilla(i,j)


#------------------------------Comienzo getters y setters-----------------------
    def crearTablero(self ):
        pass




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
        for i in range(self.get_filas()):
            for j in range(self.get_columnas()):
                self.get_matriz()[i][j].set_habilitado(False)
                if self.get_matriz()[i][j].get_activo() == True:
                    if self.get_matriz()[i][j].get_id() not in self.get_coorUsadas(): #agrega solamente si no estan en esta lista para que no haya coordenadas repetidas
                        self.get_coordenadasActivas().append(self.get_matriz()[i][j].get_id())
                        self.get_coorUsadas().append(self.get_matriz()[i][j].get_id())

        if len(self.get_coordenadasActivas()) == 1:
            try:
                self.get_matriz()[self.get_coordenadasActivas()[0][0] + 1][self.get_coordenadasActivas()[0][1] + 0 ].set_habilitado(True)

            except IndexError:
                print("HUBO UN ERROR DE INDEXACION") #Borrar
                pass
            try:
                self.get_matriz()[self.get_coordenadasActivas()[0][0] + 0][self.get_coordenadasActivas()[0][1] + 1].set_habilitado(True)
            except IndexError:
                print("HUBO UN ERROR DE INDEXACION") #Borrar
                pass
        if (len(self.get_coordenadasActivas()) > 1):
            coordenada_max = max(self.get_coordenadasActivas())
            coordenada_min = min(self.get_coordenadasActivas())
            print(coordenada_max)
            print(coordenada_min)
            horizontal = False
            if coordenada_max[0] == coordenada_min[0]:
                horizontal = True
            if horizontal:
                try:
                    self.get_matriz()[coordenada_max[0] ][coordenada_max[1]+ 1].set_habilitado(True)
                except IndexError:
                    print("ERROR?")#borrar
                    pass
            else:
                try:
                    self.get_matriz()[coordenada_max[0]+1][coordenada_max[1]].set_habilitado(True)
                except IndexError:
                    pass

    def calcular_puntaje(self, lista):
        dic_puntos = Fichas.crear_diccionario_de_puntos()
        total = 0
        for coor in lista:
            if self.get_matriz()[coor[0]][coor[1]].get_letra() in dic_puntos.keys():
                total = total + dic_puntos[self.get_matriz()[coor[0]][coor[1]].get_letra()]
        return total
    def set_palabra_definitiva(self, lista_coors): #ver si se usa
        for coor in lista_coors:
            #eliminar_letra(lista_letras) hay que hacerlo!!
            self.get_matriz()[coor[0]][coor[1]].set_definitivo(True)

    def validar_pal(self, lista_coors):
        puntaje = self.calcular_puntaje(lista_coors)
        w = Wiktionary(language="es")
        palabra_separada = []
        for coor in lista_coors:
            palabra_separada.append(self.get_matriz()[coor[0]][coor[1]].get_letra())
        palabra = ''.join(palabra_separada)
        analisis = parse(palabra.lower()).split('/')
        if analisis[1] == "JJ" or analisis[1] == "VB":
            self.set_palabra_definitiva(lista_coors)           # la palabra es definitiva
            return (True, puntaje)
        elif (analisis[1] == "NN"):
            article=w.search(palabra.lower())
            if (article != None):
                self.set_palabra_definitiva(lista_coors)       # la palabra es definitiva
                return (True, puntaje)
            else:

                return (False, 0)
        else:
            return (False, 0)

    def desbloquear_tablero(self):
        '''desbloquea el tablero menos los botones activos'''  #ver botones definitivos
        for i in range(self.get_filas()):
            for j in range(self.get_columnas()):
                if (self.get_matriz()[i][j].get_activo() == False):
                    self.get_matriz()[i][j].set_habilitado(True)
#______________________________________________________agregado nuevo


    def modificar_premios(self,lista, tipo,clave, color):
        for valor in lista:
            try:
                self.get_matriz()[valor[0]][valor[1]].set_premio(tipo) # si es palabra x2, letrax2, letrax3
                self.get_matriz()[valor[0]][valor[1]].set_color(color )
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
        letter_tablero = { 'size' : (4,2), 'pad' : (0,0)} # ACA PODEMOS MODIFICAR EL TAMAN
        layout = [[sg.Button(key = (i, j),button_text= self.get_matriz()[i][j].get_premio(),button_color=('white',self.get_matriz()[i][j].get_color()),  **letter_tablero) for i in range(filas)] for j in range(columnas)]

        return layout
