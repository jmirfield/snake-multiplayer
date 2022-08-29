import pygame
import random
from snake import Snake
from cell import Cell
from board import Board
from food import Food

class Game:
    def __init__(self, grid, screen):
        pygame.init()
        self.display = pygame.display
        self.screen = self.display.set_mode(screen)
        self.grid = grid
        self.grid_width = screen[0]/grid[0]
        self.grid_height = screen[1]/grid[1]
        self.events = pygame.event
        self.clock = pygame.time.Clock()
        self.snakes = [Snake(Cell(20,22,"SNAKE"), self.grid_width, self.grid_height)]
        self.board = Board(grid, self.snakes)
        self.running = True
        self.food = None
        self.foodSpawned = False
        self._run()
    
    def _run(self):
        while self.running:
            self._draw()
            self._manage_events()
            self._update()
        pygame.quit()

    def _manage_events(self):
        for event in self.events.get():
            if event.type == pygame.QUIT:
                self._quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.snakes[0].get_direction() != 2:
                    self.snakes[0].set_direction(0)
                if event.key == pygame.K_RIGHT and self.snakes[0].get_direction() != 3:
                    self.snakes[0].set_direction(1)
                if event.key == pygame.K_DOWN and self.snakes[0].get_direction() != 0:
                    self.snakes[0].set_direction(2)
                if event.key == pygame.K_LEFT and self.snakes[0].get_direction() != 1:
                    self.snakes[0].set_direction(3)

    def _quit(self):
        self.running = False

    def _update(self):
        self._snake_handler()
        self._food_handler()
        # self.board.update()
        self.clock.tick(10)
    
    def _snake_handler(self):
        for snake in self.snakes:
            if snake.is_next_move_valid() == False:
                return self._quit()
            cell = self.board.get_cell(snake.get_next_move())
            if self._is_snake_eating(cell):
                snake.grow()
            prev_cell = snake.move(cell.set_type("SNAKE"))
            prev_cell.set_type("EMPTY")

    def _is_snake_eating(self, cell):
        if cell.get_type() == "FOOD":
            self.foodSpawned = False
            self.food = None
            return True
    
    def _food_handler(self):
        if self.foodSpawned == False:
            x = random.randint(0, self.grid[0] - 1)
            y = random.randint(0, self.grid[1] - 1)
            if(self.board.get_cell([x,y]).get_type() != "EMPTY"):
                self._food_handler()
            self.food = Food(self.board.get_cell([x,y]).set_type("FOOD"), self.grid_width, self.grid_height)
            self.foodSpawned = True
    

    def _draw(self):
        self.screen.fill((0,0,0))
        for snake in self.snakes:
            snake.draw(self.screen)
        if self.food != None:
            self.food.draw(self.screen)
        self.display.update()

