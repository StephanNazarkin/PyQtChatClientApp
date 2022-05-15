import json
import os
import requests
from requests.structures import CaseInsensitiveDict


HOST = "localhost:"
PORT = 32844
REQUEST_URL = "http://{host}{port}/".format(host=HOST, port=PORT)
RESOURCES_PATH = "Windows\\Resources\\"
USER_ID = ''
USER_NAME = ''
HEADERS = {}

CONFIG_PATH = 'data/config.json'
if os.path.getsize(CONFIG_PATH) > 0:
    config_file = open(CONFIG_PATH)
    user_data = json.load(config_file)
    USER_ID = user_data['userId']
    USER_NAME = user_data['username']
    HEADERS = {}
    if "token" in user_data and user_data["token"]:
        HEADERS = {"Content-Type": "application/json",
                   "Authorization": "Bearer {token}".format(token=user_data['token'])}
else:
    print("file is empty")
