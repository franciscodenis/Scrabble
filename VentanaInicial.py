'''por aca empieza el programa principal'''

import PySimpleGUI as sg
import ProgramaPrincipal as Scrabble
import ConfigVentana as conf
import json

#configuro la ventana
windowPrin = sg.Window('Scrabble', size=(500, 500), background_color=('#95BD50')).Layout(conf.layoutPrin())
config = {}
config2 = {}


while True:
    #muestro y leo la ventana
    event, value = windowPrin.Read()
    if event in (None, 'quit'):
        windowPrin.Close()
        break
    elif event == 'jugar':
        # empiezo a preparar el juego

        puntos = conf.ventanaJugar(config2, Scrabble)

        if (puntos != None) and (len(config2) != 0):
            if (config2['nivel'] == 'Facil'):
                conf.abrirArch("rankingFacil.txt", puntos)
            elif(config2['nivel'] == 'Normal'):
                conf.abrirArch("rankingNormal.txt", puntos)
            else:
                conf.abrirArch("rankingDificil.txt", puntos)
        else:
            conf.abrirArch("rankingFacil.txt", puntos)

    elif event == 'config':
        config2 = conf.ventanaConfig(config)
    elif event == 'ranking':
        conf.mostrar_ranking() # MODIF AGUS
