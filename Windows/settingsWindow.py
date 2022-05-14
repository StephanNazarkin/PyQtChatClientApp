from Design.Code.settings_window import *
from Services.AccountService import AccountService
from Windows.editProfileWindow import EditProfileWindow
from Windows.contactsWindow import ContactsWindow
from Windows.createChatWindow import CreateChatWindow
import Windows.mainWindow


class SettingsWindow(QtWidgets.QDialog):
    def __init__(self, parent=None):
        self._translate = QtCore.QCoreApplication.translate
        QtWidgets.QWidget.__init__(self, parent)
        self.accountService = AccountService()
        #self.messageService = MessageService()
        self.settingsWindow = SettingsChatWindow()
        self.settingsWindow.setupUi(self)

        # Turning off the default borders of the program window
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center()

        self.settingsWindow.closeButton.clicked.connect(lambda: self.close())
        self.settingsWindow.editProfileButton.clicked.connect(lambda: self.open_edit_profile_window())
        self.settingsWindow.contactsButton.clicked.connect(lambda: self.open_contacts_window())
        self.settingsWindow.createChatButton.clicked.connect(lambda: self.open_create_chat_window())
        self.settingsWindow.logoutButton.clicked.connect(lambda: self.logout_user())

    # Dragging a frameless window
    # ==================================================================
    def center(self):
        qr = self.frameGeometry()
        center = QtWidgets.QDesktopWidget().availableGeometry().center()
        print(center, qr)
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

    def open_edit_profile_window(self):
        edit_profile_window = EditProfileWindow(self)
        edit_profile_window.show()

    def open_contacts_window(self):
        contacts_window = ContactsWindow(self)
        contacts_window.show()

    def open_create_chat_window(self):
        create_chat_window = CreateChatWindow()
        create_chat_window.show()

    def logout_user(self):
        main_window = Windows.mainWindow.MainWindow(self)
        print(main_window.close())
