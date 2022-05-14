import requests
from constants import *

class ChatroomService(object):
    def __init__(self):
        self.request = "empty"
        self.url = REQUEST_URL
        self.methodName = "empty"

    def create_chatroom(self, topic, user_id):
        self.methodName = "Chatroom/CreateChatroom"
        self.url += self.methodName
        self.request = requests.post(self.url, headers=HEADERS, json={'topic': topic,
                                                                      'userId': user_id})
        return self.request

    def edit_chatroom(self, chat_id, topic, password):
        self.methodName = "Chatroom/EditChatroom"
        self.url += self.methodName
        self.request = requests.post(self.url, json={'chatId': chat_id,
                                                     'topic': topic,
                                                     'password': password})
        return self.request

    def delete_chatroom(self, chat_id):
        self.methodName = "Chatroom/DeleteChatroom?chatId={chatId}".format(chatId=chat_id)
        self.url += self.methodName
        print(self.url)
        self.request = requests.delete(self.url)
        print(self.request)
        return self.request

    def get_chatroom(self, chat_id):
        self.methodName = "Chatroom/GetChatroom?chatId={chatId}".format(chatId=chat_id)
        self.url += self.methodName
        print(self.url)
        self.request = requests.get(self.url)
        print(self.request)
        return self.request

    def get_all_chatrooms(self):
        self.methodName = "Chatroom/GetAllChatrooms"
        self.url += self.methodName
        self.request = requests.get(self.url, headers=HEADERS)
        return self.request

    def add_to_chatroom(self, chat_id, user_id):
        self.methodName = "Chatroom/AddToChatroom?chatId={chatid}".format(chatid=chat_id)
        self.url += self.methodName
        self.request = requests.post(self.url, headers=HEADERS, json=user_id)
        print(self.request.text)
        return self.request

    def leave_from_chatroom(self, chat_id):
        self.methodName = "Chatroom/LeaveFromChatroom"
        self.url += self.methodName
        self.request = requests.post(self.url, headers=HEADERS, json=chat_id)
        return self.request

    def kick_user(self, user_id):
        self.methodName = "Chatroom/KickUser"
        self.url += self.methodName
        self.request = requests.post(self.url, headers=HEADERS, json=user_id)
        print(self.request)
        return self.request

    def ban_user(self, user_account_id):
        self.methodName = "Chatroom/BanUser"
        self.url += self.methodName
        self.request = requests.post(self.url, headers=HEADERS, json=user_account_id)
        return self.request

    def unban_user(self, user_account_id):
        self.methodName = "Chatroom/UnbanUser"
        self.url += self.methodName
        self.request = requests.post(self.url, headers=HEADERS, json=user_account_id)
        return self.request

    def set_admin(self, user_account_id):
        self.methodName = "Chatroom/SetAdmin"
        self.url += self.methodName
        self.request = requests.post(self.url, headers=HEADERS, json=user_account_id)
        return self.request

    def unset_admin(self, user_account_id):
        self.methodName = "Chatroom/UnsetAdmin"
        self.url += self.methodName
        self.request = requests.post(self.url, headers=HEADERS, json=user_account_id)
        return self.request

    def get_all_banned_users(self, chat_id):
        self.methodName = "Chatroom/GetAllBannedUsers"
        self.url += self.methodName
        self.request = requests.post(self.url, headers=HEADERS, json=chat_id)
        return self.request

    def get_all_admins(self, chat_id):
        self.methodName = "Chatroom/GetAllAdmins"
        self.url += self.methodName
        self.request = requests.post(self.url, headers=HEADERS, json=chat_id)
        return self.request

    def get_all_users_from_chat(self, chat_id):
        self.methodName = "Chatroom/GetAllUsers"
        self.url += self.methodName
        self.request = requests.post(self.url, headers=HEADERS, json=chat_id)
        return self.request
