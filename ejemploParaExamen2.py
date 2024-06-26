import sys
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTableView, QLineEdit, QLabel, QMessageBox, QComboBox

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo de Interfaz")
        self.setGeometry(100, 100, 560, 700)

        # Inicializar la base de datos y la tabla
        self.init_database()
        self.init_table_model()

        # Crear la interfaz
        self.init_ui()

    def init_database(self):
        self.db = QSqlDatabase("QSQLITE")
        self.db.setDatabaseName("baseDatos2.dat")

        if not self.db.open():
            QMessageBox.critical(self, "Error", "No se pudo abrir la base de datos")
            sys.exit(1)

    def init_table_model(self):
        self.table_model = QSqlTableModel(db=self.db)
        self.table_model.setTable("usuarios")
        self.table_model.select()

    def init_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Etiquetas y líneas de texto para los datos
        dni_label = QLabel("DNI:")
        self.dni_line_edit = QLineEdit()
        layout.addWidget(dni_label)
        layout.addWidget(self.dni_line_edit)

        nome_label = QLabel("Nome:")
        self.nome_line_edit = QLineEdit()
        layout.addWidget(nome_label)
        layout.addWidget(self.nome_line_edit)

        edade_label = QLabel("Edade:")
        self.edade_line_edit = QLineEdit()
        layout.addWidget(edade_label)
        layout.addWidget(self.edade_line_edit)

        xenero_label = QLabel("Xenero:")
        self.xenero_combobox = QComboBox()
        self.xenero_combobox.addItems(["Home", "Muller", "Outros"])
        layout.addWidget(xenero_label)
        layout.addWidget(self.xenero_combobox)

        falecido_label = QLabel("Falecido:")
        self.falecido_combobox = QComboBox()
        self.falecido_combobox.addItems(["Sí", "No"])
        layout.addWidget(falecido_label)
        layout.addWidget(self.falecido_combobox)

        # Deshabilitar líneas de texto inicialmente
        self.dni_line_edit.setEnabled(False)
        self.nome_line_edit.setEnabled(False)
        self.edade_line_edit.setEnabled(False)
        self.xenero_combobox.setEnabled(False)
        self.falecido_combobox.setEnabled(False)

        # Buscador
        search_label = QLabel("Buscar:")
        search_line_edit = QLineEdit()
        search_line_edit.textChanged.connect(self.filter_table)
        layout.addWidget(search_label)
        layout.addWidget(search_line_edit)

        # Tabla
        table_view = QTableView()
        table_view.setModel(self.table_model)
        layout.addWidget(table_view)

        # Mensaje de éxito
        self.success_label = QLabel()
        layout.addWidget(self.success_label)

        # Botones
        button_layout = QVBoxLayout()

        add_button = QPushButton("Agregar")
        add_button.clicked.connect(self.start_adding)  # Conectar botón Agregar
        button_layout.addWidget(add_button)

        save_button = QPushButton("Guardar")
        save_button.clicked.connect(self.save_changes)
        save_button.setEnabled(False)
        button_layout.addWidget(save_button)

        delete_button = QPushButton("Borrar")
        delete_button.clicked.connect(self.delete_record)
        button_layout.addWidget(delete_button)

        cancel_button = QPushButton("Cancelar")
        cancel_button.clicked.connect(self.cancel_changes)
        cancel_button.setEnabled(False)
        button_layout.addWidget(cancel_button)

        edit_button = QPushButton("Editar")
        edit_button.clicked.connect(self.edit_data)
        edit_button.setEnabled(True)
        button_layout.addWidget(edit_button)

        layout.addLayout(button_layout)

        # Establecer comportamiento de los botones
        self.add_button = add_button
        self.save_button = save_button
        self.delete_button = delete_button
        self.cancel_button = cancel_button
        self.edit_button = edit_button

    def filter_table(self, text):
        filter_string = f"dni LIKE '%{text}%' OR nome LIKE '%{text}%' OR edade LIKE '%{text}%' OR xenero LIKE '%{text}%'"
        self.table_model.setFilter(filter_string)

    def start_adding(self):
        # Habilitar líneas de texto y deshabilitar botón Agregar
        self.dni_line_edit.setEnabled(True)
        self.nome_line_edit.setEnabled(True)
        self.edade_line_edit.setEnabled(True)
        self.xenero_combobox.setEnabled(True)
        self.falecido_combobox.setEnabled(True)
        self.add_button.setEnabled(False)
        self.save_button.setEnabled(True)
        self.delete_button.setEnabled(False)
        self.cancel_button.setEnabled(True)

    def save_changes(self):
        dni = self.dni_line_edit.text()
        nome = self.nome_line_edit.text()
        edade = self.edade_line_edit.text()
        xenero = self.xenero_combobox.currentText()
        falecido = self.falecido_combobox.currentText()

        if not dni or not nome or not edade or not xenero or not falecido:
            QMessageBox.warning(self, "Advertencia", "Todos los campos son obligatorios")
            return

        row = self.table_model.rowCount()
        self.table_model.insertRow(row)

        self.table_model.setData(self.table_model.index(row, 0), dni)
        self.table_model.setData(self.table_model.index(row, 1), nome)
        self.table_model.setData(self.table_model.index(row, 2), edade)
        self.table_model.setData(self.table_model.index(row, 3), xenero)
        self.table_model.setData(self.table_model.index(row, 4), falecido)

        # Aplicar cambios a la base de datos
        self.table_model.submitAll()

        # Actualizar el modelo para reflejar los cambios en la tabla
        self.table_model.select()

        # Limpiar campos y deshabilitar botón Guardar
        self.dni_line_edit.clear()
        self.nome_line_edit.clear()
        self.edade_line_edit.clear()
        self.xenero_combobox.setCurrentIndex(0)
        self.falecido_combobox.setCurrentIndex(0)
        self.dni_line_edit.setEnabled(False)
        self.nome_line_edit.setEnabled(False)
        self.edade_line_edit.setEnabled(False)
        self.xenero_combobox.setEnabled(False)
        self.falecido_combobox.setEnabled(False)
        self.add_button.setEnabled(True)
        self.save_button.setEnabled(False)
        self.delete_button.setEnabled(True)
        self.cancel_button.setEnabled(False)

        # Mostrar mensaje de éxito
        self.success_label.setText("<html><b style='color: green;'>LOS DATOS SE HAN GUARDADO CORRECTAMENTE</b></html>")

    def delete_record(self):
        selected_rows = self.centralWidget().findChild(QTableView).selectionModel().selectedRows()

        if selected_rows:
            reply = QMessageBox.question(self, "Confirmación", "¿Estás seguro que quieres borrar los datos?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

            if reply == QMessageBox.StandardButton.Yes:
                for index in selected_rows:
                    self.table_model.removeRow(index.row())

                # Actualizar el modelo para reflejar los cambios en la tabla
                self.table_model.select()

                # Limpiar campos y deshabilitar botón Guardar
                self.dni_line_edit.clear()
                self.nome_line_edit.clear()
                self.edade_line_edit.clear()
                self.xenero_combobox.setCurrentIndex(0)
                self.falecido_combobox.setCurrentIndex(0)
                self.dni_line_edit.setEnabled(False)
                self.nome_line_edit.setEnabled(False)
                self.edade_line_edit.setEnabled(False)
                self.xenero_combobox.setEnabled(False)
                self.falecido_combobox.setEnabled(False)
                self.add_button.setEnabled(True)
                self.save_button.setEnabled(False)
                self.delete_button.setEnabled(True)
                self.cancel_button.setEnabled(False)
                self.success_label.setText("<html><b style='color: red;'>BORRADO EXITOSO</b></html>")
            else:
                # Si el usuario elige no borrar, mantener los campos y habilitar el botón Agregar
                self.add_button.setEnabled(True)
                self.save_button.setEnabled(False)
                self.delete_button.setEnabled(True)
                self.cancel_button.setEnabled(False)
        else:
            QMessageBox.warning(self, "Advertencia", "Selecciona al menos una fila para borrar.\nPulsa en el número de la fila.")

    def cancel_changes(self):
        reply = QMessageBox.question(self, "Confirmación", "¿Estás seguro que quieres borrar los datos introducidos?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:
            # Limpiar campos y deshabilitar botón Guardar
            self.dni_line_edit.clear()
            self.nome_line_edit.clear()
            self.edade_line_edit.clear()
            self.xenero_combobox.setCurrentIndex(0)
            self.falecido_combobox.setCurrentIndex(0)
            self.dni_line_edit.setEnabled(False)
            self.nome_line_edit.setEnabled(False)
            self.edade_line_edit.setEnabled(False)
            self.xenero_combobox.setEnabled(False)
            self.falecido_combobox.setEnabled(False)
            self.add_button.setEnabled(True)
            self.save_button.setEnabled(False)
            self.delete_button.setEnabled(True)
            self.cancel_button.setEnabled(False)
            self.success_label.clear()
        else:
            # Si el usuario elige no borrar, mantener los campos y habilitar el botón Agregar
            self.add_button.setEnabled(False)
            self.save_button.setEnabled(True)
            self.cancel_button.setEnabled(True)

    def edit_data(self):
        try:
            if self.edit_button.text() == "Editar":
                reply = QMessageBox.question(self, "Confirmación",
                                             "Estás entrando en el proceso de Edición de datos, ¿Quieres continuar?",
                                             QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

                if reply == QMessageBox.StandardButton.Yes:
                    selected_indexes = self.centralWidget().findChild(QTableView).selectionModel().selectedIndexes()

                    if selected_indexes:
                        # Obtener datos de la fila seleccionada
                        row = selected_indexes[0].row()
                        dni = str(self.table_model.index(row, 0).data())
                        nome = str(self.table_model.index(row, 1).data())
                        edade = str(self.table_model.index(row, 2).data())
                        xenero = str(self.table_model.index(row, 3).data())
                        falecido = str(self.table_model.index(row, 4).data())

                        # Rellenar líneas de texto con los datos seleccionados
                        self.dni_line_edit.setText(dni)
                        self.nome_line_edit.setText(nome)
                        self.edade_line_edit.setText(edade)
                        self.xenero_combobox.setCurrentText(xenero)
                        self.falecido_combobox.setCurrentText(falecido)

                        # Habilitar líneas de texto y deshabilitar/agregar/eliminar/botones según sea necesario
                        self.dni_line_edit.setEnabled(True)
                        self.nome_line_edit.setEnabled(True)
                        self.edade_line_edit.setEnabled(True)
                        self.xenero_combobox.setEnabled(True)
                        self.falecido_combobox.setEnabled(True)
                        self.add_button.setEnabled(False)
                        self.save_button.setEnabled(False)
                        self.delete_button.setEnabled(False)
                        self.cancel_button.setEnabled(True)
                        self.edit_button.setText("Guardar Edición")

                        # Pintar el recuadro de las líneas de texto de color verde
                        self.dni_line_edit.setStyleSheet("QLineEdit { background-color: lightgreen; }")
                        self.nome_line_edit.setStyleSheet("QLineEdit { background-color: lightgreen; }")
                        self.edade_line_edit.setStyleSheet("QLineEdit { background-color: lightgreen; }")
                        self.xenero_combobox.setStyleSheet("QComboBox { background-color: lightgreen; }")
                        self.falecido_combobox.setStyleSheet("QComboBox { background-color: lightgreen; }")
                    else:
                        QMessageBox.warning(self, "Advertencia", "Selecciona al menos una fila para editar.")
                else:
                    # Si el usuario elige no continuar, mantener los botones en su estado anterior
                    self.add_button.setEnabled(True)
                    self.save_button.setEnabled(False)
                    self.delete_button.setEnabled(True)
                    self.cancel_button.setEnabled(False)
                    self.edit_button.setEnabled(True)
            elif self.edit_button.text() == "Guardar Edición":
                # Obtener la fila seleccionada
                selected_indexes = self.centralWidget().findChild(QTableView).selectionModel().selectedIndexes()

                if selected_indexes:
                    # Obtener datos de la fila seleccionada
                    row = selected_indexes[0].row()

                    # Obtener los nuevos datos de los campos
                    dni = self.dni_line_edit.text()
                    nome = self.nome_line_edit.text()
                    edade = self.edade_line_edit.text()
                    xenero = self.xenero_combobox.currentText()
                    falecido = self.falecido_combobox.currentText()

                    # Actualizar la tabla y la base de datos con los nuevos datos
                    self.table_model.setData(self.table_model.index(row, 0), dni)
                    self.table_model.setData(self.table_model.index(row, 1), nome)
                    self.table_model.setData(self.table_model.index(row, 2), edade)
                    self.table_model.setData(self.table_model.index(row, 3), xenero)
                    self.table_model.setData(self.table_model.index(row, 4), falecido)
                    self.table_model.submitAll()  # Guardar cambios en la base de datos

                    # Deshabilitar líneas de texto y habilitar/deshabilitar/agregar/eliminar botones según sea necesario
                    self.dni_line_edit.clear()
                    self.nome_line_edit.clear()
                    self.edade_line_edit.clear()
                    self.xenero_combobox.setCurrentIndex(0)
                    self.falecido_combobox.setCurrentIndex(0)
                    self.dni_line_edit.setEnabled(False)
                    self.nome_line_edit.setEnabled(False)
                    self.edade_line_edit.setEnabled(False)
                    self.xenero_combobox.setEnabled(False)
                    self.falecido_combobox.setEnabled(False)
                    self.add_button.setEnabled(True)
                    self.save_button.setEnabled(False)
                    self.delete_button.setEnabled(True)
                    self.cancel_button.setEnabled(False)
                    self.edit_button.setEnabled(True)
                    self.success_label.setText("<html><b style='color: green;'>CAMBIO EXITOSO</b></html>")

                    # Refrescar la tabla para reflejar los cambios
                    self.table_model.select()

                    # Restablecer el nombre del botón y dejar de pintar en verde las líneas de texto
                    self.edit_button.setText("Editar")
                    self.dni_line_edit.setStyleSheet("")
                    self.nome_line_edit.setStyleSheet("")
                    self.edade_line_edit.setStyleSheet("")
                    self.xenero_combobox.setStyleSheet("")
                    self.falecido_combobox.setStyleSheet("")
                else:
                    QMessageBox.warning(self, "Advertencia", "Selecciona al menos una fila para editar.")
        except Exception as e:
            print(f"Excepción en edit_data: {e}")
            QMessageBox.critical(self, "Error", f"Excepción en edit_data: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyMainWindow()
    window.show()

    sys.exit(app.exec())