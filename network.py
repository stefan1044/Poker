import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.SERVER="192.168.100.3"
        self.PORT=5555
        self.address=(self.SERVER, self.PORT)
        self.pos=self.connect()
    
    def getPos(self):
        return self.pos
    
        
    def connect(self):
        try:
            self.client.connect(self.address)
            return self.client.recv(2048).decode()
        except:
            pass
            
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)
            
n=Network()
print(n.send("hello"))
print(n.send("working"))