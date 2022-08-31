import random
from time import sleep
from snake import Snake
from cell import Cell
from board import Board
from food import Food
class Game:
    def __init__(self, server, grid):
        self.server = server
        self.events = {}
        self.events["p1"] = []
        self.events["p2"] = []
        self.snakes = [Snake(Cell([10,10],"SNAKE"), "p1"), Snake(Cell([30,30],"SNAKE"), "p2")]
        self.grid = grid
        self.board = Board(self.grid, self.snakes)
        self.running = True
        self.food = None
        self.foodSpawned = False
    
    def start(self):
        self.server.broadcast(self.get_serialized_snakes())
        self.run()
    
    def get_serialized_snakes(self):
        snakes = "s["
        for snake in self.snakes:
            snakes += snake.get_serialized_pos() + "/"
        snakes += "]"
        return snakes
    
    def get_serialized_food(self):
        food = "f["
        for food_item in self.food:
            food += food_item.get_serialized_pos()
        food += "]"
        return food
    
    def run(self):
        while self.running:
            self.update()
            self.server.broadcast(self.get_serialized_snakes())
            self.server.broadcast(self.get_serialized_food())
            sleep(2)
    
    def update(self):
        self.player_events_handler()
        self.snake_handler()
        self.food_handler()
    
    def player_events_handler(self):
        # 79 right 
        # 82 up 
        # 80 left 
        # 81 down
        for snake in self.snakes:
            id = snake.get_id()
            if self.events[id]:
                while self.events[id]:
                    if self.events[id][0] == "79" and snake.get_direction() != 3:
                        self.events[id].pop(0)
                        snake.set_direction(1)
                        break
                    elif self.events[id][0] == "80" and snake.get_direction() != 1:
                        self.events[id].pop(0)
                        snake.set_direction(3)
                        break
                    elif self.events[id][0] == "82" and snake.get_direction() != 2:
                        self.events[id].pop(0)
                        snake.set_direction(0)
                        break
                    elif self.events[id][0] == "81" and snake.get_direction() != 0:
                        self.events[id].pop(0)
                        snake.set_direction(2)
                        break
                    else:
                        self.events[id].pop(0)
                        continue
    
    def snake_handler(self):
        for snake in self.snakes:
            if snake.is_next_move_valid() == False:
                self.running = False
            cell = self.board.get_cell(snake.get_next_move())
            if self.is_snake_eating(cell):
                snake.grow()
            prev_cell = snake.move(cell.set_type("SNAKE"))
            prev_cell.set_type("EMPTY")
    
    def is_snake_eating(self, cell):
        if cell.get_type() == "FOOD":
            self.foodSpawned = False
            self.food = None
            return True
    
    def food_handler(self):
        if self.foodSpawned == False:
            x = random.randint(0, self.grid[0] - 1)
            y = random.randint(0, self.grid[1] - 1)
            if(self.board.get_cell([x,y]).get_type() != "EMPTY"):
                self.food_handler()
            self.food = [Food(self.board.get_cell([x,y]).set_type("FOOD"), "f1")]
            self.foodSpawned = True
    
    def add_event(self, id, event):
        self.events[id].append(event)
        print(self.events)