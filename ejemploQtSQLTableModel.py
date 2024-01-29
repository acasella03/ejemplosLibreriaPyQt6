import sys

from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QComboBox,
                             QWidget, QCheckBox, QHBoxLayout, QLineEdit, QTableView)
from PyQt6.QtCore import Qt, QAbstractTableModel,QSize
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQueryModel, QSqlQuery

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        # Inicializa la clase base QMainWindow
        super().__init__()
        self.setWindowTitle("Ejemplo SqlQTableModel con Qt") # Establece el título de la ventana

        baseDatos = QSqlDatabase ("QSQLITE") # Creación de la base de datos
        baseDatos.setDatabaseName("baseDatos2.dat") # Establece el nombre de la base de datos
        baseDatos.open() # Abre la base de datos

        cajaV= QVBoxLayout() # Creación de la caja vertical

        self.tabla= QTableView() # Creación de la vista de la tabla
        self.modelo= QSqlTableModel(db=baseDatos) # Creación del modelo de la tabla
        cajaV.addWidget(self.tabla) # Añade la vista de la tabla a la caja vertical
        self.modelo.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange) # Establece la estrategia de edición de la tabla para que se actualice al cambiar el valor de un campo
        # self.modelo.setEditStrategy(QSqlTableModel.EditStrategy.OnRowChange)
        # self.modelo.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)
        self.tabla.setModel(self.modelo) # Establece el modelo de la tabla

        self.modelo.setTable("usuarios") # Establece la tabla de la base de datos
        self.modelo.select() # Selecciona los datos de la tabla

        container = QWidget() # Creación del widget contenedor
        container.setLayout(cajaV) # Establece la caja vertical como diseño del widget contenedor
        self.setCentralWidget(container) # Establece el widget contenedor como widget central de la ventana

        cajaH = QHBoxLayout()  # Creación de la caja horizontal
        cajaV.addLayout(cajaH) # Añade la caja horizontal a la caja vertical
        self.botonAceptar = QPushButton("Aceptar") # Creación del botón Aceptar
        self.botonCancelar = QPushButton("Cancelar") # Creación del botón Borrar
        # añadir los botones a la caja horizontal
        cajaH.addWidget(self.botonAceptar) # Añade el botón Aceptar a la caja horizontal
        cajaH.addWidget(self.botonCancelar) # Añade el botón Borrar a la caja horizontal
        # Conexión de los botones con sus funciones
        self.botonAceptar.clicked.connect(self.on_botonAceptar_clicked) # Conexión del botón Aceptar con la función on_botonAceptar_clicked
        self.botonCancelar.clicked.connect(self.on_botonCancelar_clicked) # Conexión del botón Cancelar con la función on_botonCancelar_clicked

        # Configuración del tamaño fijo de la ventana y visualización
        self.setMinimumSize(500, 300)
        self.show()

    def on_botonAceptar_clicked(self): # Función que se ejecuta al pulsar el botón Aceptar
        self.modelo.submitAll() # Envía los cambios al modelo

    def on_botonCancelar_clicked(self): # Función que se ejecuta al pulsar el botón Cancelar
        self.modelo.revertAll() # Revierte los cambios del modelo

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    aplicacion.exec()
