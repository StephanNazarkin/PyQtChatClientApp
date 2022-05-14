from design.code.mainpage import *
from SettingsWindow import SettingPanel

import sys


class Client(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_7.clicked.connect(self.setting_panel)

    def setting_panel(self):
        setting_win = SettingPanel(self)
        setting_win.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Client()
    myapp.show()
    sys.exit(app.exec_())