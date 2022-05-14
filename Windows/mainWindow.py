from Services.ChatroomService import ChatroomService
from Windows.chatMembersWindow import ChatMembersWindow
from Windows.settingsWindow import SettingsWindow
from constants import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Design.Code.main_window_des import *
from Services.AccountService import AccountService
from Services.MessageService import MessageService


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        self._translate = QtCore.QCoreApplication.translate
        QtWidgets.QWidget.__init__(self, parent)
        self.accountService = AccountService()
        self.messageService = MessageService()
        self.chatroomService = ChatroomService()
        self.mainWindow = MainChatWindow()
        self.mainWindow.setupUi(self)
        self.chatDict = {}
        self.currentChatId = ''

        self.mainWindow.removeButton.hide()

        self.build_chats()

        '''self.timer = QTimer()
        self.timer.setInterval(500)
        self.timer.timeout.connect(self.build_chats)
        self.timer.start()'''

        # Turning off the default borders of the program window
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center()

        # Button handlers
        self.mainWindow.closeButton.clicked.connect(lambda: self.close())
        self.mainWindow.minimizeButton.clicked.connect(lambda: self.showMinimized())
        self.mainWindow.sendButton.clicked.connect(lambda: self.send_message())
        self.mainWindow.attachButton.clicked.connect(lambda: self.attach())
        self.mainWindow.settingsButton.clicked.connect(lambda: self.open_settings_window())
        self.mainWindow.refreshButton.clicked.connect(lambda: self.build_chats())
        self.mainWindow.removeButton.clicked.connect(lambda: self.delete_chat())
        self.mainWindow.addToChatButton.clicked.connect(lambda: self.open_chat_members_window())

        self.mainWindow.chatListWidget.itemClicked.connect(self.get_messages)

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

    def send_message(self):
        message_text = self.mainWindow.messageTextEdit.toPlainText()
        print(message_text)
        message_service = MessageService()
        if len(message_text) != 0:
            message_service.send_message(self.currentChatId, USER_ID, message_text)
            print(self.currentChatId)
            self.mainWindow.messageTextEdit.clear()
            item = QtWidgets.QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignRight)
            item.setText(f"{USER_NAME} (You):\n{message_text}")
            self.mainWindow.messageListWidget.addItem(item)
        else:
            pass

    def attach(self):
        path = QFileDialog.getOpenFileName(self, 'Open a file', '', 'All Files (*.*)')
        if path != ('', ''):
            print(path[0])
        print(path)
        self.mainWindow.messageListWidget.setWordWrap(True)
        icon = QtGui.QIcon(path[0])
        print(icon)
        item = QtWidgets.QListWidgetItem()
        item.setIcon(icon)
        item.setTextAlignment(QtCore.Qt.AlignRight)
        size = QtCore.QSize(300, 300)
        combo = QComboBox()
        self.mainWindow.messageListWidget.setIconSize(size)
        self.mainWindow.messageListWidget.addItem(item)
        self.mainWindow.messageListWidget.setItemAlignment(Qt.AlignRight)

    def build_chats(self):
        chat_service = ChatroomService()
        res = chat_service.get_all_chatrooms()
        self.mainWindow.chatListWidget.clear()
        for topic in res.json()['$values']:
            self.chatDict[topic['topic']] = topic['id']
            item = QtWidgets.QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)
            item.setText(topic['topic'])
            self.mainWindow.chatListWidget.addItem(item)

    def get_messages(self, item):
        self.mainWindow.chatLabel.setText(item.text())
        self.currentChatId = self.chatDict[item.text()]
        chat_serv = ChatroomService()
        response = chat_serv.get_owner(self.currentChatId)
        owner = response.json()['user']['userName']
        print(owner)
        if USER_NAME == owner:
            self.mainWindow.removeButton.show()
        else:
            self.mainWindow.removeButton.hide()
        ms = MessageService()
        res = ms.get_messages_from_chat(self.chatDict[item.text()])
        message_dict = {}
        self.mainWindow.messageListWidget.clear()
        if res.json()['$values']:
            for message in res.json()['$values']:
                if 'text' in message:
                    if message['user']['userName'] == USER_NAME:
                        item = QtWidgets.QListWidgetItem()
                        item.setTextAlignment(QtCore.Qt.AlignRight)
                        message_text = "{username} (YOU):\n{message}\n".format(username=message['user']['userName'],
                                                                               message=message['text'])
                        item.setText(message_text)
                        self.mainWindow.messageListWidget.addItem(item)
                    else:
                        item = QtWidgets.QListWidgetItem()
                        item.setTextAlignment(QtCore.Qt.AlignLeft)
                        message_text = "{username}:\n{message}\n".format(username=message['user']['userName'],
                                                                         message=message['text'])
                        item.setText(message_text)
                        self.mainWindow.messageListWidget.addItem(item)

    def open_settings_window(self):
        settings_window = SettingsWindow(self)
        settings_window.show()

    def open_chat_members_window(self):
        chat_members_window = ChatMembersWindow(self.currentChatId)
        print('error')
        chat_members_window.show()

    def delete_chat(self):
        chat_service = ChatroomService()
        print(chat_service.delete_chatroom(self.currentChatId))
