import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QCheckBox, QRadioButton


class VentanaPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle( "Ejemplo con QCheckBox y QRadioButton")

        cajaV = QVBoxLayout()

        self.chkBoton1 = QCheckBox ("Boton 1")
        self.chkBoton1.toggled.connect(self.on_chkBoton1_toggled)
        cajaV.addWidget(self.chkBoton1)

        self.chkBoton2 = QCheckBox ("Boton 2")
        self.chkBoton2.toggled.connect (self.on_chkBoton2_toggled)
        cajaV.addWidget(self.chkBoton2)


        cajaV2 = QVBoxLayout()
        containerV2 = QWidget()
        containerV2.setLayout(cajaV2)
        cajaV.addWidget(containerV2)

        self.rbtRadioButton1 = QRadioButton("Opción 1", containerV2)
        self.rbtRadioButton1.toggled.connect (self.on_rbtRadioButton1_toggled)
        cajaV2.addWidget(self.rbtRadioButton1)

        self.rbtRadioButton2 = QRadioButton("Opción 2", containerV2)
        self.rbtRadioButton2.toggled.connect(self.on_rbtRadioButton2_toggled)
        cajaV2.addWidget(self.rbtRadioButton2)

        self.rbtRadioButton3 = QRadioButton("Opción 3", containerV2)
        self.rbtRadioButton3.toggled.connect(self.on_rbtRadioButton3_toggled)
        cajaV2.addWidget(self.rbtRadioButton3)

        cajaV3 = QVBoxLayout()
        cajaV.addLayout(cajaV3)

        self.rbtRadioButton4 = QRadioButton("Opción 1 Grupo 2")
        self.rbtRadioButton4.toggled.connect(self.on_rbtRadioButton1_toggled)
        cajaV3.addWidget(self.rbtRadioButton4)

        self.rbtRadioButton5 = QRadioButton("Opción 2 Grupo 2")
        self.rbtRadioButton5.toggled.connect(self.on_rbtRadioButton2_toggled)
        cajaV3.addWidget(self.rbtRadioButton5)

        self.rbtRadioButton6 = QRadioButton("Opción 3 Grupo 2")
        self.rbtRadioButton6.toggled.connect(self.on_rbtRadioButton3_toggled)
        cajaV3.addWidget(self.rbtRadioButton6)




        container = QWidget()
        container.setLayout(cajaV)
        self.setCentralWidget(container)

        self.setFixedSize(400,300)
        self.show()

    def on_btnSaludo_clicked(self):
        saludo = self.txtSaludo.text()
        self.lblEtiqueta1.setText(saludo)


    def on_chkBoton1_toggled(self):
        if self.chkBoton1.isChecked():
            print ("Boton check seleccionado: ", self.chkBoton1.text())
        else:
            print("Boton check deseleccionado: ", self.chkBoton1.text())

    def on_chkBoton2_toggled(self):
        if self.chkBoton2.isChecked():
            print ("boton check seleccionado: ", self.chkBoton2.text())
        else:
            print("Boton check deseleccionado: ", self.chkBoton2.text())


    def on_rbtRadioButton1_toggled(self):
        if self.rbtRadioButton1.isChecked():
            print ("Boton check seleccionado: ", self.rbtRadioButton1.text())
        else:
            print("Boton check deseleccionado: ", self.rbtRadioButton1.text())


    def on_rbtRadioButton2_toggled(self):
        if self.rbtRadioButton2.isChecked():
            print ("Boton check seleccionado: ", self.rbtRadioButton2.text())
        else:
            print("Boton check deseleccionado: ", self.rbtRadioButton2.text())


    def on_rbtRadioButton3_toggled(self):
        if self.rbtRadioButton3.isChecked():
            print ("Boton check seleccionado: ", self.rbtRadioButton3.text())
        else:
            print("Boton check deseleccionado: ", self.rbtRadioButton3.text())

if __name__=="__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    aplicacion.exec()