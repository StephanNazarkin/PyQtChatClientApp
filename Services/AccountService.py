import http
import json.decoder

import requests
from constants import *
from Exceptions.ResponseIsFalseException import ResponseIsFalseException
from Exceptions.IncorrectPasswordException import IncorrectPasswordException


class AccountService(object):
    def __init__(self):
        self.request = "empty"
        self.url = REQUEST_URL
        self.methodName = "empty"

    def register_user(self, user_name, email, password):
        self.methodName = "Account/Register"
        self.url += self.methodName
        self.request = requests.post(self.url, json={'userName': user_name,
                                                     'email': email,
                                                     'password': password})
        response_json = self.request.json()
        response = {'status code': self.request.status_code,
                    'user id': response_json['id'],
                    'user name': response_json['userName'],
                    'user email': response_json['email'],
                    'user token': response_json['token']}
        print(response)
        return response

    def login_user(self, user_name, password):
        self.methodName = "Account/Login"
        self.url += self.methodName
        self.request = requests.post(self.url, json={'userName': user_name,
                                                     'password': password})
        response_json = self.request.json()
        print(response_json)
        return response_json

    def change_user_password(self, new_password, old_password):
        self.methodName = "Account/ChangePassword"
        self.url += self.methodName
        self.request = requests.post(self.url, headers=HEADERS, json={'id': USER_ID,
                                                                      'oldPassword': old_password,
                                                                      'newPassword': new_password})
        response = {'status code': self.request.status_code,
                    'response': self.request.text}
        print(self.request.text)
        return response

    def get_user_by_username(self, username):
        self.methodName = "Account/GetUserByUserName"
        self.url += self.methodName
        self.request = requests.post(self.url, headers=HEADERS, json=username)
        return self.request

    def add_friend(self, friend_id):
        self.methodName = "Account/AddFriend"
        self.url += self.methodName
        self.request = requests.post(self.url, headers=HEADERS, json=friend_id)
        return self.request

    def delete_friend(self, friend_id):
        self.methodName = "Account/DeleteFriend"
        self.url += self.methodName
        self.request = requests.post(self.url, headers=HEADERS, json=friend_id)
        return self.request

    def get_all_friends(self, user_id):
        self.methodName = "Account/GetAllFriends"
        self.url += self.methodName
        self.request = requests.post(self.url, headers=HEADERS, json=user_id)
        return self.request

    def block_user(self, user_id):
        self.methodName = "Account/BlockUser"
        self.url += self.methodName
        self.request = requests.post(self.url, headers=HEADERS, json=user_id)
        return self.request

    def unblock_user(self, user_id):
        self.methodName = "Account/UnblockUser"
        self.url += self.methodName
        self.request = requests.post(self.url, headers=HEADERS, json=user_id)
        return self.request

    def get_all_blocked_users(self, user_id):
        self.methodName = "Account/GetAllBlockedUsers"
        self.url += self.methodName
        self.request = requests.post(self.url, headers=HEADERS, json=user_id)
        return self.request

    def update_user(self, user_name, email):
        self.methodName = "Account/UpdateUser"
        self.url += self.methodName
        self.request = requests.post(self.url, headers=HEADERS, json={'id': USER_ID,
                                                                      'userName': user_name,
                                                                      'email': email})
        response = {'status code': self.request.status_code,
                    'response': self.request.text}
        if response['response'] == 'false':
            raise ResponseIsFalseException()
        return response
