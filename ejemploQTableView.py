import sys
import typing

from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QComboBox,
                             QWidget, QCheckBox, QHBoxLayout, QLineEdit, QTableView)
from PyQt6.QtCore import Qt, QAbstractTableModel

class ModeloTabla(QAbstractTableModel):
    def __init__(self, tabla):
        super().__init__()
        self.tabla = tabla # Se almacena la tabla en un atributo de la clase
    # Métodos abstractos que deben implementarse
    def rowCount(self, indice): # Devuelve el número de filas de la tabla
        return len(self.tabla)
    def columnCount(self, indice): # Devuelve el número de columnas de la tabla
        return len(self.tabla[0])
    def data(self, indice, rol): # Devuelve el dato que se encuentra en el índice de la tabla
        if indice.isValid(): # Si el índice es válido
            if rol == Qt.ItemDataRole.EditRole or rol == Qt.ItemDataRole.DisplayRole: # Si el rol es de edición o visualización de datos de la tabla
                valor = self.tabla[indice.row()][indice.column()] # Se obtiene el valor de la tabla
                return valor
    def setData(self, indice, valor, rol): # Establece el dato en el índice de la tabla
        if rol == Qt.ItemDataRole.EditRole: # Si el rol es de edición de datos de la tabla
            self.tabla[indice.row()][indice.column()] = valor # Se establece el valor en la tabla
            return True # Se devuelve True para indicar que se ha establecido el valor
        return False # Se devuelve False para indicar que no se ha establecido el valor
    def flags(self, indice): # Devuelve los flags de edición de la tabla
        if indice.row() == 0:
            return Qt.ItemFlag.ItemIsEnabled
        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsSelectable # Se devuelven los flags de edición de la tabla

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        # Inicializa la clase base QMainWindow
        super().__init__()
        self.setWindowTitle("Ejemplo QTableView con Qt") # Establece el título de la ventana
        self.datos=[["Nome", "Dni", "Xenero", "Falecido"],
               ["Ana Pérez","12345678Y","Muller",True],
               ["Luis González","87654321K","Home",False],
               ["María Sánchez","87654891H","Muller",False],
               ["Jorge Ruíz","32754981U","Home",True],
               ]

        cajaV=QVBoxLayout()
        self.tvwTabla = QTableView() # Creación de la vista de la tabla
        modelo = ModeloTabla(self.datos) # Creación del modelo de datos de la tabla
        self.tvwTabla.setModel(modelo) # Configuración del modelo de datos de la tabla
        self.seleccion= self.tvwTabla.selectionModel()
        self.seleccion.selectionChanged.connect(self.on_filaSeleccionada)
        cajaV.addWidget(self.tvwTabla)
        cajaH=QHBoxLayout()
        cajaV.addLayout(cajaH)
        self.txtNombre=QLineEdit("Nome")
        cajaH.addWidget(self.txtNombre)
        txtDni=QLineEdit("DNI")
        cajaH.addWidget(txtDni)
        cmbGenero=QComboBox()
        cmbGenero.addItems(('Home', 'Muller', 'Outros'))
        cajaH.addWidget(cmbGenero)
        chkFallecido=QCheckBox('Falecido')
        cajaH.addWidget(chkFallecido)


        componentePrincipal=QWidget()
        componentePrincipal.setLayout(cajaV)
        self.setCentralWidget(componentePrincipal) # Configuración de la vista de la tabla como widget central

        # Configuración del tamaño fijo de la ventana y visualización
        self.setFixedSize(400, 400)
        self.show()

    def on_filaSeleccionada(self):
        indices= self.tvwTabla.selectedIndexes()
        print(indices)
        self.txtNombre.setText(self.datos[indices[0].row()][0])

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    aplicacion.exec()
