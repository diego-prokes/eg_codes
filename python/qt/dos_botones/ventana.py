from ventana_ui import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        # Se edita la interfaz
        self.label.setText("Haz click en un botón")
        self.btn_1.setText("1")
        self.btn_2.setText("2")

        # Conectamos los eventos con sus acciones
        self.btn_1.clicked.connect(self.actualizar1)
        self.btn_2.clicked.connect(self.actualizar2)


    def actualizar1(self):
        self.label.setText(str(1))
    
    def actualizar2(self):
        self.label.setText(str(2))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()