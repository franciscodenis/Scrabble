import PySimpleGUI as sg
import ProgramaPrincipal as Scrabble
import ConfigVentana as conf
import json


windowPrin = sg.Window('Scrabble', size=(500, 500), background_color=('#95BD50')).Layout(conf.layoutPrin())
config = {}
config2 = {}


while True:
    event, value = windowPrin.Read()
    if event in (None, 'quit'):
        break
    elif event == 'jugar':
        puntos = conf.ventanaJugar(config2, Scrabble)
        if (puntos != None):
            if (config2['nivel'] == 'Facil'):
                conf.abrirArch("rankingFacil.txt", puntos)
            elif(config2['nivel'] == 'Normal'):
                conf.abrirArch("rankingNormal.txt", puntos)
            else:
                conf.abrirArch("rankingDificil.txt", puntos)
    elif event == 'config':
        config2 = conf.ventanaConfig(config)
    elif event == 'ranking':
        niv = conf.ventanaSelecTop()
        try:
            if (niv == 'Facil'):
                archivo = open('rankingFacil.txt', 'r')
            elif(niv == 'Normal'):
                archivo = open('rankingNormal.txt', 'r')
            else:
                archivo = open('rankingDificil.txt', 'r')       
            datos = json.load(archivo)
            conf.ventanaRanking(sorted(datos, key = lambda puntaje: puntaje['Puntaje'], reverse=True))
        except:
            print('No se registro ningun jugador')
