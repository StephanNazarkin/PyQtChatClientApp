from Services.ChatroomService import ChatroomService
from constants import *
from Design.Code.create_chat_window import *


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
        if len(topic) == 0:
            self.createChatWindow.chatNameLabel.setText("Chat name can't be empty")
        else:
            self.createChatWindow.chatNameLabel.setText("Chat Name")
            response = chat_service.create_chatroom(topic, USER_ID)
            print(response)
