import socket
from threading import *

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 8000

serversocket.bind((host, port))

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            r = input(" -->")
            clientsocket.send(r.encode())
            msg = clientsocket.recv(1024).decode()
            print("client : " + str(msg))


serversocket.listen(5)
print("Sender is ready and listening")
    
clientsocket, address = serversocket.accept()
print("Reciever " + str(address) + " connected")
client(clientsocket, address)

#avoid taking direct input in threaded environment. sayan hazra
