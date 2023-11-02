import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QPushButton,
                             QVBoxLayout, QMainWindow, QWidget, QStackedLayout)

from cajaColor import CajaColor

class GridConContenido(QGridLayout):
    def __init__(self):
        super().__init__()
        self.addWidget(CajaColor("red"))
        self.addWidget(CajaColor("blue"), 0, 1, 1, 2)
        self.addWidget(CajaColor("Green"), 1, 0, 2, 1)
        self.addWidget(CajaColor("pink"), 1, 1, 1, 2)
        self.addWidget(CajaColor("orange"), 2, 1, 1, 1)
        self.addWidget(CajaColor("yellow"), 2, 2, 1, 1)

class HBoxModificado (QHBoxLayout):
    def __init__(self):
        super().__init__()

        caja2 = QVBoxLayout()
        caja3 = QVBoxLayout()

        caja2.addWidget(CajaColor("red"))
        caja2.addWidget(CajaColor("yellow"))
        caja2.addWidget(CajaColor("purple"))
        self.addLayout(caja2)

        self.addWidget(CajaColor("green"))

        caja3.addWidget(CajaColor ("blue"))
        caja3.addWidget(CajaColor ("orange"))
        self.addLayout(caja3)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo QStacked Layout con Qt")

        cajaV = QVBoxLayout()
        cajaBotones = QHBoxLayout()
        cajaV.addLayout(cajaBotones)
        self.tarjetas = QStackedLayout()
        cajaV.addLayout(self.tarjetas)

        btnRojo=QPushButton("Rojo")
        btnRojo.pressed.connect(self.on_btnRojo_pressed)
        cajaBotones.addWidget(btnRojo)

        btnAzul = QPushButton("Azul")
        btnAzul.pressed.connect(self.on_btnAzul_pressed)
        cajaBotones.addWidget(btnAzul)

        btnVerde = QPushButton("Verde")
        btnVerde.pressed.connect(self.on_btnVerde_pressed)
        cajaBotones.addWidget(btnVerde)

        btnMalla = QPushButton("Malla")
        btnMalla.pressed.connect(self.on_btnMalla_pressed)
        cajaBotones.addWidget(btnMalla)

        btnBModificado = QPushButton("Box modificado")
        btnBModificado.pressed.connect(self.on_btnBModificado_pressed)
        cajaBotones.addWidget(btnBModificado)

        self.tarjetas.addWidget(CajaColor("red"))
        self.tarjetas.addWidget(CajaColor("blue"))
        self.tarjetas.addWidget(CajaColor("green"))
        widgedGrid=QWidget()
        widgedGrid.setLayout(GridConContenido())
        self.tarjetas.addWidget(widgedGrid)
        widgedBox = QWidget()
        widgedBox.setLayout(HBoxModificado())
        self.tarjetas.addWidget(widgedBox)
        self.tarjetas.setCurrentIndex(1)

        control = QWidget()
        control.setLayout(cajaV)
        self.setCentralWidget(control)
        self.show()

    def on_btnRojo_pressed(self):
        self.tarjetas.setCurrentIndex(0)

    def on_btnAzul_pressed(self):
        self.tarjetas.setCurrentIndex(1)

    def on_btnVerde_pressed(self):
        self.tarjetas.setCurrentIndex(2)

    def on_btnMalla_pressed(self):
        self.tarjetas.setCurrentIndex(3)

    def on_btnBModificado_pressed(self):
        self.tarjetas.setCurrentIndex(4)


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    sys.exit(aplicacion.exec())
