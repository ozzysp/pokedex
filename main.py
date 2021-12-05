# importa todas as bibliotecas definidas 
# no arquivo qt_core.py
from qt_core import *
#importa a classe MainWindow - Janela principal
from controller.main_window import MainWindow

if __name__ == "__main__":
    # cria a aplicação
    app = QApplication(sys.argv)
    #app.setWindowIcon(QIcon('assets/logo/logo.png'))
    app.setStyle('Fusion')
    # definir os widgets que aparecerão na tela
    window = MainWindow()
    window.show() # carregar o elemento para a tela



    #executar o aplicativo
    sys.exit(app.exec())