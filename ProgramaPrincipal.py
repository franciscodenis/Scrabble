import PySimpleGUI as sg
import Tablero
import Atril
import Casilla

filas = 5
columnas = 6
tablero = Tablero.Tablero(filas,columnas)
atril = Atril.Atril(5)
atril.agregar_letras()
list_coor = []
puntaje_total = 0


letter_button = { 'size' : (5, 2), 'pad' : (0,0)  } #"image_filename" : 'fondoBoton.png', 'image_subsample': 30

layout = [[sg.Button(key = (i, j),button_text= ' ', **letter_button) for i in range(filas)] for j in range(columnas)]

layout.append([sg.Text('Seleccione una letra de abajo', auto_size_text=True)])
layout.append([sg.Button(key=(-1, i) , button_text= atril.get_espacio_fichas()[i].get_letra(), **letter_button) for i in range(5)])
botones = [sg.Button(key='vali', button_text='Validar'), sg.Text('Puntaje total: '), sg.Text('0', key='punt')]
layout.append(botones)

window = sg.Window('Scrabble').Layout(layout)

while True:
    event, values = window.Read()

    if event in tablero.listado_botones():
        if (atril.get_casilla_seleccionada().get_id() in atril.listado_botones()):
            refresh = tablero.click(atril, event)
            window.Element(event).Update(refresh[0])
            window.Element(atril.get_casilla_seleccionada().get_id()).Update(refresh[1])
            if (refresh[1] == ' '):
                list_coor.append(event)

    if event in atril.listado_botones():
        refresh = atril.click(tablero, event)
        #window.Element(event).Update(refresh)
    if event == 'vali':
        ToF = tablero.validar_pal(list_coor)
        if(ToF[0] == True):
            puntaje_total = puntaje_total + ToF[1]
            print('Palabra correcta su puntaje por la palabra: ', ToF[1])
            window.Element('punt').Update(puntaje_total)
        else:
            print('Palabra incorrecta, se le devolvera las fichas')

    if event in (None, 'Exit'):
        break
