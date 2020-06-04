import random

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




    def jugar_computadora(self, tablero,atril):
        # bloquear_tablero
        #iniciar contador
        #bloquear atril
        #buscar_palabra
        #colocar palabra
        #rellenar atril--- si me quedo sin letras pasar turno
        #detener_contador
        # si no pase turno
            #desbloquear tablero
            #desbloquear atril
        pass
