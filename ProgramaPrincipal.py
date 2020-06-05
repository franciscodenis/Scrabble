def seleccionar_turno():

    turno=random.choice(['computadora','jugador'])
    return turno

def cambiarTurno():
    pass



def mostrarModo():
    pass

import PySimpleGUI as sg
import Tablero
import Atril
import Casilla
import Fichas
import pickle
import time
import Jugar


def main():

    filas = 15
    columnas = 15
    letras_de_atril = 7
    jugar= Jugar.Jugar()
    tablero = Tablero.Tablero(filas,columnas)
    atril = Atril.Atril(letras_de_atril)

    fichas_jugador= Fichas.crear_bolsa_de_fichas()
    puntajes_letras = Fichas.crear_diccionario_de_puntos()
    #diccionario = Fichas.crear_diccionario()
    diccionario=['a','v','b','c'] # lo comento porque no me funca
    palabras_permitidas = ['NN', 'JJ', 'VB' ]

    atril.agregar_letras(fichas_jugador)

    puntaje_total = 0 # Debería estar en la clase jugador

    letter_atril = { 'size' : (3, 2), 'pad' : (0,0), 'button_color' : ('white', '#C8C652')}
    layout= []
    layout.append([sg.Text('', size=(8, 2), font=('Helvetica', 20), justification='center', key='tempo_compu')]) #Temporizador Computadora
    layout.extend(tablero.crear_tablero('principiante'))
    layout.append([sg.Text('Seleccione una letra de abajo', auto_size_text=True, font='Helvetica', background_color=('#5CA2A3'))])
    layout.append([sg.Button(key=(-1, i) , button_text= atril.get_espacio_fichas()[i].get_letra(), **letter_atril) for i in range(letras_de_atril)])
    botones = [sg.Button(key='vali', button_text='Validar', button_color=('white', '#C54F1F'), font='Helvetica'),sg.Button(button_text='Cambiar letras',key ="cambiar_letras", button_color=('white', '#C54F1F'), font='Helvetica'), sg.Text('Puntaje total: ', font='Helvetica', background_color=('#5CA2A3')), sg.Text('000', key='punt', font='Helvetica', background_color=('#5CA2A3'))]
    layout.append([sg.Checkbox("", key=('Checkbox', i), size=(2, 2))for i in range(letras_de_atril)])
    layout.append(botones)
    layout.append([sg.Text('', size=(8, 2), font=('Helvetica', 20), justification='center', key='text')]) #Temporizador


    window = sg.Window('Scrabble', background_color='#5CA2A3').Layout(layout)
    current_time=0
    tiempo_computadora = 0 # inicializo el tiempo actual en 0
    paused = False
    start_time = int(round(time.time() * 100))
    print(jugar.get_turno())
    tiempo_max= 1000 # SETEARRRRRRRR

    while True:


        if jugar.get_turno()=='computadora':
            if (tiempo_computadora> tiempo_max):
                print('terminoeltiempo')
                jugar.cambiar_turno() # o terminar


            event, values = window.Read(timeout=0)
            tiempo_computadora = int(round(time.time() * 100))-current_time - start_time
            window['tempo_compu'].update('{:02d}:{:02d}.{:02d}'.format((tiempo_computadora // 100) // 60,(tiempo_computadora // 100) % 60, tiempo_computadora % 100))
            jugar.jugar_computadora(tablero,atril)




        elif jugar.get_turno()=='jugador':
            if (current_time> tiempo_max):
                print('terminoeltiempo jugador') #MODULO TERMINAR

                break
            event, values = window.Read(timeout=10)
            current_time = int(round(time.time() * 100))-(tiempo_computadora) - start_time
            if event in tablero.listado_botones():
                tablero.click(atril, event, window)
            elif event == "cambiar_letras":
                atril.cambiar_letras(fichas_jugador,window,tablero,values,fichas_jugador,jugar)
            elif event in atril.listado_botones():
                atril.click(tablero, event)

            elif event == 'vali':
                puntaje_total = tablero.click_validar(atril, tablero, window, diccionario, puntaje_total, fichas_jugador,jugar, palabras_permitidas)
            elif event == 'Run':
                paused = False
                start_time = start_time + int(round(time.time() * 100)) - paused_time
                element = window['button']

            window['text'].update('{:02d}:{:02d}.{:02d}'.format((current_time // 100) // 60, (current_time // 100) % 60, current_time % 100))

if __name__ == '__main__':
    main()
