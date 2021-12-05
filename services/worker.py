
from qt_core import *


class WorkerSignals(QObject):
    # padrão
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    # meus
    progress = pyqtSignal(int)
    insert = pyqtSignal(tuple)


class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress
        self.kwargs['insert_callback'] = self.signals.insert

    @pyqtSlot()
    def run(self):
        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except Exception as e:
            # traceback.print_exc()
            # lança o tipo e a descrição da exceção
            self.signals.error.emit((type(e), str(e)))
        else:
            # Return the result of the processing
            self.signals.result.emit(result)