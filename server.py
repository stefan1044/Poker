import socket
import select
import pickle

IP_ADDRESS = "127.0.0.1"
PORT = 1234
HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((IP_ADDRESS, PORT))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection established from {address}")

    d = {1: "Hey", 2: "There"}
    msg = pickle.dumps(d)

    msg = bytes(f"{len(msg): < {HEADERSIZE}}", "utf-8") + msg

    clientsocket.send(msg)
