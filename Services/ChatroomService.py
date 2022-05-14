import requests
from constants import *


class ChatroomService(object):
    def __init__(self):
        self.response = ""
        self.url = REQUEST_URL
        self.methodName = ""

    def create_chatroom(self, topic, user_id):
        self.methodName = "Chatroom/CreateChatroom"
        self.url += self.methodName
        self.response = requests.post(self.url, headers=HEADERS, json={'topic': topic,
                                                                       'userId': user_id})
        return self.response

    def edit_chatroom(self, chat_id, topic, password):
        self.methodName = "Chatroom/EditChatroom"
        self.url += self.methodName
        self.response = requests.post(self.url, json={'chatId': chat_id,
                                                      'topic': topic,
                                                      'password': password})
        return self.response

    def delete_chatroom(self, chat_id):
        self.methodName = "Chatroom/DeleteChatroom?chatId={chatId}".format(chatId=chat_id)
        self.url += self.methodName
        self.response = requests.delete(self.url, headers=HEADERS)
        return self.response

    def get_chatroom(self, chat_id):
        self.methodName = "Chatroom/GetChatroom?chatId={chatId}".format(chatId=chat_id)
        self.url += self.methodName
        self.response = requests.get(self.url)
        return self.response

    def get_all_chatrooms(self):
        self.methodName = "Chatroom/GetAllChatrooms"
        self.url += self.methodName
        self.response = requests.get(self.url, headers=HEADERS)
        return self.response

    def add_to_chatroom(self, chat_id, user_id):
        self.methodName = "Chatroom/AddToChatroom?chatId={chatid}".format(chatid=chat_id)
        self.url += self.methodName
        self.response = requests.post(self.url, headers=HEADERS, json=user_id)
        return self.response

    def leave_from_chatroom(self, chat_id):
        self.methodName = "Chatroom/LeaveFromChatroom"
        self.url += self.methodName
        self.response = requests.post(self.url, headers=HEADERS, json=chat_id)
        return self.response

    def kick_user(self, user_id):
        self.methodName = "Chatroom/KickUser"
        self.url += self.methodName
        self.response = requests.post(self.url, headers=HEADERS, json=user_id)
        return self.response

    def ban_user(self, user_account_id):
        self.methodName = "Chatroom/BanUser"
        self.url += self.methodName
        self.response = requests.post(self.url, headers=HEADERS, json=user_account_id)
        return self.response

    def unban_user(self, user_account_id):
        self.methodName = "Chatroom/UnbanUser"
        self.url += self.methodName
        self.response = requests.post(self.url, headers=HEADERS, json=user_account_id)
        return self.response

    def set_admin(self, user_account_id):
        self.methodName = "Chatroom/SetAdmin"
        self.url += self.methodName
        self.response = requests.post(self.url, headers=HEADERS, json=user_account_id)
        return self.response

    def unset_admin(self, user_account_id):
        self.methodName = "Chatroom/UnsetAdmin"
        self.url += self.methodName
        self.response = requests.post(self.url, headers=HEADERS, json=user_account_id)
        return self.response

    def get_owner(self, chat_id):
        self.methodName = "Chatroom/GetOwner"
        self.url += self.methodName
        self.response = requests.post(self.url, headers=HEADERS, json=chat_id)
        return self.response

    def get_all_banned_users(self, chat_id):
        self.methodName = "Chatroom/GetAllBannedUsers"
        self.url += self.methodName
        self.response = requests.post(self.url, headers=HEADERS, json=chat_id)
        return self.response

    def get_all_admins(self, chat_id):
        self.methodName = "Chatroom/GetAllAdmins"
        self.url += self.methodName
        self.response = requests.post(self.url, headers=HEADERS, json=chat_id)
        return self.response

    def get_all_users_from_chat(self, chat_id):
        self.methodName = "Chatroom/GetAllUsers"
        self.url += self.methodName
        self.response = requests.post(self.url, headers=HEADERS, json=chat_id)
        return self.response
