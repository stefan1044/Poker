import socket
import select
import pickle
import _thread 
from poker import Poker


SERVER = "192.168.100.3"
PORT = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    s.bind((SERVER, PORT))
except socket.error as e:
    print(e)


s.listen(9)
print("Waiting for connections, Server Started")

def threaded_client(clientConnection):
    clientConnection.send(str.encode("Connected"))
    reply=""
    while True:
        try:
            data=clientConnection.recv(2048)
            reply=data.decode("utf-8")
            
            if not data:
                print ("Disconnected")
                break
            else:
                print(f"Received: {reply}")
                print(f"Sending: {reply}")
            
            clientConnection.sendall(str.encode(reply))
        except:
            break
    
    print("Lost connection")
    clientConnection.close()

while True:
    clientConnection, clientAddress=s.accept()
    print (f"Connected to: {clientAddress}")
    
    _thread.start_new_thread(threaded_client, (clientConnection,))