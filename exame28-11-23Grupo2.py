import sys
from PyQt6.QtCore import QSize, Qt, QModelIndex
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QLabel, QListWidget, QPushButton, QComboBox, QLineEdit,
                             QRadioButton, QVBoxLayout, QGridLayout, QWidget, QHBoxLayout)



class FiestraPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exame 12-12_2022")
        self.setFixedSize(800, 400)

        self.cajaV = QVBoxLayout()

        red = QGridLayout()
        self.cajaV.addLayout(red)


        lblNome = QLabel("Nome")
        lblApelido = QLabel("Apelido")
        lblTratamento = QLabel("Tratamento")
        lblUsuario = QLabel("Usuario")
        red.addWidget(lblNome, 0, 0)
        red.addWidget(lblApelido, 2, 0)
        red.addWidget(lblTratamento, 0, 1)
        red.addWidget(lblUsuario, 2, 1)
        self.txtNome = QLineEdit()
        red.addWidget(self.txtNome, 1, 0)
        self.txtApelido = QLineEdit()
        red.addWidget(self.txtApelido, 3, 0)
        txtTratamento = QLineEdit()
        red.addWidget(txtTratamento, 1, 1)
        txtUsuario = QLineEdit()
        red.addWidget(txtUsuario, 3, 1)


        cajaH1=QHBoxLayout()
        self.cajaV.addLayout(cajaH1)
        lblFormato = QLabel("Formato")
        cajaH1.addWidget(lblFormato)
        self.cmbFormato = QComboBox()
        self.cmbFormato.addItems(["HTML","Texto Plano","Personalizado"])
        self.cmbFormato.currentTextChanged.connect(self.text_changed)
        cajaH1.addWidget(self.cmbFormato)

        cajaH2=QHBoxLayout()
        self.cajaV.addLayout(cajaH2)
        cajaV2=QVBoxLayout()
        cajaH2.addLayout(cajaV2)


        cajaH3=QHBoxLayout()
        cajaV2.addLayout(cajaH3)
        lblDireccionC = QLabel("Dirección de correo")
        cajaH3.addWidget(lblDireccionC)
        self.txtDireccionC = QLineEdit()
        cajaH3.addWidget(self.txtDireccionC)
        self.lstDireccionC = QListWidget()
        #self.lstDireccionC.setModel(self.modelo)
        #self.lstDireccionC.setSelectionMode(QListWidget.SelectionMode.SingleSelection)
        cajaV2.addWidget(self.lstDireccionC)

        cajaV3=QVBoxLayout()
        cajaH2.addLayout(cajaV3)
        red2=QGridLayout()
        cajaV3.addLayout(red2)
        self.btnEngadir = QPushButton("Engadir")
        self.btnEngadir.clicked.connect(self.on_btnEnganir_click)
        red2.addWidget(self.btnEngadir)
        btnEditar = QPushButton("Editar")
        red2.addWidget(btnEditar)
        self.btnBorrar = QPushButton("Borrar")
        self.btnBorrar.clicked.connect(self.on_btnBorrar_click)
        red2.addWidget(self.btnBorrar)
        btnPorDefecto = QPushButton("Por Defecto")
        red2.addWidget(btnPorDefecto)


        lblFormato = QLabel("Formato de correo:")
        cajaV2.addWidget(lblFormato)
        cajaH4=QHBoxLayout()
        cajaV2.addLayout(cajaH4)
        self.rbtHtml = QRadioButton("HTML")
        cajaH4.addWidget(self.rbtHtml)
        rbtTextoPlano = QRadioButton ("Texto Plano")
        cajaH4.addWidget(rbtTextoPlano)
        rbtPersonalizado = QRadioButton ("Personalizado")
        cajaH4.addWidget(rbtPersonalizado)

        cajaH5=QHBoxLayout()
        self.cajaV.addLayout(cajaH5)
        cajaH5.setAlignment(Qt.AlignmentFlag.AlignRight)
        btnAceptar = QPushButton("Aceptar")
        cajaH5.addWidget(btnAceptar)
        btnCancelar = QPushButton("Cancelar")
        cajaH5.addWidget(btnCancelar)

        container = QWidget()
        container.setLayout(self.cajaV)
        self.setCentralWidget(container)

    def on_btnEnganir_click(self):
        self.nombre = self.txtNome.text()
        self.apellido = self.txtApelido.text()
        self.email = self.txtDireccionC.text()
        self.lista = self.nombre + "," + self.apellido + "," + self.email

        self.lstDireccionC.addItems([self.lista])
        self.txtNome.setText("")
        self.txtApelido.setText("")
        self.txtDireccionC.setText("")

    def text_changed(self,s):
        print(s)

    def on_rbtHtml_click(self):
        text=self.rbtHtml.text()
        if self.rbtHtml.isChecked():
            self.cmbFormato.currentIndex()



    def on_btnBorrar_click(self):
        self.modelo= QModelIndex()




if __name__=="__main__":

    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    fiestra.show()
    aplicacion.exec()