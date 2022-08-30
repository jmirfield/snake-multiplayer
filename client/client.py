import pygame
from network import Network
from snake import Snake

class Client:
    def __init__(self, screen):
        pygame.init()
        self.display = pygame.display
        self.screen = self.display.set_mode(screen)
        self.events = pygame.event.get()
        self.clock = pygame.time.Clock()
        self.running = True
        self.server = Network(self,'localhost', 8080)
        self._run()
    
    def _run(self):
        while self.running:
            self.clock.tick(10)
            self._manage_events()
        pygame.quit()
        self.server.close_connection()
    
    def _manage_events(self):
        self.events = self.events + pygame.event.get()
        while self.events:
            if self.events[0].type == pygame.QUIT:
                self.running = False
                break
            else:
                self.events.pop(0)
                continue

    def update(self, data):
        print(Snake.parse_data(data))
        
    def set(self, id):
        self.id = id
        print(self.id)