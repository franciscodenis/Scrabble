import RegistroPartidas

def click_dificultad(window, evento, botones_dificultad, configuracion_partida):
    for boton in botones_dificultad:
        if evento == boton:
            configuracion_partida[0] = evento
            window[boton].update(button_color=('white', 'black'))
        else:
            window[boton].update(button_color=('#FFFFFF', '#283b5b'))


def click_tiempo_turno(window, evento, botones_tiempo_turno, configuracion_partida):
    diccionario_tiempo_turnos = {'tiempo_turno_30_seg': 30, 'tiempo_turno_60_seg': 60, 'tiempo_turno_90_seg': 90}
    for boton in botones_tiempo_turno:
        if evento == boton:
            configuracion_partida[1] = diccionario_tiempo_turnos[evento]
            window[boton].update(button_color=('white', 'black'))
        else:
            window[boton].update(button_color=('#FFFFFF', '#283b5b'))


def click_mejores_puestos(window, evento, botones_mejores_puestos):
    for boton in botones_mejores_puestos:
        if evento == boton:
            RegistroPartidas.mostrar_ranking(boton)
            window[boton].update(button_color=('white', 'black'))


        else:
            window[boton].update(button_color=('#FFFFFF', '#283b5b'))
