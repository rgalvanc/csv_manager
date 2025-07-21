from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QFormLayout, QLineEdit, QPushButton, QCheckBox, QHBoxLayout



class DetailView(QDialog):
    data_updated = pyqtSignal()
    def __init__(self,row_data,headers,model, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Datos por CAS")
        self.setMinimumWidth(500)

        self.row_data = row_data
        self.headers = headers
        self.model = model
        self.index_in_model = model.data.index(row_data)

        self.fields = []

        layout = QVBoxLayout()
        form_layout = QFormLayout()
        for header,value in zip(headers,row_data[:-1]):
            label = QLabel(header)
            field = QLineEdit(value)
           # field.setReadOnly(True)
            form_layout.addRow(label,field)
            self.fields.append(field)

        layout.addLayout(form_layout)

        self.active_checkbox = QCheckBox("Fila activa")
        self.active_checkbox.setChecked(row_data[-1]=="1")
        layout.addWidget(self.active_checkbox)

        button_layout = QHBoxLayout()
        save_btn = QPushButton("Guardar cambios")
        save_btn.clicked.connect(self.save_changes)
        layout.addWidget(save_btn)

        close_btn = QPushButton("Cerrar")
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

    def save_changes(self):
        new_row = [field.text() for field in self.fields] #fila con los datos editados
        new_row.append("1" if self.active_checkbox.isChecked() else "0")
        self.model.data[self.index_in_model] = new_row #actualizamos la fila que se ha seleccionado
        self.model.save_data()
        self.data_updated.emit()
        self.accept()