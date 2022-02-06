import socket
import pickle


IP_ADDRESS = "127.0.0.1"
PORT = 1234

HEADER_SIZE = 10

client_username = input("Username: ")
client_username_send = client_username.encode("utf-8")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP_ADDRESS, PORT))
# s.setblocking(False)


while True:

    full_msg = b""
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print(f"new message length: {msg[:HEADER_SIZE]}")
            msglen = int(msg[:HEADER_SIZE])
            new_msg = False

        full_msg += msg

        if len(full_msg) - HEADER_SIZE == msglen:
            print("full msg recived")
            print(full_msg[HEADER_SIZE:])

            d = pickle.loads(full_msg[HEADER_SIZE:])
            print(d)

            new_msg = True
            full_msg = b''
    print(full_msg)
