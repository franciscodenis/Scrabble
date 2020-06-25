
import PySimpleGUI as sg
import Tablero
import Atril
import Casilla
import Fichas
import pickle
import time
import Jugar
import ConfigVentana as conf
import RegistroPartidas





def seleccionar_turno():

    turno=random.choice(['computadora','jugador'])
    return turno



def main(nivel = 'Facil', tiempo = 30):

    nombre = RegistroPartidas.ingresar_usuario()
    filas = 15
    columnas = 15
    letras_de_atril = 7
    jugar= Jugar.Jugar()
    tablero = Tablero.Tablero(filas,columnas)
    atril = Atril.Atril(letras_de_atril)
    atril_pc = Atril.Atril_PC(letras_de_atril)

    fichas_jugador= Fichas.crear_bolsa_de_fichas()
    puntajes_letras = Fichas.crear_diccionario_de_puntos()
    diccionario = Fichas.crear_diccionario()
    palabras_permitidas = ['NN', 'JJ', 'VB' ]

    atril.agregar_letras(fichas_jugador)
    atril_pc.agregar_letras(fichas_jugador)

    puntaje_total = 0 # Debería estar en la clase jugador

    letter_atril = { 'size' : (3, 2), 'pad' : (0,0), 'button_color' : ('white', '#C8C652')}
    layout= []
    layout.append([sg.Button(key=('Atril_PC', i), button_text=atril_pc.get_espacio_fichas()[i].get_letra(), **letter_atril) for i in range(letras_de_atril)])
    PC = [sg.Text('', size=(8, 2), font=('Helvetica', 20), justification='center', key='tempo_compu'), sg.Text('Puntaje computadora: ', font='Helvetica', background_color=('#5CA2A3')), sg.Text('000', key='puntPC', font='Helvetica', background_color='#5CA2A3')] #Temporizador Computadora
    layout.append(PC)
    layout.extend(tablero.crear_tablero(nivel))
    layout.append([sg.Text('Seleccione una letra de abajo', auto_size_text=True, font='Helvetica', background_color=('#5CA2A3'))])
    layout.append([sg.Button(key=('Atril_jugador', i) , button_text= atril.get_espacio_fichas()[i].get_letra(), **letter_atril) for i in range(letras_de_atril)])
    botones = [sg.Button(key='vali', button_text='Validar', button_color=('white', '#C54F1F'), font='Helvetica'),sg.Button(button_text='Cambiar letras',key ="cambiar_letras", button_color=('white', '#C54F1F'), font='Helvetica'), sg.Text('Puntaje total: ', font='Helvetica', background_color=('#5CA2A3')), sg.Text('000', key='punt', font='Helvetica', background_color=('#5CA2A3'))]
    layout.append([sg.Checkbox("", key=('Checkbox', i), size=(2, 2))for i in range(letras_de_atril)])
    layout.append(botones)
    layout.append([sg.Text('', size=(8, 2), font=('Helvetica', 20), justification='center', key='timer_jugador')]) #Temporizador


    window = sg.Window('Scrabble', background_color='#5CA2A3').Layout(layout)
    current_time=0
    tiempo_computadora = 0 # inicializo el tiempo actual en 0
    paused = False
    start_time = int(round(time.time() * 100))
    print(jugar.get_turno())
    tiempo_max= tiempo * 100
    tiempo_comienzo_juego=int(round(time.time() * 100))
    tiempo_fin_juego=20#MODIFICAR
    while True:
        event, values = window.Read(timeout=0)
        if(int(round(time.time() * 100))-tiempo_comienzo_juego> tiempo_fin_juego):  # el juego terminó
            window.close()
            RegistroPartidas.guardar_score(nivel, nombre, puntaje_total)
            conf.ventanaGanador(puntaje_total, atril_pc.get_puntaje(), nivel)

            break
        else:
            # turno de la computadora

            if jugar.get_turno()=='computadora':
                start_time=int(round(time.time()*100)) # momento en el que empiezo a contar
                window.Read(timeout=0)
                current_time= 0 #tiempo transcurrido
                tiempo_computadora = int(round(time.time()*100))-current_time - start_time
                window.Element('tempo_compu').Update('{:02d}:{:02d}.{:02d}'.format((tiempo_computadora // 100) // 60,(tiempo_computadora // 100) % 60, tiempo_computadora % 100))
                seguir_jugando = atril_pc.jugar_turno(tablero, diccionario, window, fichas_jugador, puntajes_letras, palabras_permitidas)
                tiempo_computadora = int(round(time.time()))-current_time - start_time
                window.Element('tempo_compu').Update('{:02d}:{:02d}.{:02d}'.format((tiempo_computadora // 100) // 60,(tiempo_computadora // 100) % 60, tiempo_computadora % 100))

                if not seguir_jugando:
                    jugar.cambiar_turno()
                if (tiempo_computadora > tiempo_max):
                    print('terminoeltiempo')
                    jugar.cambiar_turno() # o terminar


                tiempo_computadora = int(round(time.time()*100))-current_time - start_time
                window.Element('tempo_compu').Update('{:02d}:{:02d}.{:02d}'.format((tiempo_computadora // 100) // 60,(tiempo_computadora // 100) % 60, tiempo_computadora % 100))

                if (tiempo_computadora > tiempo_max):
                    print('terminoeltiempo')
                    jugar.cambiar_turno()

            #turno del jugador
            elif jugar.get_turno()=='jugador':
                #se termino el tiempo del jugador
                if (current_time> tiempo_max):
                    sg.Popup('Termino el tiempo')
                    print('terminoeltiempo jugador') # insertat
                    jugar.cambiar_turno()
                    continue    #no sacar el continue, lo que hace es volver al while sin pasar por lo que esta abajo

                # no se termino el tiempo del jugador
                event, values = window.read(timeout=0)
                current_time = int(round(time.time() * 100))-(tiempo_computadora) - start_time  # tiempo actual - tiempo de la computadora - el momento en que empezo
                if event in tablero.listado_botones():
                    tablero.click(atril, event, window)
                elif event in atril.listado_botones():
                    atril.click(tablero, event)
                elif event == "cambiar_letras":
                    if (atril.get_cambios_atril()>0):
                        atril.cambiar_letras(fichas_jugador,window,tablero,values,fichas_jugador,jugar)
                    else:
                        sg.Popup('no hay mas cambios de atril')
                elif event in atril.listado_botones():
                    atril.click(tablero, event)

                elif event == 'vali':
                    puntaje_total = tablero.click_validar(atril, tablero, window, diccionario, puntaje_total, fichas_jugador,jugar, palabras_permitidas)
                elif event == 'Run':
                    paused = False
                    start_time = start_time + int(round(time.time() * 100)) - paused_time
                    element = window.Element('button')
                elif event == None:
                    break;

                window.Element('timer_jugador').Update('{:02d}:{:02d}.{:02d}'.format((current_time // 100) // 60, (current_time // 100) % 60, current_time % 100)) #muestro el contador
    window.Close()

    RegistroPartidas.guardar_score(nivel, nombre, puntaje_total)

if __name__ == '__main__':
    main()
