from assets.types.color_types import color_type
from qt_core import *

FILE_UI = 'view/type_poke.ui'


class Type_poke(QWidget):
    def __init__(self, type_poke):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        self.icon.setPixmap(QPixmap(f"assets/types/{type_poke}.svg"))
        self.type.setText(type_poke[0].upper()+type_poke[1:])
        
        rgb = color_type(type_poke)
        sheet = """.QFrame{border: 1px solid;
               border-radius: 10px;
               padding: 2px;
               border-color: rgb(192, 191, 188);
               background-color: """+str(rgb)+""";
           }"""
        self.frame.setStyleSheet(sheet)
