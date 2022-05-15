import os
import json
from Design.Code.login import *
import Windows.mainWindow as mainWindow
import Windows.registrationWindow as rWindow
from Services.AccountService import AccountService
import constants


# Login window
class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        self._translate = QtCore.QCoreApplication.translate
        QtWidgets.QWidget.__init__(self, parent)
        self.accountService = AccountService()
        self.loginWindow = Login()
        self.loginWindow.setupUi(self)

        # Turning off the default borders of the program window
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center()

        # Button handlers
        self.loginWindow.closeButton.clicked.connect(lambda: self.close())
        self.loginWindow.minimizeButton.clicked.connect(lambda: self.showMinimized())
        self.loginWindow.loginButton.clicked.connect(lambda: self.log_in())
        self.loginWindow.registerButton.clicked.connect(lambda: self.open_registration_window())

    # Dragging a frameless window
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

    # Log in user
    def log_in(self):
        username = self.loginWindow.usernameLineEdit.text()
        password = self.loginWindow.passwordLineEdit.text()
        if len(password) >= 8 and len(username) != 0:
            response = self.accountService.login_user(username, password)
            print(response.json()['id'])
            with open(os.path.join("data", "config.json"), "w") as file:
                data = {'userId': response.json()['id'], 'username': username, 'token': response.json()['token']}
                json.dump(data, file, indent=6)
            if response.status_code == 200:
                main_window = mainWindow.MainWindow(self)
                self.close()
                main_window.show()
            else:
                message = "Log in error"
                QtWidgets.QMessageBox.about(self, "Error", message)
        else:
            message = "Incorrect username or password"
            QtWidgets.QMessageBox.about(self, "Error", message)

    # Open window for user registration
    def open_registration_window(self):
        register_window = rWindow.RegistrationWindow(self)
        self.hide()
        register_window.show()







