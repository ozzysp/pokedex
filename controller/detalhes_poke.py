from qt_core import *

FILE_UI = 'view/detalhes_poke.ui'


class DetalhesPoke(QWidget):
    def __init__(self, poke, mainWindow):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.poke = poke
        self.id = poke.id
        self.nome = poke.nome

        self.id_label.setText('# '+str(self.id))
        self.nome_label.setText(self.nome[0].upper()+self.nome[1:])
        self.img_label.setPixmap(poke.img)

       

        self.voltar.clicked.connect(
            lambda: mainWindow.stackedWidget.setCurrentIndex(0))
