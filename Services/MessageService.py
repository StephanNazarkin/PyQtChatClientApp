import requests
from constants import *


class MessageService(object):
    def __init__(self):
        self.response = ""
        self.url = REQUEST_URL
        self.methodName = ""

    def send_message(self, chat_id, user_id, text, files=""):
        self.methodName = "Message/SendMessage"
        self.url += self.methodName
        self.response = requests.post(self.url, headers=HEADERS, json={'chatId': chat_id,
                                                                       'userId': user_id,
                                                                       'text': text}, files=files)
        return self.response

    def edit_message(self, message_id, text, file, image_id=''):
        self.methodName = "Message/EditMessage"
        self.url += self.methodName
        self.response = requests.post(self.url, data={'id': message_id,
                                                      'text': text,
                                                      'file': file,
                                                      'imageId': image_id})
        return self.response

    def delete_message(self, message_id):
        self.methodName = "Message/DeleteMessage?messageId={messageId}" \
            .format(messageId=message_id)
        self.url += self.methodName
        self.response = requests.delete(self.url)
        return self.response

    def get_message(self, message_id):
        self.methodName = "Message/GetMessage?messageId={messageId}" .format(messageId=message_id)
        self.url += self.methodName
        self.response = requests.get(self.url)
        return self.response

    def get_messages_from_chat(self, chat_id):
        self.methodName = "Message/GetMessagesFromChat?chatId={chatId}".format(chatId=chat_id)
        self.url += self.methodName
        self.response = requests.get(self.url, headers=HEADERS)
        return self.response
