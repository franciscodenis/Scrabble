def mostrarModo():
    pass

import PySimpleGUI as sg
import Tablero
import Atril
import Casilla
import Fichas
def main():
    filas = 15
    columnas = 15
    tablero = Tablero.Tablero(filas,columnas)

    atril = Atril.Atril(5)
    fichas_jugador= Fichas.crear_bolsa_de_fichas()
    atril.agregar_letras(fichas_jugador)
    puntaje_total = 0 # Debería estar en la clase jugador
    letter_atril = { 'size' : (3, 2), 'pad' : (0,0), 'button_color' : ('white', '#C8C652')}
    layout= tablero.crear_tablero('principiante')
    layout.append([sg.Text('Seleccione una letra de abajo', auto_size_text=True, font='Helvetica', background_color=('#5CA2A3'))])
    layout.append([sg.Button(key=(-1, i) , button_text= atril.get_espacio_fichas()[i].get_letra(), **letter_atril) for i in range(5)])
    botones = [sg.Button(key='vali', button_text='Validar', button_color=('white', '#C54F1F'), font='Helvetica'),sg.Button(button_text='Cambiar letras',key ="cambiar_letras", button_color=('white', '#C54F1F'), font='Helvetica'), sg.Text('Puntaje total: ', font='Helvetica', background_color=('#5CA2A3')), sg.Text('0', key='punt', font='Helvetica', background_color=('#5CA2A3'))]
    layout.append(botones)

    window = sg.Window('Scrabble', background_color='#5CA2A3').Layout(layout)

    while True:
        event, values = window.Read()

        if event in tablero.listado_botones():
            tablero.click(atril, event, window)


        if event ==  "cambiar_letras":
            if atril.get_cambios_atril()>0 and len(fichas_jugador)>7:
                atril.cambiar_letras(fichas_jugador,window,tablero)
            else:
                if(atril.get_cambios_atril()<1):
                    sg.Popup('no tienes mas cambios')

        if event in atril.listado_botones():
            refresh = atril.click(tablero, event)
            #window.Element(event).Update(refresh)
        if event == 'vali':
            ToF = tablero.validar_pal()
            if(ToF[0] == True):
                puntaje_total = puntaje_total + ToF[1]
                print('Palabra correcta su puntaje por la palabra: ', ToF[1])
                window.Element('punt').Update(puntaje_total)
                atril.llenar_atril(fichas_jugador) #no pude probar el llenar atril
                atril.refrescar_atril(window)
                tablero.get_coordenadasActivas().clear() #libera la lista de coordenadas activas para que me tome las coordenadas mini y max correcta
            else:
                print('Palabra incorrecta, se le devolvera las fichas')
                atril.devolver_fallo(window, tablero) #Devuelve las letras del tablero al atril(falta pulir)
                tablero.get_coordenadasActivas().clear() #libera la lista de coordenadas activas para que me tome las coordenadas mini y max correcta
            tablero.desbloquear_tablero() #desbloquea el tablero
        if event in (None, 'Exit'):
            break
if __name__ == '__main__':
    main()
