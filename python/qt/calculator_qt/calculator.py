from calculator_ui import *
from PyQt5.QtWidgets import QMainWindow, QApplication


class MainWindow(QMainWindow ,Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setWindowTitle("Calculadora")
        
        # acciones 
            # self.btn_0.clicked.connect(self.add_chr(self.btn_0.text())) # ERROR
            # no sé por qué puedo mandar info con la expresión lambda
        self.btn_0.clicked.connect(lambda: self.add_chr(self.btn_0.text()))
        self.btn_1.clicked.connect(lambda: self.add_chr(self.btn_1.text()))
        self.btn_2.clicked.connect(lambda: self.add_chr(self.btn_2.text()))
        self.btn_3.clicked.connect(lambda: self.add_chr(self.btn_3.text()))
        self.btn_4.clicked.connect(lambda: self.add_chr(self.btn_4.text()))
        self.btn_5.clicked.connect(lambda: self.add_chr(self.btn_5.text()))
        self.btn_6.clicked.connect(lambda: self.add_chr(self.btn_6.text()))
        self.btn_7.clicked.connect(lambda: self.add_chr(self.btn_7.text()))
        self.btn_8.clicked.connect(lambda: self.add_chr(self.btn_8.text()))
        self.btn_9.clicked.connect(lambda: self.add_chr(self.btn_9.text()))
        self.btn_suma.clicked.connect(lambda: self.add_chr(self.btn_suma.text()))
        self.btn_resta.clicked.connect(lambda: self.add_chr(self.btn_resta.text()))
        self.btn_multiplicacion.clicked.connect(lambda: self.add_chr(self.btn_multiplicacion.text()))
        self.btn_division.clicked.connect(lambda: self.add_chr(self.btn_division.text()))
        self.btn_division_entera.clicked.connect(lambda: self.add_chr(self.btn_division_entera.text()))
        self.btn_modulo.clicked.connect(lambda: self.add_chr(self.btn_modulo.text()))
        self.btn_abre_parentesis.clicked.connect(lambda: self.add_chr(self.btn_abre_parentesis.text()))
        self.btn_cierra_parentesis.clicked.connect(lambda: self.add_chr(self.btn_cierra_parentesis.text()))
        self.btn_igual.clicked.connect(self.display_igual)
        self.btn_ac.clicked.connect(self.erase_all)

    # agrega caracteres a la label de operaciones
    def add_chr(self, caracter):
        self.operacion += str(caracter)
        self.equal_btn_update_enabled()
        self.lb_operacion.setText(self.operacion)
    # actualiza la habilitación del botón igual
    def equal_btn_update_enabled(self):
        isValidOperation = True
        try:
            eval(self.operacion)
        except:
            isValidOperation = False
        if(isValidOperation):
            self.btn_igual.setEnabled(True)
        else:
            self.btn_igual.setEnabled(False)
    # reinicia la calculadora
    def erase_all(self):
        self.operacion = ''
        self.lb_operacion.setText(self.operacion)
        self.lcd_resultado.display(0)
    # despliega el resultado de las operaciones en el lcd_resultado
    def display_igual(self):
        resultado = eval(self.operacion)
        self.lcd_resultado.display(resultado)
    
    # variables
    operacion = ''

class Funciones():
    # comprueba si un caracter es un numero
    def isNum(caracter):
        isNum = True
        try:
            int(caracter)
        except:
            isNum = False
        return(isNum)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()