from controller.type_poke import Type_poke
from qt_core import *

FILE_UI = 'view/pokemon.ui'


class Pokemon(QWidget):
    def __init__(self, poke):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.id = poke['id']
        self.nome = poke['name']

        self.id_label.setText('# '+str(self.id))
        self.nome_label.setText(self.nome[0].upper()+self.nome[1:])
        self.img_label.setPixmap(poke['pixmap'])
        self.loadTypes(poke['types'])

        # personalizações
        self.img_label.setStyleSheet(
            "background-image : url(assets/patterns/pokeball.svg); background-repeat: no-repeat; background-position: right; ")
        self.frame.setStyleSheet(
            ".QFrame::hover {background-color : rgb(222, 221, 218);}")

    def mousePressEvent(self, event):
        print('clicou >>>> ' + self.nome)

    def loadTypes(self, type_list):
        for type in type_list:
            self.type_layout.addWidget(Type_poke(type['type']['name']))
