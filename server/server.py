import socket
import threading
import os
from game import Game

class ThreadedServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))
        self.connections = {}
        self.playerCount = 0

    def listen(self):
        self.sock.listen(2)
        while True:
            client, address = self.sock.accept()
            self.playerCount += 1
            threading.Thread(target = self.threaded_client, args = (client,address, f"p{self.playerCount}")).start()
            if len(self.connections) >= 2:
                self.game = Game(self, [40,40])

    def threaded_client(self, client, address, id):
        self.connections[id] = client
        client.send(str.encode(id))
        while True:
            try:
                data = client.recv(2048).decode()
                if data == 'shutdown':
                    client.send(str.encode('success'))
                    os._exit(0)
                if not data:
                    del self.connections[client]
                    client.close()
            except socket.error:
                print(f"{address} has left...")
                client.close()
                return False

    def get_connections(self):
        return self.connections
    
    def broadcast(self, data):
        for client in self.connections:
            self.connections[client].sendall(str.encode(data))