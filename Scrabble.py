import PySimpleGUI as sg
import ProgramaPrincipal
# Todavia no modifique nada es solo para que quede esto que va a ser la clase principal. (no ProgramaPrincipal)-agus

layout = [[ sg.Text('Scrabble'),],
          [sg.Text('', key='_OUTPUT_')],
          [sg.Button('JUGAR!')]]

win1 = sg.Window('Window 1', layout)
win2_active=False
while True:
    ev1, vals1 = win1.Read(timeout=100)
    if ev1 is None:
        break

    if ev1 == 'JUGAR!'  and not win2_active:
        ProgramaPrincipal.main()
        win2_active = True
        win1.Hide()
        layout2 = [[sg.Text('Window 2')],       # note must create a layout from scratch every time. No reuse
        [sg.Button('Exit')]]

        win2 = sg.Window('Window 2', layout2)
        while True:
            ev2, vals2 = win2.Read()
            if ev2 is None or ev2 == 'Exit':
                win2.Close()
                win2_active = False
                break
