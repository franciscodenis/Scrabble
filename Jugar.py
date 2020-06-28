import random
import PySimpleGUI as sg

class Jugar :


    def __init__(self):
        self.set_turno(self.seleccionar_turno())


    # _____________________Setters y GETTERS

    def set_intentos(self, intento):
        self.__intentos= intento
    def get_intentos(self, intentos):
        return self.__intentos
    def set_turno(self, turno):
        self.__turno= turno
    def get_turno(self):
        return self.__turno



    def cambiar_turno(self):
        if(self.get_turno()== 'computadora'):
            self.set_turno('jugador')
        else:
            self.set_turno('computadora')
    def seleccionar_turno(self):

        turno=random.choice(['computadora','jugador'])
        return turno

    def mostrar_dificultad(self, dificultad, tipo ):

        if dificultad=='dificultad_maxima':
            diccionario= dict(NN='sustantivos', JJ='adjetivos', VB='verbos')
            text= 'Usted eligio la dificultad maxima.\n  Debe jugar con ' + diccionario[tipo[0]]
            sg.popup(text)

    def mostrar_modos(self, dificultad, tipo, minutos_partida, minutos_ronda,restantes):

        '''muestra modo de juego'''
        diccionario_dificultad={}
        diccionario_dificultad= {'dificultad_media':' MEDIA', 'dificultad_facil':'FACIL', 'dificultad_maxima':'MAXIMA'}
        diccionario = dict(NN='SUSTANTIVOS', JJ='ADJETIVOS', VB='VERBOS ')
        string =' '
        for texto in tipo:
            string= string +diccionario[texto] +' '


        texto=(''' DIFICULTAD:'''+diccionario_dificultad[dificultad]+'''
        
            
    ----------USTED PUEDE INGRESAR----------
            '''+string+'''
    MINUTOS DE PARTIDA:'''+ str(minutos_partida)+'''
                    
    MINUTOS DE RONDA :'''+ str(minutos_ronda) +'''
     
     RESTAN:'''+ str(restantes)+ 'min')
        sg.popup(texto, title='Modo de juego')
