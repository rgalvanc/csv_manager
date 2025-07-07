import os

class CSVModel:


    def __init__(self, filepath):
        self.filepath = filepath
        self.data = []



    def load_data(self):
        if not os.path.isfile(self.filepath):
            raise FileNotFoundError("Archivo no encontrado.")

        with open(self.filepath, newline='', encoding='utf-8') as csvfile:
            lines = csvfile.readlines()



        for i, line in enumerate(lines):
            line = line.strip()
            if not line:
                continue

            #headers de la tabla
            if i == 0:
                # Primera línea: encabezados
                headers = line.strip('#').split(';') # hacer que no se visualice el # y dividir por ;
                self.data.append(headers)
            else:
                is_active = True
                if line.startswith('#'):
                    is_active = False
                    line = line[1:]  # quitar el '#'

                row = line.split(';')
                row.append("1" if is_active else "0")  # Agregamos columna de estado
                self.data.append(row)

        return self.data

    def get_headers(self):
        return self.data[0] if self.data else []

    def get_all_rows(self):
        return self.data[1:] if len(self.data) > 1 else []

    def get_active_rows(self):
        return [row for row in self.get_all_rows() if row[-1] == "1"]

    def get_inactive_rows(self):
        return [row for row in self.get_all_rows() if row[-1] == "0"]
