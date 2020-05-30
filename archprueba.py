import PySimpleGUI as sg

def modificarTablero(self):




def modificar_premios(self,lista, tipo, color):
    for valor in lista_perdidas:
        try:
            self.get_matriz()[valor[0]][valor[1]].set_premio(tipo) # si es palabra x2, letrax2, letrax3
            self.get_matriz()[valor[0]][valor[1]].set_color(color )
        except
def devolver_lista(self,lista):
    for tupla in lista:
        lista.append((tupla[1],tupla[0]))
    return lista

def modificaciones_principiante(self):
    lista_3p=[(1,1),(1,4),(1,3),(1,12),(1,15),(2,2),(2,14)]
    lista_3p= devolver_lista(lista_3p)
    self.modificar_premios(lista_3p,'3P','3P','#33FF71') #verde
    lista_2p=[(2,5),(2,11),(3,3),(3,6),(3,10),(3,13),(4,4),(4,12,)]
    lista_2p= devolver_lista(lista_2p)
    self.modificar_premios(lista_2p,'2P','2P','#FFC133') #naranja
    lista_3L=[(4,7),(4,9),(5,5),(5,11),(6,6),(6,10),(7,8),(8,7),(8,9)]
    lista_3L=devolver_lista(lista_3L)
    self.modificar_premios(lista_3L,'3L','3L','#334CFF') #azul
    lista_2L=[(5,8),(7,7),(7,9)]
    lista_2L= devolver_lista(lista_2L)
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
def crear_tablero(self):
    if nivel== 'principiante':
        modificaciones_principiante()
    elif nivel== 'intermedio':
        modificaciones_intermedio()
    elif nivel=="experto":
        modificaciones_experto()
    else:
        modificaciones_usuario()
    layout = [[sg.Button(key = (i, j),button_text= ' ',button_color=self.get_matriz()[i][j].get_color(),  **letter_tablero) for i in range(filas)] for j in range(columnas)]

    return layout
