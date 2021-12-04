import sys, os, time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import * 
from PyQt5 import uic

def getAbsPath(path):
    ui_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(ui_path, path)
