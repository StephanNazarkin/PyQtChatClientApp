import requests
from constants import *


class MessageService(object):
    def __init__(self):
        self.request = "empty"
        self.url = REQUEST_URL
        self.methodName = "empty"

    def send_message(self, chat_id, user_id, text, files=""):
        self.methodName = "Message/SendMessage"
        self.url += self.methodName
        print(self.url)
        self.request = requests.post(self.url, headers=HEADERS, json={'chatId': chat_id,
                                                                      'userId': user_id,
                                                                      'text': text}, files=files)
        #print(self.headers)
        print(self.request.text)
        return self.request

    def edit_message(self, message_id, text, file, image_id=''):
        self.methodName = "Message/EditMessage"
        self.url += self.methodName
        print(self.url)
        self.request = requests.post(self.url, data={'id': message_id,
                                                     'text': text,
                                                     'file': file,
                                                     'imageId': image_id})
        print(self.request)
        return self.request

    def delete_message(self, message_id):
        self.methodName = "Message/DeleteMessage?messageId={messageId}" \
            .format(messageId=message_id)
        self.url += self.methodName
        print(self.url)
        self.request = requests.delete(self.url)
        print(self.request)
        return self.request

    def get_message(self, message_id):
        self.methodName = "Message/GetMessage?messageId={messageId}" .format(messageId=message_id)
        self.url += self.methodName
        self.request = requests.get(self.url)
        response_json = self.request.json()
        response = {'status code': self.request.status_code,
                    'user name': response_json['user']['userName'],
                    'message text': response_json['text']}
        return response

    def get_messages_from_chat(self, chat_id):
        self.methodName = "Message/GetMessagesFromChat?chatId={chatId}".format(chatId=chat_id)
        self.url += self.methodName
        self.request = requests.get(self.url, headers=HEADERS)
        return self.request



