import random
from snake import Snake
from cell import Cell
from board import Board
from food import Food
class Game:
    def __init__(self, server, grid):
        self.server = server
        self.events = {}
        self.snakes = [Snake(Cell([10,10],"SNAKE"), "p1"), Snake(Cell([30,30],"SNAKE"), "p2")]
        self.board = Board(grid, self.snakes)
        self.start()
    
    def start(self):
        starting_pos = f"[p1{self.snakes[0].get_pos_as_string()}/p2{self.snakes[1].get_pos_as_string()}]"
        self.server.broadcast(starting_pos)