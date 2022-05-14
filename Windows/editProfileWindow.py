from Design.Code.edit_profile_window import *
from Windows.registrationWindow import *
from Windows.changePasswordWindow import *
from Services.AccountService import AccountService
import Windows.settingsWindow as sw


class EditProfileWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        self._translate = QtCore.QCoreApplication.translate
        QtWidgets.QWidget.__init__(self, parent)
        self.accountService = AccountService()
        self.editProfileWindow = EditProfile()
        self.editProfileWindow.setupUi(self)

        # Turning off the default borders of the program window
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center()

        # Button handlers
        self.editProfileWindow.closeButton.clicked.connect(lambda: self.close())
        self.editProfileWindow.cancelButton.clicked.connect(lambda: self.back())
        self.editProfileWindow.saveButton.clicked.connect(lambda: self.update_profile())
        self.editProfileWindow.changePasswordButton.clicked.connect(lambda: self.open_change_password_window())
        #self.editProfileWindow.backButton.clicked.connect(lambda: self.back())

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

    def update_profile(self):
        username = self.editProfileWindow.usernameLineEdit.text()
        email = self.editProfileWindow.emailLineEdit.text()
        print(username, email)
        self.accountService.update_user(username, email)

    def open_change_password_window(self):
        change_password_window = ChangePasswordWindow(self)
        change_password_window.show()

    def back(self):
        settings_window = sw.SettingsWindow(self)
        settings_window.close()







