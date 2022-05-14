import json
import os

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Design.Code.registration import *

from Services.AccountService import AccountService


# Registration window
class RegistrationWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        self._translate = QtCore.QCoreApplication.translate
        QtWidgets.QWidget.__init__(self, parent)
        self.accountService = AccountService()
        self.registrationWindow = Registration()
        self.registrationWindow.setupUi(self)

        # Turning off the default borders of the program window
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center()

        # Button handlers
        self.registrationWindow.closeButton.clicked.connect(lambda: self.close())
        self.registrationWindow.minimizeButton.clicked.connect(lambda: self.showMinimized())
        self.registrationWindow.registerButton.clicked.connect(lambda: self.register())


    # Dragging a frameless window
    # ==================================================================
    def center(self):
        qr = self.frameGeometry()
        center = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(center)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        try:
            delta = QtCore.QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        except AttributeError:
            pass
    # ==================================================================

    # Register user
    def register(self):
        username = self.registrationWindow.usernameLineEdit.text()
        email = self.registrationWindow.emailLineEdit.text(0)
        password = self.registrationWindow.passwordLineEdit.text()
        #self.accountService.login_user(username, password)

        if len(password) > 8 and len(username) != 0:
            response = self.accountService.login_user(username, password)
            with open(os.path.join("data", "config.json"), "w") as file:
                data = {"username": username, "token": response['token']}
                json.dump(data, file, indent=6)

        else:
            message = "Incorrect username or password"
            QtWidgets.QMessageBox.about(self, "Error", message)