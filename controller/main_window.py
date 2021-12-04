from controller.pokemon import Pokemon
from qt_core import *
from services.api import buscar_pokemons

FILE_UI = 'view/main_window.ui'
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)
    
    def loadPokemons(self):
        #self.clear()
        list = buscar_pokemons()
        
        i = 0
        for x in range(len(list)//2):
            for y in range(2):
                QApplication.processEvents()
                self.layout_pokemons.addWidget(Pokemon(list[i]), x, y)
                i+=1
                