from qt_core import *
import requests
from services.api import buscar_pokemon

FILE_UI = 'view/pokemon.ui'


class Pokemon(QWidget):
    def __init__(self, data_poke):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.nome = data_poke['name']
        self.url = data_poke['url']

        self.nome_label.setText(self.nome[0].upper()+self.nome[1:])

        self.frame.setStyleSheet(
            """.QFrame{border: 1px solid;
                border-radius: 10px;
                padding: 2px;
                border-color: rgb(192, 191, 188);
                background-color: rgb(153, 193, 241);
            }""")

        self.loadDados()

    def loadDados(self):
        res = buscar_pokemon(self.url)
        self.id_label.setText('# '+str(res['id']))
        # obs.: Alguns possuem mais de um tipo
        type = res['types'][0]['type']['name']
        self.type_label.setText(type[0].upper()+type[1:])
        img = res['sprites']['front_default']

        self.img_label.setPixmap(self.loadImg(img))

        def icon_type(type): return f"assets/types/{type}.svg"
        self.type_icon_label.setPixmap(QPixmap(icon_type(type)))

    def loadImg(self, url_image):
        if url_image != "":
            image = QImage()
            img = requests.get(url_image).content
            image.loadFromData(img)
            return QPixmap(image)
