import csv
import os

class CSVModel:
    def __init__(self,filepath):
        self.filepath = filepath
        self.data = []

    def load_data(self):
        if not os.path.isfile(self.filepath):
            raise FileNotFoundError("Archivo no encontrado.")
        with open(self.filepath, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            self.data = [row for row in reader]
        return self.data