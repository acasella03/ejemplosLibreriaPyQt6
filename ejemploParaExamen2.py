import sys
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTableView, QLineEdit, QLabel, QMessageBox, QComboBox

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo de Interfaz")
        self.setGeometry(100, 100, 800, 600)

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

        layout.addLayout(button_layout)

        # Establecer comportamiento de los botones
        self.add_button = add_button
        self.save_button = save_button
        self.delete_button = delete_button
        self.cancel_button = cancel_button

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
        self.cancel_button.setEnabled(False)

        # Mostrar mensaje de éxito
        self.success_label.setText("<html><b style='color: green;'>LOS DATOS SE HAN GUARDADO CORRECTAMENTE</b></html>")

    def delete_record(self):
        selected_rows = self.centralWidget().findChild(QTableView).selectionModel().selectedRows()

        if selected_rows:
            for index in selected_rows:
                self.table_model.removeRow(index.row())

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

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyMainWindow()
    window.show()

    sys.exit(app.exec())