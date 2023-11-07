import sys

from PyQt6.QtWidgets import (QApplication, QMainWindow, QCheckBox, QVBoxLayout, QWidget)
from PyQt6.QtCore import Qt


class SegundaVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo con QCheckBox y QRadioButton")

        cajaV = QVBoxLayout()

        self.chkBoton1 = QCheckBox("Botón 1")
        self.chkBoton1.toggled.connect(self.on_chkBoton1_toggled)
        cajaV.addWidget(self.chkBoton1)

        self.chkBoton2 = QCheckBox("Botón 2")
        self.chkBoton2.toggled.connect(self.on_chkBoton2_toggled)
        cajaV.addWidget(self.chkBoton2)

        container = QWidget()
        container.setLayout(cajaV)

        self.setCentralWidget(container)

        self.setFixedSize(400, 300)
        self.show()

    def on_chkBoton1_toggled(self):
        if self.chkBoton1.isChecked():
            print("Botón check activado: ", self.chkBoton1.text())
        else:
            print("Botón check desactivado: ", self.chkBoton1.text())

    def on_chkBoton2_toggled(self):
        if self.chkBoton2.isChecked():
            print("Botón check activado: ", self.chkBoton2.text())
        else:
            print("Botón check desactivado: ", self.chkBoton2.text())


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = SegundaVentana()
    aplicacion.exec()
