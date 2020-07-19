import PySimpleGUI as sg
from datetime import date
import sqlite3
import pickle
import os
import ScrabbleAR

nombre_archivo_rankings = 'ranking_nuevo'

def guardar_score (dificultad, nombre, puntos, conexion):
    '''guardo score en archivo ingresado como parametro'''
    puntero = conexion.cursor()
    dia = date.today().day
    mes = date.today().month
    ano = date.today().year
    fecha = "{}/{}/{}".format(dia, mes, ano)
    score = [
            (nombre, puntos, fecha, dificultad)
    ]
    try:
        puntero.executemany("INSERT INTO RANKING VALUES (?, ?, ?, ?)", score)
        conexion.commit()
    except sqlite3.OperationalError:
        puntero.execute("CREATE TABLE RANKING (NOMBRE VARCHAR(50), PUNTOS INTEGER, FECHA VARCHAR(10), NIVEL VARCHAR(10))")
        puntero.executemany("INSERT INTO RANKING VALUES (?, ?, ?, ?)", score)
        conexion.commit()



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

def mostrar_ranking(nivel, puntero):
    '''Muestro ranking '''
    try:
        query = "SELECT * FROM RANKING WHERE NIVEL = ?  ORDER BY PUNTOS DESC"
        puntero.execute(query, (nivel.strip('-'),))
        usuarios_ranking = puntero.fetchall()
        if (len(usuarios_ranking) > 0):
            for linea in usuarios_ranking[:10]:
                print('Nombre: {}    Puntaje: {}    Fecha: {}'.format(linea[0],linea[1],linea[2]))
        else:
            print('No se han cargado datos en este nivel')
    except sqlite3.OperationalError:
        puntero.execute("CREATE TABLE RANKING (NOMBRE VARCHAR(50), PUNTOS INTEGER, FECHA VARCHAR(10), NIVEL VARCHAR(10))")


def ventanaGanador(puntaje_jugador, puntaje_maquina,nivel):
    '''imprime en una ventana quien fue el ganador y pone un menu para volver al juego'''
    text=[' ']
    if (puntaje_jugador< puntaje_maquina):
        imagen= '/imagenes/perdiste.png'
        text= 'PERDISTE :()'
    elif (puntaje_maquina< puntaje_jugador):
        imagen= '/imagenes/ganaste.png'
        text:'GANASTE :)'
    else:
        imagen='/imagenes/empataron.png'
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
            windowTop.Close()
            conexion = sqlite3.connect("Usuarios")
            ScrabbleAR.main(conexion)
            conexion.close()
            break
