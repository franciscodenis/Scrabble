import PySimpleGUI as sg
import Tablero
import Atril
import Casilla
import Fichas

filas = 6
columnas = 5
tablero = Tablero.Tablero(filas,columnas)
atril = Atril.Atril(5)
fichas_jugador= Fichas.crear_bolsa_de_fichas()
atril.agregar_letras(fichas_jugador)
list_coor = []
puntaje_total = 0


letter_tablero = { 'size' : (5, 2), 'pad' : (0,0), 'button_color' : ('white', 'white')} #"image_filename" : 'fondoBoton.png', 'image_subsample': 30
letter_atril = { 'size' : (5, 2), 'pad' : (0,0), 'button_color' : ('white', '#C8C652')}

layout = [[sg.Button(key = (i, j),button_text= ' ', **letter_tablero) for i in range(filas)] for j in range(columnas)]

layout.append([sg.Text('Seleccione una letra de abajo', auto_size_text=True, font='Helvetica', background_color=('#5CA2A3'))])
layout.append([sg.Button(key=(-1, i) , button_text= atril.get_espacio_fichas()[i].get_letra(), **letter_atril) for i in range(5)])
botones = [sg.Button(key='vali', button_text='Validar', button_color=('white', '#C54F1F'), font='Helvetica'),sg.Button(button_text='Cambiar letras',key ="cambiar_letras", button_color=('white', '#C54F1F'), font='Helvetica'), sg.Text('Puntaje total: ', font='Helvetica', background_color=('#5CA2A3')), sg.Text('0', key='punt', font='Helvetica', background_color=('#5CA2A3'))]
layout.append(botones)

window = sg.Window('Scrabble', background_color='#5CA2A3').Layout(layout)

while True:
    event, values = window.Read()

    if event in tablero.listado_botones():
        if (atril.get_casilla_seleccionada().get_id() in atril.listado_botones()):
            refresh = tablero.click(atril, event)
            if (refresh[1] == ' '):
                window.Element(event).Update(refresh[0], button_color=('white', '#C8C652'))
                window.Element(atril.get_casilla_seleccionada().get_id()).Update(refresh[1])
            if (refresh[1] == ' '):
                list_coor.append(event)
    if event ==  "cambiar_letras":
        if atril.get_cambios_atril()>0 and len(fichas_jugador)>7:
            atril.agregar_letras(fichas_jugador)
            atril.refrescar_atril(window)

        else:
            if(atril.get_cambios_atril()<1):
                sg.Popup('no tienes mas cambios')

    if event in atril.listado_botones():
        refresh = atril.click(tablero, event)
        #window.Element(event).Update(refresh)
    if event == 'vali':
        ToF = tablero.validar_pal(list_coor)
        if(ToF[0] == True):
            puntaje_total = puntaje_total + ToF[1]
            print('Palabra correcta su puntaje por la palabra: ', ToF[1])
            window.Element('punt').Update(puntaje_total)
            atril.llenar_atril(fichas_jugador) #no pude probar el llenar atril
            atril.refrescar_atril(window)
            tablero.get_coordenadasActivas().clear() #libera la lista de coordenadas activas para que me tome las coordenadas mini y max correcta
        else:
            print('Palabra incorrecta, se le devolvera las fichas')
            atril.devolver_fallo(list_coor, window, tablero) #Devuelve las letras del tablero al atril(falta pulir)
            tablero.get_coordenadasActivas().clear() #libera la lista de coordenadas activas para que me tome las coordenadas mini y max correcta
        tablero.desbloquear_tablero() #desbloquea el tablero 
        list_coor.clear()
    if event in (None, 'Exit'):
        break
