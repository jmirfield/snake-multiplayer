import pygame
from Snake import Snake
from Cell import Cell
from Board import Board

class Game:
    def __init__(self):
        pygame.init()
        self.display = pygame.display
        self.screen = self.display.set_mode([800,800])
        self.events = pygame.event
        self.clock = pygame.time.Clock()
        self.snakes = [Snake(Cell(20,22,"SNAKE"))]
        self.board = Board([40,40], self.snakes)
        self.running = True
        self.run()
    
    def run(self):
        print("Starting game...")
        while self.running:
            self.draw()
            self.manage_events()
            self.update()

    def manage_events(self):
        for event in self.events.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snakes[0].set_direction(0)
                if event.key == pygame.K_RIGHT:
                    self.snakes[0].set_direction(1)
                if event.key == pygame.K_DOWN:
                    self.snakes[0].set_direction(2)
                if event.key == pygame.K_LEFT:
                    self.snakes[0].set_direction(3)

    def quit(self):
        self.running = False
        pygame.quit()

    def update(self):
        self.snake_handler()
        # self.board.update()
        self.clock.tick(10)
    
    def snake_handler(self):
        for snake in self.snakes:
            if snake.is_next_move_valid() == False:
                return self.quit()
            cell = self.board.get_cell(snake.get_next_move())
            # Check if food or other snake?
            if 2 == 1:
                snake.grow()
            prev_cell = snake.move(cell.set_type("SNAKE"))
            prev_cell.set_type("EMPTY")
    

    def draw(self):
        self.screen.fill((0,0,0))
        for snake in self.snakes:
            snake.draw(self.screen)
        self.display.update()

