import sys

from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout


class CajaColor(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(paleta)


class CuartaVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplicación con Box con Qt")

        contenedorPrincipal = QHBoxLayout()
        caja2 = QVBoxLayout()
        caja3 = QVBoxLayout()

        caja2.addWidget(CajaColor("red"))
        caja2.addWidget(CajaColor("yellow"))
        caja2.addWidget(CajaColor("purple"))
        contenedorPrincipal.addLayout(caja2)

        contenedorPrincipal.addWidget(CajaColor("green"))

        caja3.addWidget(CajaColor("blue"))
        caja3.addWidget(CajaColor("orange"))
        contenedorPrincipal.addLayout(caja3)

        widgetPrincipal = QWidget()
        widgetPrincipal.setLayout(contenedorPrincipal)
        self.setCentralWidget(widgetPrincipal)


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = CuartaVentana()
    ventana.show()
    sys.exit(aplicacion.exec())
