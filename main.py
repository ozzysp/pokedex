# importa todas as bibliotecas definidas 
# no arquivo qt_core.py
from qt_core import *
#importa a classe MainWindow - Janela principal
from controller.main_window import MainWindow

# cria a aplicação
app = QApplication(sys.argv)
app.setStyle('Fusion')
# definir os widgets que aparecerão na tela
window = MainWindow()
window.show() # carregar o elemento para a tela
# deixa para carregar após a abertura da janela
#window.loadPokemons()


#executar o aplicativo
app.exec()