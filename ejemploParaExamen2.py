import sys
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QTableView, QLineEdit, QLabel, QMessageBox


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
        db = QSqlDatabase("QSQLITE")
        db.setDatabaseName("baseDatos2.dat")

        if not db.open():
            QMessageBox.critical(self, "Error", "No se pudo abrir la base de datos")
            sys.exit(1)

    def init_table_model(self):
        self.table_model = QSqlTableModel()
        self.table_model.setTable("ejemplo")
        self.table_model.select()

    def init_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

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

        # Botones
        button_layout = QVBoxLayout()

        add_button = QPushButton("Agregar")
        add_button.clicked.connect(self.add_record)
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
        filter_string = f"Nombre LIKE '%{text}%' OR Edad LIKE '%{text}%' OR Ciudad LIKE '%{text}%'"
        self.table_model.setFilter(filter_string)

    def add_record(self):
        self.table_model.insertRow(self.table_model.rowCount())

    def save_changes(self):
        if self.table_model.submitAll():
            self.table_model.select()
            self.disable_editing()

    def delete_record(self):
        selected_rows = self.centralWidget().findChild(QTableView).selectionModel().selectedRows()

        if selected_rows:
            for index in selected_rows:
                self.table_model.removeRow(index.row())

    def cancel_changes(self):
        self.table_model.revertAll()
        self.disable_editing()

    def enable_editing(self):
        self.add_button.setEnabled(False)
        self.save_button.setEnabled(True)
        self.delete_button.setEnabled(True)
        self.cancel_button.setEnabled(True)

    def disable_editing(self):
        self.add_button.setEnabled(True)
        self.save_button.setEnabled(False)
        self.delete_button.setEnabled(True)
        self.cancel_button.setEnabled(False)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyMainWindow()
    window.show()

    sys.exit(app.exec())