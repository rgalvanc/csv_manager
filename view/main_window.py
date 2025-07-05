from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, data):
        super().__init__()
        self.setWindowTitle("CSV Manager")
        self.resize(800, 600)

        central_widget = QtWidgets.QWidget(self)
        layout = QtWidgets.QVBoxLayout()
        self.table = QtWidgets.QTableWidget()
        layout.addWidget(self.table)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.populate_table(data)

    def populate_table(self, data):
        if not data:
            return

        headers = data[0]
        rows = data[1:]

        self.table.setColumnCount(len(headers))
        self.table.setRowCount(len(rows))
        self.table.setHorizontalHeaderLabels(headers)

        for row_idx, row in enumerate(rows):
            for col_idx, cell in enumerate(row):
                item = QTableWidgetItem(cell)
                self.table.setItem(row_idx, col_idx, item)
