from Design.Code.change_password_window import *
from Windows.registrationWindow import *
from Services.AccountService import AccountService
from Services.MessageService import MessageService


class ChangePasswordWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        self._translate = QtCore.QCoreApplication.translate
        QtWidgets.QWidget.__init__(self, parent)
        self.accountService = AccountService()
        self.messageService = MessageService()
        self.changePasswordWindow = ChangePassword()
        self.changePasswordWindow.setupUi(self)

        # Turning off the default borders of the program window
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center()

        # Button handlers
        self.changePasswordWindow.closeButton.clicked.connect(lambda: self.close())
        self.changePasswordWindow.cancelButton.clicked.connect(lambda: self.close())
        self.changePasswordWindow.saveButton.clicked.connect(lambda: self.change_password())

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

    def change_password(self):
        old_password = self.changePasswordWindow.oldPasswordLineEdit.text()
        new_password = self.changePasswordWindow.newPasswordLineEdit.text()
        if len(old_password) != 0 and len(new_password) != 0:
            print(self.accountService.change_user_password(old_password, new_password))
        if len(old_password) == 0:
            self.changePasswordWindow.oldPasswordLabel.setText('''Your old password can't be empty''')
        if len(old_password) != 0:
            self.changePasswordWindow.oldPasswordLabel.setText('''Old Password''')
        if len(new_password) == 0:
            self.changePasswordWindow.newPasswordLabel.setText('''Your new password can't be empty''')
        if len(new_password) != 0:
            self.changePasswordWindow.newPasswordLabel.setText('''New Password''')
