class NavigationController:
    def __init__(self, stacked_widget):
        self.stacked_widget = stacked_widget
        self.pages = {}


    def add_page(self, name: str, widget):
        index = self.stacked_widget.addWidget(widget)  #añadir paginas
        self.pages[name] = index

    def show_page(self, name: str):
        if name in self.pages:
            self.stacked_widget.setCurrentIndex(self.pages[name])  #vista de pagina actual

'QStackedWidget := contenedor para apilar varios widgets (paginas) pero solo mostrar uno a la vez. útil para sidebars, formularios con varias paginas...'