from controller.pokemon import Pokemon
from qt_core import *
from services.api import *
from services.worker import Worker

FILE_UI = 'view/main_window.ui'


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)

        # lista de pokemons
        self.lista_pokes = []
        self.lista_search = []

        # 
        self.scrollArea.setStyleSheet(
            ".QScrollArea {border-color: rgb(192, 191, 188);}")

        # connect pesquisar
        self.buscar_poke.textEdited.connect(self.text_edited)
        self.buscar_poke.hide()

        self.threadpool = QThreadPool()
        worker = Worker(self.loadPokemons)

        # padrões
        worker.signals.result.connect(self.print_result)
        worker.signals.error.connect(self.thread_error)

        # personalizados
        worker.signals.progress.connect(self.progress_fn)
        worker.signals.insert.connect(self.insert_fn)

        # start
        self.threadpool.start(worker)

    def text_edited(self, search):
        for i in reversed(range(self.layout_pokemons.count())):
               self.layout_pokemons.itemAt(i).widget().deleteLater()
        if search == "":
            self.carrega_dados(self.lista_pokes)
        else:
            lista_search = []
            for p in self.lista_pokes:
                if search in p['name']:
                    lista_search.append(p)
            self.carrega_dados(lista_search)

    def carrega_dados(self, lista):
        lin = 0
        i = 0
        try:
            while i < len(lista):
                for col in range(0, 3):
                    self.layout_pokemons.addWidget(
                        Pokemon(lista[i]), lin, col)
                    i += 1
                lin += 1
        except:
            pass

    def progress_fn(self, i):
        msg = f"Carregando Pokemons... {i} de {NUMBER_MAX_POKEMONS_API}"
        self.statusbar.showMessage(msg)

    def insert_fn(self, t):
        # print(t)
        poke = t[0]
        x = t[1]
        y = t[2]
        self.lista_pokes.append(poke)
        self.layout_pokemons.addWidget(
            Pokemon(poke), x, y)

    def loadPokemons(self, progress_callback, insert_callback):
        res = buscar_pokemons()
        list = res['results']
        lin = 0
        i = 0
        try:
            while i < len(list):
                for col in range(0, 3):
                    progress_callback.emit(i)
                    # pega os dados que exigem request
                    data_poke = list[i]
                    info_poke = buscar_pokemon(list[i]['url'])
                    poke = {'id': info_poke['id'],
                            'name': data_poke['name'],
                            'pixmap': loadImg(info_poke['sprites']['other']['dream_world']['front_default']),
                            'types': info_poke['types']
                            }
                    # emit os dados coletados
                    insert_callback.emit((poke, lin, col))
                    i += 1
                lin += 1
        except Exception as e:
            print(e)

        return "Carregamento concluído com sucesso!"

    def thread_error(self, err):
        print(err)
        self.statusbar.showMessage(
            "Erro ao carregar Pokemons. Por favor, tente novamente.")

    def print_result(self, result):
        self.statusbar.showMessage(result)
        self.buscar_poke.show()
