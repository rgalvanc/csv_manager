from dataclasses import field
from os import close

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QFormLayout, QLineEdit, QPushButton


class DetailView(QDialog):
    def __init__(self,row_data,headers,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Datos por CAS")
        self.setMinimumWidth(500)

        layout = QVBoxLayout()
        form_layout = QFormLayout()
        for header,value in zip(headers,row_data):
            label = QLabel(header)
            field = QLineEdit(value)
            field.setReadOnly(True)
            form_layout.addRow(label,field)

        layout.addLayout(form_layout)

        close_btn = QPushButton("Close")
        close_btn.clicked.connect(self.accept)
        layout.addWidget(close_btn,alignment=Qt.AlignRight)

        self.setStyleSheet("""
                    QDialog {
                        background-color: #f8f9fa;
                        font-family: 'Segoe UI', sans-serif;
                        font-size: 14px;
                    }
                    QLabel {
                        color: #333;
                        font-weight: bold;
                    }
                    QLineEdit {
                        padding: 6px;
                        border: 1px solid #ccc;
                        border-radius: 6px;
                        background-color: #fff;
                    }
                    QPushButton {
                        background-color: #6b5bd1;
                        color: white;
                        padding: 8px 16px;
                        border-radius: 8px;
                        font-weight: bold;
                    }
                    QPushButton:hover {
                        background-color: #5749b5;
                    }
                """)


        self.setLayout(layout)