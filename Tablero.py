import PySimpleGUI as sg
import MetaTablero

filas = 5
columnas = 6
tablero = MetaTablero.Tablero(filas,columnas)
atril = MetaTablero.Atril(5)
atril.agregar_letras()


letter_button = { 'size' : (5, 2), 'pad' : (0,0)  } #"image_filename" : 'fondoBoton.png', 'image_subsample': 30

layout = [[sg.Button(key = (i, j),button_text= ' ', **letter_button) for i in range(filas)] for j in range(columnas)]

layout.append([sg.Text('Seleccione una letra de abajo', auto_size_text=True)])
layout.append([sg.Button(key=(-1, i) , button_text= atril.espacio_fichas[i].letra, **letter_button) for i in range(5)])

window = sg.Window('Scrabble', layout)

while True:
    event, values = window.read()

    if event in tablero.listado_botones():
        if (atril.casilla_seleccionada.ID in atril.listado_botones()):
            refresh = tablero.click(atril, event)
            window[event].update(refresh[0])
            window[atril.casilla_seleccionada.ID].update(refresh[1])

    if event in atril.listado_botones():
        refresh = atril.click(tablero, event)
        window[event].update(refresh)

    if event in (None, 'Exit'):
        break
