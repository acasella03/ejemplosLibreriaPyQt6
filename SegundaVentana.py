import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit
from PyQt6.QtCore import Qt


class SegundaVentana(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi segunda ventana con Qt")

        self.txtSaludo = QLineEdit()

        self.lblEtiqueta1 = QLabel("Hola a los presentes")
        fuente= self.lblEtiqueta1.font()
        fuente.setPointSize(30)
        self.lblEtiqueta1.setFont(fuente)
        self.lblEtiqueta1.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        btnSaludo=QPushButton("Saludo")
        btnSaludo.clicked.connect(self.on_btnSaludo_clicked)
        #self.txtSaludo.editingFinished.connect(self.on_btnSaludo_clicked)
        self.txtSaludo.returnPressed.connect(self.on_btnSaludo_clicked) #sirve con returnPressed y con el anterior editingFinished

        cajaV=QVBoxLayout()
        cajaV.addWidget(self.lblEtiqueta1)
        cajaV.addWidget(self.txtSaludo)
        cajaV.addWidget(btnSaludo)

        container=QWidget()
        container.setLayout(cajaV)

        self.setCentralWidget(container)

        self.setFixedSize(400, 300)
        self.show()

    def on_btnSaludo_clicked(self):
        saludo=self.txtSaludo.text()
        self.lblEtiqueta1.setText(saludo)

if __name__=="__main__":
    aplicacion = QApplication(sys.argv)
    ventana = SegundaVentana()
    aplicacion.exec()