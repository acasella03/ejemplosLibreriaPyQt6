import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QPixmap


class PrimeraVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi primera ventana con Qt")

        self.lblEtiqueta1 = QLabel("Hola a los presentes")
        lblEtiqueta2 = QLabel()
        lblEtiqueta2.setPixmap(QPixmap("gatito.png"))
        btnSaludo=QPushButton("Saludo")
        btnSaludo.clicked.connect(self.on_btnSaludo_clicked)

        cajaV=QVBoxLayout()
        cajaV.addWidget(self.lblEtiqueta1)
        cajaV.addWidget(lblEtiqueta2)
        cajaV.addWidget(btnSaludo)

        container=QWidget()
        container.setLayout(cajaV)

        self.setCentralWidget(container)

        self.setFixedSize(400, 300)
        self.show()

    def on_btnSaludo_clicked(self):
        self.lblEtiqueta1.setText("Hola, Hola!!!!!!")

if __name__=="__main__":
    aplicacion = QApplication(sys.argv)
    ventana = PrimeraVentana()
    aplicacion.exec()
