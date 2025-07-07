from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox
from view.table_widget import CSVTable

class CSV(QWidget):

    def __init__(self, model):
        super().__init__()
        self.model = model

        self.layout = QVBoxLayout(self)
        self.filter_combo = QComboBox()
        self.filter_combo.addItems(["Mostrar activos", "Mostrar todos"])
        self.filter_combo.currentIndexChanged.connect(self.update_table)

        self.table = CSVTable(model)

        self.layout.addWidget(self.filter_combo)
        self.layout.addWidget(self.table)

        self.update_table()

    def update_table(self):
        mostrar_todos = self.filter_combo.currentText() == "Mostrar todos"
        rows = self.model.get_all_rows() if mostrar_todos else self.model.get_active_rows()
        self.table.update_data(rows)

