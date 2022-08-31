import pygame
from network import Network
from snake import SnakeController

class Client:
    def __init__(self, screen):
        pygame.init()
        self.display = pygame.display
        self.screen = self.display.set_mode(screen)
        self.grid_width = screen[0]/40
        self.grid_height = screen[0]/40
        self.events = pygame.event.get()
        self.clock = pygame.time.Clock()
        self.running = True
        self.server = Network(self,'localhost', 8080)
        self.snakes = {}
        self.food = {}
        self.run()
    
    def run(self):
        while self.running:
            self.manage_events()
        self.quit()
        self.server.close_connection()
    
    def manage_events(self):
        self.events = self.events + pygame.event.get()
        while self.events:
            if self.events[0].type == pygame.QUIT:
                self.running = False
                break
            elif self.events[0].type == pygame.KEYDOWN:
                if self.events[0].key == pygame.K_UP or self.events[0].key == pygame.K_DOWN or self.events[0].key == pygame.K_LEFT or self.events[0].key == pygame.K_RIGHT:
                    self.server.send(str(self.events[0].scancode))
                    self.events.pop(0)
                    break
            else:
                self.events.pop(0)
                continue

    def update(self, data):
        if data[0] == "s":
            self.snakes = SnakeController.parse_data(data[1:])
        if data[0] == "f":
            self.food = SnakeController.parse_data(data[1:])
        self.draw()
    
    def draw(self):
        self.screen.fill((0,0,0))
        self.draw_snakes()
        self.draw_food()
        self.display.update()
    
    def draw_snakes(self):
        for player in self.snakes:
            color = (255,255,255)
            if player == self.id: color = (0,255,255)
            for cell in self.snakes[player]:
                self.screen.fill(color, (cell[0]*self.grid_width,cell[1]*self.grid_height,self.grid_width,self.grid_height))

    def draw_food(self):
        for food in self.food:
            for cell in self.food[food]:
                self.screen.fill((0,0,255), (cell[0]*self.grid_width,cell[1]*self.grid_height,self.grid_width,self.grid_height))

    def set(self, id):
        self.id = id
    
    def quit(self):
        self.running = False
        pygame.quit()