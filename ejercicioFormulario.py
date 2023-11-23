import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QHBoxLayout, \
    QCheckBox, QListView, QGridLayout, QComboBox, QFrame
from PyQt6.QtGui import QPixmap


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejercicio Formulario")
        self.setFixedSize(800, 500)

        cajaV= QVBoxLayout()
        cajaH1= QHBoxLayout()
        cajaV.addLayout(cajaH1)
        cajaH2= QHBoxLayout()
        cajaV.addLayout(cajaH2)

        cajaH1V1= QVBoxLayout()
        cajaH1.addLayout(cajaH1V1)
        cajaH1V1.setAlignment(Qt.AlignmentFlag.AlignTop)
        lblIconCd= QLabel()
        lblIconCd.setPixmap(QPixmap("iconCd.png"))
        cajaH1V1.addWidget(lblIconCd)
        chkAnimado= QCheckBox("Animado")
        cajaH1V1.addWidget(chkAnimado)


        cajaH1V2= QVBoxLayout()
        cajaH1.addLayout(cajaH1V2)
        lswLista= QListView()
        cajaH1V2.addWidget(lswLista)


        cajaH1V3= QVBoxLayout()
        cajaH1.addLayout(cajaH1V3)
        btnEngadirLista= QPushButton("Engadir a lista a reproducir")
        cajaH1V3.addWidget(btnEngadirLista)
        btnSubirLista= QPushButton("Subir na lista")
        cajaH1V3.addWidget(btnSubirLista)
        btnBaixarLista= QPushButton("Baixar na lista")
        cajaH1V3.addWidget(btnBaixarLista)
        grid = QGridLayout()
        btnSaltar= QPushButton("Saltar")
        grid.addWidget(btnSaltar)
        cmbSaltar=QComboBox()
        grid.addWidget(cmbSaltar,0,1,1,1)
        cajaH1V3.addLayout(grid)
        btnAbrirFicheiro= QPushButton("Abrir ficheiro")
        cajaH1V3.addWidget(btnAbrirFicheiro)
        btnReproducirFicheiro= QPushButton("Reproducir ficheiro")
        cajaH1V3.addWidget(btnReproducirFicheiro)
        btnGardar= QPushButton("Gardar")
        cajaH1V3.addWidget(btnGardar)
        btnEliminar= QPushButton("Eliminar")
        cajaH1V3.addWidget(btnEliminar)

        grid2 = QGridLayout()
        cajaH2.addLayout(grid2)
        lblSon= QLabel("Son:")
        lblRitmo = QLabel("Ritmo:")
        lblVolume = QLabel("Volume:")
        lblFormato = QLabel("Formato:")
        lblSaida = QLabel("Saída de audio:")
        grid2.addWidget(lblSon,0,0,1,1)
        grid2.addWidget(lblRitmo,1,0,1,1)
        grid2.addWidget(lblVolume,2,0,1,1)
        grid2.addWidget(lblFormato,3,0,1,1)
        grid2.addWidget(lblSaida,4,0,1,1)

        cajaH2V2= QVBoxLayout()
        frmReproducion= QFrame()
        frmReproducion.setLayout(cajaH2V2)
        frmReproducion.setWindowTitle("Opcións de reprodución")
        cajaH2.addWidget(frmReproducion)
        cajaH2V2C1= QVBoxLayout()
        cajaH2V2.addLayout(cajaH2V2C1)
        chkAsincrono = QCheckBox("Asíncrono")
        chkNome = QCheckBox("É nome de fichero")
        chkXml = QCheckBox("XML persistente")
        cajaH2V2C1.addWidget(chkAsincrono)
        cajaH2V2C1.addWidget(chkNome)
        cajaH2V2C1.addWidget(chkXml)

        cajaH2V2C2= QVBoxLayout()
        cajaH2V2.addLayout(cajaH2V2C2)
        chkFiltrar= QCheckBox("Filtrar antes de reproducir")
        chkXml2 = QCheckBox("É XML")
        chkNpl = QCheckBox("Reproducción NPL")
        cajaH2V2C2.addWidget(chkFiltrar)
        cajaH2V2C2.addWidget(chkXml2)
        cajaH2V2C2.addWidget(chkNpl)



        container=QWidget()
        container.setLayout(cajaV)

        self.setCentralWidget(container)


        self.show()


if __name__=="__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    aplicacion.exec()
