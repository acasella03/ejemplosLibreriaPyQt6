import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery


class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora con Base de Datos")
        self.setGeometry(100, 100, 400, 400)

        self.create_database()
        self.init_ui()

    def create_database(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('calculator.dat')

        if not db.open():
            QMessageBox.critical(self, 'Error', 'No se pudo abrir la base de datos', QMessageBox.StandardButton.Ok)
            return False

        query = QSqlQuery()
        query.exec("""
                    CREATE TABLE IF NOT EXISTS calculations (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        operand1 REAL,
                        operand2 REAL,
                        operator TEXT,
                        result REAL
                    )
                    """)

        if not query.isActive():
            QMessageBox.critical(self, 'Error', 'Error al crear la tabla', QMessageBox.StandardButton.Ok)
            return False

        return True

    def init_ui(self):
        layout = QVBoxLayout()

        self.result_display = QLineEdit(self)
        self.result_display.setReadOnly(True)
        layout.addWidget(self.result_display)

        grid_layout = QGridLayout()

        button_grid = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2),
            ('0', 3, 1),
        ]

        for (text, row, col) in button_grid:
            button = QPushButton(text, self)
            button.clicked.connect(lambda _, text=text: self.handle_button_click(text))
            grid_layout.addWidget(button, row, col)

        operators = ['+', '-', '*', '/']
        for i, op in enumerate(operators):
            op_button = QPushButton(op, self)
            op_button.clicked.connect(lambda _, op=op: self.handle_button_click(op))
            grid_layout.addWidget(op_button, i, 3)

        equal_button = QPushButton('=', self)
        equal_button.clicked.connect(self.calculate_result)
        grid_layout.addWidget(equal_button, 3, 3)

        layout.addLayout(grid_layout)

        self.calculation_table = QTableWidget(self)
        self.calculation_table.setColumnCount(3)
        self.calculation_table.setHorizontalHeaderLabels(['Operand1', 'Operand2', 'Result'])
        layout.addWidget(self.calculation_table)

        save_button = QPushButton('Guardar', self)
        save_button.clicked.connect(self.save_calculation)
        layout.addWidget(save_button)

        delete_button = QPushButton('Borrar', self)
        delete_button.clicked.connect(self.delete_calculation)
        layout.addWidget(delete_button)

        self.setLayout(layout)

    def handle_button_click(self, text):
        current_text = self.result_display.text()
        self.result_display.setText(current_text + text)

    def calculate_result(self):
        try:
            expression = self.result_display.text()
            result = eval(expression)
            self.result_display.setText(str(result))
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error en la expresión: {str(e)}', QMessageBox.StandardButton.Ok)

    def save_calculation(self):
        expression = self.result_display.text()

        try:
            result = eval(expression)
            operands = [float(op) for op in expression.split('+') + expression.split('-') + expression.split('*') + expression.split('/')]

            model = QSqlTableModel()
            model.setTable('calculations')
            model.insertRow(0)
            model.setData(model.index(0, 1), operands[0])
            model.setData(model.index(0, 2), operands[1])
            model.setData(model.index(0, 3), expression.replace(str(operands[0]), '').replace(str(operands[1]), ''))
            model.setData(model.index(0, 4), result)

            if not model.submitAll():
                QMessageBox.critical(self, 'Error', 'Error al guardar el cálculo', QMessageBox.StandardButton.Ok)
            else:
                self.calculation_table.setRowCount(self.calculation_table.rowCount() + 1)
                self.populate_table()

        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Error en la expresión: {str(e)}', QMessageBox.StandardButton.Ok)

    def delete_calculation(self):
        selected_row = self.calculation_table.currentRow()

        if selected_row >= 0:
            model = QSqlTableModel()
            model.setTable('calculations')
            model.setFilter(f'id = {selected_row + 1}')  # id en la base de datos comienza desde 1
            model.select()

            if model.rowCount() > 0:
                model.removeRow(0)
                if not model.submitAll():
                    QMessageBox.critical(self, 'Error', 'Error al borrar el cálculo', QMessageBox.StandardButton.Ok)
                else:
                    self.populate_table()
            else:
                QMessageBox.critical(self, 'Error', 'La fila seleccionada no existe en la base de datos', QMessageBox.StandardButton.Ok)
        else:
            QMessageBox.critical(self, 'Error', 'Por favor, selecciona una fila para borrar', QMessageBox.StandardButton.Ok)

    def populate_table(self):
        model = QSqlTableModel()
        model.setTable('calculations')
        model.select()

        row_count = model.rowCount()

        self.calculation_table.setRowCount(row_count)

        for row in range(row_count):
            for col in range(3):
                item = model.index(row, col)
                self.calculation_table.setItem(row, col, QTableWidgetItem(str(item.data())))


def main():
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
