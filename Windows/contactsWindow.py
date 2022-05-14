from Services.ChatroomService import ChatroomService
from constants import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Design.Code.contacts_window import *
from Services.AccountService import AccountService
from Services.MessageService import MessageService


class ContactsWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        self._translate = QtCore.QCoreApplication.translate
        QtWidgets.QWidget.__init__(self, parent)
        self.accountService = AccountService()
        self.messageService = MessageService()
        self.chatroomService = ChatroomService()
        self.contactsWindow = Contacts()
        self.contactsWindow.setupUi(self)

        self.friend = ''
        self.selectedUser = ''

        self.build_contacts()
        self.build_blocked()

        # Turning off the default borders of the program window
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center()

        self.contactsWindow.deleteContactButton.hide()
        self.contactsWindow.blockButton.hide()
        self.contactsWindow.unblockButton.hide()
        # Button handlers
        self.contactsWindow.closeButton.clicked.connect(lambda: self.close())
        self.contactsWindow.closeButton_2.clicked.connect(lambda: self.close())
        self.contactsWindow.closeButton_3.clicked.connect(lambda: self.close())
        self.contactsWindow.findButton.clicked.connect(lambda: self.find_user())
        self.contactsWindow.addContactButton.clicked.connect(lambda: self.add_contact(self.friend))
        self.contactsWindow.blockButton.clicked.connect(lambda: self.block_user())
        self.contactsWindow.deleteContactButton.clicked.connect(lambda: self.delete_friend())
        self.contactsWindow.unblockButton.clicked.connect(lambda: self.unblock_user())

        self.contactsWindow.contactsListWidget.itemClicked.connect(self.show_contacts)
        self.contactsWindow.blockedListWidget.itemClicked.connect(self.show_blocked)

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

    def build_contacts(self):
        account_service = AccountService()
        response = account_service.get_all_friends(USER_ID).json()['$values']
        self.contactsWindow.contactsListWidget.clear()
        for user in response:
            item = QtWidgets.QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)
            item.setText(user['userName'])
            self.contactsWindow.contactsListWidget.addItem(item)

    def build_blocked(self):
        account_service = AccountService()
        response = account_service.get_all_blocked_users(USER_ID).json()['$values']
        self.contactsWindow.blockedListWidget.clear()
        for user in response:
            item = QtWidgets.QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)
            item.setText(user['userName'])
            self.contactsWindow.blockedListWidget.addItem(item)

    def find_user(self):
        account_service = AccountService()
        username = self.contactsWindow.searchLineEdit.text()
        self.friend = account_service.get_user_by_username(username).json()
        print(self.friend)
        self.contactsWindow.usernameLabel.setText("{username}".format(username=username))

    def add_contact(self, friend):
        account_service = AccountService()
        print(account_service.add_friend(friend['id']).text)
        self.contactsWindow.contactsListWidget.clear()
        self.build_contacts()

    def show_contacts(self):
        if self.contactsWindow.deleteContactButton.isHidden() and self.contactsWindow.blockButton.isHidden():
            self.contactsWindow.deleteContactButton.show()
            self.contactsWindow.blockButton.show()
        account_service = AccountService()
        username = self.contactsWindow.contactsListWidget.currentItem().text()
        self.selectedUser = account_service.get_user_by_username(username).json()
        print(self.selectedUser['id'])

    def show_blocked(self):
        if self.contactsWindow.unblockButton.isHidden():
            self.contactsWindow.unblockButton.show()
        account_service = AccountService()
        username = self.contactsWindow.blockedListWidget.currentItem().text()
        self.selectedUser = account_service.get_user_by_username(username).json()
        print(self.selectedUser['userName'])

    def block_user(self):
        account_service = AccountService()
        print(self.selectedUser['id'])
        print(account_service.block_user(self.selectedUser['id']))
        self.build_blocked()

    def unblock_user(self):
        account_service = AccountService()
        print(self.selectedUser['id'])
        print(account_service.unblock_user(self.selectedUser['id']))
        self.build_blocked()

    def delete_friend(self):
        account_service = AccountService()
        print(self.selectedUser['id'])
        print(account_service.delete_friend(self.selectedUser['id']))
        self.build_contacts()

