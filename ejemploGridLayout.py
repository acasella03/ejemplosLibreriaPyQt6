import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QGridLayout, QLabel, QMainWindow, QWidget, QPushButton

from cajaColor import CajaColor

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo Grid Layout con Qt")

        red= QGridLayout()

        red.addWidget(CajaColor("red"))
        red.addWidget(CajaColor("blue"),0,1,1,2)
        red.addWidget(CajaColor("Green"),1,0,2,1)
        red.addWidget(CajaColor("pink"),1,1,1,2)
        red.addWidget(CajaColor("orange"),2,1,1,1)
        red.addWidget(CajaColor("yellow"),2,2,1,1)

        control=QWidget()
        control.setLayout(red)
        self.setCentralWidget(control)
        self.show()

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    sys.exit(aplicacion.exec())

