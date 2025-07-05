from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QTableWidgetItem, QComboBox


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, model):
        super().__init__()

        #estructura visual
        self.setWindowTitle("CSV Manager")
        self.resize(800, 600)

        self.model = model #CSVModel pasado como objeto
        self.headers = model.get_headers()


        central_widget = QtWidgets.QWidget(self)
        main_layout = QtWidgets.QVBoxLayout()

        #Topbar
        self.filter_combo = QComboBox()
        self.filter_combo.addItems(["Mostrar activos","Mostrar todos"])
        self.filter_combo.currentIndexChanged.connect(self.update_table)
        main_layout.addWidget(self.filter_combo)

        #Tabla
        self.table = QtWidgets.QTableWidget()
        main_layout.addWidget(self.table)


        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.update_table()

    #Toma los datos del modelo y los visualiza en el QTableWidget
    def update_table(self):
        mostrar_todos = self.filter_combo.currentText() == "Mostrar todos"

        rows = self.model.get_all_rows() if mostrar_todos  else self.model.get_active_rows()

        self.table.clearContents()
        self.table.setRowCount(len(rows))
        self.table.setColumnCount(len(self.headers) )  # Ocultar columna de estado
        self.table.setHorizontalHeaderLabels(self.headers)

        for row_idx, row in enumerate(rows):
            for col_idx, cell in enumerate(row[:-1]):
                item = QTableWidgetItem(cell)
                if mostrar_todos and row[-1] == "0":
                    item.setBackground(QColor(220, 220, 220))  # sombrear inactiva
                self.table.setItem(row_idx, col_idx, item)