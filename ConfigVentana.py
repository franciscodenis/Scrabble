import PySimpleGUI as sg

def layoutPrin():
    layoutPrincipal = [
            [sg.Button('Jugar', key='jugar', pad=((130, 0), 35), size=(25,1))],
            [sg.Button('Configurar', key='config', pad=((130, 0), 35), size=(25,1))],
            [sg.Button('Estadisticas', key='ranking', pad=((130, 0), 35), size=(25,1))],
            [sg.Button('Salir', key='quit', pad=((130, 0), 35), size=(25,1))],
    ]
    return layoutPrincipal

def layoutConfig():
    layoutconfig = [
                [sg.Text('Seleccione el nivel de dificultad:', font='Helvetica', background_color=('#A72D2D'))],
                [sg.InputCombo(('Facil', 'Normal', 'Dificil'), size=(25,1), key='nivel')],
                [sg.Text('Seleccione el tiempo por ronda:', font='Helvetica', background_color=('#A72D2D'))],
                [sg.InputCombo(('20 seg(facil)', '15 seg(normal)', '10 seg(dificil)'), size=(20,1), key='tiempo')],
                [sg.Button('Aceptar', key='Ok', pad=(80,5))]
    ]
    return layoutconfig

def layoutNoConfig():
    layoutNoConfig = [
                    [sg.Text('Antes de comenzar configure el juego', font='Helvetiva', background_color=('#A72D2D'))],
                    [sg.Ok()]
    ]
    return layoutNoConfig

def layoutUsuario():
    layoutUs = [
               [sg.Text('Ingrese un nombre de usuario: ', background_color=('#A72D2D')), sg.InputText(key='usuario')],
               [sg.Button('Aceptar', pad=(100,10), key='ok')]
    ]
    return layoutUs



def ventanaConfig (config):
    try:
        windowConfig = sg.Window('Configuracion', size=(300,160), background_color=('#A72D2D')).Layout(layoutConfig())
        event, value = windowConfig.Read()
        if event == None:
            windowConfig.Close()
            return config
        if event == 'Ok':
            config = value
        windowConfig.Close()
        return config
    except:
        print('Error al abrir la ventana')
        pass

def ventanaJugar (config, Scrabble):
    if (len(config) == 0):
        try:
            windowNoConfig = sg.Window('Aviso', size=(450,100), background_color=('#A72D2D')).Layout(layoutNoConfig())
            event, value = windowNoConfig.Read()
            if (event == 'Ok'):
                windowNoConfig.Close()
            else:
                windowNoConfig.Close()
        except:
            print('Error al abrir la ventana')
            pass
    else:
        windowUs = sg.Window('Usuario', size=(350, 100), background_color=('#A72D2D')).Layout(layoutUsuario())
        event, value = windowUs.Read()
        if event == 'ok':
            nombre = value['usuario']
            windowUs.Close()
            return (nombre, Scrabble.main(config['nivel'], config['tiempo'].split(' ')[0]))
