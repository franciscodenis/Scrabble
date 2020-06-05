import PySimpleGUI as sg
import ProgramaPrincipal as Scrabble
import ConfigVentana as conf
import json

windowPrin = sg.Window('Scrabble', size=(500, 500), background_color=('#95BD50')).Layout(conf.layoutPrin())
config = {}
config2 = {}
datos = []


while True:
    event, value = windowPrin.Read()
    if event in (None, 'quit'):
        break
    elif event == 'jugar':
        puntos = conf.ventanaJugar(config2, Scrabble)
        if (puntos != None):
            try:
                archivo = open("ranking.txt", "r")
                datos = json.load(archivo)
                datos.append({'Nombre': puntos[0], 'Puntaje': puntos[1]})
                archivo = open("ranking.txt", "w")
                archivo.write(json.dumps(datos))
                archivo.close()
            except:
                archivo = open("ranking.txt", "w")
                datos.append({'Nombre': puntos[0], 'Puntaje': puntos[1]})
                json.dump(datos, archivo)
                archivo.close()
    elif event == 'config':
        config2 = conf.ventanaConfig(config)
    #elif event == 'ranking':
