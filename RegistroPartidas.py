import PySimpleGUI as sg
from datetime import date

import pickle
import os

nombre_archivo_rankings = 'ranking_nuevo'

def guardar_score (dificultad, nombre, puntos):
    '''guardo score en archivo '''
    dia = date.today().day
    mes = date.today().month
    ano = date.today().year
    nuevo_record = {'Nombre': nombre, 'Puntaje': puntos, 'Fecha': "{}/{}/{}".format(dia, mes, ano)}

    print(nuevo_record)


    try:
        try:
            file=open(nombre_archivo_rankings, 'rb')
            data = pickle.load(file)
        except(FileNotFoundError):
            file= open(nombre_archivo_rankings,'w')
            data={}
        data[dificultad].append(nuevo_record)
        print(data)

    except (KeyError):
        print("No record yet")
        data[dificultad]= [nuevo_record]
    file.close()
    with open(nombre_archivo_rankings, 'wb') as file:
        pickle.dump(data, file)
        file.close()


def ingresar_usuario():
    '''muestro una ventana para ingresar nombre de usuario. si no se ingresa se toma como nombre "anonimo"'''
    layout_ingreso_usuario = [
               [sg.Text('Ingrese un nombre de usuario: ', background_color=('#A72D2D')), sg.InputText(key='usuario')],
               [sg.Button('Aceptar', pad=(100,10), key='ok')]
    ]
    nombre = 'Anonimo'
    windowUs = sg.Window('Usuario', size=(350, 100), background_color=('#A72D2D')).Layout(layout_ingreso_usuario)
    event, value = windowUs.Read()
    if event == 'ok':
        nombre = value['usuario']
        windowUs.Close()

    return nombre

def mostrar_ranking(nivel):
    '''Muestro ranking '''

    diccionario_dificultad_según_boton = {'mejores_puestos_dif_facil': 'dificultad_facil',
                                          'mejores_puestos_dif_media': 'dificultad_media',
                                          'mejores_puestos_dif_maxima' : 'dificultad_maxima'
                                          }
    try:
        with open(nombre_archivo_rankings, 'rb') as f:
            datos = pickle.load(f)
            f.close()
        try:
            dificultad = diccionario_dificultad_según_boton[nivel]
            datos_a_imprimir = datos[dificultad]
            datos_a_imprimir = list(map( lambda x : list([x['Nombre'],x['Puntaje'], x['Fecha']]), datos_a_imprimir ))
            datos_a_imprimir = sorted(datos_a_imprimir,key= lambda x : x[1], reverse = True)
            for linea in datos_a_imprimir:
                print('Nombre: {}    Puntaje: {}    Fecha: {}'.format(linea[0],linea[1],linea[2]))
        except KeyError:
            print('No hay jugadores record en esta dificultad')

    except (FileNotFoundError, IOError):
        print("No record yet")
def ventanaGanador(puntaje_jugador, puntaje_maquina,nivel):
    '''imprime en una ventana quien fue el ganador y pone un menu para volver al juego'''
    if (puntaje_jugador< puntaje_maquina):
        imagen= '\imagenes\perdiste.png'
        text= 'PERDISTE :()'
    elif (puntaje_maquina< puntaje_jugador):
        imagen= '\imagenes\ganaste.png'
        text:'GANASTE :)'
    else:
        imagen='\imagenes\empataron.png'
        text='EMPATE '
    texto = "TU PUNTAJE= "  + str(puntaje_jugador)
    texto2= "COMPUTADORA= " + str(puntaje_maquina)

    #AGREGAR EL PUNTAJE A LA LISTA
    layout = [[sg.Image((os.getcwd()+imagen), size=(400,300))],
            [sg.Txt(texto )],
            [sg.Txt(texto2)],
    		[sg.Button('Salir', key='quit', size=(25,1),focus=True)],
            [sg.Button('Volver al menu', key='volver', size=(25,1))],

    	]


    windowTop = sg.Window(text , size=(800,500), background_color=('white')).Layout(layout)
    while True:
        event, value = windowTop.Read()
        if (event == 'quit'):
            break

        elif event== 'volver':
            windowTop.close()
            import Ventanas
            Ventanas.Ventanas() #Aparece error pero no hay error ???







