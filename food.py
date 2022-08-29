import pygame

class Food:
    def __init__(self, cell, width, height):
        self.cell = cell
        self.width = width
        self.height = height

    def draw(self, screen):
        [x,y] = self.cell.get_pos()
        screen.fill((255,255,255), (x*self.width,y*self.height,self.width,self.height))