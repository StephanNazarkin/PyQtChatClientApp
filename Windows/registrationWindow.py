import json
import os
import re
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Design.Code.registration import *
import Windows.loginWindow as lWindow

from Services.AccountService import AccountService


# Registration window
class RegistrationWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        self._translate = QtCore.QCoreApplication.translate
        QtWidgets.QWidget.__init__(self, parent)
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
        self.registrationWindow.loginButton.clicked.connect(lambda: self.show_login_window())


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
        email = self.registrationWindow.emailLineEdit.text()
        password = self.registrationWindow.passwordLineEdit.text()
        #self.accountService.login_user(username, password)

        EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

        if len(email) == 0 or len(password) < 8 or len(username) == 0:
            print("error")
            message = "Incorrect username, email or password"
            QtWidgets.QMessageBox.about(self, "Error", message)

        elif len(password) >= 8 and len(username) != 0:
            print('OK')
            account_service = AccountService()
            response = account_service.register_user(username, email, password)
            if response.status_code != 200:
                message = "Check the entered data"
                QtWidgets.QMessageBox.about(self, "Error", message)
            else:
                self.close()
                login_window = lWindow.LoginWindow()
                login_window.show()
            print(response.status_code)

    def show_login_window(self):
        self.close()
        login_window = lWindow.LoginWindow()
        login_window.show()