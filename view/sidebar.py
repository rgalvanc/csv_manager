from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize


class Sidebar(QWidget):
    def __init__(self):
        super().__init__()

        # Colapso del sidebar
        self.collapsed = False
        self.expanded_width = 200
        self.collapsed_width = 60

        self.setFixedWidth(self.expanded_width)   #fijo el ancho dependiendo de si está expandido = 200 ; colapsado = 60
        self.buttons = []

        # Layout principal
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # Boton toggle (colapsar/expandir)
        self.toggle_btn = QPushButton("⮜")
        self.toggle_btn.setObjectName("toggleButton")
        self.toggle_btn.setCursor(Qt.PointingHandCursor)
        self.toggle_btn.clicked.connect(self.toggle_sidebar) #accion
        self.layout.addWidget(self.toggle_btn)

        #botones del sidebar (ejemplo inicial)
        self.nav_buttons = [
            ("Home", "resources/icons/dashboard.svg"),
            ("CSV", "resources/icons/orders.svg"),
            ("Settings", "resources/icons/settings.svg"),
        ]

        for name, icon_path in self.nav_buttons:
            btn = QPushButton(name)
            btn.setObjectName("sidebarButton")
            btn.setIcon(QIcon(icon_path))
            btn.setIconSize(QSize(40, 40))
            btn.setCursor(Qt.PointingHandCursor)
            btn.setMinimumHeight(40)
            self.layout.addWidget(btn)
            self.buttons.append(btn)

        self.layout.addStretch()  #rellena el espacio sobrante

        #APARIENCIA DEL SIDEBAR CON LOS BOTONES. DE MOMENTO AQUI PERO DEBERIA METERLO EN ARCHIVO STYLE LUEGO.
        self.setStyleSheet("""
            QWidget {
                background-color: #100a2b;
            }

            QPushButton#sidebarButton {
                background-color: transparent;
                border: none;
                color: #100a2b;
                padding: 12px 20px;
                text-align: left;
                font-size: 22px;
                border-radius: 12px;
            }

            QPushButton#sidebarButton:hover {
                background-color: #968dba;
            }

            QPushButton#toggleButton {
                background-color: transparent;
                border: none;
                color: #100a2b;
                font-size: 22px;
                padding: 10px;
                border-radius: 12px;
            }

            QPushButton#toggleButton:hover {
                background-color: #968dba;
            }
        """)

    #Metodo para expandir/colapsar el sidebar
    def toggle_sidebar(self):
        self.collapsed = not self.collapsed

        if self.collapsed:
            self.setFixedWidth(self.collapsed_width)
            self.toggle_btn.setText("⮞")
            for btn in self.buttons:
                btn.setText("")  # Oculta texto
        else:
            self.setFixedWidth(self.expanded_width)
            self.toggle_btn.setText("⮜")
            for i, (name, _) in enumerate(self.nav_buttons):
                self.buttons[i].setText(name)
