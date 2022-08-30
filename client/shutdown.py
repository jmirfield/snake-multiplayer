from network import Network

n = Network(None, 'localhost', 8080)

n.send('shutdown')