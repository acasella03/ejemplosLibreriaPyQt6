import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QLabel, QListWidget, QPushButton, QComboBox, QLineEdit,
                             QRadioButton, QVBoxLayout, QHBoxLayout, QWidget, QGridLayout)



class FiestraPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exame 12-12_2022")
        self.setFixedSize(800, 400)

        self.cajaV=QVBoxLayout()

        red = QGridLayout()
        self.cajaV.addLayout(red)

        lblNome = QLabel("Nome")
        lblApelido = QLabel("Apelido")
        lblTratamento = QLabel("Tratamento")
        lblTelefono = QLabel("Teléfono")
        red.addWidget(lblNome,0,0)
        red.addWidget(lblApelido,0,2)
        red.addWidget(lblTratamento,1,0)
        red.addWidget(lblTelefono,1,2)
        self.txtNome = QLineEdit()
        red.addWidget(self.txtNome,0,1)
        self.txtApelido = QLineEdit()
        red.addWidget(self.txtApelido,0,3)
        self.txtTratamento = QLineEdit()
        red.addWidget(self.txtTratamento,1,1)
        self.txtTelefono = QLineEdit()
        red.addWidget(self.txtTelefono,1,3)
        lblFormato = QLabel("Formato")
        red.addWidget(lblFormato,2,0)
        cmbFormato = QComboBox()
        red.addWidget(cmbFormato,2,1,1,3)

        cajaH1 = QHBoxLayout()
        self.cajaV.addLayout(cajaH1)
        self.lstDireccionC = QListWidget()
        cajaH1.addWidget(self.lstDireccionC)

        cajaV1= QVBoxLayout()
        cajaH1.addLayout(cajaV1)
        cajaV1.setAlignment(Qt.AlignmentFlag.AlignTop)
        lblFormato = QLabel("Formato de correo:")
        cajaV1.addWidget(lblFormato)
        self.rbtHtml = QRadioButton("HTML")
        self.rbtHtml.toggled.connect(self.on_rbtHtml_toggled)
        cajaV1.addWidget(self.rbtHtml)
        self.rbtTextoPlano = QRadioButton("Texto Plano")
        self.rbtTextoPlano.toggled.connect(self.on_rbtTextoPlano_toggled)
        cajaV1.addWidget(self.rbtTextoPlano)
        self.rbtPersonalizado = QRadioButton("Personalizado")
        self.rbtPersonalizado.toggled.connect(self.on_rbtPersonalizado_toggled)
        cajaV1.addWidget(self.rbtPersonalizado)

        cajaH2 = QHBoxLayout()
        self.cajaV.addLayout(cajaH2)
        lblDireccionC = QLabel("Dirección de correo")
        cajaH2.addWidget(lblDireccionC)
        txtDireccionC = QLineEdit()
        cajaH2.addWidget(txtDireccionC)

        red2=QGridLayout()
        self.cajaV.addLayout(red2)
        self.btnEngadir = QPushButton("Engadir")
        self.btnEngadir.clicked.connect(self.on_btnEnganir_click)
        red2.addWidget(self.btnEngadir,0,0)
        btnEditar = QPushButton("Editar")
        red2.addWidget(btnEditar,0,1)
        btnBorrar = QPushButton("Borrar")
        red2.addWidget(btnBorrar,0,3)
        btnPorDefecto = QPushButton("Por Defecto")
        red2.addWidget(btnPorDefecto,0,4)

        btnAceptar = QPushButton("Aceptar")
        red2.addWidget(btnAceptar,1,3)
        self.btnCancelar = QPushButton("Cancelar")
        red2.addWidget(self.btnCancelar,1,4)
        self.btnCancelar.clicked.connect(self.on_btnCancelar_click)

        container = QWidget()
        container.setLayout(self.cajaV)
        self.setCentralWidget(container)

    def on_rbtHtml_toggled(self):
        if self.rbtHtml.isChecked():
            print("RadioButton selecccionado: ", self.rbtHtml.text())
        else:
            print("RadioButton deseleccinado: ", self.rbtHtml.text())

    def on_rbtTextoPlano_toggled(self):
        if self.rbtTextoPlano.isChecked():
            print("RadioButton selecccionado: ", self.rbtTextoPlano.text())
        else:
            print("RadioButton deseleccinado: ", self.rbtTextoPlano.text())

    def on_rbtPersonalizado_toggled(self):
        if self.rbtPersonalizado.isChecked():
            print("RadioButton selecccionado: ", self.rbtPersonalizado.text())
        else:
            print("RadioButton deseleccinado: ", self.rbtPersonalizado.text())

    def on_btnEnganir_click(self):
        self.nombre= self.txtNome.text()
        self.apellido=self.txtApelido.text()
        self.telefono=self.txtTelefono.text()
        self.lista= self.nombre+","+self.apellido+","+self.telefono

        self.lstDireccionC.addItems([self.lista])
        self.txtNome.setText("")
        self.txtApelido.setText("")
        self.txtTelefono.setText("")

    def on_btnCancelar_click(self):
        ventana=self.cajaV
        ventana.exit()

if __name__=="__main__":

    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    fiestra.show()
    aplicacion.exec()