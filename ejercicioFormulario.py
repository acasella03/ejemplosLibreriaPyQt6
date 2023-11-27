import sys

from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel,QCheckBox,
                             QVBoxLayout, QHBoxLayout, QWidget, QListView, QLineEdit,
                             QComboBox, QGridLayout, QSlider, QFrame)
from PyQt6.QtCore import Qt, QStringListModel
from PyQt6.QtGui import QPixmap


class VentanaPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle( "Ejercicio Formulario")
        self.setFixedSize(800,400)

        caixaV = QVBoxLayout()
        caixaH1 = QHBoxLayout()
        caixaV.addLayout(caixaH1)
        caixaH2 = QHBoxLayout()
        caixaV.addLayout(caixaH2)
        caixa3 = QVBoxLayout()
        caixa3.setAlignment(Qt.AlignmentFlag.AlignTop)
        caixaH1.addLayout(caixa3)
        lblIconoCd = QLabel ()
        lblIconoCd.setPixmap(QPixmap("ico_cd.png"))
        caixa3.addWidget(lblIconoCd)
        chkAnimado = QCheckBox("Animado")
        caixa3.addWidget(chkAnimado)
        self.lswLista = QListView()
        self.lswLista.setFixedSize(300,200)
        self.modelo_lista = QStringListModel() # Crear un modelo de lista para la QListView
        self.lswLista.setModel(self.modelo_lista) # Asignar el modelo a la lista
        caixaH1.addWidget(self.lswLista)

        caixa4 = QVBoxLayout()
        caixaH1.addLayout(caixa4)
        btnEngadirLista =QPushButton("Engadir Lista a reproducir")
        caixa4.addWidget(btnEngadirLista)
        btnSubirLista = QPushButton("Subir na lista")
        caixa4.addWidget(btnSubirLista)
        btnBaixarLista = QPushButton("Baixar na lista")
        caixa4.addWidget(btnBaixarLista)
        grid = QGridLayout()
        btnSaltar = QPushButton("Saltar")
        grid.addWidget(btnSaltar)
        caixa4.addLayout(grid)
        cmbSaltar = QComboBox()
        grid.addWidget(cmbSaltar,0,1,1,2)
        btnAbrirFicheiro = QPushButton("Abrir Ficheiro...")
        caixa4.addWidget(btnAbrirFicheiro)
        btnReproducirFicheiro = QPushButton("Reproducir Ficheiro")
        caixa4.addWidget(btnReproducirFicheiro)
        btnGardar = QPushButton("Gardar como...")
        caixa4.addWidget(btnGardar)
        btnEliminarPista = QPushButton("EliminarPista")
        caixa4.addWidget(btnEliminarPista)

        grid2 = QGridLayout()
        caixaH2.addLayout(grid2)
        lblSon = QLabel("Son:")
        lblRitmo = QLabel("Ritmo:")
        lblVolume = QLabel("Volume:")
        lblFormato = QLabel("Formato:")
        lblSaida = QLabel("Saída de audio:")
        grid2.addWidget(lblSon,0,0,1,1)
        grid2.addWidget(lblRitmo, 1, 0, 1, 1)
        grid2.addWidget(lblVolume, 2, 0, 1, 1)
        grid2.addWidget(lblFormato, 3, 0, 1, 1)
        grid2.addWidget(lblSaida,4, 0, 1, 1)

        cmbSon = QComboBox()
        cmbSon.addItems(["Maracas", "Marimba", "Triángulo", "Timbales"])
        cmbSon.currentTextChanged.connect(self.text_changed)
        grid2.addWidget(cmbSon,0,1,1,2)
        sldRitmo = QSlider(Qt.Orientation.Horizontal)
        grid2.addWidget(sldRitmo, 1, 1, 1, 2)
        sldVolume = QSlider(Qt.Orientation.Horizontal)
        grid2.addWidget(sldVolume, 2, 1, 1, 2)
        cmbFormato = QComboBox()
        cmbFormato.addItems(["mp3", "wav", "wma", "ogg"])
        cmbFormato.currentTextChanged.connect(self.text_changed)
        grid2.addWidget(cmbFormato, 3, 1, 1, 2)
        cmbSaida = QComboBox()
        grid2.addWidget(cmbSaida, 4, 1, 1, 2)

        caixa5 = QHBoxLayout()
        frmOpReproduccion = QFrame()
        frmOpReproduccion.setFrameStyle(QFrame.Shape.Box)

        frmOpReproduccion.setLayout(caixa5)
        frmOpReproduccion.setWindowTitle("Opcións de reproducción")
        caixaH2.addWidget(frmOpReproduccion)
        caixa6 = QVBoxLayout()
        caixa7 = QVBoxLayout()
        caixa5.addLayout(caixa6)
        caixa5.addLayout(caixa7)
        self.chkAsincrono = QCheckBox ("Asíncrono")
        # Conectar la señal stateChanged del QCheckBox a la función correspondiente
        self.chkAsincrono.clicked.connect(self.chkAsincrono_clicked)
        self.chkENome = QCheckBox("É nome de ficheiro")
        self.chkENome.clicked.connect(self.chkENome_clicked)
        self.chkXml = QCheckBox("XML persistente")
        self.chkXml.clicked.connect(self.chkXml_clicked)
        caixa6.addWidget(self.chkAsincrono)
        caixa6.addWidget(self.chkENome)
        caixa6.addWidget(self.chkXml)

        self.chkFiltrar = QCheckBox("Filtrar antes de reproducir")
        self.chkFiltrar.clicked.connect(self.chkFiltrar_clicked)
        self.chkEXml = QCheckBox("É XML")
        self.chkEXml.clicked.connect(self.chkEXml_clicked)
        self.chkReproduccion = QCheckBox("Reproducción NPL")
        self.chkReproduccion.clicked.connect(self.chkReproduccion_clicked)
        caixa7.addWidget(self.chkFiltrar)
        caixa7.addWidget(self.chkEXml)
        caixa7.addWidget(self.chkReproduccion)

        container = QWidget()
        container.setLayout(caixaV)
        self.setCentralWidget (container)


        self.show()

    def text_changed(self,s):
        print(s)

    def chkAsincrono_clicked(self):
        # Obtener el texto del QCheckBox
        text = self.chkAsincrono.text()
        # Verificar si el QCheckBox está marcado o no
        if self.chkAsincrono.isChecked():
            # Agregar el texto al modelo de la lista
            self.modelo_lista.insertRow(self.modelo_lista.rowCount())
            index=self.modelo_lista.index(self.modelo_lista.rowCount()-1)
            self.modelo_lista.setData(index,text)
        # else:
            # Quitar el texto del modelo de la lista
            #rows_to_remove = [index for index in range(self.model.rowCount()) if
                              #self.model.data(self.model.index(index)) == text]
            #for row in reversed(rows_to_remove):
                #self.model.removeRow(row)

    def chkENome_clicked(self):
        # Obtener el texto del QCheckBox
        text = self.chkENome.text()
        # Verificar si el QCheckBox está marcado o no
        if self.chkENome.isChecked():
            # Agregar el texto al modelo de la lista
            self.modelo_lista.insertRow(self.modelo_lista.rowCount())
            index = self.modelo_lista.index(self.modelo_lista.rowCount() - 1)
            self.modelo_lista.setData(index, text)
        # else:
        # Quitar el texto del modelo de la lista
        # rows_to_remove = [index for index in range(self.model.rowCount()) if
        # self.model.data(self.model.index(index)) == text]
        # for row in reversed(rows_to_remove):
        # self.model.removeRow(row)

    def chkXml_clicked(self):
        # Obtener el texto del QCheckBox
        text = self.chkXml.text()
        # Verificar si el QCheckBox está marcado o no
        if self.chkXml.isChecked():
            # Agregar el texto al modelo de la lista
            self.modelo_lista.insertRow(self.modelo_lista.rowCount())
            index = self.modelo_lista.index(self.modelo_lista.rowCount() - 1)
            self.modelo_lista.setData(index, text)
        # else:
        # Quitar el texto del modelo de la lista
        # rows_to_remove = [index for index in range(self.model.rowCount()) if
        # self.model.data(self.model.index(index)) == text]
        # for row in reversed(rows_to_remove):
        # self.model.removeRow(row)

    def chkFiltrar_clicked(self):
        # Obtener el texto del QCheckBox
        text = self.chkFiltrar.text()
        # Verificar si el QCheckBox está marcado o no
        if self.chkFiltrar.isChecked():
            # Agregar el texto al modelo de la lista
            self.modelo_lista.insertRow(self.modelo_lista.rowCount())
            index = self.modelo_lista.index(self.modelo_lista.rowCount() - 1)
            self.modelo_lista.setData(index, text)
        # else:
        # Quitar el texto del modelo de la lista
        # rows_to_remove = [index for index in range(self.model.rowCount()) if
        # self.model.data(self.model.index(index)) == text]
        # for row in reversed(rows_to_remove):
        # self.model.removeRow(row)

    def chkEXml_clicked(self):
        # Obtener el texto del QCheckBox
        text = self.chkEXml.text()
        # Verificar si el QCheckBox está marcado o no
        if self.chkEXml.isChecked():
            # Agregar el texto al modelo de la lista
            self.modelo_lista.insertRow(self.modelo_lista.rowCount())
            index = self.modelo_lista.index(self.modelo_lista.rowCount() - 1)
            self.modelo_lista.setData(index, text)
        # else:
        # Quitar el texto del modelo de la lista
        # rows_to_remove = [index for index in range(self.model.rowCount()) if
        # self.model.data(self.model.index(index)) == text]
        # for row in reversed(rows_to_remove):
        # self.model.removeRow(row)

    def chkReproduccion_clicked(self):
        # Obtener el texto del QCheckBox
        text = self.chkReproduccion.text()
        # Verificar si el QCheckBox está marcado o no
        if self.chkReproduccion.isChecked():
            # Agregar el texto al modelo de la lista
            self.modelo_lista.insertRow(self.modelo_lista.rowCount())
            index = self.modelo_lista.index(self.modelo_lista.rowCount() - 1)
            self.modelo_lista.setData(index, text)
        # else:
        # Quitar el texto del modelo de la lista
        # rows_to_remove = [index for index in range(self.model.rowCount()) if
        # self.model.data(self.model.index(index)) == text]
        # for row in reversed(rows_to_remove):
        # self.model.removeRow(row)



if __name__=="__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    aplicacion.exec()
