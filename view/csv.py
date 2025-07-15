from PyQt5.QtWidgets import QWidget, QVBoxLayout, QComboBox, QHBoxLayout, QLineEdit
from view.table_widget import CSVTable
from view.detail_view import DetailView

class CSV(QWidget):

    def __init__(self, model):
        super().__init__()
        self.model = model

        self.layout = QVBoxLayout(self)

        #fila compuesta por : filtro_combo y buscador de CAS
        filter_row = QHBoxLayout()

        #selector
        self.filter_combo = QComboBox()
        self.filter_combo.addItems(["Mostrar activos", "Mostrar todos"])
        self.filter_combo.currentIndexChanged.connect(self.update_table)

        filter_row.addWidget(self.filter_combo)

        #buscador
        self.search_input  = QLineEdit()
        self.search_input.setPlaceholderText("Buscar por CAS")
        self.search_input.textChanged.connect(self.update_table)
        filter_row.addWidget(self.search_input)

        self.table = CSVTable(model)

        self.table.cellClicked.connect(self.handle_row_click)

        #self.layout.addWidget(filter_row) no deja añadirlo directamente

        filter_container = QWidget()
        filter_container.setLayout(filter_row)
        self.layout.addWidget(filter_container)
        self.layout.addWidget(self.table)

        self.update_table()

    def handle_row_click(self, row,column):
        cas = self.table.item(row,1).text()

        # Filtrar datos (usar todos o solo activos según la opción actual)
        mostrar_todos = self.filter_combo.currentText() == "Mostrar todos"
        all_rows = self.model.get_all_rows() if mostrar_todos else self.model.get_active_rows()

        # Buscar la fila correspondiente al CAS
        matching_rows = [r for r in all_rows if r[1] == cas]

        if matching_rows:
            #print("Fila seleccionada por CAS:", matching_rows[0])
            headers = self.model.get_headers()
            detail_window = DetailView(matching_rows[0], headers,self)
            detail_window.exec_()
        else:
            print(f"No se encontró ninguna fila con CAS: {cas}")


    def update_table(self):

        #filtro por activos/mostrar todos
        mostrar_todos = self.filter_combo.currentText() == "Mostrar todos"
        rows = self.model.get_all_rows() if mostrar_todos else self.model.get_active_rows()


        #filtro por CAS
        search_text = self.search_input.text().strip().lower()
        if search_text:
            cas_colum_index= 1
            rows = [
                row for row in rows
                if search_text in row[cas_colum_index].lower()
            ]

        self.table.update_data(rows)

