from PyQt5.QtWidgets import QDialog,QVBoxLayout,QLabel

class DetailView(QDialog):
    def __init__(self,row_data,headers,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Datos por CAS")
        self.setMinimumWidth(400)

        layout = QVBoxLayout()
        for header,value in zip(headers,row_data):
            label = QLabel(f"<b>{header}:</b> {value}")
            layout.addWidget(label)

        self.setLayout(layout)