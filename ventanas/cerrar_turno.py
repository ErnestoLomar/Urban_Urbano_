##########################################
# Autor: Ernesto Lomar
# Fecha de creación: 12/04/2022
# Ultima modificación: 13/08/2022
#
# Script de la ventana turno.
#
##########################################

#Librerías externas
from PyQt5 import uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from queries import obtener_datos_aforo
from chofer import VentanaChofer
import logging
import RPi.GPIO as GPIO

#Librerías propias
import variables_globales
from variables_globales import VentanaActual

try:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(33, GPIO.OUT)
except Exception as e:
    print("No se pudo inicializar el ventilador: "+str(e))

class CerrarTurno(QWidget):
    close_signal = pyqtSignal()
    def __init__(self):
        super().__init__()
        try:
            uic.loadUi("/home/pi/Urban_Urbano/ui/cerrarturno.ui", self)

            #Realizamos configuración de la ventana turno.
            self.setGeometry(0, 0, 800, 440)
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.label_cancel.mousePressEvent = self.cancelar
            self.label_fin.mousePressEvent = self.cerrar_turno
            self.label_cambiar_ruta.mousePressEvent = self.cambiar_ruta
            self.idUnidad = str(obtener_datos_aforo()[1])
            self.settings = QSettings('/home/pi/Urban_Urbano/ventanas/settings.ini', QSettings.IniFormat)
        except Exception as e:
            print(e)
            logging.info(f"Error al cargar la ventana de turno: {e}")

    #Función para cancelar el turno.
    def cancelar(self, event):
        try:
            self.settings.setValue('ventana_actual', "enviar_vuelta")
            self.close()
        except Exception as e:
            print(e)
            logging.info(f"Error al cancelar el turno: {e}")
    
    #Función para cerrar la ventana de turno.
    def cerrar_turno(self, event):
        try:
            self.close()
            self.close_signal.emit()
            variables_globales.ventana_actual = VentanaActual.CHOFER
            self.settings.setValue('servicio', "")
            self.settings.setValue('ventana_actual', "")
            self.settings.setValue('csn_chofer', "")
            GPIO.output(33, False)
        except Exception as e:
            print(e)
            logging.info(f"Error al cerrar el turno: {e}")

    def cambiar_ruta(self, event):
        try:
            self.close()
            self.close_signal.emit()
            self.settings.setValue('ventana_actual', "")
            from abrir_ventanas import AbrirVentanas
            variables_globales.ventana_actual = VentanaActual.CHOFER
            self.registrar_usuario = VentanaChofer(AbrirVentanas.cerrar_vuelta.close_signal, AbrirVentanas.cerrar_vuelta.close_signal_pasaje)
            self.registrar_usuario.show()
            self.settings.setValue('servicio', "")
        except Exception as e:
            print(e)
            logging.info(f"Error al cambiar la ruta: {e}")

    def cargar_datos(self):
        try:
            self.settings.setValue('ventana_actual', "cerrar_turno")
            self.label_head.setText(f"{self.idUnidad} {str(self.settings.value('servicio')[6:])}")
            self.label_vuelta.setText(f"Vuelta {str(self.settings.value('vuelta'))}")
            self.label_total_a_liquidar.setText(self.settings.value('total_a_liquidar'))
        except Exception as e:
            print(e)
            logging.info(f"Error al cargar los datos: {e}")