import socket
import random
import time
import threading
import json
import pathlib


HEADER = 64
path = pathlib.Path(__file__).parent.absolute()
with open(f'{path}\\vars.json') as f:
    data = json.load(f)
for p in data["vars"]:
    SERVER = p["IP"]
    PORT = int(p["PORT"])
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    msg = str(msg)
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


def generate_random_num():
   num = random.randint(0,10)
   return num

def quit():
    while True:
        user_input = input()
        if user_input == "quit":
            send(DISCONNECT_MESSAGE)

while True:
    thread = threading.Thread(target=quit)
    thread.start()
    num = generate_random_num()
    send(num)
    time.sleep(5)
    