import socket
import threading
import json
import os
import pathlib


all_messages = []
HEADER = 64
path = pathlib.Path(__file__).parent.absolute()
with open(f'{path}\\vars.json') as f:
    data = json.load(f)
for p in data["vars"]:
    SERVER = p["IP"]
    PORT = p["PORT"]
ADDR = (SERVER, int(PORT))
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    all_messages.append(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length=int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            all_messages.append(f"[{addr}] {msg}")
    conn.close()

        

def start():
    all_messages.append("[STARTING] server is starting...")
    server.listen()
    all_messages.append(f"[LISTENING] server is listening on {SERVER}")
    work = True
    while work:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        all_messages.append(f"[ACTIVE CONNECTION] {threading.activeCount()-4}")