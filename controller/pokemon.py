from controller.type_poke import Type_poke
from qt_core import *
from services.api import buscar_pokemon

FILE_UI = 'view/pokemon.ui'


class Pokemon(QWidget):
    def __init__(self, data_poke):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.nome = data_poke['name']
        self.url = data_poke['url']

        self.nome_label.setText(self.nome[0].upper()+self.nome[1:])

        res = buscar_pokemon(self.url)
        self.id_label.setText('# '+str(res['id']))

        img = res['sprites']['front_default']
        self.img_label.setPixmap(loadImg(img))

        self.loadTypes(res['types'])

    def loadTypes(self, type_list):
        for type in type_list:
            self.type_layout.addWidget(Type_poke(type['type']['name']))
