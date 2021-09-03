from ci_ui import *
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtGui
from datetime import date, timedelta
import random

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self,*args,**kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.btn_generar.clicked.connect(self.createCarnet)
    

    def createCarnet(self):
        apellidos = self.le_apellidos.text()
        nombres = self.le_nombres.text()
        nacionalidad = self.le_nacionalidad.text()
        fechaNacimiento = self.makeDate('fechaNacimiento')
        fechaEmision = self.makeDate('fechaEmision')
        sexo = self.cb_sexo.currentText()
        numeroDocumento = str(int(random.random()*1000000000))
        fechaVencimiento = self.makeDate('fechaVencimiento')

        self.lb_d_apellidos.setText("APELLIDOS\n"+apellidos)
        self.lb_d_nombres.setText("NOMBRES\n"+nombres)
        self.lb_d_nacionalidad.setText("NACIONALIDAD\n"+nacionalidad)
        self.lb_d_fecha_nacimiento.setText("FECHA DE NACIMIENTO\n"+fechaNacimiento)
        self.lb_d_fecha_emision.setText("FECHA DE EMISION\n"+fechaEmision)
        self.lb_d_sexo.setText("SEXO\n"+sexo)
        self.lb_d_numero_documento.setText("NÚMERO DOCUMENTO\n"+numeroDocumento)
        self.lb_d_fecha_vencimiento.setText("FECHA DE VENCIMIENTO\n"+fechaVencimiento)



        pass

    def makeDate(self, tipo):
        if(tipo == 'fechaNacimiento'):
            dia = self.sp_fn_dia.text()
            mes = self.sp_fn_mes.text()
            anio = self.sp_fn_anio.text()
        elif(tipo == 'fechaEmision'):
            hoy = date.today()
            dia = str(hoy.day)
            mes = str(hoy.month)
            anio = str(hoy.year)
        elif(tipo == 'fechaVencimiento'):
            hoy = date.today()
            tenYear = timedelta(days = 365*10)
            vencimiento = hoy + tenYear
            dia = str(vencimiento.day)
            mes = str(vencimiento.month)
            anio = str(vencimiento.year)
        fecha = " - ".join([dia,mes,anio])
        return fecha
        

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()