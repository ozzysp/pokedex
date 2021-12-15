from controller.type_poke import Type_poke
from qt_core import *

FILE_UI = 'view/pokemon.ui'


class CardPokemon(QWidget):
    def __init__(self, poke, mainWindow):
        super().__init__()
        uic.loadUi(FILE_UI, self)
        self.mainWindow = mainWindow

        self.poke = poke

        self.id_label.setText('# '+str(self.poke.id))
        self.nome_label.setText(self.poke.nome[0].upper()+self.poke.nome[1:])
        self.img_label.setPixmap(self.poke.img)
        self.loadTypes(poke.tipos)

        # personalizações
        self.img_label.setStyleSheet(
            "background-image : url(assets/patterns/pokeball.svg); background-repeat: no-repeat; background-position: right; background-size: auto; ")
        self.frame.setStyleSheet(
            ".QFrame::hover {background-color : rgb(222, 221, 218);}"
            ".QFrame {background-color : rgb(255, 255, 255);border: 1px solid; border-radius: 10px; border-color: rgb(192, 191, 188);}")

    def mousePressEvent(self, event):
        self.mainWindow.showInfoPoke(self.poke)

    def loadTypes(self, type_list):
        for type in type_list:
            self.type_layout.addWidget(Type_poke(type))
