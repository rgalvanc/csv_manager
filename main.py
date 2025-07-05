import sys
from PyQt5.QtWidgets import QApplication
from model.csv_model import CSVModel
from view.main_window import MainWindow
def main():
    csv_path = 'data/cyclo-xxx.csv'
    model = CSVModel(csv_path)
    data = model.load_data()

    app = QApplication(sys.argv)
    window = MainWindow(data)
    window.show()
    sys.exit(app.exec_())



#inicialización
if __name__ == '__main__':
    main()