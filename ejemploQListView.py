import sys
import typing

from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout,
                             QWidget, QListView, QHBoxLayout, QLineEdit)
from PyQt6.QtCore import Qt, QAbstractListModel
from PyQt6.QtGui import QImage

tick = QImage('check-mark.png')


class TareasModelo(QAbstractListModel):
    def __init__(self, tareas=None):
        # Inicializa la clase base QAbstractListModel
        super().__init__()
        # Inicializa la lista de tareas, utilizando la lista proporcionada o una lista vacía si no se proporciona
        self.tareas = tareas or []

    def data(self, indice, rol):
        # Verifica si el rol es el de visualización del ítem
        if rol == Qt.ItemDataRole.DisplayRole:
            # Obtiene el estado y el texto de la tarea en la posición dada por el índice
            _, texto = self.tareas[indice.row()]
            return texto  # Devuelve el texto de la tarea
        # Verifica si el rol es el de decoración del ítem
        if rol == Qt.ItemDataRole.DecorationRole:
            estado, _ = self.tareas[indice.row()] # Obtiene el estado de completitud de la tarea en la posición dada por el índice
            # Devuelve la marca de verificación si la tarea está completa
            if estado:
                return tick

    def rowCount(self, indice):
        return len(self.tareas)  # Devuelve la cantidad de tareas en el modelo


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        # Inicializa la clase base QMainWindow
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle("Ejemplo QListView con Qt")

        # Inicialización de la lista de tareas y el modelo
        listaTareas = [(False, 'Primera tarea'), (False, 'Segunda tarea')]
        self.modelo = TareasModelo(listaTareas)

        # Configuración del diseño vertical principal
        cajaV = QVBoxLayout()

        # Configuración de la vista de lista y asignación del modelo
        self.lstTareas = QListView()
        self.lstTareas.setModel(self.modelo)
        self.lstTareas.setSelectionMode(QListView.SelectionMode.MultiSelection)
        cajaV.addWidget(self.lstTareas)

        # Configuración del diseño horizontal para botones
        cajaH = QHBoxLayout()
        btnBorrar = QPushButton("Borrar")
        btnBorrar.pressed.connect(self.on_btnBorrar_pressed)
        btnHecho = QPushButton("Hecho")
        btnHecho.pressed.connect(self.on_btnHeccho_pressed)
        cajaH.addWidget(btnBorrar)
        cajaH.addWidget(btnHecho)

        # Agrega el diseño horizontal al diseño vertical principal
        cajaV.addLayout(cajaH)

        # Configuración de la entrada de texto para agregar tareas
        self.txtTarea = QLineEdit()
        cajaV.addWidget(self.txtTarea)

        # Configuración del botón para agregar tareas y conexión al evento
        btnAgregarTarea = QPushButton("Añadir Tarea")
        btnAgregarTarea.pressed.connect(self.on_btnAgregarTarea_pressed)
        cajaV.addWidget(btnAgregarTarea)

        # Configuración del contenedor principal y asignación como widget central
        container = QWidget()
        container.setLayout(cajaV)
        self.setCentralWidget(container)

        # Configuración del tamaño fijo de la ventana y visualización
        self.setFixedSize(400, 400)
        self.show()

    def on_btnAgregarTarea_pressed(self):
        texto = self.txtTarea.text().strip()  # Obtener el texto de la entrada y eliminar espacios (strip) al inicio y al final
        # Verificar si hay texto antes de agregar la tarea al modelo
        if texto:
            self.modelo.tareas.append((False,texto))  # Agrega una nueva tarea al modelo con una marca de no completado (False) y el texto ingresado
            self.modelo.layoutChanged.emit()  # Emitir la señal para indicar cambios en el diseño del modelo
            self.txtTarea.setText("")  # Limpiar el campo de entrada de la tarea después de agregarla

    def on_btnBorrar_pressed(self):
        # Obtiene los índices de los elementos seleccionados en la lista de tareas
        indices = self.lstTareas.selectedIndexes()
        # Verifica si hay elementos seleccionados
        if indices:
            # Elimina las tareas correspondientes a los índices seleccionados
            for indice in sorted(indices, reverse=True):
                del self.modelo.tareas[indice.row()]
            self.modelo.layoutChanged.emit()  # Emite la señal para indicar que el diseño del modelo ha cambiado
            self.lstTareas.clearSelection()  # Desactiva la selección en la lista de tareas

    def on_btnHeccho_pressed(self):
        # Obtiene los índices de los elementos seleccionados en la lista de tareas
        indices = self.lstTareas.selectedIndexes()
        # Verifica si hay elementos seleccionados
        if indices:
            for indice in indices:
                estado, texto = self.modelo.tareas[indice.row()] # Obtiene el estado y el texto de la tarea en la posición dada por el índice
                self.modelo.tareas[indice.row()] = (True, texto)  # Actualiza el estado de la tarea a completada
                # self.modelo.tareas.[indice.row()]=(True, self.modelo.tareas[indice.row()][1]]
            self.modelo.dataChanged.emit(indice, indice) # Emite la señal para indicar que los datos de la tarea han cambiado
            self.lstTareas.clearSelection() # Desactiva la selección en la lista de tareas


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    aplicacion.exec()
