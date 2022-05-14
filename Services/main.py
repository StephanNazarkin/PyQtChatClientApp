import logging
import sys
from signalrcore.hub_connection_builder import HubConnectionBuilder

def input_with_default(input_text, default_value):
    value = input(input_text.format(default_value))
    return default_value if value is None or value.strip() == "" else value
server_url = input_with_default('Enter your server url(default: {0}): ', "http://localhost:32844/hubs/chat")
username = input_with_default('Enter your username (default: {0}): ', "risten")
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
hub_connection = HubConnectionBuilder()\
            .with_url(server_url,
            options={
                "headers": {"Authorization": "Bearer "
                                             "eyJhbGciOiJIUzI1NiIsInR5cCI6Ikp"
                                             "XVCJ9.eyJ1bmlxdWVfbmFtZSI6InJpc"
                                             "3RlbiIsIm5hbWVpZCI6ImJjMjgwOGI2"
                                             "LTc0MDctNDUwNy05NmI5LWQ5NWIxMT"
                                             "gwNjdiMiIsIm5iZiI6MTY1MjExNzA4O"
                                             "SwiZXhwIjoxNjUyNzIxODg5LCJpYXQiO"
                                             "jE2NTIxMTcwODl9.AVz29PLhGo0J5Ylw4L"
                                             "PptEtpNtW3AKdxJOqG5EHfUCo"}
            })\
            .configure_logging(logging.DEBUG)\
            .with_automatic_reconnect({
                "type": "raw",
                "keep_alive_interval": 10,
                "reconnect_interval": 5,
                "max_attempts": 5
            }).build()

hub_connection.on_open(lambda: print("connection opened and handshake received ready to send messages"))
hub_connection.on_close(lambda: print("connection closed"))

hub_connection.on("ReceiveMessage", print)
hub_connection.start()
message = None

# Do login

while message != "exit()":
    message = input(">> ")
    if message is not None and message != "" and message != "exit()":
        hub_connection.send("Send", ['Chat', message])

hub_connection.stop()

sys.exit(0)