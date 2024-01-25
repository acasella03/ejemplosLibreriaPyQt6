import sys
import typing

from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QComboBox,
                             QWidget, QCheckBox, QHBoxLayout, QLineEdit, QTableView)
from PyQt6.QtCore import Qt, QAbstractTableModel
from PyQt6 import QtGui

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
            if rol == Qt.ItemDataRole.ForegroundRole:
                if self.tabla[indice.row()][3] == True:
                    return QtGui.QColor("red")
            if rol == Qt.ItemDataRole.BackgroundRole:
                if self.tabla[indice.row()][2] == "Home":
                    return QtGui.QColor("lightblue")
                if self.tabla[indice.row()][2] == "Muller":
                    return QtGui.QColor("pink")
                if self.tabla[indice.row()][2] == "Outros":
                    return QtGui.QColor("lightgrey")
            if rol == Qt.ItemDataRole.DecorationRole:
                if isinstance(self.tabla[indice.row()][indice.column()], bool):
                    if self.tabla[indice.row()][indice.column()]:
                        return QtGui.QIcon("check-mark.png")


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

        cajaV=QVBoxLayout() # Creación de un layout vertical
        self.tvwTabla = QTableView() # Creación de la vista de la tabla
        modelo = ModeloTabla(self.datos) # Creación del modelo de datos de la tabla
        self.tvwTabla.setModel(modelo) # Configuración del modelo de datos de la tabla
        self.seleccion= self.tvwTabla.selectionModel() # Se obtiene el modelo de selección de la tabla
        self.seleccion.selectionChanged.connect(self.on_filaSeleccionada) # Se conecta la señal de cambio de selección de la tabla con el método correspondiente
        self.tvwTabla.setSelectionMode(QTableView.SelectionMode.SingleSelection) # evitar selección múltiple
        cajaV.addWidget(self.tvwTabla) # Se añade la vista de la tabla al layout vertical
        cajaH=QHBoxLayout() # Creación de un layout horizontal
        cajaV.addLayout(cajaH) # Se añade el layout horizontal al layout vertical
        self.txtNombre=QLineEdit("Nome") # Creación de un campo de texto
        cajaH.addWidget(self.txtNombre) # Se añade el campo de texto al layout horizontal
        self.txtDni=QLineEdit("DNI") # Creación de un campo de texto
        cajaH.addWidget(self.txtDni) # Se añade el campo de texto al layout horizontal
        self.cmbGenero=QComboBox() # Creación de un combo box
        self.cmbGenero.addItems(('Home', 'Muller', 'Outros')) # Se añaden los elementos al combo box
        cajaH.addWidget(self.cmbGenero) # Se añade el combo box al layout horizontal
        self.chkFallecido=QCheckBox('Falecido') # Creación de un check box
        cajaH.addWidget(self.chkFallecido) # Se añade el check box al layout horizontal


        componentePrincipal=QWidget() # Creación de un widget
        componentePrincipal.setLayout(cajaV) # Configuración del layout vertical como layout del widget
        self.setCentralWidget(componentePrincipal) # Configuración de la vista de la tabla como widget central

        # Configuración del tamaño fijo de la ventana y visualización
        self.setFixedSize(400, 400)
        self.show()

    def on_filaSeleccionada(self):
        indice= self.tvwTabla.selectedIndexes() # Se obtienen los índices de las filas seleccionadas
        if len(indice) == 0: # evitar el error fuera del rango de la lista
            return
        # Imprimir el indice de la fila seleccionada
        print(indice[0].row())
        # Imprimir el nombre de la persona seleccionada
        print(self.datos[indice[0].row()][0])
        # Imprimir el DNI de la persona seleccionada
        print(self.datos[indice[0].row()][1])
        # Imprimir el género de la persona seleccionada
        print(self.datos[indice[0].row()][2])
        # Se establece el nombre en el campo de texto
        self.txtNombre.setText(self.datos[indice[0].row()][0])
        # Se establece el DNI en el campo de texto
        self.txtDni.setText(self.datos[indice[0].row()][1])
        # Se establece el género en el combo box
        self.cmbGenero.setCurrentText(self.datos[indice[0].row()][2])
        # Se establece el estado de fallecido en el check box
        self.chkFallecido.setChecked(self.datos[indice[0].row()][3])

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    aplicacion.exec()
