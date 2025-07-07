from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import (
    QTableWidgetItem, QComboBox, QLabel, QPushButton,
    QHBoxLayout, QVBoxLayout, QTableWidget, QStackedWidget
)

from controller.nav_controller import NavigationController
from view.sidebar import Sidebar
from view.table_widget import CSVTable
from view.csv import CSV
from view.settings import Settings
from view.home import Home
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


        self.stack = QStackedWidget()
        main_layout.addWidget(self.stack)

        #CONTROL DE NAVEGACION
        self.navigator = NavigationController(self.stack)

        #instancio paginas
        self.csv_page = CSV(model)
        self.home_page = Home()
        self.settings_page = Settings()

        self.navigator.add_page("CSV",self.csv_page)
        self.navigator.add_page("Home",self.home_page)
        self.navigator.add_page("Settings",self.settings_page)

        #Vinculacion con los botones del sidebar
        self.sidebar.buttons[0].clicked.connect(lambda: self.navigator.show_page("Home"))
        self.sidebar.buttons[1].clicked.connect(lambda: self.navigator.show_page("CSV"))
        self.sidebar.buttons[2].clicked.connect(lambda: self.navigator.show_page("Settings"))

        #Pagina por defecto
        self.navigator.show_page("Home")








