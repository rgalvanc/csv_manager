from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class Home(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("Home en construcción")
        label.setStyleSheet("font-size: 24px; color: gray;")
        layout.addWidget(label)
        layout.addStretch()
        self.setLayout(layout)
