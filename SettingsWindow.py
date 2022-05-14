from design.code.settings import *
from PyQt5.QtWidgets import *


# Окно с настройками клиента
class SettingPanel(QWidget):
    def __init__(self):
        super(SettingPanel, self).__init__()
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
