from controller.type_poke import Type_poke
from qt_core import *

FILE_UI = 'view/pokemon.ui'


class Pokemon(QWidget):
    def __init__(self, data_poke, info_poker, icon_poker):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.nome = data_poke['name']
        self.url = data_poke['url']

        self.nome_label.setText(self.nome[0].upper()+self.nome[1:])

        self.id_label.setText('# '+str(info_poker['id']))

        self.img_label.setPixmap(icon_poker)

        self.loadTypes(info_poker['types'])

        self.frame.setStyleSheet("QFrame::hover"
                                 "{"
                                 "background-color : rgb(222, 221, 218);"
                                 "}")

    def mousePressEvent(self, event):

        print('clicou >>>> ' + self.nome)

    def loadTypes(self, type_list):
        for type in type_list:
            self.type_layout.addWidget(Type_poke(type['type']['name']))
