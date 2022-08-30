import threading
from server import ThreadedServer

def main():
    server = ThreadedServer('localhost', 8080)
    threading.Thread(target = server.listen).start()
    

if __name__ == "__main__":
    main()