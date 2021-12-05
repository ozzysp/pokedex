import sys
import os
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import requests


def getAbsPath(path):
    ui_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(ui_path, path)


def loadImg(url_image):
    if url_image != "":
        image = QImage()
        img = requests.get(url_image).content
        image.loadFromData(img)
        return QPixmap(image)

# self.frame.setStyleSheet(
        #    """.QFrame{border: 1px solid;
        #       border-radius: 10px;
        #       padding: 2px;
        #        border-color: rgb(192, 191, 188);
        #       background-color: rgb(153, 193, 241);
        #   }""")
