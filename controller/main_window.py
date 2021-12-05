from controller.pokemon import Pokemon
from qt_core import *
from services.api import *
from services.worker import Worker

FILE_UI = 'view/main_window.ui'


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(FILE_UI, self)

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

    def progress_fn(self, i):
        msg = f"Carregando Pokemons... {i} de {NUMBER_MAX_POKEMONS_API}"
        self.statusbar.showMessage(msg)

    def insert_fn(self, t):
        # print(t)
        data_poker = t[0]
        info_poker = t[1]
        icon_poker = t[2]
        x = t[3]
        y = t[4]
        self.layout_pokemons.addWidget(
            Pokemon(data_poker, info_poker, icon_poker), x, y)

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
                    data_poker = list[i]
                    info_poker = buscar_pokemon(list[i]['url'])
                    icon_poker = loadImg(info_poker['sprites']['other']['home']['front_default'])
                    # emit os dados coletados
                    insert_callback.emit(
                        (data_poker, info_poker, icon_poker, lin, col))
                    i += 1
                lin += 1
        except:
            pass

        return "Carregamento concluído com sucesso!"

    def thread_error(self, err):
        print(err)
        self.statusbar.showMessage(
            "Erro ao carregar Pokemons. Por favor, tente novamente.")

    def print_result(self, result):
        self.statusbar.showMessage(result)
        self.buscar_poke.setEnabled(True)
