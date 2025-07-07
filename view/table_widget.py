from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QColor

class CSVTable(QTableWidget):
    def __init__(self, model):
        super().__init__()
        self.model = model  #CSVModel pasado como objeto
        self.headers = model.get_headers()  #cabeceras


        self.setColumnCount(len(self.headers))
        self.setHorizontalHeaderLabels(self.headers)
        self.setShowGrid(False)
        self.verticalHeader().setVisible(False)



    # Toma los datos del modelo y los visualiza en el QTableWidget

    def update_data(self, rows):
        self.clearContents()
        self.setRowCount(len(rows))
        self.setColumnCount(len(self.headers))
        self.setHorizontalHeaderLabels(self.headers)

        for row_idx, row in enumerate(rows):
            for col_idx, cell in enumerate(row[:-1]):  # Omitir columna de estado
                item = QTableWidgetItem(cell)
                if row[-1] == "0":
                    item.setBackground(QColor(200, 200, 200))
                self.setItem(row_idx, col_idx, item)
