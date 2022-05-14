from Services.ChatroomService import ChatroomService
from Windows.settingsWindow import SettingsWindow
from constants import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Design.Code.chat_members_window import *
from Services.AccountService import AccountService
from Services.MessageService import MessageService


class ChatMembersWindow(QtWidgets.QMainWindow):
    def __init__(self, chat_id, parent=None):
        self._translate = QtCore.QCoreApplication.translate
        QtWidgets.QWidget.__init__(self, parent)
        self.accountService = AccountService()
        self.messageService = MessageService()
        self.chatroomService = ChatroomService()
        self.membersWindow = ChatMembers()
        self.membersWindow.setupUi(self)

        self.membersDict = {}
        self.adminsDict = {}
        self.restrictedUsersDict = {}
        self.contactsDict = {}

        self.membersWindow.makeAdminButton.hide()
        self.membersWindow.restrictUserButton.hide()
        self.membersWindow.deleteFromChatButton.hide()

        self.chatId = chat_id
        self.friend = ''
        self.selectedAccountId = ''
        self.selectedUserId = ''

        self.build_members()
        self.build_admins()
        self.build_restricted_users()
        self.build_contacts()

        '''self.timer = QTimer()
        self.timer.setInterval(2000)
        self.timer.timeout.connect(self.refresh_all_tabs)
        self.timer.start()'''

        # Turning off the default borders of the program window
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center()

        self.membersWindow.closeButton.clicked.connect(lambda: self.close())
        self.membersWindow.closeButton_2.clicked.connect(lambda: self.close())
        self.membersWindow.closeButton_3.clicked.connect(lambda: self.close())
        self.membersWindow.closeButton_4.clicked.connect(lambda: self.close())

        self.membersWindow.makeAdminButton.clicked.connect(lambda: self.make_admin())
        self.membersWindow.removeAdminButton.clicked.connect(lambda: self.remove_admin())
        self.membersWindow.restrictUserButton.clicked.connect(lambda: self.restrict_user())
        self.membersWindow.removeRestrictionButton.clicked.connect(lambda: self.remove_restriction())
        self.membersWindow.addToChatButton.clicked.connect(lambda: self.add_to_chat())
        self.membersWindow.deleteFromChatButton.clicked.connect(lambda: self.delete_from_chat())

        self.membersWindow.membersListWidget.clicked.connect(lambda: self.show_members_buttons())
        self.membersWindow.adminsWidgetList.clicked.connect(lambda: self.select_admin())
        self.membersWindow.mutedMembersListWidget.clicked.connect(lambda: self.select_muted_user())
        self.membersWindow.contactsListWidget.clicked.connect(lambda: self.select_contact())

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

    def refresh_all_tabs(self):
        self.build_members()
        self.build_admins()
        self.build_restricted_users()
        self.build_contacts()

    def build_members(self):
        chat_service = ChatroomService()
        response = chat_service.get_all_users_from_chat(self.chatId).json()['$values']
        self.membersWindow.membersListWidget.clear()
        for user in response:
            self.membersDict[user['user']['userName']] = [user['id'], user['user']['id']]
            item = QtWidgets.QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)
            item.setText(user['user']['userName'])
            self.membersWindow.membersListWidget.addItem(item)

    def build_admins(self):
        chat_service = ChatroomService()
        response = chat_service.get_all_admins(self.chatId).json()['$values']
        self.membersWindow.adminsWidgetList.clear()
        for user in response:
            self.adminsDict[user['user']['userName']] = [user['id'], user['user']['id']]
            item = QtWidgets.QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)
            item.setText(user['user']['userName'])
            self.membersWindow.adminsWidgetList.addItem(item)

    def build_restricted_users(self):
        chat_service = ChatroomService()
        response = chat_service.get_all_banned_users(self.chatId).json()['$values']
        self.membersWindow.mutedMembersListWidget.clear()
        for user in response:
            self.restrictedUsersDict[user['user']['userName']] = [user['id'], user['user']['id']]
            item = QtWidgets.QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)
            item.setText(user['user']['userName'])
            self.membersWindow.mutedMembersListWidget.addItem(item)

    def build_contacts(self):
        account_service = AccountService()
        response = account_service.get_all_friends(USER_ID).json()['$values']
        self.membersWindow.contactsListWidget.clear()
        for user in response:
            self.contactsDict[user['userName']] = user['id']
            item = QtWidgets.QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)
            item.setText(user['userName'])
            self.membersWindow.contactsListWidget.addItem(item)

    def show_members_buttons(self):
        if (self.membersWindow.makeAdminButton.isHidden() and
            self.membersWindow.restrictUserButton.isHidden() and
                self.membersWindow.deleteFromChatButton.isHidden()):
            self.membersWindow.makeAdminButton.show()
            self.membersWindow.restrictUserButton.show()
            self.membersWindow.deleteFromChatButton.show()
        username = self.membersWindow.membersListWidget.currentItem().text()
        self.selectedAccountId = self.membersDict[username][0]
        self.selectedUserId = self.membersDict[username][1]
        print(self.selectedAccountId, self.selectedUserId)

    def select_admin(self):
        username = self.membersWindow.adminsWidgetList.currentItem().text()
        self.selectedAccountId = self.membersDict[username][0]
        self.selectedUserId = self.membersDict[username][1]
        print(self.selectedAccountId, self.selectedUserId)

    def select_muted_user(self):
        if self.membersWindow.mutedMembersListWidget.currentItem() is not None:
            username = self.membersWindow.mutedMembersListWidget.currentItem().text()
            self.selectedAccountId = self.membersDict[username][0]
            self.selectedUserId = self.membersDict[username][1]
            print(self.selectedAccountId, self.selectedUserId)
        else:
            print(self.membersWindow.mutedMembersListWidget.currentItem())

    def select_contact(self):
        if self.membersWindow.contactsListWidget.currentItem() is not None:
            username = self.membersWindow.contactsListWidget.currentItem().text()
            self.selectedUserId = self.contactsDict[username]
            print(self.selectedUserId)
        else:
            pass

    def make_admin(self):
        chat_service = ChatroomService()
        print(self.selectedUserId)
        response = chat_service.set_admin(self.selectedAccountId)
        self.build_admins()
        print(response)

    def remove_admin(self):
        chat_service = ChatroomService()
        response = chat_service.unset_admin(self.selectedAccountId)
        self.build_admins()
        print(response)

    def restrict_user(self):
        chat_service = ChatroomService()
        response = chat_service.ban_user(self.selectedAccountId)
        self.build_restricted_users()
        print(response)

    def remove_restriction(self):
        chat_service = ChatroomService()
        response = chat_service.unban_user(self.selectedAccountId)
        self.build_restricted_users()
        print(response)

    def add_to_chat(self):
        chat_service = ChatroomService()
        response = chat_service.add_to_chatroom(self.chatId, self.selectedUserId)
        self.build_members()
        print(response.text)

    def delete_from_chat(self):
        chat_service = ChatroomService()
        print(self.selectedAccountId)
        response = chat_service.kick_user(self.selectedAccountId)
        self.build_members()
        print(response.text)


