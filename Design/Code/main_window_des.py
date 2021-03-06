# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design\uiDesign\messenger_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from constants import USER_NAME


class MainChatWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1101, 711)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 21, 311, 691))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setStyleSheet("background-color: rgb(38, 28, 70);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.searchLineEdit = QtWidgets.QLineEdit(self.frame)
        self.searchLineEdit.setGeometry(QtCore.QRect(20, 70, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.searchLineEdit.setFont(font)
        self.searchLineEdit.setStyleSheet("""QLineEdit{border-radius: 5px;
                                             background-color: #45357a; 
                                             color: white;
                                             padding:0% 10%}""")
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.settingsButton = QtWidgets.QPushButton(self.frame)
        self.settingsButton.setGeometry(QtCore.QRect(260, 13, 40, 40))
        self.settingsButton.setStyleSheet("""QPushButton{border-radius: 7px;
                                             background-image : url(Windows/Resources/settings.png);
                                             background-repeat: no-repeat;
                                             background-position: center;}
                                             QPushButton:hover{background-image : url(Windows/Resources/settings_hover.png);
                                             background-repeat: no-repeat;
                                             background-position: center;
                                             background-color: #45357a;}""")
        self.settingsButton.setText("")
        self.settingsButton.setObjectName("settingsButton")
        self.userNameLabel = QtWidgets.QLabel(self.frame)
        self.userNameLabel.setGeometry(QtCore.QRect(20, 10, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.userNameLabel.setFont(font)
        self.userNameLabel.setStyleSheet("QFrame{\n"
                                         "background-color: rgb(38, 28, 70);\n"
                                         "color: white;\n"
                                         "}")
        self.userNameLabel.setObjectName("userNameLabel")
        self.chatListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.chatListWidget.setGeometry(QtCore.QRect(0, 140, 311, 581))
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.chatListWidget.setFont(font)
        self.chatListWidget.setTabletTracking(False)
        self.chatListWidget.setAutoFillBackground(False)
        self.chatListWidget.setStyleSheet('''QListWidget{
                                                background-color: rgb(38, 28, 70);
                                                border: none;}
                                                QListWidget::item {
                                                color: white;
                                                border: none;
                                                padding: 10px 0px 10px 10px;
                                                word-wrap: break-all;}
                                                QListWidget::item:selected {
                                                border: none;
                                                background-color: #45357a;
                                                color: white;
                                                padding: 0px 0px 10px 10px;
                                                word-wrap: break-all;}
                                                QListView {
                                                outline: 0;
                                                }''')

        self.chatListWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.chatListWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.chatListWidget.setLineWidth(1)
        self.chatListWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.chatListWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.chatListWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.chatListWidget.setAutoScroll(True)
        self.chatListWidget.setTabKeyNavigation(False)
        self.chatListWidget.setProperty("showDropIndicator", True)
        self.chatListWidget.setDragDropOverwriteMode(False)
        self.chatListWidget.setAlternatingRowColors(False)
        self.chatListWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.chatListWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.chatListWidget.setMovement(QtWidgets.QListView.Static)
        self.chatListWidget.setFlow(QtWidgets.QListView.TopToBottom)
        self.chatListWidget.setProperty("isWrapping", False)
        self.chatListWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.chatListWidget.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.chatListWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.chatListWidget.setUniformItemSizes(False)
        self.chatListWidget.setWordWrap(False)
        self.chatListWidget.setSelectionRectVisible(False)
        self.chatListWidget.setObjectName("listWidget")



        self.chatScrollArea = QtWidgets.QScrollArea(self.frame)
        self.chatScrollArea.setGeometry(QtCore.QRect(0, 110, 311, 581))
        self.chatScrollArea.setStyleSheet("border: none;")
        self.chatScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.chatScrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.chatScrollArea.setWidgetResizable(False)
        self.chatScrollArea.setObjectName("chatScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 311, 581))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.chatScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(310, 21, 791, 61))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.refreshButton = QtWidgets.QPushButton(self.frame_2)
        self.refreshButton.setGeometry(QtCore.QRect(590, 12, 40, 40))
        self.refreshButton.setStyleSheet("""QPushButton{border-radius: 7px;
                                             background-image : url(Windows/Resources/refresh.png);
                                             background-repeat: no-repeat;
                                             background-position: center;}
                                             QPushButton:hover{background-image : url(Windows/Resources/refresh_hover.png);
                                             background-repeat: no-repeat;
                                             background-position: center;}""")
        self.refreshButton.setText("")
        self.refreshButton.setObjectName("editChatButton")
        self.editChatButton = QtWidgets.QPushButton(self.frame_2)
        self.editChatButton.setGeometry(QtCore.QRect(640, 12, 40, 40))
        self.editChatButton.setStyleSheet("""QPushButton{border-radius: 7px;
                                             background-image : url(Windows/Resources/edit_chat.png);
                                             background-repeat: no-repeat;
                                             background-position: center;}
                                             QPushButton:hover{background-image : url(Windows/Resources/edit_chat_hover.png);
                                             background-repeat: no-repeat;
                                             background-position: center;}""")
        self.editChatButton.setText("")
        self.editChatButton.setObjectName("editChatButton")
        self.addToChatButton = QtWidgets.QPushButton(self.frame_2)
        self.addToChatButton.setGeometry(QtCore.QRect(690, 12, 40, 40))
        self.addToChatButton.setStyleSheet("""QPushButton{border-radius: 7px;
                                             background-image : url(Windows/Resources/add_user.png);
                                             background-repeat: no-repeat;
                                             background-position: center;}
                                             QPushButton:hover{background-image : url(Windows/Resources/add_user_hover.png);
                                             background-repeat: no-repeat;
                                             background-position: center;}""")
        self.addToChatButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("design\\uiDesign\\../code/Resources/add_user1.png"), QtGui.QIcon.Normal,
                        QtGui.QIcon.Off)
        self.addToChatButton.setIcon(icon2)
        self.addToChatButton.setIconSize(QtCore.QSize(25, 25))
        self.addToChatButton.setObjectName("addToChatButton")
        self.leaveFromChatButton = QtWidgets.QPushButton(self.frame_2)
        self.leaveFromChatButton.setGeometry(QtCore.QRect(740, 12, 40, 40))
        self.leaveFromChatButton.setStyleSheet("""QPushButton{border-radius: 7px;
                                             background-image : url(Windows/Resources/leave.png);
                                             background-repeat: no-repeat;
                                             background-position: center;}
                                             QPushButton:hover{background-image : url(Windows/Resources/leave_hover.png);
                                             background-repeat: no-repeat;
                                             background-position: center;}""")
        self.leaveFromChatButton.setText("")
        self.leaveFromChatButton.setObjectName("leaveFromChatButton")
        self.chatLabel = QtWidgets.QLabel(self.frame_2)
        self.chatLabel.setGeometry(QtCore.QRect(10, 6, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Noto Naskh Arabic UI")
        font.setPointSize(11)
        self.chatLabel.setFont(font)
        self.chatLabel.setStyleSheet("")
        self.chatLabel.setObjectName("chatLabel")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(310, 660, 791, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame_3.setFont(font)
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.messageTextEdit = QtWidgets.QTextEdit(self.frame_3)
        self.messageTextEdit.setGeometry(QtCore.QRect(80, 10, 641, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.messageTextEdit.sizePolicy().hasHeightForWidth())
        self.messageTextEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.messageTextEdit.setFont(font)
        self.messageTextEdit.setStyleSheet("border: none;\n")
        self.messageTextEdit.setText("")
        self.messageTextEdit.setObjectName("messageTextLineEdit")
        self.sendButton = QtWidgets.QPushButton(self.frame_3)
        self.sendButton.setGeometry(QtCore.QRect(740, 5, 40, 40))
        self.sendButton.setStyleSheet("""QPushButton{border-radius: 7px;
                                             background-image : url(Windows/Resources/send.png);
                                             background-repeat: no-repeat;
                                             background-position: center;}
                                             QPushButton:hover{background-image : url(Windows/Resources/send_hover.png);
                                             background-repeat: no-repeat;
                                             background-position: center;}""")
        self.sendButton.setText("")
        self.sendButton.setObjectName("sendButton")
        self.attachButton = QtWidgets.QPushButton(self.frame_3)
        self.attachButton.setGeometry(QtCore.QRect(20, 5, 40, 40))
        self.attachButton.setStyleSheet("""QPushButton{border-radius: 7px;
                                             background-image : url(Windows/Resources/attach.png);
                                             background-repeat: no-repeat;
                                             background-position: center;}
                                             QPushButton:hover{background-image : url(Windows/Resources/attach_hover.png);
                                             background-repeat: no-repeat;
                                             background-position: center;}""")
        self.attachButton.setText("")
        self.attachButton.setObjectName("attachButton")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(0, 0, 1101, 25))
        self.frame_5.setStyleSheet("background-color: rgb(38, 28, 70);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.closeButton = QtWidgets.QPushButton(self.frame_5)
        self.closeButton.setGeometry(QtCore.QRect(1066, 0, 35, 25))
        self.closeButton.setStyleSheet('''QPushButton{border-radius: 15px;
                                      background-image : url(Windows/Resources/close.png);
                                      background-repeat: no-repeat;
                                      background-position: center;} 

                                      QPushButton:hover{background-image : url(Windows/Resources/close_hover.png);
                                      background-repeat: no-repeat;
                                      background-position: center;
                                      background-color: red;}''')
        self.closeButton.setText("")
        self.closeButton.setObjectName("closeButton")
        self.minimizeButton = QtWidgets.QPushButton(self.frame_5)
        self.minimizeButton.setGeometry(QtCore.QRect(996, 0, 35, 25))
        self.minimizeButton.setStyleSheet('''QPushButton{border-radius: 15px;
                                      background-image : url(Windows/Resources/minimize.png);
                                      background-repeat: no-repeat;
                                      background-position: center;} 

                                      QPushButton:hover{background-image : url(Windows/Resources/minimize_hover.png);
                                      background-repeat: no-repeat;
                                      background-position: center;
                                      background-color: #45357a;}''')
        self.minimizeButton.setText("")
        self.minimizeButton.setObjectName("minimizeButton")
        self.maximizeButton = QtWidgets.QPushButton(self.frame_5)
        self.maximizeButton.setGeometry(QtCore.QRect(1031, 0, 35, 25))
        self.maximizeButton.setStyleSheet('''QPushButton{border-radius: 15px;
                                      background-image : url(Windows/Resources/maximize.png);
                                      background-repeat: no-repeat;
                                      background-position: center;} 

                                      QPushButton:hover{background-image : url(Windows/Resources/maximize_hover.png);
                                      background-repeat: no-repeat;
                                      background-position: center;
                                      background-color: #45357a;}''')
        self.maximizeButton.setText("")
        self.maximizeButton.setObjectName("maximizeButton")

        self.messageListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.messageListWidget.setGeometry(QtCore.QRect(310, 80, 791, 581))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.messageListWidget.setFont(font)
        self.messageListWidget.setTabletTracking(False)
        self.messageListWidget.setAutoFillBackground(False)
        self.messageListWidget.setStyleSheet('''QListWidget{
                                                background-color: rgb(235, 234, 253);
                                                border: none;}
                                                QListWidget::item:hover{
                                                background-color: rgb(235, 234, 253);
                                                border: none;}
                                                QListWidget::item:active{
                                                background-color: rgb(235, 234, 253);
                                                border: none;
                                                color: black}
                                                QListView {
                                                outline: 0;
                                                }''')
        self.messageListWidget.setUniformItemSizes(True)
        self.messageListWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.messageListWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.messageListWidget.setLineWidth(1)
        self.messageListWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.messageListWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.messageListWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.messageListWidget.setAutoScroll(True)
        self.messageListWidget.setTabKeyNavigation(False)
        self.messageListWidget.setProperty("showDropIndicator", True)
        self.messageListWidget.setDragDropOverwriteMode(False)
        self.messageListWidget.setAlternatingRowColors(False)
        self.messageListWidget.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.messageListWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.messageListWidget.setMovement(QtWidgets.QListView.Static)
        self.messageListWidget.setFlow(QtWidgets.QListView.TopToBottom)
        self.messageListWidget.setProperty("isWrapping", False)
        self.messageListWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.messageListWidget.setLayoutMode(QtWidgets.QListView.SinglePass)
        self.messageListWidget.setViewMode(QtWidgets.QListView.ListMode)
        self.messageListWidget.setUniformItemSizes(False)
        self.messageListWidget.setWordWrap(False)
        self.messageListWidget.setSelectionRectVisible(False)
        self.messageListWidget.setObjectName("listWidget")

        '''self.messageScrollArea = QtWidgets.QScrollArea(self.centralwidget)
                self.messageScrollArea.setGeometry(QtCore.QRect(310, 80, 791, 581))
                self.messageScrollArea.setStyleSheet("background-color: rgb(235, 234, 253);\n"
        "border: none;")
                self.messageScrollArea.setWidgetResizable(False)
                self.messageScrollArea.setObjectName("messageScrollArea")
                self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
                self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 791, 581))
                self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
                self.messageScrollArea.setWidget(self.scrollAreaWidgetContents_2)'''

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.searchLineEdit.setPlaceholderText(_translate("MainWindow", "Search"))
        self.userNameLabel.setText(_translate("MainWindow", USER_NAME))
        self.chatLabel.setText(_translate("MainWindow", "Chat Name"))
        self.messageTextEdit.setPlaceholderText(_translate("MainWindow", "Write a message"))
