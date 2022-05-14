from Services.ChatroomService import ChatroomService
from constants import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Design.Code.create_chat_window import *
from Services.AccountService import AccountService
from Services.MessageService import MessageService
import Windows.mainWindow as mw


class CreateChatWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        self._translate = QtCore.QCoreApplication.translate
        QtWidgets.QWidget.__init__(self, parent)
        self.chatroomService = ChatroomService()
        self.createChatWindow = CreateChat()
        self.createChatWindow.setupUi(self)

        self.friend = ''
        self.selectedUser = ''

        #self.build_contacts()
        #self.build_blocked()

        # Turning off the default borders of the program window
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.center()

        self.createChatWindow.closeButton.clicked.connect(lambda: self.close())
        self.createChatWindow.cancelButton.clicked.connect(lambda: self.close())
        self.createChatWindow.saveButton.clicked.connect(lambda: self.create_chat())

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

    def create_chat(self):
        chat_service = ChatroomService()
        topic = self.createChatWindow.chatNameLineEdit.text()
        response = chat_service.create_chatroom(topic, USER_ID)
        main_window = mw.MainWindow()
        main_window.build_chats()
        print(response)
