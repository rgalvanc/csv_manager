from model.csv_model import CSVModel

def main():
    csv_path = 'data/cyclo-xxx.csv' # TODO carga del archivo. Luego añadir un buscador
    model = CSVModel(csv_path)

    try:
        data = model.load_data()
        for row in data:
            print(row) # TODO luego diferenciar los distintos atributos
    except Exception as e:
        print(e)

#inicialización
if __name__ == '__main__':
    main()