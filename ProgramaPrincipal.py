def mostrarModo():
    pass

import PySimpleGUI as sg
import Tablero
import Atril
import Casilla
import Fichas
import pickle


def main():
    filas = 15
    columnas = 15
    letras_de_atril = 7

    tablero = Tablero.Tablero(filas,columnas)
    atril = Atril.Atril(letras_de_atril)

    fichas_jugador= Fichas.crear_bolsa_de_fichas()
    puntajes_letras = Fichas.crear_diccionario_de_puntos()
    diccionario = Fichas.crear_diccionario()
    palabras_permitidas = ['NN', 'JJ', 'VB' ]
    f = open("jugadores.txt", "wb")
    pickle.dump(diccionario, f)
    f.close()

    atril.agregar_letras(fichas_jugador)

    puntaje_total = 0 # Debería estar en la clase jugador

    letter_atril = { 'size' : (3, 2), 'pad' : (0,0), 'button_color' : ('white', '#C8C652')}

    layout= tablero.crear_tablero('principiante')
    layout.append([sg.Text('Seleccione una letra de abajo', auto_size_text=True, font='Helvetica', background_color=('#5CA2A3'))])
    layout.append([sg.Button(key=(-1, i) , button_text= atril.get_espacio_fichas()[i].get_letra(), **letter_atril) for i in range(letras_de_atril)])
    botones = [sg.Button(key='vali', button_text='Validar', button_color=('white', '#C54F1F'), font='Helvetica'),sg.Button(button_text='Cambiar letras',key ="cambiar_letras", button_color=('white', '#C54F1F'), font='Helvetica'), sg.Text('Puntaje total: ', font='Helvetica', background_color=('#5CA2A3')), sg.Text('0', key='punt', font='Helvetica', background_color=('#5CA2A3'))]
    layout.append(botones)

    window = sg.Window('Scrabble', background_color='#5CA2A3').Layout(layout)

    while True:
        event, values = window.Read()

        if event in tablero.listado_botones():
            tablero.click(atril, event, window)

        if event == "cambiar_letras":
            if atril.get_cambios_atril() > 0 and len(fichas_jugador)>7:
                atril.cambiar_letras(fichas_jugador,window,tablero)
            else:
                if(atril.get_cambios_atril()<1):
                    sg.Popup('no tienes mas cambios')

        if event in atril.listado_botones():
            atril.click(tablero, event)

        if event == 'vali':
            tablero.click_validar(atril, tablero, window, diccionario, puntaje_total, fichas_jugador, palabras_permitidas)

        if event in (None, 'Exit'):
            break
if __name__ == '__main__':
    main()
