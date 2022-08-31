import socket
import threading

class Network:
    def __init__(self, client,host, port):
        self.client = client
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect()
        
    def connect(self):
        try:
            self.sock.connect((self.host, self.port))
            self.client.set(self.sock.recv(2048).decode())
            threading.Thread(target=self.threaded_listener).start()
        except:
            print("Error with connection")
            pass
    
    def threaded_listener(self):
        while True:
            data = self.sock.recv(2048).decode()
            if data:
                self.client.update(data)

    def send(self, data):
        try:
            self.sock.send(str.encode(data))
        except socket.error as e:
            print(e)
    
    def close_connection(self):
        self.client.quit()
        self.sock.close()

