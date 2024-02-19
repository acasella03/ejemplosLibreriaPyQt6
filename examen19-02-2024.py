import sys
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTableView, QLineEdit, QLabel, QMessageBox, QGridLayout

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Examen 19-02-2024")
        self.setGeometry(100, 100, 1100, 800)

        # Inicializar la base de datos y la tabla
        self.init_database()
        self.init_table_model()

        # Crear la interfaz
        self.init_ui()

    def init_database(self):
        self.db = QSqlDatabase("QSQLITE")
        self.db.setDatabaseName("modelosClasicos.dat")

        if not self.db.open():
            QMessageBox.critical(self, "Error", "No se pudo abrir la base de datos")
            sys.exit(1)

    def init_table_model(self):
        self.table_model = QSqlTableModel(db=self.db)
        self.table_model.setTable("clientes")
        self.table_model.select()

    def init_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Etiquetas y líneas de texto para los datos
        nCliente_label = QLabel("Número Cliente:")
        self.nCliente_line_edit = QLineEdit()
        layout.addWidget(nCliente_label)
        layout.addWidget(self.nCliente_line_edit)

        nome_label = QLabel("Nome:")
        self.nome_line_edit = QLineEdit()
        layout.addWidget(nome_label)
        layout.addWidget(self.nome_line_edit)

        apelidos_label = QLabel("Apelidos:")
        self.apelidos_line_edit = QLineEdit()
        layout.addWidget(apelidos_label)
        layout.addWidget(self.apelidos_line_edit)

        direccion_label = QLabel("Dirección:")
        self.direccion_line_edit = QLineEdit()
        layout.addWidget(direccion_label)
        layout.addWidget(self.direccion_line_edit)

        cidade_label = QLabel("Cidade:")
        self.cidade_line_edit = QLineEdit()
        layout.addWidget(cidade_label)
        layout.addWidget(self.cidade_line_edit)

        provincia_label = QLabel("Provincia:")
        self.provincia_line_edit = QLineEdit()
        layout.addWidget(provincia_label)
        layout.addWidget(self.provincia_line_edit)

        codigoPostal_label = QLabel("Código Postal:")
        self.codigoPostal_line_edit = QLineEdit()
        layout.addWidget(codigoPostal_label)
        layout.addWidget(self.codigoPostal_line_edit)

        telefono_label = QLabel("Teléfono:")
        self.telefono_line_edit = QLineEdit()
        layout.addWidget(telefono_label)
        layout.addWidget(self.telefono_line_edit)

        # Deshabilitar líneas de texto inicialmente
        self.nCliente_line_edit.setEnabled(False)
        self.nome_line_edit.setEnabled(False)
        self.apelidos_line_edit.setEnabled(False)
        self.direccion_line_edit.setEnabled(False)
        self.cidade_line_edit.setEnabled(False)
        self.provincia_line_edit.setEnabled(False)
        self.codigoPostal_line_edit.setEnabled(False)
        self.telefono_line_edit.setEnabled(False)

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
        filter_string = f"nCliente LIKE '%{text}%' OR nome LIKE '%{text}%' OR apelidos LIKE '%{text}%' OR direccion LIKE '%{text}%' OR direccion LIKE '%{text}%' OR cidade LIKE '%{text}%' OR provincia LIKE '%{text}%' OR codigoPostal LIKE '%{text}%' OR telefono LIKE '%{text}%'"
        self.table_model.setFilter(filter_string)

    def start_adding(self):
        # Habilitar líneas de texto y deshabilitar botón Agregar
        self.nCliente_line_edit.setEnabled(True)
        self.nome_line_edit.setEnabled(True)
        self.apelidos_line_edit.setEnabled(True)
        self.direccion_line_edit.setEnabled(True)
        self.cidade_line_edit.setEnabled(True)
        self.provincia_line_edit.setEnabled(True)
        self.codigoPostal_line_edit.setEnabled(True)
        self.telefono_line_edit.setEnabled(True)
        self.add_button.setEnabled(False)
        self.save_button.setEnabled(True)
        self.delete_button.setEnabled(False)
        self.cancel_button.setEnabled(True)

    def save_changes(self):
        nCliente = self.nCliente_line_edit.text()
        nome = self.nome_line_edit.text()
        apelidos = self.apelidos_line_edit.text()
        direccion = self.direccion_line_edit.text()
        cidade = self.cidade_line_edit.text()
        provincia = self.provincia_line_edit.text()
        codigoPostal = self.codigoPostal_line_edit.text()
        telefono = self.telefono_line_edit.text()

        if not nCliente or not nome or not apelidos or not direccion or not cidade or not provincia or not codigoPostal or not telefono:
            QMessageBox.warning(self, "Advertencia", "Todos los campos son obligatorios")
            return

        row = self.table_model.rowCount()
        self.table_model.insertRow(row)

        self.table_model.setData(self.table_model.index(row, 0), nCliente)
        self.table_model.setData(self.table_model.index(row, 1), nome)
        self.table_model.setData(self.table_model.index(row, 2), apelidos)
        self.table_model.setData(self.table_model.index(row, 3), telefono)
        self.table_model.setData(self.table_model.index(row, 4), direccion)
        self.table_model.setData(self.table_model.index(row, 5), cidade)
        self.table_model.setData(self.table_model.index(row, 6), provincia)
        self.table_model.setData(self.table_model.index(row, 7), codigoPostal)


        # Aplicar cambios a la base de datos
        self.table_model.submitAll()

        # Actualizar el modelo para reflejar los cambios en la tabla
        self.table_model.select()

        # Limpiar campos y deshabilitar botón Guardar
        self.nCliente_line_edit.clear()
        self.nome_line_edit.clear()
        self.apelidos_line_edit.clear()
        self.direccion_line_edit.clear()
        self.cidade_line_edit.clear()
        self.provincia_line_edit.clear()
        self.codigoPostal_line_edit.clear()
        self.telefono_line_edit.clear()
        self.nCliente_line_edit.setEnabled(False)
        self.nome_line_edit.setEnabled(False)
        self.apelidos_line_edit.setEnabled(False)
        self.direccion_line_edit.setEnabled(False)
        self.cidade_line_edit.setEnabled(False)
        self.provincia_line_edit.setEnabled(False)
        self.codigoPostal_line_edit.setEnabled(False)
        self.telefono_line_edit.setEnabled(False)
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
                self.nCliente_line_edit.clear()
                self.nome_line_edit.clear()
                self.apelidos_line_edit.clear()
                self.direccion_line_edit.clear()
                self.cidade_line_edit.clear()
                self.provincia_line_edit.clear()
                self.codigoPostal_line_edit.clear()
                self.telefono_line_edit.clear()
                self.nCliente_line_edit.setEnabled(False)
                self.nome_line_edit.setEnabled(False)
                self.apelidos_line_edit.setEnabled(False)
                self.direccion_line_edit.setEnabled(False)
                self.cidade_line_edit.setEnabled(False)
                self.provincia_line_edit.setEnabled(False)
                self.codigoPostal_line_edit.setEnabled(False)
                self.telefono_line_edit.setEnabled(False)
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
            self.nCliente_line_edit.clear()
            self.nome_line_edit.clear()
            self.apelidos_line_edit.clear()
            self.direccion_line_edit.clear()
            self.cidade_line_edit.clear()
            self.provincia_line_edit.clear()
            self.codigoPostal_line_edit.clear()
            self.telefono_line_edit.clear()
            self.nCliente_line_edit.setEnabled(False)
            self.nome_line_edit.setEnabled(False)
            self.apelidos_line_edit.setEnabled(False)
            self.direccion_line_edit.setEnabled(False)
            self.cidade_line_edit.setEnabled(False)
            self.provincia_line_edit.setEnabled(False)
            self.codigoPostal_line_edit.setEnabled(False)
            self.telefono_line_edit.setEnabled(False)
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
                        nCliente = str(self.table_model.index(row, 0).data())
                        nome = str(self.table_model.index(row, 1).data())
                        apelidos = str(self.table_model.index(row, 2).data())
                        telefono = str(self.table_model.index(row, 3).data())
                        direccion = str(self.table_model.index(row, 4).data())
                        cidade = str(self.table_model.index(row, 5).data())
                        provincia = str(self.table_model.index(row, 6).data())
                        codigoPostal = str(self.table_model.index(row, 7).data())

                        # Rellenar líneas de texto con los datos seleccionados
                        self.nCliente_line_edit.setText(nCliente)
                        self.nome_line_edit.setText(nome)
                        self.apelidos_line_edit.setText(apelidos)
                        self.direccion_line_edit.setText(direccion)
                        self.cidade_line_edit.setText(cidade)
                        self.provincia_line_edit.setText(provincia)
                        self.codigoPostal_line_edit.setText(codigoPostal)
                        self.telefono_line_edit.setText(telefono)

                        # Habilitar líneas de texto y deshabilitar/agregar/eliminar/botones según sea necesario
                        self.nCliente_line_edit.setEnabled(True)
                        self.nome_line_edit.setEnabled(True)
                        self.apelidos_line_edit.setEnabled(True)
                        self.direccion_line_edit.setEnabled(True)
                        self.cidade_line_edit.setEnabled(True)
                        self.provincia_line_edit.setEnabled(True)
                        self.codigoPostal_line_edit.setEnabled(True)
                        self.telefono_line_edit.setEnabled(True)
                        self.add_button.setEnabled(False)
                        self.save_button.setEnabled(False)
                        self.delete_button.setEnabled(False)
                        self.cancel_button.setEnabled(True)
                        self.edit_button.setText("Guardar Edición")

                        # Pintar el recuadro de las líneas de texto de color verde
                        self.nCliente_line_edit.setStyleSheet("QLineEdit { background-color: lightgreen; }")
                        self.nome_line_edit.setStyleSheet("QLineEdit { background-color: lightgreen; }")
                        self.apelidos_line_edit.setStyleSheet("QLineEdit { background-color: lightgreen; }")
                        self.direccion_line_edit.setStyleSheet("QLineEdit { background-color: lightgreen; }")
                        self.cidade_line_edit.setStyleSheet("QLineEdit { background-color: lightgreen; }")
                        self.provincia_line_edit.setStyleSheet("QLineEdit { background-color: lightgreen; }")
                        self.codigoPostal_line_edit.setStyleSheet("QLineEdit { background-color: lightgreen; }")
                        self.telefono_line_edit.setStyleSheet("QLineEdit { background-color: lightgreen; }")
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
                    nCliente = self.nCliente_line_edit.text()
                    nome = self.nome_line_edit.text()
                    apelidos = self.apelidos_line_edit.text()
                    direccion = self.direccion_line_edit.text()
                    cidade = self.cidade_line_edit.text()
                    provincia = self.provincia_line_edit.text()
                    codigoPostal = self.codigoPostal_line_edit.text()
                    telefono = self.telefono_line_edit.text()

                    # Actualizar la tabla y la base de datos con los nuevos datos
                    self.table_model.setData(self.table_model.index(row, 0), nCliente)
                    self.table_model.setData(self.table_model.index(row, 1), nome)
                    self.table_model.setData(self.table_model.index(row, 2), apelidos)
                    self.table_model.setData(self.table_model.index(row, 3), telefono)
                    self.table_model.setData(self.table_model.index(row, 4), direccion)
                    self.table_model.setData(self.table_model.index(row, 5), cidade)
                    self.table_model.setData(self.table_model.index(row, 6), provincia)
                    self.table_model.setData(self.table_model.index(row, 7), codigoPostal)

                    self.table_model.submitAll()  # Guardar cambios en la base de datos

                    # Deshabilitar líneas de texto y habilitar/deshabilitar/agregar/eliminar botones según sea necesario
                    self.nCliente_line_edit.clear()
                    self.nome_line_edit.clear()
                    self.apelidos_line_edit.clear()
                    self.direccion_line_edit.clear()
                    self.cidade_line_edit.clear()
                    self.provincia_line_edit.clear()
                    self.codigoPostal_line_edit.clear()
                    self.telefono_line_edit.clear()
                    self.nCliente_line_edit.setEnabled(False)
                    self.nome_line_edit.setEnabled(False)
                    self.apelidos_line_edit.setEnabled(False)
                    self.direccion_line_edit.setEnabled(False)
                    self.cidade_line_edit.setEnabled(False)
                    self.provincia_line_edit.setEnabled(False)
                    self.codigoPostal_line_edit.setEnabled(False)
                    self.telefono_line_edit.setEnabled(False)
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
                    self.nCliente_line_edit.setStyleSheet("")
                    self.nome_line_edit.setStyleSheet("")
                    self.apelidos_line_edit.setStyleSheet("")
                    self.direccion_line_edit.setStyleSheet("")
                    self.cidade_line_edit.setStyleSheet("")
                    self.provincia_line_edit.setStyleSheet("")
                    self.codigoPostal_line_edit.setStyleSheet("")
                    self.telefono_line_edit.setStyleSheet("")
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