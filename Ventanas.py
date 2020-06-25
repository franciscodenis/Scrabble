

import PySimpleGUI as sg
import VentanasBackEnd
import ProgramaPrincipal

ancho_total = 120
layout_ventana_principal = [
    [sg.Button('Jugar', key='jugar', pad=((0, 0), 10), size=(ancho_total + 8, 1))],

    [sg.Text('Seleccione nivel de dificultad: ')],
    [sg.Button('Facil', key='dificultad_facil', pad=((0, 0), 10), size=(round(ancho_total/3), 1)),
     sg.Button('Media', key='dificultad_media', pad=((0, 0), 10), size=(round(ancho_total/3), 1)),
     sg.Button('Máxima', key='dificultad_maxima', pad=((0, 0), 10), size=(round(ancho_total/3), 1))],

    [sg.Text('Seleccione el tiempo por turno: ')],
    [sg.Button('30 seg', key='tiempo_turno_30_seg', pad=((0, 0), 10), size=(round(ancho_total/3), 1)),
     sg.Button('60 seg', key='tiempo_turno_60_seg', pad=((0, 0), 10), size=(round(ancho_total/3), 1)),
     sg.Button('90 seg', key='tiempo_turno_90_seg', pad=((0, 0), 10), size=(round(ancho_total/3), 1))],

    [sg.Text('Ver records por dificultad ')],
    [sg.Button('Mejores Puestos - Dificultad Facil', key='mejores_puestos_dif_facil', pad=((0, 0), 10), size=(round(ancho_total / 3), 1)),
     sg.Button('Mejores Puestos - Dificultad Media', key='mejores_puestos_dif_media', pad=((0, 0), 10), size=(round(ancho_total / 3), 1)),
     sg.Button('Mejores Puestos - Dificultad Máximo', key='mejores_puestos_dif_maxima', pad=((0, 0), 10), size=(round(ancho_total / 3), 1))],

    [sg.Output(size=(ancho_total+80, 5), key='-OUTPUT-', )],
    [sg.Button('Salir', key='quit', pad=((0, 0), 35), size=(ancho_total + 8, 1))],
]

botones_dificultad = ['dificultad_facil', 'dificultad_media', 'dificultad_maxima']
botones_tiempo_turno = ['tiempo_turno_30_seg', 'tiempo_turno_60_seg', 'tiempo_turno_90_seg']
botones_mejores_puestos = ['mejores_puestos_dif_media', 'mejores_puestos_dif_facil', 'mejores_puestos_dif_maxima']
configuracion_partida = ['dificultad_facil', 90]
window_principal = sg.Window('Scrabble', size=(ancho_total * 8, 475)).Layout(layout_ventana_principal)

diccionario_mejores_puestos = {'juan' : 90}

jugar = False

while True:
    event, value = window_principal.Read()
    if event in (None, 'quit'):
        window_principal.Close()
        break

    if event in botones_dificultad:
        VentanasBackEnd.click_dificultad(window_principal, event, botones_dificultad, configuracion_partida)

    if event in botones_tiempo_turno:
        VentanasBackEnd.click_tiempo_turno(window_principal, event, botones_tiempo_turno, configuracion_partida)

    if event in botones_mejores_puestos:
        window_principal.FindElement('-OUTPUT-').Update('')
        VentanasBackEnd.click_mejores_puestos(window_principal, event, botones_mejores_puestos)

    if event in 'jugar':
        window_principal.Close()
        ProgramaPrincipal.main(configuracion_partida[0], configuracion_partida[1])
        break
