import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QGridLayout, QLabel, QMainWindow, QWidget, QPushButton, QTabWidget

from cajaColor import CajaColor

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo QTabWidget con Qt")

        tabs= QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.South)
        tabs.setMovable(True)

        for color in ["red","green","blue","yellow"]:
            tabs.addTab(CajaColor(color),color)

        self.setCentralWidget(tabs)
        self.show()

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    sys.exit(aplicacion.exec())
