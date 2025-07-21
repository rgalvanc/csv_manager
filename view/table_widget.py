from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QMenu
from PyQt5.QtGui import QColor

class CSVTable(QTableWidget):
    def __init__(self, model,parent=None):
        super().__init__(parent)
        self.model = model  #CSVModel pasado como objeto
        self.headers = model.get_headers()  #cabeceras


        self.setColumnCount(len(self.headers))
        self.setHorizontalHeaderLabels(self.headers)
        self.setShowGrid(False)
        self.verticalHeader().setVisible(False)

        #Para poder eliminar una fila
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_right_btn_menu)




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

    #Menu de seleccion al clickar el boton derecho

    def show_right_btn_menu(self, pos):
        index = self.indexAt(pos)
        if not index.isValid():
            return

        #fila seleccionada
        row = index.row()
        cas_item = self.item(row, 1)
        if not cas_item:
            return

        menu = QMenu()
        delete_action = menu.addAction("Eliminar fila")
        action = menu.exec_(self.mapToGlobal(pos))
        if action == delete_action:
            parent = self.parent()
            if hasattr(parent, "confirm_delete_row"):
                parent.confirm_delete_row(row)

            else:
                print("⚠️ Debí haber estudiado medicina. Sería rica y más feliz")



