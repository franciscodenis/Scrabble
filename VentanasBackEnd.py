import RegistroPartidas

def click_dificultad(window, evento, botones_dificultad, configuracion_partida):
    ''' selecciona un boton de dificultad '''

    for boton in botones_dificultad.keys():
        if evento == boton:
            configuracion_partida[0] = evento
            configuracion_partida[2] = botones_dificultad[evento]
            window.Element(boton).Update(button_color=('white', 'black'))
        else:
            window.Element(boton).Update(button_color=('#FFFFFF', '#283b5b'))


def click_tiempo_turno(window, evento, botones_tiempo_turno, configuracion_partida):
    ''' Selecciona  un tiempo de juego '''
    diccionario_tiempo_turnos = {'tiempo_turno_30_seg': 30, 'tiempo_turno_60_seg': 60, 'tiempo_turno_90_seg': 90}
    for boton in botones_tiempo_turno:
        if evento == boton:
            configuracion_partida[1] = diccionario_tiempo_turnos[evento]
            window[boton].update(button_color=('white', 'black'))
        else:
            window[boton].update(button_color=('#FFFFFF', '#283b5b'))


def click_mejores_puestos(window, evento, botones_mejores_puestos):
    ''' muestra los mejores puestos'''
    for boton in botones_mejores_puestos:
        if evento == boton:
            RegistroPartidas.mostrar_ranking(boton)
            window[boton].update(button_color=('white', 'black'))


        else:
            window[boton].update(button_color=('#FFFFFF', '#283b5b'))
