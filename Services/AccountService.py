from constants import *
from Exceptions.ResponseIsFalseException import ResponseIsFalseException


class AccountService(object):
    def __init__(self):
        self.response = ""
        self.url = REQUEST_URL
        self.methodName = ""

    def register_user(self, user_name, email, password):
        self.methodName = "Account/Register"
        self.url += self.methodName
        self.response = requests.post(self.url, json={'userName': user_name,
                                                     'email': email,
                                                     'password': password})
        return self.response

    def login_user(self, user_name, password):
        self.methodName = "Account/Login"
        self.url += self.methodName
        self.response = requests.post(self.url, json={'userName': user_name,
                                                     'password': password})
        return self.response

    def change_user_password(self, new_password, old_password):
        self.methodName = "Account/ChangePassword"
        self.url += self.methodName
        self.response = requests.post(self.url, headers=HEADERS, json={'id': USER_ID,
                                                                      'oldPassword': old_password,
                                                                      'newPassword': new_password})
        return self.response

    def get_user_by_username(self, username):
        self.methodName = "Account/GetUserByUserName"
        self.url += self.methodName
        self.response = requests.post(self.url, headers=HEADERS, json=username)
        return self.response

    def add_friend(self, friend_id):
        self.methodName = "Account/AddFriend"
        self.url += self.methodName
        self.response = requests.post(self.url, headers=HEADERS, json=friend_id)
        return self.response

    def delete_friend(self, friend_id):
        self.methodName = "Account/DeleteFriend"
        self.url += self.methodName
        self.response = requests.post(self.url, headers=HEADERS, json=friend_id)
        return self.response

    def get_all_friends(self, user_id):
        self.methodName = "Account/GetAllFriends"
        self.url += self.methodName
        self.response = requests.post(self.url, headers=HEADERS, json=user_id)
        return self.response

    def block_user(self, user_id):
        self.methodName = "Account/BlockUser"
        self.url += self.methodName
        self.response = requests.post(self.url, headers=HEADERS, json=user_id)
        return self.response

    def unblock_user(self, user_id):
        self.methodName = "Account/UnblockUser"
        self.url += self.methodName
        self.response = requests.post(self.url, headers=HEADERS, json=user_id)
        return self.response

    def get_all_blocked_users(self, user_id):
        self.methodName = "Account/GetAllBlockedUsers"
        self.url += self.methodName
        self.response = requests.post(self.url, headers=HEADERS, json=user_id)
        return self.response

    def update_user(self, user_name, email):
        self.methodName = "Account/UpdateUser"
        self.url += self.methodName
        self.response = requests.post(self.url, headers=HEADERS, json={'id': USER_ID,
                                                                      'userName': user_name,
                                                                      'email': email})
        return self.response
