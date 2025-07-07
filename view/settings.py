from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout

class Settings(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel("Settings en construcción")
        label.setStyleSheet("font-size: 24px; color: gray;")
        layout.addWidget(label)
        layout.addStretch()
        self.setLayout(layout)
