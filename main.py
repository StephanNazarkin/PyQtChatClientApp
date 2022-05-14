import sys
import os
import time
import pathlib
import json
from datetime import datetime
from datetime import timedelta
from PyQt5 import QtCore, QtGui, QtWidgets
from Windows.loginWindow import *
from Windows.mainWindow import *
from Services.AccountService import *
from Exceptions.IncorrectPasswordException import IncorrectPasswordException
from Windows.settingsWindow import SettingsWindow
from Windows.editProfileWindow import EditProfileWindow
from Windows.changePasswordWindow import ChangePasswordWindow
from Windows.contactsWindow import ContactsWindow
from Windows.chatMembersWindow import ChatMembersWindow
from Windows.createChatWindow import CreateChatWindow
from constants import *
from Services.ChatroomService import ChatroomService


def main():
    m_time = os.path.getmtime(CONFIG_PATH)
    m_datetime = datetime.fromtimestamp(m_time)
    token_deadline = m_datetime + timedelta(days=7)
    app = QtWidgets.QApplication(sys.argv)
    # start_window = SettingsWindow(100, 100)
    if os.path.getsize(CONFIG_PATH) > 0:
        config_file = open(CONFIG_PATH)
        user_data = json.load(config_file)
        if "token" in user_data and user_data["token"]:
            if token_deadline > datetime.now():
                start_window = MainWindow()
    start_window.show()
    sys.exit(app.exec_())




if __name__ == '__main__':
    main()

    '''
    m_time = os.path.getmtime(CONFIG_PATH)
    m_datetime = datetime.fromtimestamp(m_time)
    token_deadline = m_datetime + timedelta(days=7)
    app = QtWidgets.QApplication(sys.argv)
    # start_window = SettingsWindow(100, 100)
    if os.path.getsize(CONFIG_PATH) > 0:
        config_file = open(CONFIG_PATH)
        user_data = json.load(config_file)
        if "token" in user_data and user_data["token"]:
            if token_deadline > datetime.now():
                start_window = MainWindow()
    start_window.show()
    sys.exit(app.exec_())'''
