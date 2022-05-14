from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from mydesign import Ui_MainWindow  # импорт нашего сгенерированного файла
#from downloaded import Ui_MainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        #self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


app = QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())