import os
import csv

class CSVModel:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = []

    def load_data(self):
        if not os.path.isfile(self.filepath):
            raise FileNotFoundError("Archivo no encontrado.")

        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            lines = csvfile.readlines()

        data = []
        #headers = []
        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue

            if i == 0:
                # Primera línea: encabezados
                headers = line.lstrip('#').split(';')
                data.append(headers)
            else:
                is_active = True
                if line.startswith('#'):
                    is_active = False
                    line = line[1:]  # quitar el '#'

                row = line.split(';')
                row.append("1" if is_active else "0")  # Agregamos columna de estado
                data.append(row)

        self.data = data
        return self.data
