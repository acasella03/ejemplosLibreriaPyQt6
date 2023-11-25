import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo QVBoxLayout y QPushButton con Qt")

        # Creamos un widget central
        container = QWidget()

        # Creamos los botones
        button1 = QPushButton('Botón 1')
        button2 = QPushButton('Botón 2')
        button3 = QPushButton('Botón 3')
        button4 = QPushButton('Botón 4')
        button5 = QPushButton('Botón 5')
        button6 = QPushButton('Botón 6')

        # Creamos un layout vertical
        cajaV=QVBoxLayout()

        # Agregamos los botones al layout
        cajaV.addWidget(button1)
        cajaV.addWidget(button2)
        cajaV.addWidget(button3)
        cajaV.addWidget(button4)
        cajaV.addWidget(button5)
        cajaV.addWidget(button6)

        # Establecemos el layout en el widget central
        container.setLayout(cajaV)

        # Establecemos el widget central en la QMainWindow
        self.setCentralWidget(container)


if __name__=="__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(aplicacion.exec())