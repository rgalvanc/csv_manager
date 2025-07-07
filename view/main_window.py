from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (
    QTableWidgetItem, QComboBox, QLabel, QPushButton,
    QHBoxLayout, QVBoxLayout, QTableWidget
)
from view.sidebar import Sidebar
from view.table_widget import CSVTable
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.setWindowTitle("CSV Manager")
        self.resize(1200, 800)


        '''ESTRUCTURA INICIAL: de momento sin QTDesigner ya que tengo que familiarizarme con la aplicacion.
         Coloco los wigets "manualmente" y ya veré como mejorar la apariencia'''



        # --- Widget central ---  OJO : MainWindow solo admite un único widget central
        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget) #hay que instanciarlo

        # --- Layout principal horizontal --- "caja" para organizar las cosas de izq a derecha
        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        #Sidebar a la izquierda
        self.sidebar = Sidebar()
        main_layout.addWidget(self.sidebar)

        # --- Contenido principal (derecha) ---
        content_layout = QVBoxLayout()


        #TODO : AÑADIR EL COMBOBOX FILTRO Y LA TABLA AL COMBO A LA DERECHA Y QUE SE ACTIVE AL DARLE AL BOTON DE CSV

        # --- ComboBox filtro arriba ---
        self.filter_combo = QComboBox()
        self.filter_combo.addItems(["Mostrar activos", "Mostrar todos"])
        self.filter_combo.currentIndexChanged.connect(self.update_table)
        content_layout.addWidget(self.filter_combo)

        # --- Tabla principal ---
        self.table = CSVTable(model)
        content_layout.addWidget(self.table)

        main_layout.addLayout(content_layout)

        self.update_table()

    def update_table(self):
        mostrar_todos = self.filter_combo.currentText() == "Mostrar todos"
        rows = self.model.get_all_rows() if mostrar_todos else self.model.get_active_rows()
        self.table.update_data(rows)




