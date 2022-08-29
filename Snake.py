import random
import pygame

class Snake:
    def __init__(self,head):
        self.head = head
        self.body = [self.head, self.head]
        self.direction = random.randint(0,3)

    def get_body(self):
        return self.body
    
    def is_next_move_valid(self):
        next_move = self.get_next_move()
        if self._is_out_of_bounds(next_move):
            return False
        
    def get_next_move(self):
        [x,y] = self.head.get_pos()
        match self.direction:
            case 0:
                return [x,y-1]
            case 1:
                return [x+1,y]
            case 2:
                return [x,y+1]
            case 3:
                return [x-1,y]
                
    def _is_out_of_bounds(self, next_move):
        if next_move[0] < 0 or next_move[0] >= 40 or next_move[1] < 0 or next_move[1] >= 40:
            return True
    

    def move(self, cell):
        self.head = cell
        self.body.insert(0, self.head)
        return self.body.pop()

    def draw(self, screen):
        for cell in self.body:
            [x,y] = cell.get_pos()
            screen.fill((255,255,255), (x*20,y*20,20,20))

    def grow(self):
        self.body.append(self.head)

    def set_direction(self, direction):
        self.direction = direction