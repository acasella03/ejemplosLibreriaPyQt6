import sys

from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QComboBox,
                             QWidget, QCheckBox, QHBoxLayout, QLineEdit, QTableView, QMessageBox)
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
        self.botonCancelar = QPushButton("Cancelar") # Creación del botón Cancelar
        self.botonBorrar = QPushButton("Borrar") # Creación del botón Borrar
        # añadir los botones a la caja horizontal
        cajaH.addWidget(self.botonAceptar) # Añade el botón Aceptar a la caja horizontal
        cajaH.addWidget(self.botonCancelar) # Añade el botón Cancelar a la caja horizontal
        cajaH.addWidget(self.botonBorrar) # Añade el botón Borrar a la caja horizontal
        # Conexión de los botones con sus funciones
        self.botonAceptar.clicked.connect(self.on_botonAceptar_clicked) # Conexión del botón Aceptar con la función on_botonAceptar_clicked
        self.botonCancelar.clicked.connect(self.on_botonCancelar_clicked) # Conexión del botón Cancelar con la función on_botonCancelar_clicked
        self.botonBorrar.clicked.connect(self.on_botonBorrar_clicked) # Conexión del botón Borrar con la función on_botonBorrar_clicked

        # Configuración del tamaño fijo de la ventana y visualización
        self.setMinimumSize(500, 300)
        self.show()

    def on_botonAceptar_clicked(self): # Función que se ejecuta al pulsar el botón Aceptar
        self.modelo.submitAll() # Envía los cambios al modelo

    def on_botonCancelar_clicked(self): # Función que se ejecuta al pulsar el botón Cancelar
        self.modelo.revertAll() # Revierte los cambios del modelo

    def on_botonBorrar_clicked(self, fila):
        # Obtener el índice de la fila seleccionada de la tabla
        fila_seleccionada = self.tabla.currentIndex().row()
        if fila_seleccionada != -1:
            # Borra la fila del modelo y aplica los cambios
            self.modelo.removeRow(fila_seleccionada) #  Para eliminar la fila seleccionada del modelo
            self.modelo.submitAll() # Para enviar los cambios a la base de datos
            self.modelo.select() # Para actualizar la vista de la tabla y mostrar los cambios
        else:
            # USABILIDAD: Muestra un mensaje de advertencia si no hay fila seleccionada
            dialogo = QMessageBox(self) # se utilizará para mostrar la advertencia. El argumento self se pasa al constructor para indicar que el cuadro de diálogo pertenece a la ventana principal.
            dialogo.setWindowTitle("ADVERTENCIA") # Se establece el título del cuadro de diálogo
            dialogo.setText("Selecciona una fila para borrar.") # Se establece el texto del cuadro de diálogo con la advertencia deseada
            boton = dialogo.exec() # Se ejecuta el cuadro de diálogo y se obtiene el botón presionado por el usuario. El valor de retorno boton será un valor que indica qué botón se presionó (en este caso, el botón "Ok").
            # boton = QMessageBox.warning(self, "ADVERTENCIA", "Selecciona una fila para borrar.") # También se podría abreviar así. En lugar de llamar exec() ahora simplemente llamamos al método de diálogo y se crea el diálogo.
            if boton == QMessageBox.StandardButton.Ok: # Se verifica si el botón presionado es el botón "Ok".
                print("OK!") # Si es así, imprime "OK!" en la consola.

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    aplicacion.exec()
